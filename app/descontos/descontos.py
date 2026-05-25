def calcular_desconto(valor, cliente_vip):
    if valor <= 0:
        return 0
    if cliente_vip:
        return valor - (valor *0.20)
    return valor - valor *0.10
