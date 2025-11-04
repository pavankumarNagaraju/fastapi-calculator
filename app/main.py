from __future__ import annotations
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, field_validator
import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path
import uuid

from .operations import add, subtract, multiply, divide, power, modulo

# ---------- Logging ----------
LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)
logger = logging.getLogger("calculator")
logger.setLevel(logging.INFO)
fmt = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
fh = RotatingFileHandler(LOG_DIR / "app.log", maxBytes=500_000, backupCount=3)
fh.setFormatter(fmt)
sh = logging.StreamHandler()
sh.setFormatter(fmt)
if not logger.handlers:
    logger.addHandler(fh)
    logger.addHandler(sh)

# ---------- App ----------
app = FastAPI(title="FastAPI Calculator", version="1.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], allow_methods=["*"], allow_headers=["*"],
)

@app.middleware("http")
async def log_requests(request: Request, call_next):
    req_id = str(uuid.uuid4())[:8]
    logger.info(f"[{req_id}] Incoming {request.method} {request.url.path}")
    try:
        resp = await call_next(request)
        logger.info(f"[{req_id}] Completed {request.method} {request.url.path} -> {resp.status_code}")
        return resp
    except Exception:
        logger.exception(f"[{req_id}] Unhandled error")
        raise

class Operands(BaseModel):
    a: float
    b: float

    @field_validator("a", "b", mode="before")
    @classmethod
    def to_float(cls, v):
        try:
            return float(v)
        except Exception as e:
            raise ValueError("Operands must be numbers") from e

class Result(BaseModel):
    result: float

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/", response_class=HTMLResponse)
def root():
    return """
<!doctype html><html><head><meta charset="utf-8"><title>FastAPI Calculator</title></head>
<body>
  <h1>FastAPI Calculator</h1>
  <input id="a" placeholder="a" />
  <input id="b" placeholder="b" />
  <select id="op">
    <option value="add">add</option>
    <option value="subtract">subtract</option>
    <option value="multiply">multiply</option>
    <option value="divide">divide</option>
    <option value="power">power</option>
    <option value="modulo">modulo</option>
  </select>
  <button id="calc">Calculate</button>
  <div id="out" style="margin-top:8px"></div>
  <script>
    const go = async () => {
      const a = document.getElementById("a").value;
      const b = document.getElementById("b").value;
      const op = document.getElementById("op").value;
      const r = await fetch(`/api/${op}`, {
        method: "POST", headers: {"Content-Type": "application/json"},
        body: JSON.stringify({a, b})
      });
      const j = await r.json();
      document.getElementById("out").textContent = r.ok ? j.result : (j.detail || "error");
    };
    document.getElementById("calc").onclick = go;
  </script>
</body></html>
    """

@app.post("/api/add", response_model=Result)
def api_add(data: Operands):
    logger.info(f"ADD {data.a}, {data.b}")
    return Result(result=add(data.a, data.b))

@app.post("/api/subtract", response_model=Result)
def api_subtract(data: Operands):
    logger.info(f"SUBTRACT {data.a}, {data.b}")
    return Result(result=subtract(data.a, data.b))

@app.post("/api/multiply", response_model=Result)
def api_multiply(data: Operands):
    logger.info(f"MULTIPLY {data.a}, {data.b}")
    return Result(result=multiply(data.a, data.b))

@app.post("/api/divide", response_model=Result)
def api_divide(data: Operands):
    logger.info(f"DIVIDE {data.a}, {data.b}")
    try:
        return Result(result=divide(data.a, data.b))
    except ZeroDivisionError:
        logger.warning("Division by zero")
        raise HTTPException(status_code=400, detail="Division by zero")

@app.post("/api/power", response_model=Result)
def api_power(data: Operands):
    logger.info(f"POWER {data.a}, {data.b}")
    return Result(result=power(data.a, data.b))

@app.post("/api/modulo", response_model=Result)
def api_modulo(data: Operands):
    logger.info(f"MODULO {data.a}, {data.b}")
    try:
        return Result(result=modulo(data.a, data.b))
    except ZeroDivisionError:
        logger.warning("Modulo by zero")
        raise HTTPException(status_code=400, detail="Modulo by zero")
