from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def post(op, a, b):
    return client.post(f"/api/{op}", json={"a": a, "b": b})

def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"

def test_add():
    r = post("add", 2, 3)
    assert r.status_code == 200
    assert r.json()["result"] == 5.0

def test_subtract():
    r = post("subtract", 5, 2)
    assert r.status_code == 200
    assert r.json()["result"] == 3.0

def test_multiply():
    r = post("multiply", 2, 4.5)
    assert r.status_code == 200
    assert r.json()["result"] == 9.0

def test_divide_ok():
    r = post("divide", 9, 3)
    assert r.status_code == 200
    assert r.json()["result"] == 3.0

def test_divide_by_zero():
    r = post("divide", 1, 0)
    assert r.status_code == 400
    assert r.json()["detail"] == "Division by zero"

def test_power():
    r = post("power", 2, 4)
    assert r.status_code == 200
    assert r.json()["result"] == 16.0

def test_modulo_ok():
    r = post("modulo", 10, 4)
    assert r.status_code == 200
    assert r.json()["result"] == 2.0

def test_modulo_by_zero():
    r = post("modulo", 1, 0)
    assert r.status_code == 400
    assert r.json()["detail"] == "Modulo by zero"
