#sacar, depositar, visualizar extrato

menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
    
 
while True:
    opcao = input(menu)
    if opcao== "d":

        valor = float(input('Informe o valor do depósito:'))
        if valor<=0:
            print('Operação inválida! O valor de depósito deve ser maior que 0.')
        elif valor>=0 :
            opcao ==True
            saldo+= valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print (f'depósito de R$ {valor:.2f} realizado com sucesso!')
            continue
    
    elif opcao =='s':
        print(f"Saldo disponível: R$ {saldo:.2f}")
        print('===================================')
        valor = float(input('Informe o valor do saque:'))

        excedeu_Lim_saques= numero_saques>= LIMITE_SAQUES
        excedeu_valor_saque = valor>limite
        saldo_insuficiente = valor> saldo

        if saldo_insuficiente:
            print("Impossível realizar o saque! Saldo insuficiente.")
        elif excedeu_Lim_saques:
            print("Não foi possivel realizar a operação! Limite de saques diários excedido.")
            
        elif excedeu_valor_saque:
            print('Não foi possível realizar a operação! O limite máximo para saque é R$ 500,00.')
        elif valor >0:
            saldo -=valor
            extrato+=  f'Saque: R${valor:.2f}\n'
            numero_saques += 1
            print (f'Saque de R$ {valor:.2f} realizado com sucesso!')
            print('==========================================')
            print(f'Saldo disponível após o saque: R${saldo:.2f}')
        
        else:
            print('Operação inválida.')
    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")
        break
        
    elif opcao == 'q':
         break
    else:
        print('Opção Invalida')
