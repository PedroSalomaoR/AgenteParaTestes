import pytes

def test_soma_sucesso():
    # Teste de soma com números positivos
    assert soma(2, 3) == 5
    # Teste de soma com números negativos
    assert soma(-2, -3) == -5
    # Teste de soma com números mistos
    assert soma(-2, 3) == 1

def test_soma_falha():
    # Teste de soma com tipos incorretos
    with pytest.raises(TypeError):
        soma("a", 2)

def test_subtracao_sucesso():
    # Teste de subtração com números positivos
    assert subtracao(5, 3) == 2
    # Teste de subtração com números negativos
    assert subtracao(-5, -3) == -2
    # Teste de subtração com números mistos
    assert subtracao(-5, 3) == -8

def test_subtracao_falha():
    # Teste de subtração com tipos incorretos
    with pytest.raises(TypeError):
        subtracao("a", 2)