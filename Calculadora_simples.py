# construção de uma calculadora
print('*' * 8 + 'CALCULADORA' + '*' * 8)
print('+ Adição')
print('- Subtração')
print('* Mutiplicação')
print('/ Divisão')
print('Pressione outra tecla para sair')
op = input('Qual operação deseja fazer?:')
x = int(input('Digite o primeiro valor:'))
y = int(input('Digite o segundo valor:'))
if (op == '+'):
    res = x + y
    print('Resultado:{} + {} = {}'.format(x, y, res))
elif (op == '-'):
    res = x - y
    print('Resultado:{} - {} = {}'.format(x, y, res))
elif (op == '*'):
    res = x * y
    print('Resultado: {} * {} = {}'.format(x, y, res))
elif (op == '/'):
    res = x / y
    print('Resultado: {} / {} = {}'.format(x, y, res))

