from math import pi

class Circulo:
    def __init__(self, radio):
        if type(radio) not in [int, float]:
            raise TypeError(f'{type(radio)} no es un radio valido, intentalo nuevamente!')
        elif radio <= 0:
            raise ValueError('El radio tiene que ser mayor a 0')
        else:
            self.radio = radio

    def area(self):
        return pi*(self.radio**2)

    def perimetro(self):
        return 2*pi*self.radio

    def multiplicacion(self, n):
        if n <= 0:
            raise Exception('No es posible multiplicar por un numero menor o igual a 0')
        else:
            circle = Circulo(self.radio*n)
            return circle