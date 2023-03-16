from datetime import date

def calcular_idade(data_nascimento):
    hoje = date.today()
    idade = hoje.year - data_nascimento.year - ((hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day))
    return idade

# Exemplo de uso:
data_nascimento = date(2006, 12, 19)
idade = calcular_idade(data_nascimento)
print(f"A idade da pessoa é {idade} anos.")