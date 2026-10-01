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

def update_publications():
    manual = json.load(open("data/publications-manual.json"))
    known = {p["doi"].split("doi.org/")[-1].lower() for p in manual if p.get("doi")}
    for doi in orcid_dois():
        if doi in known:
            continue
        try:
            manual.append(crossref(doi))
            print("added from ORCID:", doi)
        except Exception as e:
            print("skip", doi, e)
    manual.sort(key=lambda p: p.get("year", ""), reverse=True)
    json.dump(manual, open("data/publications.json", "w"), indent=1, ensure_ascii=False)
    print("publications:", len(manual))

ok = True
for fn in (update_stats, update_publications):
    try:
        fn()
    except Exception as e:
        ok = False
        print(fn.__name__, "failed:", e, file=sys.stderr)
sys.exit(0 if ok else 1)
