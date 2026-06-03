
def calcular_pontuacao_atendimento(tempo_minutos, resolvido_primeiro_contato, reincidencia):
    if tempo_minutos <=0:
        return 0
    if resolvido_primeiro_contato and tempo_minutos <=10: 
        base=10
    if resolvido_primeiro_contato and 11 <= tempo_minutos <= 20:
        base=8
    if resolvido_primeiro_contato and tempo_minutos >20:
        base=6
    if resolvido_primeiro_contato == False and tempo_minutos <=10:
        base=5
    if resolvido_primeiro_contato == False and 11 <= tempo_minutos <=20:
        base=3
    if resolvido_primeiro_contato == False and tempo_minutos >20:
        base=1
    if reincidencia:
        base = base-2

    return base

def classificar_atendimento(pontuacao):
    if pontuacao >=9:
        return "Excelente"
    if pontuacao >=7:
        return "Bom"
    if pontuacao >=4:
        return "Regular"
    return "Crítico"


    
