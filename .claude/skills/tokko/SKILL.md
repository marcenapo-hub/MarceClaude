---
name: tokko
description: Consultar el CRM inmobiliario Tokko Broker de Krak Real Estate vía API. Usar cuando el usuario pregunte por propiedades en cartera, publicaciones, precios, el pipeline comercial de Krak RE, o mencione Tokko — aunque no lo nombre explícitamente (ej. "¿cuántas propiedades tenemos activas?", "buscá el depto de Gorostiaga en el CRM").
---

# Tokko Broker

Cliente de la API v1 de Tokko Broker (CRM inmobiliario de Krak Real Estate y Rebis).

## Uso

```bash
python3 .claude/skills/tokko/scripts/tokko.py ping                    # verificar conexión
python3 .claude/skills/tokko/scripts/tokko.py properties --limit 20   # cartera
python3 .claude/skills/tokko/scripts/tokko.py property <id>           # detalle
python3 .claude/skills/tokko/scripts/tokko.py search "Gorostiaga"     # búsqueda
python3 .claude/skills/tokko/scripts/tokko.py raw "/contact/"         # explorar API
```

## Credenciales — reglas de seguridad

- `TOKKO_API_KEY` por variable de entorno o `.env` gitignoreado (raíz del repo
  o `~`). Nunca en chat, commits ni argumentos de línea de comandos.
- Si la key se expone, pedir una nueva a soporte de Tokko Broker.

## Requisitos del entorno

- Dominio `api.tokkobroker.com` debe estar en los dominios permitidos del
  entorno cloud (Acceso a la red → Personalizado). **Verificar con `ping`**;
  si falla con error de red/403 del proxy, falta permitir el dominio.

## Contexto

- Pipeline comercial de Krak RE en Tokko: 7 estados con SLAs y lógica de
  colores (configurado por Marce).
- La API v1 es de solo lectura para la mayoría de los recursos con key simple.
- Endpoints útiles: `/property/` (cartera), `/property/search/`, `/contact/`
  (según permisos de la key). Explorar con `raw` y documentar acá lo aprendido.
