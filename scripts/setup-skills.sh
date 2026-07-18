#!/usr/bin/env bash
# =============================================================================
# Setup de Skills/Plugins para Claude Code — Marcelo Napolitano (Krak / VAV / Rebis)
# =============================================================================
# CÓMO USAR:
#   1. Instalá Claude Code si todavía no lo tenés: npm install -g @anthropic-ai/claude-code
#   2. Corré `claude` una vez en tu terminal para loguearte.
#   3. Ejecutá este script: bash setup-skills.sh
#      (o pegá los comandos uno por uno dentro de una sesión de `claude` con /plugin ...)
#
# Todos los comandos de abajo están verificados contra los repos oficiales
# (anthropics/skills, anthropics/knowledge-work-plugins, anthropics/claude-plugins-official,
# twilio/ai) al 18/07/2026. Si algún plugin cambió de nombre, corré
# `claude plugin marketplace list` para ver el catálogo actualizado.
# =============================================================================

set -e

echo "== 1) Skills de documentos (docx, pdf, pptx, xlsx) + ejemplos (frontend-design, etc.) =="
claude plugin marketplace add anthropics/skills
claude plugin install document-skills@anthropic-agent-skills
claude plugin install example-skills@anthropic-agent-skills

echo "== 2) Bright Data (scraping — el mismo que usamos para la base de empresas industriales) =="
# Ya viene precargado en el marketplace oficial de Claude Code, no hace falta agregarlo
claude plugin install brightdata-plugin@claude-plugins-official

echo "== 3) Twilio (relevante para el bot de WhatsApp de Rebis España) =="
claude plugin marketplace add twilio/ai
claude plugin install twilio-developer-kit@twilio
# Si el plugin no trae el MCP embebido, agregalo aparte:
claude mcp add --transport http twilio-docs https://mcp.twilio.com/docs

echo "== 4) Paquete de Knowledge Work Plugins (sales, marketing, finance, hr, data, product-management, design, operations, brand-voice, productivity) =="
claude plugin marketplace add anthropics/knowledge-work-plugins
claude plugin install sales@knowledge-work-plugins
claude plugin install marketing@knowledge-work-plugins
claude plugin install finance@knowledge-work-plugins
claude plugin install human-resources@knowledge-work-plugins
claude plugin install data@knowledge-work-plugins
claude plugin install product-management@knowledge-work-plugins
claude plugin install design@knowledge-work-plugins
claude plugin install operations@knowledge-work-plugins
claude plugin install brand-voice@knowledge-work-plugins
claude plugin install productivity@knowledge-work-plugins

echo "== LISTO =="
echo "Corré 'claude plugin list' para confirmar que todo quedó instalado."
echo "Los nombres exactos de los paquetes 4) pueden variar levemente — si alguno falla,"
echo "corré 'claude' y usá el menú interactivo '/plugin' para buscarlo por nombre."
