(() => {
  const root = document.documentElement;
  try { const t = localStorage.getItem('theme'); if (t) root.dataset.theme = t; } catch (e) {}
  document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('[data-year]').forEach(n => n.textContent = new Date().getFullYear());
    document.querySelectorAll('.theme-toggle').forEach(b => b.addEventListener('click', () => {
      const next = root.dataset.theme === 'dark' ? 'light' : 'dark';
      root.dataset.theme = next;
      try { localStorage.setItem('theme', next); } catch (e) {}
    }));
    const menu = document.querySelector('.menu-btn'), nav = document.querySelector('.nav');
    if (menu && nav) menu.addEventListener('click', () => {
      const open = nav.classList.toggle('open');
      menu.setAttribute('aria-expanded', open);
    });
    // data-driven publications + stats (fall back to the static HTML if fetch fails)
    const esc = t => String(t == null ? '' : t).replace(/[&<>"]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
    const pubHTML = (p, filt) => {
      const b = [];
      if (p.first) b.push('<span class="pub-badge first">First author</span>');
      if (p.status === 'review') b.push('<span class="pub-badge review">Under review</span>');
      if (p.status === 'prep') b.push('<span class="pub-badge prep">In preparation</span>');
      const url = p.doi || p.url;
      const act = url ? `<a href="${esc(url)}" rel="noopener" target="_blank">${p.type === 'conference' ? 'Link' : 'DOI'} ↗</a>` : '';
      const cat = filt ? ` data-categories="${esc(p.cats)}"` : '';
      return `<article class="pub-item"${cat}><div class="pub-year">${esc(p.year)}</div><div><h3>${esc(p.title)}</h3><div class="pub-meta"><span class="pub-venue">${esc(p.venue)}</span> · ${b.length ? `<span class="pub-badges">${b.join('')}</span> ` : ''}<span class="pub-authors">${esc(p.authors)}</span></div></div><div class="pub-action">${act}</div></article>`;
    };
    const bindFilters = () => {
      const buttons = [...document.querySelectorAll('.filter-btn')];
      const items = [...document.querySelectorAll('.pub-item[data-categories]')];
      buttons.forEach(btn => btn.addEventListener('click', () => {
        const f = btn.dataset.filter;
        items.forEach(i => i.style.display = f === 'all' || i.dataset.categories.split(/\s+/).includes(f) ? '' : 'none');
        buttons.forEach(x => x.classList.toggle('active', x === btn));
      }));
    };
    const setText = (id, v) => { const n = document.getElementById(id); if (n && v != null) n.textContent = v; };
    const loadJSON = u => fetch(u + '?v=' + Date.now(), { cache: 'no-store' }).then(r => { if (!r.ok) throw new Error(u); return r.json(); });
    loadJSON('data/publications.json').then(list => {
      const journals = list.filter(p => p.type !== 'conference'), confs = list.filter(p => p.type === 'conference');
      const put = (id, items, filt) => { const n = document.getElementById(id); if (n && items.length) n.innerHTML = items.map(p => pubHTML(p, filt)).join(''); };
      put('journal-list', journals, true);
      put('conf-list', confs, false);
      put('recent-contributions', journals.slice(0, 5), false);
      setText('journal-count', journals.length);
    }).catch(() => {}).finally(bindFilters);
    loadJSON('scholar-stats.json').then(s => {
      if (Number.isFinite(+s.citations)) setText('stat-citations', (+s.citations).toLocaleString());
      if (Number.isFinite(+s.h_index)) setText('stat-h', (+s.h_index).toLocaleString());
      if (s.source) setText('stat-source', s.source + ' · ' + (s.updated || ''));
    }).catch(() => {});
    // contact form (EmailJS, same service as the previous site)
    const form = document.getElementById('contact-form');
    if (form && window.emailjs) {
      emailjs.init('6l6wMbqUhp1iOrsu2');
      form.addEventListener('submit', e => {
        e.preventDefault();
        const btn = form.querySelector('button[type=submit]'), label = btn.textContent;
        btn.textContent = 'Sending...'; btn.disabled = true;
        const email = form.user_email.value;
        emailjs.send('service_xi6qi1j', 'template_vjd6iil', {
          to_name: 'Pouya Zarbipour', from_name: form.user_name.value, from_email: email, message: form.message.value, reply_to: email
        }).then(() => { alert("Thank you for your message! I'll get back to you soon."); form.reset(); },
          err => alert('Sorry, there was an error sending your message. Please contact me directly at pouyazarbipour@gmail.com'))
          .finally(() => { btn.textContent = label; btn.disabled = false; });
      });
    }
  });
})();
