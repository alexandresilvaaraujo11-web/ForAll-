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
  document.addEventListener("DOMContentLoaded", function() {
    // Pega todos os popups (toasts) que aparecerem na tela
    const toasts = document.querySelectorAll('.toast');
    
    toasts.forEach(function(toast) {
      
      // Criamos uma função separada só para fazer a animação de sumir
      function dismissToast() {
        toast.style.transition = 'opacity 0.3s ease, transform 0.3s ease';
        toast.style.opacity = '0';
        toast.style.transform = 'translateY(15px)';
        
        // Remove de verdade do código HTML depois de 300 milissegundos
        setTimeout(function() {
          if (toast.parentNode) {
            toast.remove();
          }
        }, 300);
      }

      // 1. Faz o popup sumir sozinho depois de 4 segundos
      const autoDismiss = setTimeout(dismissToast, 3000);

      // 2. Faz o popup sumir na hora se o usuário clicar nele
      toast.addEventListener('click', function() {
        clearTimeout(autoDismiss); // Cancela o timer automático para não dar erro
        dismissToast(); // Chama a função de sumir
      });
      
    });
  });
