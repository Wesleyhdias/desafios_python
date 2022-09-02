res = input('digite uma string qualquer: ')
ser = ''
for c in range((len(res)-1), -1, -1):
    ser += res[c]
    
print(f'se invertermos a string "{res}" teremos "{ser}"')
