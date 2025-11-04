# FastAPI Calculator

https://github.com/pavankumarNagaraju/fastapi-calculator.git

A neat FastAPI calculator with:
- Arithmetic API (`add`, `subtract`, `multiply`, `divide`, `power`, `modulo`)
- Minimal browser UI at `/`
- Logging (console + rotating file `logs/app.log` with request IDs)
- Tests: unit, integration, and Playwright end-to-end
- GitHub Actions CI (pytest with coverage + Playwright)

---

## Project Structure
app/
init.py
operations.py # all math functions
main.py # FastAPI app, routes, logging, tiny UI, /health
tests/
unit/ # tests for operations.py
integration/ # API tests for /api/* endpoints & /health
e2e/ # Playwright UI tests
.github/
workflows/
ci.yml # CI pipeline: pytest (with coverage) + Playwright
package.json
pytest.ini
requirements.txt
README.md


---

## Requirements
- **Python** 3.10+ (tested on 3.12)
- **Node.js** 18+ (for Playwright E2E)
- **Git** (to push and run CI on GitHub)

---

## Setup (Windows PowerShell)
```powershell
# from project root
. .\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt

Setup (macOS/Linux)
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt

Run the App
# either of these (inside the activated venv)
uvicorn app.main:app --reload
# OR (works even if PATH is funky)
python -m uvicorn app.main:app --reload


Open: http://127.0.0.1:8000
 (simple UI to test operations)

Health check: http://127.0.0.1:8000/health
 → {"status":"ok"}