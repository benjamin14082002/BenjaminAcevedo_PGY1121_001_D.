document.addEventListener('DOMContentLoaded', function() {
    var passwordInput = document.getElementById('password');
    var togglePasswordButton = document.getElementById('toggle-password');

    togglePasswordButton.addEventListener('click', function() {
        var type = passwordInput.getAttribute('type') === 'password' ? 'text' : 'password';
        passwordInput.setAttribute('type', type);
        this.textContent = type === 'password' ? 'Mostrar contraseña' : 'Ocultar contraseña';
    });
});













