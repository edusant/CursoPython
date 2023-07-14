class ValdacaoSaqueDTO:
    LIMITE_SAQUE_QUANTIDADE = 3
    LIMITE_SAQUE = 500
    saquesRealizados = 0
   
    def __init__(self, saldo, saque, saquesRealizados):
        self.saldo = saldo
        self.saques = saque
        self.saquesRealizados = saquesRealizados
        self.valid = []
    
    def _validarSaque(self):
        if self.saques < 0:
            self.valid.append("Valor de saque não pode ser menor que zero!")
        if self.saldo == 0:
            self.valid.append("Sua conta está sem saldo!")
        if self.saques > saldo:
            self.valid.append("Valor de saque não pode ser maior que o saldo!")
        if self.saques > LIMITE_SAQUE:
            self.valid.append(f"O limite para saque é R$ {LIMITE_SAQUE} !")
        if  self.saquesRealizados  >= LIMITE_SAQUE_QUANTIDADE:
            self.valid.append("Limite de saque excedido")

            """ saldo -= self.saques
            saquesRealizados += 1
            extrato += f"Saque de R$: {self.saques}, saldo: {saldo}\n";  """
    def isValid(self):
        self._validarSaque()
        return len(self.valid) == 0

    def getErrors(self):
        return self.valid


class PrintErros():
    def printErros(erros):
        print("=============Erros=============")
        for i in erros:
            print(i)
        print("=============end=============")

LIMITE_SAQUE_QUANTIDADE = 3
LIMITE_SAQUE = 500
saldo = 0
saquesRealizados = 0
extrato = ""
valida = True
while valida:
    n = int(input("Digite 1 para deposito, Digite 2 para sacar, Digite 3 para ver o extrato, Digite 4 para encerrar a operação: "))

    if n == 1:
        while True:
            valor = float(input("Digite o valor que será adicionado na sua conta: "))
            if valor > 0:
                saldo += valor
                extrato += f"Deposito de R$: {valor}, saldo: {saldo}\n"; 
                break
            else:
                print("Valor de deposito não pode ser negativo!")
                continue 
    elif n == 2:
        while True:
            valorSaque = float(input("Digite o valor que será retirado da sua conta ou digite 0 para encerrar a operação: "))
            if valorSaque == 0:
                break
            valida =  ValdacaoSaqueDTO(saldo, valorSaque, saquesRealizados)
            if valida.isValid():
                pass
            else:
                PrintErros.printErros(valida.getErrors())
                pass

            
    elif n == 3:
        print ("Não foram registradas movimentações " if not extrato else extrato)
    elif n == 4:
        valida = False

    else: 
        print("Opção inválida")

    
           