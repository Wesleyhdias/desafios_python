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

print(f'O menor faturamento ocorrido foi de {round(valor_min, 2)} no dia {d_min}')
print(f'O maior faturamento ocorrido foi de {round(valor_max, 2)} no dia {d_max}')
print(f'e a média do faturamento mensal é de {round(media, 2)}')
