# Manual de procesos: conectar tu Trello con Claude

**Equipo Krak Studio** · Versión 1.0 · Julio 2026

Este manual explica cómo conectar tu cuenta de Trello a Claude Code para poder pedirle resúmenes de tableros, ver tarjetas vencidas y crear tareas desde el chat. Sigue el proceso que ya probamos y funciona.

---

## Qué vas a lograr

Una vez conectado, podés pedirle a Claude cosas como:

- "¿Qué hay vencido en Krak Studio?"
- "Resumime el tablero de Tienda Tool"
- "Agregá una tarjeta a Tareas que diga X, vence el viernes"

---

## Paso 1: Conseguir tu Clave de API de Trello

⚠️ **Ojo con esta confusión** (nos pasó): la página de "Tokens de API" de **id.atlassian.com NO sirve** para Trello, aunque Trello sea de Atlassian. Esos tokens son para Jira/Confluence.

El lugar correcto es:

1. Entrá a **https://trello.com/power-ups/admin**
2. Creá un Power-Up nuevo (nombre sugerido: "Claude Assistant"). No hace falta completar nada más que el nombre y el workspace.
3. Entrá al Power-Up creado → menú **"Clave de API"**
4. Copiá la **Clave de API** (un código de 32 caracteres)

## Paso 2: Generar tu Token

1. En esa misma pantalla, a la derecha hay un texto que dice *"puedes generar de manera manual un token"* — hacé clic en el link **"token"**
2. Autorizá la aplicación con tu cuenta de Trello
3. Copiá el **Token** (un código largo que empieza con `ATTA...`)

Ya tenés las dos credenciales que necesitás: **Clave de API** + **Token**.

## Paso 3: Reglas de seguridad (leer antes de seguir)

Estas credenciales dan acceso total a tus tableros. Tratalas como una contraseña:

| ❌ Nunca | ✅ Siempre |
|---|---|
| Pegarlas en un chat (ni siquiera con Claude) | Guardarlas en un archivo `.env.trello` local |
| Subirlas a un repositorio de git | Verificar que `.env.trello` esté en `.gitignore` |
| Mandarlas por WhatsApp/Slack/mail | Pasarlas solo por un gestor de contraseñas si hay que compartirlas |
| Ponerlas en capturas de pantalla | Tapar/recortar credenciales antes de compartir capturas |

**Si una credencial se expuso** (la pegaste en un chat, quedó en una captura, la mandaste por error): no entres en pánico, pero **regenerá el token ya mismo** desde la misma página donde lo creaste. El viejo deja de funcionar y listo.

## Paso 4: Configurar el entorno de Claude Code

### 4a. Permitir el dominio de la API

Si usás Claude Code en la nube (claude.ai/code) con acceso a red "Personalizado":

1. Abrí la configuración del entorno → **"Acceso a la red"**
2. En **"Dominios permitidos"** agregá una línea que diga: `api.trello.com` (sin `https://`, sin barras)
3. Guardá. Los cambios aplican a las sesiones nuevas.

Sin este paso, Claude no puede llegar a la API de Trello y todo lo demás falla.

⚠️ **No pongas la clave ni el token en el campo "Variables de entorno"** de esa misma pantalla: la propia interfaz avisa que son visibles para cualquiera que use el entorno.

### 4b. Crear el archivo de credenciales

En la raíz del proyecto (o en tu carpeta home), creá un archivo llamado `.env.trello` con exactamente estas dos líneas:

```
TRELLO_API_KEY=tu_clave_de_api
TRELLO_TOKEN=tu_token
```

Y asegurate de que el `.gitignore` del proyecto incluya:

```
.env.trello
.env
```

En el repo MarceClaude esto ya está configurado. Podés pedirle a Claude: *"creá el archivo .env.trello, te dicto los valores"* — pero dictáselos en el momento de crear el archivo, no los dejes escritos en la conversación.

## Paso 5: Probar la conexión

Pedile a Claude que verifique la conexión, o corré directamente:

```bash
python3 .claude/skills/trello/scripts/trello.py whoami
```

Si responde con tu nombre y usuario de Trello, está todo conectado. ✅

## Comandos disponibles (skill `trello`)

```bash
python3 .claude/skills/trello/scripts/trello.py whoami                  # verificar conexión
python3 .claude/skills/trello/scripts/trello.py boards                  # tableros abiertos
python3 .claude/skills/trello/scripts/trello.py summary "Krak Studio"   # resumen por listas
python3 .claude/skills/trello/scripts/trello.py overdue "Krak Studio"   # solo vencidas
python3 .claude/skills/trello/scripts/trello.py cards "Krak Studio" "En proceso"
python3 .claude/skills/trello/scripts/trello.py add-card "Krak Studio" "Tareas" "Título" --due 2026-08-01
```

Los nombres de tablero y lista aceptan coincidencia parcial y no distinguen mayúsculas ("krak studio", "proceso").

## Problemas frecuentes

**"ERROR: faltan credenciales"** → No existe el `.env.trello` o le falta una de las dos líneas. Revisá el Paso 4b.

**Error de red / timeout** → El dominio `api.trello.com` no está permitido en el entorno. Revisá el Paso 4a.

**HTTP 401** → El token es inválido o fue regenerado. Generá uno nuevo (Paso 2) y actualizá el `.env.trello`.

**HTTP 400 con "invalid key"** → La clave de API está mal copiada. Revisá el Paso 1.

**"No encontré el tablero X"** → El script lista los tableros abiertos disponibles en el mensaje de error; fijate si el nombre coincide o si el tablero está archivado.

---

*Este manual sale de la sesión de conexión real del 18/07/2026. Si algo cambió en las pantallas de Trello, avisá para actualizarlo.*
