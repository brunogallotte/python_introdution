variavel = lambda n1, n2: print(n1 + n2)

variavel(1, 2)
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numeros_pares = filter(lambda num: num % 2 == 0, numeros)

print(list(numeros_pares))
