import pytest
from geometria.geometria import classificar_triangulo
import re

# ------------------------------------VALIDANDO STRING ------------------------------------------------------

def test_isosceles():
    a = 3
    b = 5
    c = 3

    resultado = classificar_triangulo(a, b, c)
    assert resultado == ("Isósceles.")

def test_equilatero():
    a = 5
    b = 5
    c = 5

    resultado = classificar_triangulo(a, b, c)
    assert resultado == ("Equilátero.")

def test_escaleno():
    a = 3
    b = 2
    c = 4

    resultado = classificar_triangulo(a, b, c)
    assert resultado == ("Escaleno.")

# VALIDANDO STRING ------------------------------------------

# lado a
def test_classificar_string_A():
    # Definindo a entrada
    a = "oi"
    b = 10
    c = 3

    # Executando a função e esperando erro
    mensagem = "Lados devem ser numéricos."
    with pytest.raises(TypeError, match=re.escape(mensagem)):
        classificar_triangulo(a, b, c)

# lado b
def test_classificar_string_B():
    # Definindo a entrada
    a = 5
    b = "oi"
    c = 3

    # Executando a função e esperando erro
    mensagem = "Lados devem ser numéricos."
    with pytest.raises(TypeError, match=re.escape(mensagem)):
        classificar_triangulo(a, b, c)

# lado c
def test_classificar_string_C():
    # Definindo a entrada
    a = 5
    b = 10
    c = "oi"

    # Executando a função e esperando erro
    mensagem = "Lados devem ser numéricos."
    with pytest.raises(TypeError, match=re.escape(mensagem)):
        classificar_triangulo(a, b, c)

# VALIDANDO POSITIVO OU NEGATIVO
# lado A
def test_validar_negativo_A():
    # Definindo a entrada
    a = -5
    b = 10
    c = 3

    # Executando a função e esperando erro
    mensagem = "lados devem ser positivos."
    with pytest.raises(ValueError, match=re.escape(mensagem)):
        classificar_triangulo(a, b, c)

# lado B 
def test_validar_negativo_B():
    # Definindo a entrada
    a = 5
    b = -10
    c = 3

    # Executando a função e esperando erro
    mensagem = "lados devem ser positivos."
    with pytest.raises(ValueError, match=re.escape(mensagem)):
        classificar_triangulo(a, b, c)

# lado C
def test_validar_negativo_C():
    # Definindo a entrada
    a = 5
    b = 10
    c = -3

    # Executando a função e esperando erro
    mensagem = "lados devem ser positivos."
    with pytest.raises(ValueError, match=re.escape(mensagem)):
        classificar_triangulo(a, b, c)

# VALIDANDO SE É TRIÂNGULO OU NÃO ----------------------------------------

# A + B < C
def test_lado_ab_menor_c():
    a = 3
    b = 2
    c = 6

    # Executando a função e esperando erro
    mensagem = "Lados não formam um triângulo."
    with pytest.raises(ValueError, match=re.escape(mensagem)):
        classificar_triangulo(a, b, c)

# A + C < B
def test_lado_ac_menor_b():
    a = 3
    b = 6
    c = 2

    # Executando a função e esperando erro
    mensagem = "Lados não formam um triângulo."
    with pytest.raises(ValueError, match=re.escape(mensagem)):
        classificar_triangulo(a, b, c)

# B + C < A
def test_lado_bc_menor_a():
    a = 6
    b = 3
    c = 2

    # Executando a função e esperando erro
    mensagem = "Lados não formam um triângulo."
    with pytest.raises(ValueError, match=re.escape(mensagem)):
        classificar_triangulo(a, b, c)