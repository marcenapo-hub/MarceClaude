# Sitio de marca personal — Marce Napolitano

Sitio estático de una página. Sin frameworks, sin build, sin dependencias:
son tres archivos y se abren con doble clic.

```
web/
├── index.html              ← todo el contenido y los textos
├── assets/
│   ├── css/styles.css      ← diseño, colores y tipografía
│   ├── js/main.js          ← menú, animaciones y envío del formulario
│   ├── img/                ← fotos (ver assets/img/LEEME.md)
│   └── fonts/              ← Gotham (ver assets/fonts/LEEME.md)
└── README.md
```

---

## 1. Verlo en tu computadora

Doble clic en `index.html`. Nada más.

Para verlo como lo va a ver un visitante (con las rutas resueltas igual que en
el servidor), desde la carpeta `web/`:

```bash
python3 -m http.server 8000
```

y abrir <http://localhost:8000>.

---

## 2. Activar el formulario de contacto

Hoy el formulario funciona en **modo provisorio**: al enviarlo abre el programa
de mail del visitante con el mensaje ya escrito. Sirve, pero se pierden
contactos (mucha gente no tiene mail configurado en el celular).

Para que los mensajes lleguen solos a **marcelo@krak.com.ar**:

1. Crear una cuenta gratis en [formspree.io](https://formspree.io) con esa casilla.
2. Crear un formulario nuevo. Te da un ID que se ve así: `xayzbwqd`.
3. En `index.html`, buscar `TU_ID_DE_FORMSPREE` y reemplazarlo por ese ID:

   ```html
   <form ... action="https://formspree.io/f/xayzbwqd" method="POST">
   ```

4. Enviar un mensaje de prueba y confirmar el mail de verificación que llega de
   Formspree la primera vez.

El plan gratuito da 50 mensajes por mes. Si se pasa, el plan pago es ~USD 10/mes.
Alternativas equivalentes: [Web3Forms](https://web3forms.com) (gratis, sin límite
mensual) o [Basin](https://usebasin.com).

**Ya viene incluido:** trampa antispam (honeypot), validación de campos, avisos
de éxito y error, y el selector de motivo de contacto para que sepas de entrada
si el mensaje es de Krak RE, Krak Studio, VAV o una tasación.

---

## 3. Publicarlo

### Opción A — Vercel (recomendada, 5 minutos)

1. Entrar a [vercel.com](https://vercel.com) e iniciar sesión con GitHub.
2. *Add New → Project* → elegir este repositorio.
3. En **Root Directory** poner `web`. Framework: *Other*. Sin comando de build.
4. *Deploy*.

Queda online en una URL `.vercel.app`. Para usar `marcenapolitano.com`:
*Settings → Domains → Add*, y Vercel te dice qué registros DNS cargar donde
tengas comprado el dominio.

### Opción B — GitHub Pages

*Settings → Pages* del repositorio → *Deploy from a branch* → rama
`claude/marce-napolitano-website-d2eejy`, carpeta `/web`. Tarda un par de
minutos en levantar.

---

## 4. Editar los textos

Todo el contenido está en `index.html`, en castellano y ordenado por secciones
marcadas con comentarios en mayúsculas (`<!-- ============ PERFIL ============ -->`).
Se edita con cualquier editor de texto: cambiás lo que dice entre las etiquetas
y guardás.

### Cambiar los colores

Están todos juntos al principio de `assets/css/styles.css`, en el bloque `:root`:

```css
--salvia:  #869f9b;   /* acento principal */
--niebla:  #d0d5d9;
--gris:    #ededed;
--crema:   #fcf9f4;   /* fondo del sitio */
--tinta:   #23292b;   /* texto */
```

> **Nota sobre la paleta:** los cuatro colores de marca son claros o medios.
> `#869f9b` sobre `#fcf9f4` da 2.2:1 de contraste, muy por debajo del mínimo
> legible (4.5:1), así que no puede usarse para texto. Por eso se agregaron dos
> derivados de la misma familia — `--tinta` (#23292b) para texto y `--salvia-osc`
> (#55696f) para links — que sí cumplen. Si el manual de marca ya define tonos
> oscuros propios, reemplazá esos dos valores y el sitio entero se actualiza.

---

### Cambiar la tipografía

Gotham ya está instalada y se sirve desde el propio sitio, en los títulos. El
texto corrido va en Montserrat porque **falta Gotham Book**, la pesada de
lectura. Detalle completo y cómo activarla: `assets/fonts/LEEME.md`.

---

## 5. Pendientes antes de salir a producción

- [ ] Conseguir **Gotham Book** para el texto corrido (ver `assets/fonts/LEEME.md`)
- [ ] Cargar la foto principal en `assets/img/marce-retrato.jpg`
- [ ] Cargar la imagen de compartir en `assets/img/og-marce.jpg`
- [ ] Configurar Formspree (punto 2)
- [ ] Confirmar las URLs reales de Krak Real Estate y Krak Studio en `index.html`
      (hoy apuntan a `krak.com.ar` y `krakstudio.com.ar`)
- [ ] Definir si VAV Desarrollos tiene sitio propio para enlazar
- [ ] Comprar el dominio y reemplazar `marcenapolitano.com` en las etiquetas
      `<meta>` y `<link rel="canonical">` del `<head>`
- [ ] Revisar y ajustar los textos del perfil: están escritos con tu criterio y
      tu información, pero la voz final es tuya
