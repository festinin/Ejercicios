"""
1. definir una funcion max()mque tome como 
argumento dos numeros y devuelva el mayor de ellos.
"""

def custon_max(n1: int, n2: int) -> int:
    """
    Dado dos numeros de entrada retorna el maximo de ambos

    Args:
    n1 (int): Primer numero
    n2(int): segundo numero

    Returns:
    int: Mayor de ambos

    """

    if n2 > n1:
        return n2
    elif n1 > n2: 
        return n1
    else:
        raise Exception("no cumple")

print(custon_max(37, 3))