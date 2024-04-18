class Retangulo:
    def __init__(self, altura, largura):
        self.altura = altura
        self.largura = largura

    def calcular_area(self):
        return f' A area é igual a: {self.altura * self.largura}'
    
    def perimetro_retangulo(self):
        return f'o perimetro do retangulo é igual a: {self.altura + self.largura}'
    
if __name__ == '__main__':
    forma1 = Retangulo(12, 10)
    
    print(forma1.calcular_area())
    print(forma1.perimetro_retangulo())
