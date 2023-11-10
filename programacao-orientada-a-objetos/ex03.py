class Circulo(object):

    def __init__(self, raio: int):
        self.raio = raio
    
    def calcular_area(self):
        return 3.14159 * (self.raio * self.raio)
    
    def calcular_circunferencia(self):
        return (2 * 3.14159) * self.raio
    
circulo1 = Circulo(4)

area1 = circulo1.calcular_area()
print(f'Area do circulo: {area1}')

circunferencia1 = circulo1.calcular_circunferencia()
print(f'Circunferencia do circulo: {circunferencia1}')
