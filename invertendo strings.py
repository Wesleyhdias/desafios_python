# modo sem utilizar nada "pré-prondo" da linguagem

res = input('digite uma string qualquer para ser invertida: ')
ser = ''
for c in range((len(res)-1), -1, -1):
    ser += res[c]
    
print(f'O resultado é: \"{res}\" teremos \"{ser}\"\nisso foi feito com o laço \'for\'')

# usando a propria linguagem(fatiamento de strings)

print(f'usando fatiamento de strings do python temos: {res[::-1]}\ncom apenas uma linha, o mesmo resultado!')
