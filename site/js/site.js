/* Writing with Local AI — site script
   Asdale Dynamics, LLC */

(() => {
  'use strict';

  // Highlight the current page in the navigation
  const current = location.pathname.split('/').pop() || 'index.html';
  const links = document.querySelectorAll('.site-nav a');
  links.forEach((link) => {
    const href = link.getAttribute('href') || '';
    const file = href.split('/').pop() || 'index.html';
    if (file === current) {
      link.classList.add('active');
      link.setAttribute('aria-current', 'page');
    }
  });

  // Convenience: print button for the templates page
  const printBtn = document.getElementById('print-templates');
  if (printBtn) {
    printBtn.addEventListener('click', () => {
      window.print();
    });
  }
})();
