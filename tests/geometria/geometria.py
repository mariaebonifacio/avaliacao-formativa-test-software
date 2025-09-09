def classificar_triangulo(a: float, b: float, c: float):
    # INT OU FLOAT---------------------------------
    # lado a
    if not isinstance(a, (int, float)):
        raise TypeError("Lados devem ser numéricos.")
    # lado b
    if not isinstance(b, (int, float)):
        raise TypeError("Lados devem ser numéricos.")
    # lado c
    if not isinstance(c, (int, float)):
        raise TypeError("Lados devem ser numéricos.")
    
    # POSITIVO OU NEGATIVO-------------------------
    # lado a
    if a < 0:
        raise ValueError("lados devem ser positivos.")
    # lado b
    if b < 0:
        raise ValueError("lados devem ser positivos.")
    # lado c
    if c < 0:
        raise ValueError("lados devem ser positivos.")
    
    # Para que os lados formem um triângulo, a soma de quaisquer dois lados deve ser maior que o terceiro lado
    # lado a
    if a + b < c:
        raise ValueError("Lados não formam um triângulo.")
    # lado b
    if a + c < b:
        raise ValueError("Lados não formam um triângulo.")
    # lado c
    if b + c < a:
        raise ValueError("Lados não formam um triângulo.")
    
    # Se todos os três lados forem iguais, a função deve retornar a string "Equilátero".
    if a == b and b == c and c == a:
        return "Equilátero."

    # Se exatamente dois lados forem iguais, a função deve retornar a string "Isósceles".
    elif a == b or b == c or c == a:
        return "Isósceles."

    # Se todos os três lados forem diferentes, a função deve retornar a string "Escaleno".
    else:
        "Escaleno"