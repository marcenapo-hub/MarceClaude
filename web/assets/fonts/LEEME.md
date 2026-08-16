# Tipografía — Gotham

## Qué hay cargado

Los cuatro archivos que entregó Marce, convertidos de `.otf` (formato de
escritorio) a `.woff2` (formato web: pesa hasta 76 % menos y carga más rápido).

| Archivo | Contiene | Peso CSS | Tamaño |
|---|---|---|---|
| `gotham-bold.woff2` | Gotham Bold | 600–700 | 30 KB |
| `gotham-black.woff2` | Gotham Black | 800–900 | 14 KB |
| `gotham-thin.woff2` | Gotham Thin | 100–250 | 30 KB |
| `gotham-bold-italic.woff2` | Gotham Bold Italic | 600–700 *itálica* | 18 KB |

> **Los nombres originales no coincidían con el contenido.** El archivo que venía
> como `Gotham_Regular.otf` es en realidad Gotham **Black**, y el que venía como
> `Gotham_Italic.otf` es **Bold Italic**. Se verificó midiendo el grosor real del
> trazo, no leyendo los metadatos (que también estaban mal). Acá quedaron
> renombrados según lo que realmente son.

## Falta Gotham Book

Las cuatro pesadas disponibles son de titular. **No hay una pesada de lectura**
(Gotham Book, ~400): Bold da un párrafo macizo e ilegible y Thin desaparece a
17 px.

Por eso hoy el sitio usa:

- **Gotham Bold** → todos los títulos y el logo
- **Montserrat** → texto corrido, menús, botones y formulario

### Cuando consigas Gotham Book

1. Dejá el archivo acá como `gotham-book.woff2`.
   Si viene en `.otf`, convertilo primero:
   ```bash
   pip install fonttools brotli
   python3 -c "from fontTools.ttLib import TTFont; f=TTFont('Gotham-Book.otf'); f.flavor='woff2'; f.save('gotham-book.woff2')"
   ```
2. En `assets/css/styles.css`, descomentá el bloque `@font-face` de Gotham Book
   (está señalado con un comentario).
3. En el mismo archivo, cambiá el token:
   ```css
   --fuente-texto: "Gotham", "Montserrat", "Helvetica Neue", Arial, sans-serif;
   ```
4. Opcional: sacá del `<head>` de `index.html` las tres líneas de Google Fonts,
   que dejan de hacer falta.

Con eso el sitio pasa a Gotham completo sin tocar nada más.

## Licencia

Los archivos entregados son de **escritorio** (los que se instalan para trabajar
en Illustrator o InDesign). Servir una tipografía desde un sitio web público es
un uso distinto, que la licencia de escritorio normalmente no cubre.

Si en algún momento se quiere regularizar, la licencia web se compra en
[typography.com](https://www.typography.com) (Cloud.typography, desde ~USD 100
al año según tráfico). Alternativa sin costo: usar Montserrat también en los
títulos — es el sustituto geométrico más cercano y nadie fuera del rubro diseño
nota la diferencia.
