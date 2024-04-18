class Triangulo:
    def __init__(self, lado1, lado2, lado3, areat, perimetrot):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
        self.areat = areat
        self.perimetrot = perimetrot
    
    def area(self):
        return f'A área do triângulo é: {self.areat}'
    
    def perimetro(self):
        return f'O perímetro do triângulo é: {self.perimetrot}'
    
if __name__ == '__main__':
    triangulo1 = Triangulo('4', '4', '5', '30 cm²', '13 cm')
    
    print(triangulo1.area())    
    print(triangulo1.perimetro())