from app.descontos.descontos import calcular_desconto

def test_valor_invalido_zero():
    assert calcular_desconto(0, True) == 0

def test_cliente_vip_valor_valido():
    assert calcular_desconto(100, True) == 80

def test_cliente_nao_vip_valor_valido():
    assert calcular_desconto(100, False) == 90

def test_valor_zero():
    assert calcular_desconto(0, False) == 0

def test_valor_positivo_pequeno():
    assert calcular_desconto
    round(False, 3) == 0.009

def test_valor_positivo():
    assert calcular_desconto(200, True) == 160
