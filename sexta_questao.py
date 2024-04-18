class Pessoa:
    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura

    def definir(self):
        return f'Seu nome é:{self.nome}, sua idade:{self.idade}, você tem {self.altura} de altura.'
    
    def obter_informacoes(self):
        return f'{self.nome} tem {self.idade} e {self.altura} de altura'
    
    def cumprimentar(self):
        return f'{self.nome} cumprimentou você'
    
if __name__ == '__main__':
    ser = Pessoa('John', '15 anos', '1,70m')
    
    print(ser.definir())
    print(ser.obter_informacoes())
    print(ser.cumprimentar())