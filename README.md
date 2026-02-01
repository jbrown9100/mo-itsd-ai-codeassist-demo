# AI Code Assist Demo Repo (GitHub Copilot)

This repository is a **self-contained demo sandbox** designed to help you demonstrate how **GitHub Copilot** supports **11 common use cases** for software modernization and code assistance.

> Tip: For the smoothest demo, open the repo in **VS Code** with Copilot enabled and keep the **Copilot Chat** panel visible.

## Quick start (local)

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
pytest -q
python -m src.app
```

Open: http://127.0.0.1:5000

## Where to look

- Use case cards + prompts: `docs/use-case-cards.md`
- Technical design template: `docs/technical-design-template.md`
- Monolith for decomposition: `src/legacy/monolith.py`
- COBOL snippet for conversion: `legacy/cobol/ELIGCALC.cbl`

## Notes on security

This repo includes intentionally insecure examples for demonstration:
- SQL injection-style query (`src/data/db.py`)
- Template safety / XSS risk (`src/templates/search.html`)

If GitHub Code Security / GHAS is enabled, you can also use:
- `.github/workflows/codeql.yml`
- `docs/ghas-demo.md`
