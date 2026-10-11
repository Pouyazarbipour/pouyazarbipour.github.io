#!/usr/bin/env python3
"""Refresh scholar-stats.json (OpenAlex) and data/publications.json (ORCID + Crossref).

data/publications-manual.json is the curated source of truth (categories, first-author
flag, under-review / in-preparation items). New DOIs found on ORCID are appended
automatically. Any network failure leaves the existing output files untouched.
"""
import json, re, sys, datetime, urllib.request, urllib.parse

ORCID = "0000-0002-8024-9062"
FAMILY = "zarbipour"
UA = {"User-Agent": "pouyazarbipour.github.io-updater (mailto:pouyazarbipour@gmail.com)",
      "Accept": "application/json"}

def get(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)

def update_stats():
    a = get(f"https://api.openalex.org/authors/orcid:{ORCID}")
    stats = {
        "citations": a["cited_by_count"],
        "h_index": a["summary_stats"]["h_index"],
        "works": a["works_count"],
        "source": "OpenAlex",
        "updated": datetime.date.today().isoformat(),
    }
    json.dump(stats, open("scholar-stats.json", "w"), indent=1)
    print("stats:", stats)

def orcid_dois():
    d = get(f"https://pub.orcid.org/v3.0/{ORCID}/works")
    dois = []
    for g in d.get("group", []):
        for ext in g.get("external-ids", {}).get("external-id", []):
            if ext.get("external-id-type") == "doi":
                dois.append(ext["external-id-value"].lower().strip())
                break
    return dois

def crossref(doi):
    m = get("https://api.crossref.org/works/" + urllib.parse.quote(doi))["message"]
    authors = [x.get("family", "") for x in m.get("author", [])]
    names = ", ".join(authors[:-1]) + (" & " if len(authors) > 1 else "") + authors[-1] if authors else ""
    parts = (m.get("issued", {}).get("date-parts") or [[None]])[0]
    return {
        "type": "conference" if m.get("type") == "proceedings-article" else "journal",
        "year": str(parts[0] or ""),
        "title": re.sub(r"<[^>]+>", "", (m.get("title") or [""])[0]),
        "venue": (m.get("container-title") or [""])[0],
        "authors": names,
        "doi": "https://doi.org/" + doi,
        "status": "published",
        "cats": "",
        "first": bool(authors) and authors[0].lower() == FAMILY,
    }

def norm_doi(v):
    return re.sub(r"^https?://(dx\.)?doi\.org/", "", (v or "").strip().lower())

def words(t):
    return set(re.findall(r"[a-z0-9]{3,}", t.lower()))

def similar(a, b):
    wa, wb = words(a), words(b)
    return bool(wa and wb) and len(wa & wb) / len(wa | wb) >= 0.6

def update_publications():
    pubs = json.load(open("data/publications-manual.json"))
    for doi in dict.fromkeys(orcid_dois()):
        doi = norm_doi(doi)
        if any(norm_doi(p.get("doi")) == doi for p in pubs):
            continue
        try:
            new = crossref(doi)
        except Exception as e:
            print("skip", doi, e)
            continue
        twin = next((p for p in pubs if similar(p["title"], new["title"])), None)
        if twin is None:
            pubs.append(new)
            print("added from ORCID:", doi)
        elif not twin.get("doi"):
            # curated entry without a DOI (under review / in preparation) is now published
            for k in ("doi", "venue", "year", "title"):
                twin[k] = new[k]
            twin["status"] = "published"
            print("published, merged into curated entry:", doi)
        else:
            print("duplicate of existing entry, skipped:", doi)
    pubs.sort(key=lambda p: p.get("year", ""), reverse=True)
    json.dump(pubs, open("data/publications.json", "w"), indent=1, ensure_ascii=False)
    print("publications:", len(pubs))

ok = True
for fn in (update_stats, update_publications):
    try:
        fn()
    except Exception as e:
        ok = False
        print(fn.__name__, "failed:", e, file=sys.stderr)
sys.exit(0 if ok else 1)
