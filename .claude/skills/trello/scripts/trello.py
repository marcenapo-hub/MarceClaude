#!/usr/bin/env python3
"""Cliente de la API de Trello para la skill 'trello'.

Credenciales: SOLO por variables de entorno o archivo .env.trello (gitignoreado).
Nunca aceptan pasarse por argumento de línea de comandos, para que no queden
en el historial de shell ni en logs de herramientas.

Uso:
  python3 trello.py whoami
  python3 trello.py boards
  python3 trello.py summary "Krak Studio"
  python3 trello.py overdue "Krak Studio"
  python3 trello.py cards "Krak Studio" "En proceso"
  python3 trello.py add-card "Krak Studio" "Tareas" "Título" [--desc "..."] [--due YYYY-MM-DD]
"""
import json
import os
import sys
import urllib.parse
import urllib.request
from collections import defaultdict
from datetime import date
from pathlib import Path

API = "https://api.trello.com/1"


def load_credentials():
    """Busca credenciales en el entorno y luego en archivos .env.trello conocidos."""
    key = os.environ.get("TRELLO_API_KEY")
    token = os.environ.get("TRELLO_TOKEN")
    if key and token:
        return key, token
    candidates = [
        Path(__file__).resolve().parents[4] / ".env.trello",  # raíz del repo
        Path.home() / ".env.trello",
    ]
    for path in candidates:
        if path.is_file():
            for line in path.read_text().splitlines():
                line = line.strip()
                if line.startswith("TRELLO_API_KEY="):
                    key = key or line.split("=", 1)[1].strip().strip('"')
                elif line.startswith("TRELLO_TOKEN="):
                    token = token or line.split("=", 1)[1].strip().strip('"')
        if key and token:
            return key, token
    sys.exit(
        "ERROR: faltan credenciales. Definí TRELLO_API_KEY y TRELLO_TOKEN como "
        "variables de entorno, o creá un archivo .env.trello (gitignoreado) en la "
        "raíz del repo o en ~ con esas dos líneas."
    )


KEY, TOKEN = load_credentials()


def api(path, params=None, method="GET"):
    params = dict(params or {})
    params.update({"key": KEY, "token": TOKEN})
    url = f"{API}{path}?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(url, method=method)
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.load(resp)
    except urllib.error.HTTPError as e:
        # Nunca imprimir la URL completa: contiene key y token.
        sys.exit(f"ERROR HTTP {e.code} en {path}: {e.read().decode()[:200]}")


def find_board(name):
    boards = api("/members/me/boards", {"fields": "name,closed"})
    matches = [b for b in boards if name.lower() in b["name"].lower() and not b["closed"]]
    if not matches:
        abiertos = ", ".join(b["name"] for b in boards if not b["closed"])
        sys.exit(f"No encontré el tablero '{name}'. Tableros abiertos: {abiertos}")
    if len(matches) > 1:
        sys.exit("Coincide con varios: " + ", ".join(b["name"] for b in matches))
    return matches[0]


def board_data(name):
    board = find_board(name)
    lists = api(f"/boards/{board['id']}/lists", {"fields": "name"})
    cards = api(
        f"/boards/{board['id']}/cards",
        {"fields": "name,idList,due,dueComplete,labels"},
    )
    return board, {l["id"]: l["name"] for l in lists}, cards


def fmt_card(c, today):
    due = (c.get("due") or "")[:10]
    flag = ""
    if due and not c["dueComplete"]:
        flag = " [VENCIDA]" if due < today else f" (vence {due})"
    labels = ",".join(lb["name"] for lb in c.get("labels", []) if lb.get("name"))
    return f"{c['name']}{flag}" + (f" [{labels}]" if labels else "")


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    cmd, args = sys.argv[1], sys.argv[2:]
    today = date.today().isoformat()

    if cmd == "whoami":
        me = api("/members/me", {"fields": "fullName,username"})
        print(f"{me['fullName']} (@{me['username']})")

    elif cmd == "boards":
        for b in api("/members/me/boards", {"fields": "name,closed"}):
            if not b["closed"]:
                print(b["name"])

    elif cmd == "summary":
        board, lists, cards = board_data(args[0])
        by_list = defaultdict(list)
        for c in cards:
            by_list[c["idList"]].append(c)
        print(f"# {board['name']} — {len(cards)} tarjetas\n")
        for lid, lname in lists.items():
            items = by_list.get(lid, [])
            print(f"## {lname} ({len(items)})")
            # La lista de terminadas suele ser enorme: solo el conteo.
            if len(items) > 60:
                print("  (lista larga: solo conteo)\n")
                continue
            for c in items:
                print("  -", fmt_card(c, today))
            print()

    elif cmd == "overdue":
        board, lists, cards = board_data(args[0])
        done_lists = {
            lid for lid, ln in lists.items()
            if ln.lower() in ("terminado", "done", "hecho", "completado")
        }
        found = False
        for c in cards:
            due = (c.get("due") or "")[:10]
            if c["idList"] in done_lists:
                continue
            if due and due < today and not c["dueComplete"]:
                print(f"- [{lists.get(c['idList'], '?')}] {c['name']} (venció {due})")
                found = True
        if not found:
            print("Sin tarjetas vencidas 🎉")

    elif cmd == "cards":
        board, lists, cards = board_data(args[0])
        wanted = [lid for lid, ln in lists.items() if args[1].lower() in ln.lower()]
        if not wanted:
            sys.exit("Listas disponibles: " + ", ".join(lists.values()))
        for c in cards:
            if c["idList"] in wanted:
                print("-", fmt_card(c, today))

    elif cmd == "add-card":
        board, lists, _ = board_data(args[0])
        wanted = [lid for lid, ln in lists.items() if args[1].lower() in ln.lower()]
        if not wanted:
            sys.exit("Listas disponibles: " + ", ".join(lists.values()))
        params = {"idList": wanted[0], "name": args[2]}
        rest = args[3:]
        for flag, param in (("--desc", "desc"), ("--due", "due")):
            if flag in rest:
                params[param] = rest[rest.index(flag) + 1]
        card = api("/cards", params, method="POST")
        print(f"Creada: {card['name']} → {card['shortUrl']}")

    else:
        sys.exit(f"Comando desconocido: {cmd}\n{__doc__}")


if __name__ == "__main__":
    try:
        main()
    except BrokenPipeError:
        sys.exit(0)
