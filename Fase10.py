'''nome = str(input('Qual é seu nome? ')).upper()
if nome == 'Arthur':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal!')
print('Bom dia, {}!'.format(nome))'''

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('A sua média foi {:.1f}'.format(m))
if m >= 6.0:
    print('PARABÉNS, VOCê FOI APROVADO!')
else:
    print('REPROVADO!')
