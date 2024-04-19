class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def frear_carro(self):
        print(f"{self.modelo} esta freando")

    def acelerar(self):
        print(f"{self.modelo} esta acelerando")

class Carro(Veiculo):
    def __init__(self, cor, modelo):
        super().__init__(cor, modelo)
        self.cor = cor

    def abrir_porta(self):
        print(f"A porta do {self.modelo} aberta")

class Moto(Veiculo):
    def __init__(self, cilindrada, modelo):
        super().__init__(cilindrada, modelo)
        self.cilindrada = cilindrada

    def empinar_moto(self):
       print(f"a moto de {self.cilindrada} esta empinando")

if __name__ == "__main__":
    veiculo1 = Veiculo("Renault","Corsa")
    print(veiculo1.marca)
    print(veiculo1.modelo)

    pessoa2 = Carro("vermelho", "Corsa")
    print(pessoa2.cor)
    pessoa2.abrir_porta()
    pessoa2.acelerar()
    pessoa2.frear_carro()

    pessoa3 = Moto("220", "Honda")
    pessoa3.empinar_moto()