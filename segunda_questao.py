class Animal:
    def __init__(self, nome, idade, especie):
        self.nome = nome
        self.idade = idade
        self.especie = especie

    def emitir_som(self):
        return f'O {self.especie} com o nome de {self.nome} está emitindo um som.'
    
    def informacoes(self):
        return f'Espécie do animal: {self.especie} \n Nome do animal: {self.nome} \n Idade do animal: {self.idade}'
    
if __name__ == '__main__':
    animal1 = Animal('John', '2 anos', 'macaco')
    
    print(animal1.emitir_som())
    print(animal1.informacoes())

    
