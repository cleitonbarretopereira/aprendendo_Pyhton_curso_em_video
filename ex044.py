print('{:=^60}'.format(' GERENCIADOR DE PAGAMENTOS '))
valor = float(input('Digite o Preço R$: '))
opcao = int(input('''
[1] À Vista no dinheiro
[2] À Vista no CHEQUE
[3] Em até 2 vezes no CARTÃO
[4] Em 3 vezes ou mais no CARTÃO

DIGITE A OPÇÃO DESEJADA: '''))

if opcao == 1:
    print('Desconto de R$ {:.2f}'.format(valor*0.10))
    valor = valor-(valor*0.10)
    print('O Total à pagar, À VISTA é de R$ {:.2f}'.format(valor))
elif opcao == 2:
    print('Desconto de R$ {:.2f}'.format(valor*0.05))
    valor = valor - (valor*0.05)
    print('O Total à pagar, À VISTA é de R$ {:.2f}'.format(valor))
elif opcao == 3:
    valorparc = valor/2
    print('Você pagará em 2x parcelas de R$ {:.2f}.'.format(valorparc))
elif opcao == 4:
    print('Juros de R$ {:.2f}'.format(valor*0.2))
    parcela = int(input('Em quantas parcelas?'))
    valorparc = valor/parcela
    valor = valor + (valor*0.20)
    print('Sua compra ficou em R$ {:.2f}, parcelado em {} vezes de R$ {:.2f}.'.format(valor, parcela, valorparc))
else:
    print('Opção inválida, tente novamente.')