const root = document.documentElement;
const themeButton = document.querySelector('.theme-button');
function updateThemeButton() {
  const dark = root.dataset.theme === 'dark';
  themeButton.setAttribute('aria-label', dark ? 'Switch to light mode' : 'Switch to dark mode');
  themeButton.title = dark ? 'Switch to light mode' : 'Switch to dark mode';
}
themeButton.addEventListener('click', () => {
  const dark = root.dataset.theme !== 'dark';
  root.dataset.theme = dark ? 'dark' : 'light';
  try { localStorage.setItem('theme', dark ? 'dark' : 'light'); } catch (_) {}
  updateThemeButton();
});
updateThemeButton();
const menuButton = document.querySelector('.menu-button');
const mobileNav = document.querySelector('.mobile-nav');
function setMenu(open) {
  mobileNav.hidden = !open;
  menuButton.setAttribute('aria-expanded', String(open));
  menuButton.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
}
menuButton.addEventListener('click', () => setMenu(menuButton.getAttribute('aria-expanded') !== 'true'));
document.addEventListener('keydown', (event) => { if (event.key === 'Escape') setMenu(false); });
