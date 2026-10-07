(function () {
  var raiz = document.documentElement;
  var botaoTema = document.getElementById('tema');

  // ----- tema claro / escuro -----
  function aplicarTema(escuro) {
    if (escuro) raiz.setAttribute('data-tema', 'escuro');
    else raiz.removeAttribute('data-tema');
    botaoTema.setAttribute('aria-pressed', escuro ? 'true' : 'false');
    botaoTema.setAttribute('aria-label', escuro ? 'Trocar para o tema claro' : 'Trocar para o tema escuro');
    var cor = escuro ? '#0A141D' : '#E9F4FC';
    var metas = document.querySelectorAll('meta[name="theme-color"]');
    for (var i = 0; i < metas.length; i++) metas[i].setAttribute('content', cor);
  }

  aplicarTema(raiz.getAttribute('data-tema') === 'escuro');

  botaoTema.addEventListener('click', function () {
    var escuro = raiz.getAttribute('data-tema') !== 'escuro';
    aplicarTema(escuro);
    try { localStorage.setItem('localyze-tema', escuro ? 'escuro' : 'claro'); } catch (e) {}
  });

  // ----- ano no rodapé -----
  var ano = document.getElementById('ano');
  if (ano) ano.textContent = new Date().getFullYear();

  // ----- entrada suave das seções -----
  var itens = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window) {
    var vistos = new IntersectionObserver(function (entradas) {
      entradas.forEach(function (e) {
        if (e.isIntersecting) {
          e.target.classList.add('entrou');
          vistos.unobserve(e.target);
        }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
    itens.forEach(function (el) { vistos.observe(el); });
  } else {
    itens.forEach(function (el) { el.classList.add('entrou'); });
  }

  // ----- esconde o botão fixo quando o contato já está na tela -----
  var barra = document.getElementById('barra');
  var contato = document.getElementById('contato');
  if (barra && contato && 'IntersectionObserver' in window) {
    new IntersectionObserver(function (entradas) {
      barra.classList.toggle('oculta', entradas[0].isIntersecting);
    }, { threshold: 0.25 }).observe(contato);
  }
})();
