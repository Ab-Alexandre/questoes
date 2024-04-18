class Livro:
    def __init__(self, titular, autor, numero_paginas):
        self.titular = titular
        self.autor = autor
        self.numero_paginas = numero_paginas

    def mostrar_informacoes(self):
        return f'Autor do livro: {self.autor} \n titular: {self.titular} \n paginas:{self.numero_paginas}.'
    
    def palavras_por_pagina(self):
        return f'O livro possui {self.numero_paginas} paginas e 350 palavras por pagina.'
    
if __name__ == '__main__':
    maquiavel = Livro('cleiton', 'Macaco', '120')
    
    print(maquiavel.mostrar_informacoes())
    print(maquiavel.palavras_por_pagina())