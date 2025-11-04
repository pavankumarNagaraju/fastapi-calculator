from __future__ import annotations

def add(a: float, b: float) -> float:
    return float(a) + float(b)

def subtract(a: float, b: float) -> float:
    return float(a) - float(b)

def multiply(a: float, b: float) -> float:
    return float(a) * float(b)

def divide(a: float, b: float) -> float:
    b = float(b)
    if b == 0.0:
        raise ZeroDivisionError("Division by zero")
    return float(a) / b

def power(a: float, b: float) -> float:
    return float(a) ** float(b)

def modulo(a: float, b: float) -> float:
    b = float(b)
    if b == 0.0:
        raise ZeroDivisionError("Modulo by zero")
    return float(a) % b
