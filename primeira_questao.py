# dupla: Cauã Quintino e Abner Alexandre
# usuários no github: CauRoss e Ab_Alexandre

class Carros:
    def __init__(self, marca, modelo, ano, cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor

    def ligar(self):
        return f'O {self.modelo} está ligado.'
    
    def desligar(self):
        return f'O {self.modelo} está desligado.'
    
    def acelerar(self):
        return f'O {self.modelo} está acelerando.'
    
if __name__ == '__main__':
    carro1 = Carros('renault', 'sandero', '2016', 'branco')
    
    print(carro1.ligar())
    print(carro1.acelerar())
    print(carro1.desligar())