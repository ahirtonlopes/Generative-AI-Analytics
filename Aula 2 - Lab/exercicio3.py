# Exercício 3 - Começando com Testes Unitários

def somar(a, b):
    return a + b

# Criar um teste unitário para a função somar

def test_somar():
    assert somar(2, 3) == 5
    assert somar(0, 0) == 0
    assert somar(-2, 2) == 0
    assert somar(-2, -2) == -4
    assert somar(2, -2) == 0
    assert somar(2, 0) == 2
    assert somar(0, 2) == 2
    assert somar(2, 2) == 4
    assert somar(2, 2) == 4
    assert somar(2, 2) == 4
    assert somar(2, 2) == 4
    assert somar(2, 2) == 4

test_somar()
print('Teste passou')



