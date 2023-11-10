#import sleep from time

# Criando uma classe

class Pessoa(object):
    
    def __init__(self, nome: str, idade: int, documento: str):
        self.nome = nome
        self.idade = idade
        self.documento = documento

    def dormir(self, horas: int) -> None:
        for hora in range(1, horas+1):
            print(f'Dormindo por {hora} horas')
            #sleep(1)
    
    def falar(self, texto:str) -> None:
        print(texto)
    
    def __str__(self) -> str:
        return f'{self.nome}, {self.idade} anos e documento numero {self.documento}'
    
bruno = Pessoa(nome='Bruno', idade=24, documento='171.495.817-57')
