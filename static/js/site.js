const toggle = document.querySelector('.menu-toggle');
const nav = document.querySelector('#main-nav');
if (toggle && nav) {
  toggle.hidden = false;
  nav.classList.add('enhanced');
  toggle.addEventListener('click', () => {
    const open = toggle.getAttribute('aria-expanded') !== 'true';
    toggle.setAttribute('aria-expanded', String(open));
    nav.classList.toggle('is-open', open);
  });
  document.addEventListener('keydown', event => {
    if (event.key === 'Escape' && toggle.getAttribute('aria-expanded') === 'true') {
      toggle.setAttribute('aria-expanded', 'false');
      nav.classList.remove('is-open');
      toggle.focus();
    }
  });
}

const filters = document.querySelector('.filters');
if (filters) {
  filters.hidden = false;
  filters.addEventListener('click', event => {
    const button = event.target.closest('[data-filter]');
    if (!button) return;
    filters.querySelectorAll('button').forEach(item => {
      item.classList.toggle('active', item === button);
      item.setAttribute('aria-pressed', String(item === button));
    });
    let count = 0;
    document.querySelectorAll('.essay-list .essay-row').forEach(row => {
      row.hidden = !!button.dataset.filter && !row.dataset.tags.split('|').includes(button.dataset.filter);
      if (!row.hidden) count++;
    });
    document.querySelector('#filter-status').textContent = count + (count === 1 ? ' essay shown' : ' essays shown');
  });
}

const toc = document.querySelector('.toc');
if (toc) {
  const mobile = matchMedia('(max-width: 767px)');
  const update = () => { toc.open = !mobile.matches; };
  update();
  mobile.addEventListener('change', update);
}
