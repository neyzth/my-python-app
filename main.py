"""
Module principal avec plusieurs fonctionnalités pour générer
une documentation utile.
"""


def add(a: int, b: int) -> int:
    """Retourne la somme de deux nombres."""
    return a + b


def subtract(a: int, b: int) -> int:
    """Retourne la différence entre deux nombres."""
    return a - b


def multiply(a: int, b: int) -> int:
    """Retourne le produit de deux nombres."""
    return a * b


def divide(a: int, b: int) -> float:
    """Retourne le quotient de deux nombres.
      Lève une exception en cas de division par zéro."""
    if b == 0:
        raise ValueError("Division par zéro non autorisée")
    return a / b


if __name__ == "__main__":
    print("Addition de 5 et 3:", add(5, 3))
    print("Soustraction de 10 et 4:", subtract(10, 4))
    print("Multiplication de 6 et 7:", multiply(6, 7))
    print("Division de 8 par 2:", divide(8, 2))
