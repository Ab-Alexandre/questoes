class Produto:
    def __init__(self, nome, preco, quantidade_estoque):
        self.nome = nome
        self.preco = preco
        self.quantidade_estoque = quantidade_estoque

    def  atualizar_estoque(self):
        return f'O estoque de {self.nome} foi atualizado. Quantidade no estoque: {self.quantidade_estoque}'
    
    def calculo_preco(self):
        return f'Com base na quantidade desejada, o preço de(da/do) {self.nome} é: {self.preco}.'
    
if __name__ == '__main__':
    produto1 = Produto('caneta', 'R$ 43,50', '123')
    
    print(produto1.atualizar_estoque())
    print(produto1.calculo_preco())