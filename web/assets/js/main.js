/* =========================================================
   Marce Napolitano — comportamiento del sitio
   Vanilla JS, sin dependencias.
   ========================================================= */
(function () {
  "use strict";

  /* ---------- Año en el pie ---------- */
  var anio = document.getElementById("anio");
  if (anio) anio.textContent = new Date().getFullYear();

  /* ---------- Menú mobile ---------- */
  var botonMenu = document.getElementById("menu-boton");
  var nav = document.getElementById("nav");

  if (botonMenu && nav) {
    botonMenu.addEventListener("click", function () {
      var abierto = botonMenu.getAttribute("aria-expanded") === "true";
      botonMenu.setAttribute("aria-expanded", String(!abierto));
      botonMenu.setAttribute("aria-label", abierto ? "Abrir menú" : "Cerrar menú");
      nav.setAttribute("data-abierto", String(!abierto));
    });

    // Cerrar al tocar un enlace
    nav.addEventListener("click", function (e) {
      if (e.target.closest("a")) {
        botonMenu.setAttribute("aria-expanded", "false");
        botonMenu.setAttribute("aria-label", "Abrir menú");
        nav.setAttribute("data-abierto", "false");
      }
    });

    // Cerrar con Escape
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && nav.getAttribute("data-abierto") === "true") {
        botonMenu.setAttribute("aria-expanded", "false");
        nav.setAttribute("data-abierto", "false");
        botonMenu.focus();
      }
    });
  }

  /* ---------- Header con borde al hacer scroll ---------- */
  var encabezado = document.getElementById("encabezado");
  if (encabezado) {
    var alScrollear = function () {
      encabezado.setAttribute("data-fijo", String(window.scrollY > 12));
    };
    alScrollear();
    window.addEventListener("scroll", alScrollear, { passive: true });
  }

  /* ---------- Revelado al entrar en pantalla ---------- */
  var revelables = document.querySelectorAll(".revelar");
  if ("IntersectionObserver" in window && revelables.length) {
    var observador = new IntersectionObserver(function (entradas) {
      entradas.forEach(function (entrada, i) {
        if (!entrada.isIntersecting) return;
        var elemento = entrada.target;
        // Escalonado suave dentro de un mismo grupo visible
        setTimeout(function () {
          elemento.setAttribute("data-visible", "true");
        }, Math.min(i * 90, 360));
        observador.unobserve(elemento);
      });
    }, { threshold: 0.12, rootMargin: "0px 0px -60px 0px" });

    revelables.forEach(function (el) { observador.observe(el); });
  } else {
    revelables.forEach(function (el) { el.setAttribute("data-visible", "true"); });
  }

  /* ---------- Navegación activa según sección ---------- */
  var enlacesNav = Array.prototype.slice.call(
    document.querySelectorAll('.nav__lista a[href^="#"]:not(.boton)')
  );
  var secciones = enlacesNav
    .map(function (a) { return document.querySelector(a.getAttribute("href")); })
    .filter(Boolean);

  if ("IntersectionObserver" in window && secciones.length) {
    var observadorNav = new IntersectionObserver(function (entradas) {
      entradas.forEach(function (entrada) {
        if (!entrada.isIntersecting) return;
        enlacesNav.forEach(function (a) {
          var activo = a.getAttribute("href") === "#" + entrada.target.id;
          if (activo) { a.setAttribute("aria-current", "true"); }
          else { a.removeAttribute("aria-current"); }
        });
      });
    }, { rootMargin: "-45% 0px -50% 0px" });

    secciones.forEach(function (s) { observadorNav.observe(s); });
  }

  /* ---------- Fotos: ocultar el marcador cuando la imagen carga ---------- */
  document.querySelectorAll("[data-foto]").forEach(function (img) {
    var figura = img.closest("figure");
    var marcador = figura ? figura.querySelector("[data-marcador]") : null;

    var ok = function () { if (marcador) marcador.remove(); };
    var falla = function () { img.remove(); }; // queda el marcador visible

    if (img.complete) {
      (img.naturalWidth > 0 ? ok : falla)();
    } else {
      img.addEventListener("load", ok);
      img.addEventListener("error", falla);
    }
  });

  /* ---------- Formulario de contacto ---------- */
  var form = document.getElementById("form-contacto");
  if (!form) return;

  var avisoOk = document.getElementById("aviso-ok");
  var avisoError = document.getElementById("aviso-error");
  var botonEnviar = document.getElementById("boton-enviar");
  var MAIL = "marcelo@krak.com.ar";

  var mostrarError = function (texto) {
    if (!avisoError) return;
    avisoError.textContent = texto;
    avisoError.hidden = false;
  };

  var limpiarAvisos = function () {
    if (avisoOk) avisoOk.hidden = true;
    if (avisoError) avisoError.hidden = true;
  };

  // Si todavía no se configuró Formspree, se arma un mail con los datos.
  var enviarPorMail = function (datos) {
    var cuerpo = [
      "Nombre: " + (datos.get("nombre") || ""),
      "Email: " + (datos.get("email") || ""),
      "Teléfono: " + (datos.get("telefono") || "—"),
      "Motivo: " + (datos.get("motivo") || ""),
      "",
      datos.get("mensaje") || ""
    ].join("\n");

    window.location.href = "mailto:" + MAIL +
      "?subject=" + encodeURIComponent("Contacto desde la web — " + (datos.get("nombre") || "")) +
      "&body=" + encodeURIComponent(cuerpo);
  };

  form.addEventListener("submit", function (e) {
    e.preventDefault();
    limpiarAvisos();

    // Validación nativa con mensajes del navegador
    if (!form.checkValidity()) {
      form.reportValidity();
      return;
    }

    var datos = new FormData(form);

    // Honeypot: si vino completo, es un bot. Simulamos éxito y no enviamos.
    if (datos.get("_gotcha")) {
      if (avisoOk) avisoOk.hidden = false;
      form.reset();
      return;
    }

    var destino = form.getAttribute("action") || "";

    if (destino.indexOf("TU_ID_DE_FORMSPREE") !== -1) {
      enviarPorMail(datos);
      return;
    }

    botonEnviar.disabled = true;
    var textoOriginal = botonEnviar.textContent;
    botonEnviar.textContent = "Enviando…";

    fetch(destino, {
      method: "POST",
      body: datos,
      headers: { Accept: "application/json" }
    })
      .then(function (r) {
        if (r.ok) {
          form.reset();
          if (avisoOk) avisoOk.hidden = false;
          avisoOk.scrollIntoView({ block: "center", behavior: "smooth" });
        } else {
          return r.json().then(function (d) {
            throw new Error(
              (d.errors && d.errors.map(function (x) { return x.message; }).join(", ")) ||
              "No se pudo enviar."
            );
          });
        }
      })
      .catch(function () {
        mostrarError(
          "No pudimos enviar el mensaje. Escribime directo a " + MAIL + " y lo resolvemos."
        );
      })
      .finally(function () {
        botonEnviar.disabled = false;
        botonEnviar.textContent = textoOriginal;
      });
  });
})();
