import json
import os

valor_max = valor_min = soma = d = 0

defalt_dir = os.path.dirname(__file__)
json_dir = os.path.join(defalt_dir, "dados.json")


with open(json_dir, encoding='utf-8') as json_data:
    dados = json.load(json_data) 
    
for c in dados:
    if c["valor"] > 0:
        if c["valor"] > valor_max:
            valor_max = c["valor"]
            d_max = c["dia"]
        if c["valor"] < valor_min:
            valor_min = c["valor"]
            d_min = c["dia"]
        elif valor_min <= 0:
            valor_min = valor_max
        soma += c["valor"]
        d += 1

media = soma / d

for c in dados:
    print (f'dia: {c["dia"]} e valor: {round(c["valor"], 2)})')

print(f'O menor faturamento ocorrido foi de {round(valor_min, 2)} no dia {d_min}')
print(f'O maior faturamento ocorrido foi de {round(valor_max, 2)} no dia {d_max}')
print(f'E a média do faturamento mensal é de {round(media, 2)}, considerando apenas os dias úteis')

while True:
    res = input('gostaria de ver o faturamento de um dia em especifico?(S/N)').upper()
    if res[0] == 'S':
        dia = int(input('qual é o dia que deseja saber? '))
        data = dados[dia - 1]
        print(f'O faturamento no dia {dia} foi de: R${data["valor"]}')
    elif res[0] == 'N':
        print('Obrigado, Programa encerrado')
        break
    else:
        print('digite somente \'S\' ou \'N\'!')
