meses = ('janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 
         'agosto', 'setembro', 'outubro', 'novembro', 'dezembro')
s = 'S'

while s[0] == 'S':
    try:
        num = int(input("digite um numero para saber seu mes correspondente: "))
    except:
        print('digite apenas numeros!')
        
    if num > 12 or num <= 0:
        print("esse número não corresponde a nenhum mes")
    else:
        for c in range(1, 13):
            if num == c:
                print(f"o numero {num} corresponde ao mes {meses[c-1]}")
                
    while True:
        s = input("escolher outro numero?(S/N): ").upper()
        if s[0] != 'S' and s[0] != 'N':
            print("escolha apenas entre 'S' ou 'N'")
        else:
            break
        
    while True:
        s = input("escolher outro numero?(S/N): ").upper()
        if s[0] != 'S' and s[0] != 'N':
            print("escolha apenas entre 'S' ou 'N'")
        else:
            break