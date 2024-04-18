class Pedido:
    def __init__(self, itens_do_pedido, total_a_ser_pago, status_do_pedido):
        self.itens_pedido = itens_do_pedido
        self.total = total_a_ser_pago
        self.status = status_do_pedido

    def pedido(self):
        return f'O {self.especie} com o nome de {self.nome} está emitindo um som.'
    
    def calcular(self):
        return f'Espécie do animal: {self.especie} \n Nome do animal: {self.nome} \n Idade do animal: {self.idade}'
   
    def alterar_status(self):


if __name__ == '__main__':
    item = Pedido('John', '2 anos', 'macaco')
    
    print(item.emitir_som())
    print(item.informacoes())