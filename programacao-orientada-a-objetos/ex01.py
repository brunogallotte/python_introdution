class Ponto (object):

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
    
    def mostrar_coordenadas(self):
        print(f'As coordenadas sāo x: {self.x} e y: {self.y}')

ponto1 = Ponto(3, 4)

ponto1.mostrar_coordenadas()

ponto2 = Ponto(-1, 2)

ponto2.mostrar_coordenadas()
