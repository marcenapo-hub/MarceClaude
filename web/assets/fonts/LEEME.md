# Tipografía — Gotham

Gotham es una tipografía **licenciada** de Hoefler&Co. No es gratuita ni está en
Google Fonts: para usarla en un sitio web hace falta una licencia de *webfont*.

## Cómo activarla

1. Conseguir la licencia web en [typography.com](https://www.typography.com)
   (plan Cloud.typography) o los archivos `.woff2` con licencia web incluida.
2. Dejar los archivos en esta carpeta con estos nombres exactos:

   - `gotham-book.woff2`   → peso 400 (texto)
   - `gotham-medium.woff2` → peso 500 (destacados)
   - `gotham-bold.woff2`   → peso 700 (títulos)

3. Listo. El `@font-face` ya está declarado al inicio de
   `web/assets/css/styles.css` y toma los archivos automáticamente.

> Si en vez de archivos usás el CDN de Cloud.typography, pegá el `<link>` que te
> dan en el `<head>` de `index.html` y borrá los tres bloques `@font-face` del CSS.

## Mientras tanto

El sitio usa **Montserrat** (Google Fonts), que es el reemplazo geométrico más
cercano a Gotham y es gratuita. Si el presupuesto de licencia no se justifica,
Montserrat sola es una decisión perfectamente defendible: nadie fuera del rubro
diseño va a notar la diferencia.

**Importante:** no subas a este repositorio archivos de Gotham obtenidos de
fuentes no oficiales. Es la fuente tipográfica más pirateada del mundo y el
riesgo legal es real, sobre todo en un sitio con tu nombre y matrícula.
