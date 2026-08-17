# Logos de las unidades de negocio

Los tres están cargados, en el verde de marca y con fondo transparente.

| Archivo | Empresa | Original |
|---|---|---|
| `krak-real-estate.png` | Krak Real Estate | `LogoKrak Horizontal RE sin.png` |
| `krak-studio.png` | Krak Studio | `studio_h-4x.png` |
| `vav-desarrollos.png` | VAV Desarrollos | `logos_VAV_0 1.png` |

## Cómo se prepararon

Los originales venían en colores distintos —azul los Krak, negro VAV— y en dos
formatos: blanco sobre transparente uno, tinta sobre fondo blanco los otros. Se
los pasó a **silueta monocroma** en `#364c49`, el mismo verde del texto del
sitio, tomando la forma del canal de transparencia o de la luminosidad según el
caso.

Los tres no están al mismo alto: los Krak son icono + texto al costado y VAV es
un bloque apilado, así que igualarlos por altura los haría ver de tamaños
distintos. Se ajustó el de VAV al 72 % para que la palabra principal quede
ópticamente pareja con "KRAK".

Los archivos son lienzos de 120 px de alto (3× de los 40 px a los que se
muestran, para que se vean nítidos en pantallas retina), con el logo centrado
verticalmente. Ese lienzo común es lo que mantiene la proporción entre los tres.

## Para regenerarlos

El script está en el historial de la conversación; en esencia: tomar el molde
(canal alfa si el fondo ya es transparente, luminosidad si el fondo es blanco),
pintarlo del color deseado, recortar el aire sobrante, escalar a la altura que
corresponda y centrar en el lienzo de 120 px.

Si algún día conseguís los logos en **SVG**, mejor: se ven nítidos a cualquier
tamaño y el recoloreado es cambiar un atributo `fill`.
