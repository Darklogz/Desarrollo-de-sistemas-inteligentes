(function () {
  "use strict";

  // Credenciales de demostración (reemplazar por autenticación real en el servidor)
  const DEMO_USER = "admin";
  const DEMO_PASS = "admin123";

  // ========== Protección de páginas ==========
  if (document.body.dataset.requiresAuth === "true") {
    const usuario = sessionStorage.getItem("usuario");
    if (!usuario) {
      window.location.href = "login.html";
      return;
    }
    const lbl = document.getElementById("nombreUsuario");
    if (lbl) lbl.textContent = usuario;
  }

  // ========== Login ==========
  const loginForm = document.getElementById("loginForm");
  if (loginForm) {
    // Si ya hay sesión, ir directo al panel
    if (sessionStorage.getItem("usuario")) {
      window.location.href = "index.html";
      return;
    }

    const inputUser = document.getElementById("usuario");
    const inputPass = document.getElementById("password");
    const errorBox = document.getElementById("loginError");

    loginForm.addEventListener("submit", function (e) {
      e.preventDefault();
      errorBox.classList.add("d-none");

      const userOk = inputUser.value.trim() !== "";
      const passOk = inputPass.value !== "";
      inputUser.classList.toggle("is-invalid", !userOk);
      inputPass.classList.toggle("is-invalid", !passOk);
      if (!userOk || !passOk) return;

      if (inputUser.value.trim() === DEMO_USER && inputPass.value === DEMO_PASS) {
        sessionStorage.setItem("usuario", inputUser.value.trim());
        window.location.href = "index.html";
      } else {
        errorBox.classList.remove("d-none");
      }
    });

    // Mostrar / ocultar contraseña
    const toggleBtn = document.getElementById("togglePassword");
    toggleBtn.addEventListener("click", function () {
      const visible = inputPass.type === "text";
      inputPass.type = visible ? "password" : "text";
      toggleBtn.innerHTML = visible
        ? '<i class="bi bi-eye"></i>'
        : '<i class="bi bi-eye-slash"></i>';
    });
  }

  // ========== Sidebar toggle ==========
  const sidebarToggle = document.getElementById("sidebarToggle");
  const wrapper = document.getElementById("wrapper");
  if (sidebarToggle && wrapper) {
    sidebarToggle.addEventListener("click", function () {
      wrapper.classList.toggle("toggled");
    });
  }

  // ========== Logout ==========
  const btnLogout = document.getElementById("btnLogout");
  if (btnLogout) {
    btnLogout.addEventListener("click", function (e) {
      e.preventDefault();
      sessionStorage.removeItem("usuario");
      window.location.href = "login.html";
    });
  }
})();