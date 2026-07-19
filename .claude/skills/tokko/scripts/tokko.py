#!/usr/bin/env python3
"""Cliente de la API de Tokko Broker para la skill 'tokko'.

Credenciales: SOLO por variable de entorno TOKKO_API_KEY o archivo .env
(gitignoreado) en la raíz del repo o en ~. Nunca por argumentos ni en chat.

Uso:
  python3 tokko.py ping                      # verificar conexión
  python3 tokko.py properties [--limit 20]   # propiedades activas
  python3 tokko.py property <id>             # detalle de una propiedad
  python3 tokko.py search "texto"            # buscar propiedades
  python3 tokko.py raw "/property/?..."      # llamada cruda (para explorar la API)

Nota: la API v1 de Tokko (api.tokkobroker.com/api/v1/) usa el parámetro `key`.
El endpoint de propiedades es /property/. Otros recursos (contactos, leads)
dependen del plan/permisos de la key — explorar con `raw`.
"""
import json
import os
import sys
import urllib.parse
import urllib.request
from pathlib import Path

BASE = os.environ.get("TOKKO_BASE_URL", "https://api.tokkobroker.com/api/v1").rstrip("/")


def load_key():
    key = os.environ.get("TOKKO_API_KEY")
    if key:
        return key
    for path in (Path(__file__).resolve().parents[4] / ".env", Path.home() / ".env"):
        if path.is_file():
            for line in path.read_text().splitlines():
                if line.strip().startswith("TOKKO_API_KEY="):
                    return line.split("=", 1)[1].strip().strip('"')
    sys.exit(
        "ERROR: falta TOKKO_API_KEY. Definila como variable de entorno o en el "
        ".env (gitignoreado) de la raíz del repo."
    )


KEY = load_key()


def api(path, params=None):
    params = dict(params or {})
    params.setdefault("key", KEY)
    params.setdefault("format", "json")
    sep = "&" if "?" in path else "?"
    url = f"{BASE}{path}{sep}{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(url, headers={"Accept": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.load(resp)
    except urllib.error.HTTPError as e:
        # No imprimir la URL completa: contiene la key.
        sys.exit(f"ERROR HTTP {e.code} en {path}: {e.read().decode()[:300]}")


def fmt_property(p):
    op = ", ".join(
        f"{o.get('operation_type','?')} {c.get('currency','')} {c.get('price','')}"
        for o in p.get("operations", [])
        for c in o.get("prices", [])
    )
    loc = (p.get("location") or {}).get("name", "")
    return f"[{p.get('id')}] {p.get('publication_title') or p.get('address','(sin título)')} | {p.get('type',{}).get('name','')} | {loc} | {op}"


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    cmd, args = sys.argv[1], sys.argv[2:]

    if cmd == "ping":
        data = api("/property/", {"limit": 1})
        total = data.get("meta", {}).get("total_count", "?")
        print(f"Conexión OK — {total} propiedades en la cuenta")

    elif cmd == "properties":
        limit = args[args.index("--limit") + 1] if "--limit" in args else "20"
        data = api("/property/", {"limit": limit})
        for p in data.get("objects", []):
            print(fmt_property(p))
        meta = data.get("meta", {})
        print(f"-- mostrando {len(data.get('objects', []))} de {meta.get('total_count', '?')}")

    elif cmd == "property":
        p = api(f"/property/{args[0]}/")
        print(json.dumps(p, indent=2, ensure_ascii=False)[:6000])

    elif cmd == "search":
        data = api("/property/search/", {"query": args[0], "limit": 20})
        objs = data.get("objects", data if isinstance(data, list) else [])
        for p in objs:
            print(fmt_property(p))

    elif cmd == "raw":
        print(json.dumps(api(args[0]), indent=2, ensure_ascii=False)[:8000])

    else:
        sys.exit(f"Comando desconocido: {cmd}\n{__doc__}")


if __name__ == "__main__":
    try:
        main()
    except BrokenPipeError:
        sys.exit(0)
