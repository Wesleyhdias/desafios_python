# dados fictícios para fazer a leitura
faturamentos = {'Sao Paulo': 67836.43, 'Rio de Janeiro': 36678.66, 'Minas Gerais': 29229.88, 
               'Espirito Santo': 27165.48, 'Outros': 19849.53}

# soma o faturamento para tirar as porcentagens individuais
soma = 0
for c in faturamentos.values():
    soma += c

# calcula as porcentagens individuais e printa na tela
for k, v in faturamentos.items():
    p = (faturamentos[k] / soma) * 100
    print(f'o faturamento de {k} corresponde a: {round(p, 2)}% do faturamento total')
