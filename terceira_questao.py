class Conta_bancaria:
    def __init__(self, numero_conta, saldo, titular):
        self.numero_conta = numero_conta
        self.saldo = saldo
        self.titular = titular

    def depositar(self):
        return f'Você está depositando na conta {self.numero_conta} com o titular {self.titular}.'
    
    def sacar(self):
        return f'Você está sacando da sua conta.'
    
    def saldo_da_conta(self):
        return f'O seu saldo é {self.saldo}.'
    
if __name__ == '__main__':
    conta1 = Conta_bancaria('184719834', 'R$ 128974,89', 'Cleiton')
    
    print(conta1.depositar())
    print(conta1.saldo_da_conta())
    print(conta1.sacar())