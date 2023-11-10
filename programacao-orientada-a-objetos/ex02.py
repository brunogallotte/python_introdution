class Retangulo(object):
    
    def __init__(self, largura: int, altura: int):
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        return self.largura * self.altura
    
    def calcular_perimetro(self):
        return 2 * (self.largura + self.altura)
    
retangulo1 = Retangulo(5, 3)

area1 = retangulo1.calcular_area()
print(f'Area do retangulo: {area1}')

perimetro1 = retangulo1.calcular_perimetro()
print(f'Perimetro do retangulo: {perimetro1}')
