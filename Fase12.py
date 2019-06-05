nome = str(input('Qual é o seu nome? '))
if nome == 'Arthur':
    print('Que nome lindo!')
elif nome == 'Pedro' or nome == 'Maria' or nome =='Paulo':
    print('Seu nome é bem popular no Brasil!')
else:
    print('Seu nome é bem normal!')
print('Tenha um bom dia, {}!'.format(nome))
