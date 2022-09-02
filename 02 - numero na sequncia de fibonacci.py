n1 = n3 = 0
n2 = 1
n3 = 0
s = 'S'

while s[0] == 'S':
    while True:
        try:
            res = int(input('digite um numero inteiro para saber se\n'
                            'ele faz parte da sequencia de fibonacci que inicia com 0 e 1: '))
        except ValueError:
            print('digite somente um numero inteiro: ')
        else:
            break
        
    while n3 <= res:
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        
    if res == n1 or res == n2 or res == n3:
        print('esse numero FAZ parte da sequncia de fibonacci que inicia com 0 e 1')
    else:
        print('esse numero NÃO FAZ parte da sequncia de fibonacci que inicia com 0 e 1')
        
    while True:
        s = input("escolher outro numero?(S/N): ").upper()
        if s[0] != 'S' and s[0] != 'N':
            print("escolha apenas entre 'S' ou 'N'")
        else:
            break
    