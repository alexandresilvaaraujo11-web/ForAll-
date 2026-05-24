const mobileMenu = document.getElementById("mobileMenu");
function toggleMenu() {
    document.getElementById('mobileMenu').classList.toggle('open');
}

/* Mudou tamanho da tela? Menu fica invisível*/
window.addEventListener('resize', () => {
    document.getElementById('mobileMenu').classList.remove('open');
});

  let timeoutPesquisa;

  function pesquisarComDelay(input) {

    clearTimeout(timeoutPesquisa);

    timeoutPesquisa = setTimeout(() => {
      input.form.submit();
    }, 1500);

}