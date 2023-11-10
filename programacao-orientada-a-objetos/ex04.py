class Pessoa(object):

    def __init__(self, nome: str, idade: int, altura: float):
        self.nome = nome
        self.idade = idade
        self.altura = altura
    
    def saudacao(self):
        print(f'Olá {self.nome}, como você está?')
    
    def fazer_aniversario(self):
        idadeAntiga = self.idade
        self.idade += 1
        print(f'Parabéns {self.nome}, você tinha {idadeAntiga} anos e agora está com {self.idade}')
    
    def crescer(self):
        alturaAntiga = self.altura
        self.altura += 0.10
        print(f'Você acaba de ganhar 10cm de altura e agora está com {self.altura} de altura!')

class Estudante(Pessoa):
    
    def __init__(self, nome: str, idade: int, altura: float, curso: str):

        # Chamando o init da classe pai
        super().__init__(nome, idade, altura)
        self.curso = curso

    def exibir_informacoes(self):
        print(f'{self.nome} está estudando {self.curso}')

pessoa1 = Pessoa('Bruno', 24, 1.75)
estudante1 = Estudante('Joao', 18, 1.82, 'Computer Science')

estudante1.exibir_informacoes()
estudante1.saudacao()
