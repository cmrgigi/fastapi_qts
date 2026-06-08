def calcular_pontuacao_atendimento(tempo_minutos, resolvido_primeiro_contato, reincidencia):
    if tempo_minutos <=0:
        return 0
    
    if resolvido_primeiro_contato: 
        if tempo_minutos <=10:
            base = 10
        elif tempo_minutos <=20:
            base = 8
        else:
            base = 6
    else:
        if tempo_minutos <=10:
            base = 5
        elif tempo_minutos <=20:
            base = 3
        else:
            base = 1

    if reincidencia:
        base = base-2

    if base < 0:
        return 0
    
#print(calcular_pontuacao_atendimento(10, True, False))

def classificar_atendimento(pontuacao):
    if pontuacao >=9:
        return "Excelente"
    
    if pontuacao >=7:
        return "Bom"
    
    if pontuacao >=4:
        return "Regular"
    
    return "Crítico"

print(calcular_pontuacao_atendimento (9, True, False))
print(classificar_atendimento (3))
