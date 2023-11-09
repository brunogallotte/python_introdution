preco = 132.85
pessoas = 0

try:
    valor_por_pessoa = preco / pessoas
    print(valor_por_pessoa)
except ZeroDivisionError:
    print('Numero de pessoas inválido!')

