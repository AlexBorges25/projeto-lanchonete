print('Bem vindo a lanchonete do Alex')
print('*****************Cardápio*****************')
print('| Código |        Descrição      | Valor |')
print('|  100   |    Cachorro Quente    |  9,00 |')
print('|  101   | Cachorro Quente Duplo | 11,00 |')
print('|  102   |        X-Egg          | 12,00 |')
print('|  103   |       X-Salada        | 12,00 |')
print('|  104   |       X-Bacon         | 14,00 |')
print('|  105   |       X-Tudo          | 17,00 |')
print('|  200   |   Refrigerante Lata   |  5,00 |')
print('|  201   |      Chá Gelado       |  4,00 |')
acumulador = 0
while True:
    codigo =  input('Entre com o código desejado: ')
    if codigo != '100' and codigo != '101' and codigo != '102' and codigo != '103' and codigo != '104' and codigo != '105' and codigo != '200' and codigo != '201': #validação do codigos
        print('Opção inválida, entre com um código que exista!')
        continue
    elif codigo == '100': #entrada da condição do código
        print('Você pediu um Cachorro quente no valor de R$9,00') #mostrar o pedido selecionado
        acumulador = acumulador + 9 #acumulador de contagem dos valores do pedido
    elif codigo == '101':
        print('Você pediu um Cachorro quente duplo no valor de R$11,00')
        acumulador = acumulador + 11
    elif codigo == '102':
        print('Você pediu um X-Egg no valor de R$12,00')
        acumulador = acumulador + 12
    elif codigo == '103':
        print('Você pediu um X-Salada no valor de R$12,00')
        acumulador = acumulador + 12
    elif codigo == '104':
        print('Você pediu um X-Bacon no valor de R$14,00')
        acumulador = acumulador + 14
    elif codigo == '105':
        print('Você pediu um X-Tudo no valor de R$17,00')
        acumulador = acumulador + 17
    elif codigo == '200':
        print('Você pediu um Refrigerante Lata no valor de R$5,00')
        acumulador = acumulador + 5
    elif codigo == '201':
        print('Você pediu um Chá Gelado no valor de R$4,00')
        acumulador = acumulador + 4
    pedir_mais = input('Você deseja pedir mais alguma coisa? \n 1 - Sim \n 2 - não \n')
    if pedir_mais == '1': #confirmação de que se a resposta for 1 continua o programa.
        continue
    else:
        print('O valor total a ser pago é de R${:.2f}' . format(acumulador)) #print final do valor total dos produtos.
        break #parando o laço de repetição.