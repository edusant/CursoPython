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
        if saquesRealizados < LIMITE_SAQUE_QUANTIDADE:
            while True:
                valorSaque = float(input("Digite o valor que será retirado da sua conta: "))
           
                if valorSaque < 0:
                    print("Valor de saque não pode ser menor que zero!")
                    continue 
                if saldo == 0:
                    print("Sua conta está sem saldo!")
                    break 
                elif valorSaque > saldo:
                    print("Valor de saque não pode ser maior que o saldo!")
                    continue 
                elif valorSaque > LIMITE_SAQUE:
                    print(f"O limite para saque é R$ {LIMITE_SAQUE} !")
                    continue 
                else:
                    saldo -= valorSaque
                    saquesRealizados += 1
                    extrato += f"Saque de R$: {valorSaque}, saldo: {saldo}\n"; 
                    break
        else:
            print("Limite de saque excedido")
    elif n == 3:
        print ("Não foram registradas movimentações " if not extrato else extrato)
    elif n == 4:
        valida = False

    else: 
        print("Opção inválida")

    
           