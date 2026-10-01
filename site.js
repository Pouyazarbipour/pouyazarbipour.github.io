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
    // publication filters
    const buttons = [...document.querySelectorAll('.filter-btn')];
    const items = [...document.querySelectorAll('.pub-item[data-categories]')];
    buttons.forEach(btn => btn.addEventListener('click', () => {
      const f = btn.dataset.filter;
      items.forEach(i => i.style.display = f === 'all' || i.dataset.categories.split(/\s+/).includes(f) ? '' : 'none');
      buttons.forEach(b => b.classList.toggle('active', b === btn));
    }));
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
