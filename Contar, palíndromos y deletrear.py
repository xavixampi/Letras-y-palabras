#Inicio
print('Bienvenido a mi programa')
inicio=input('Pulsa 1 para contar palabras, Pulsa 2 para comprobar palindromos, Pulsa 3 para deletrear|')

#Contador de palabras
if inicio == ('1'):
    Texto1 = input('Introduce el texto:')
    Contador=(len (Texto))
    print('Este texto tiene', Contador,'caracteres')

#palindromos
if inicio == ('2'):
    Cadena1 = input('Introduce la palabra:')
    Cadena2 = Cadena1[::-1]
    print(Cadena1, 'al revés es', Cadena2)
    if Cadena1==Cadena2:
        print('Por lo tanto', Cadena1,'es un  palindromo')
    else:
        print('Por lo tanto', Cadena1, 'no es un  palindromo')

#Deletrear
if inicio==('3'):
    Deletrear=input('Escribe tu palabra:')
    palabra=Deletrear
    for (palabra) in (Deletrear):
        print(palabra)
