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

Para que los mensajes lleguen solos a **info@marcenapolitano.com.ar**:

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
si el mensaje es de Krak RE, Krak Studio o VAV.

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
--salvia:      #869f9b;   /* color de marca: titular, acentos, banda */
--salvia-300:  #5e7d78;   /* títulos de sección */
--salvia-500:  #47625d;   /* texto secundario y etiquetas */
--salvia-700:  #364c49;   /* texto corrido */
--salvia-900:  #1f2e2b;   /* pie, botones, texto sobre el salvia */
--crema:       #fcf9f4;   /* fondo del sitio */
--niebla:      #d0d5d9;   /* líneas y bordes */
```

**Todo el texto del sitio es del color de marca.** El `#869f9b` puro tiene sólo
2,7:1 de contraste sobre el fondo crema, muy por debajo de lo legible, así que
en vez de mezclarlo con grises ajenos se construyó una escala del *mismo* color:
idéntico matiz (170°) y saturación equivalente, oscurecido en cuatro pasos. A
simple vista todo se lee como el mismo verde de la marca; la diferencia es que
cada paso se usa donde su contraste alcanza.

| Paso | Contraste sobre crema | Mínimo exigido | Dónde se usa |
|---|---|---|---|
| `#869f9b` | 2,7:1 | 3:1 (texto grande) | Titular del inicio, acentos, fondo de la banda |
| `#5e7d78` | 4,3:1 | 3:1 | Títulos de sección |
| `#47625d` | 6,3:1 | 4,5:1 | Texto secundario, etiquetas en versalitas |
| `#364c49` | 8,7:1 | 4,5:1 | Texto corrido |
| `#1f2e2b` | 13,5:1 | 4,5:1 | Pie, botones, texto sobre el fondo salvia |

> El único elemento que queda por debajo del mínimo es el **titular del inicio**,
> por decisión de marca: va en el `#869f9b` exacto del manual. Si alguna vez se
> quiere que cumpla, `#77908c` da 3,25:1 y a simple vista es el mismo color.

Las etiquetas en versalitas van en peso 700 en vez de 600: al ir en color y no
en negro, el peso extra compensa la pérdida de definición.

---

### Cambiar la tipografía

Gotham ya está instalada y se sirve desde el propio sitio, en los títulos. El
texto corrido va en Montserrat porque **falta Gotham Book**, la pesada de
lectura. Detalle completo y cómo activarla: `assets/fonts/LEEME.md`.

---

## 5. Pendientes antes de salir a producción

- [x] ~~Foto principal, logos e imagen de compartir~~ — cargados
- [ ] Configurar Formspree (punto 2) — **es lo único que falta para publicar**
- [ ] Conseguir **Gotham Book** para el texto corrido (ver `assets/fonts/LEEME.md`)
- [ ] Confirmar el dominio: hoy las etiquetas `<meta>` y `<link rel="canonical">`
      dicen `www.marcenapolitano.com.ar`, deducido del mail de contacto
- [ ] Revisar y ajustar los textos del perfil: están escritos con tu criterio y
      tu información, pero la voz final es tuya
