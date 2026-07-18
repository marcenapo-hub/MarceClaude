# MarceClaude — Contexto de trabajo de Marce

Este archivo es la memoria de trabajo persistente. Marce lo va cargando con
contexto de sus proyectos y tareas. Leerlo al inicio de cada sesión y mantenerlo
actualizado cuando pida "acordate de X" o "guardá esto".

## Quién es Marce

- Marce Napolitano, dirige **Krak Studio**, agencia de marketing (Buenos Aires).
- Habla español (Argentina). Responder siempre en español.
- Prefiere soluciones concretas y acción directa antes que explicaciones largas.

## Clientes y proyectos activos

- **Krak Inmobiliaria / Krak Real Estate** — el cliente más grande (inmobiliaria,
  incluye Krak Industrial, embudos, campañas Meta/Google, Tokko CRM, Hubspot).
- **Moto Morini San Isidro** — concesionaria de motos (contenido POV, Hubspot, pauta).
- **Tienda Tool** — e-commerce de herramientas (WooCommerce, Hubspot, WhatsApp).
- **Rebis, Smarthomes, Compass, VAV Desarrollos, China Fit, Stark** — clientes activos.
- **Marce Marca Personal** — su marca personal (capacitaciones, LinkedIn).

## Herramientas conectadas

- **Trello** (workspace `marcekrak`): skill `trello` en `.claude/skills/trello/`.
  El tablero central de operaciones es **Krak Studio**. Credenciales en
  `.env.trello` local (gitignoreado) — ver reglas de seguridad en la skill.
- **Google** (Gmail, Calendar, Drive) y **GitHub** vía conectores.
- Manual de procesos para el equipo: `docs/manual-conexion-trello.md`.

## Reglas de trabajo

- Seguridad de credenciales: nunca en chat, commits ni capturas. Si Marce pega
  una credencial en el chat, avisarle y pedirle que la regenere.
- Al resumir tableros de Trello: primero lo vencido y lo que vence pronto.
- El dominio `api.trello.com` está permitido en el entorno cloud.

## Memorias de tareas

(Sección que Marce va cargando — agregar entradas nuevas acá con fecha.)

- 2026-07-18: Se conectó la API de Trello, se creó la skill `trello` y el
  manual de procesos para el equipo.
