---
name: trello
description: Consultar y operar los tableros de Trello de Marce (Krak Studio, Krak Real Estate, Moto Morini, Tienda Tool, Rebis, Smarthomes, etc.) vía la API REST de Trello. Usar esta skill siempre que el usuario mencione Trello, un tablero, tarjetas, listas, vencimientos de publicaciones, o pida un resumen del estado de algún cliente/proyecto que se gestiona en Trello — aunque no diga la palabra "Trello" explícitamente (ej. "¿qué hay vencido de Krak Studio?", "agregá una tarea a Tienda Tool").
---

# Trello

Integración con la API REST de Trello para los tableros del workspace de Marce
(usuario Trello: `marcekrak`).

## Herramienta principal

Usar el script `scripts/trello.py` para todo — no armar URLs de la API a mano,
porque el script ya maneja credenciales sin exponerlas, búsqueda de tableros por
nombre parcial, y formato de salida con vencimientos:

```bash
python3 .claude/skills/trello/scripts/trello.py whoami                      # verificar conexión
python3 .claude/skills/trello/scripts/trello.py boards                      # tableros abiertos
python3 .claude/skills/trello/scripts/trello.py summary "Krak Studio"       # resumen por listas
python3 .claude/skills/trello/scripts/trello.py overdue "Krak Studio"       # solo vencidas
python3 .claude/skills/trello/scripts/trello.py cards "Krak Studio" "En proceso"
python3 .claude/skills/trello/scripts/trello.py add-card "Krak Studio" "Tareas" "Título" --due 2026-08-01
```

Los nombres de tablero y lista aceptan coincidencia parcial sin distinguir
mayúsculas ("krak studio", "proceso").

## Credenciales — reglas de seguridad (importantes)

El script lee `TRELLO_API_KEY` y `TRELLO_TOKEN` desde variables de entorno, o
desde un archivo `.env.trello` en la raíz del repo o en `~`. Ese archivo está en
`.gitignore` y **nunca debe commitearse**.

- Nunca pegar la key o el token en el chat, en commits, en código, ni en logs.
  Si el usuario los pega en el chat, avisarle que quedaron expuestos y que debe
  regenerar el token en https://trello.com/power-ups/admin (sección "Clave de API").
- Nunca pasar credenciales como argumentos de línea de comandos ni imprimirlas.
- Si faltan credenciales, el script lo dice claramente: pedirle al usuario que
  cree `.env.trello` (dos líneas: `TRELLO_API_KEY=...` y `TRELLO_TOKEN=...`) o
  configure las variables. NO ofrecerle que las pegue en el chat.
- Ojo con el campo "Variables de entorno" del entorno cloud de Claude Code: la
  UI advierte que son visibles para cualquiera que use el entorno. Preferir el
  archivo `.env.trello` local a la sesión.

## Contexto del workspace (aprendido 2026-07)

- Tableros abiertos: Administración, Compass, Krak Real Estate, **Krak Studio**
  (el central de la agencia), Marce Marca Personal, Marce Personal, Moto Morini
  San Isidro, Smarthomes, Tablero de Control Tienda Tool, Tienda Tool.
- "Krak Studio" es el tablero de operaciones de la agencia. Sus listas:
  *Generales de cada cliente Activo* (fichas por cliente + calendario de
  publicaciones IG/LinkedIn con vencimientos), *Tareas* (backlog), *En proceso*,
  *En revisión*, *Stand By*, *Terminado* (300+ tarjetas históricas — en
  resúmenes mostrar solo el conteo).
- Las etiquetas de tarjeta indican el cliente (Krak Inmobiliaria, Moto Morini,
  Tienda Tool, Rebis, Smarthomes, VAV Desarrollos, etc.).
- Al resumir un tablero, destacar primero las tarjetas vencidas y las que vencen
  en los próximos días — es lo que más le importa al usuario.

## Requisitos del entorno

El dominio `api.trello.com` debe estar en la lista de dominios permitidos del
entorno cloud (Acceso a la red → Personalizado). Ya fue agregado; si las
llamadas fallan con error de red, verificar eso primero.
