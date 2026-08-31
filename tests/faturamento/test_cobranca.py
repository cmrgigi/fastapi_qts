import pytest

from app.faturamento.cobranca import processar_cobranca

@pytest.mark.parametrize(
    "valor_base, plano, dias_atraso, retorno_esperado",
    [
        (0, "basico", -1, -1.0), #1
        (-1.0, "basico", 0, -1.0), #2
        (2.0, "basico", -2, -1.0), #3
        (2.0, "basico", 0, 2.0), #4
        (4.0, "premium", 0, 3.6), #5
        (6.0, "empresarial", 0, 4.8), #6
        (3.0, "estudante", 0, -2.0), #7
        (3.0, "individual", 0, -2.0), #8
        (2.0, "basico", 1, 7.01), #9 
        (4.0, "premium", 1, 8.62), #10 
        (6.0, "empresarial", 1, 9.82), #11 
        (2.0, "basico", 30, 7.3), #,12
        (4.0, "premium", 30, 9.14), #13
        (6.0, "empresarial", 30, 10.52), #14 
        (2.0, "basico", 31, 27.62), #15
        (4.0, "premium", 31, 29.72), #16
        (6.0, "empresarial", 31, 31.29) #17
    ]
)
def test_classificar_cobranca_caixa_preta(
    valor_base, plano, dias_atraso, retorno_esperado
):
    assert processar_cobranca(valor_base, plano, dias_atraso) == retorno_esperado


import time

from app.faturamento.cobranca import processar_cobranca

def test_tempo_execucao_classificar_nao_funcional():
    inicio = time.perf_counter()
    resultado = processar_cobranca(6.0, "empresarial", 30)
    fim = time.perf_counter()
    tempo_decorrido = fim - inicio

    assert resultado > 0.0
    # Garante que executa em menos de 100 milissegundos
    assert tempo_decorrido < 0.08