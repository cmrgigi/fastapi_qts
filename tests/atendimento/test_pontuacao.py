from app.atendimento.pontuacao import calcular_pontuacao_atendimento, classificar_atendimento

def test_tempo_minutos_igual_zero():
    assert calcular_pontuacao_atendimento (0, True, False) == 0

def test_tempo_minutos_menos_tres():
    assert calcular_pontuacao_atendimento (-3, False, False) == 0

def test_tempo_minutos_igual_dez():
    assert calcular_pontuacao_atendimento (10, True, False) == 10

def test_tempo_minutos_igual_onze():
    assert calcular_pontuacao_atendimento (11, True, False) == 8

def test_tempo_minutos_igual_vinte():
    assert calcular_pontuacao_atendimento (20, True, False) == 8

def test_tempo_minutos_igual_dez_sem_primeiro_contato():
    assert calcular_pontuacao_atendimento (10, True, False) == 5

def test_tempo_minutos_igual_quinze_sem_primeiro_contato():
    assert calcular_pontuacao_atendimento (5, False, True) == 3

def test_tempo_minutos_igual_vinteecinco_sem_primeiro_contato():
    assert calcular_pontuacao_atendimento (25, False, True) == 0




def test_classificar_atendimento_excelente():
    resultado = calcular_pontuacao_atendimento (10, True, False)
    assert classificar_atendimento (resultado)  == "Excelente"

def test_classificar_atendimento_bom():
    resultado = calcular_pontuacao_atendimento (8, True, False)
    assert classificar_atendimento (resultado)  == "Bom"

def test_classificar_atendimento_regular():
    resultado = calcular_pontuacao_atendimento (6, True, False)
    assert classificar_atendimento (resultado)  == "Regular"

def test_classificar_atendimento_critico():
    resultado = calcular_pontuacao_atendimento (3, False, False)
    assert classificar_atendimento (resultado)  == "Crítico"