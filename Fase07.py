nome = input('Qual o seu nome? ')
print('Prazer em te conhecer {}'.format(nome))
print('Prazer em te conhecer {:20}'.format(nome)) #Espaço para o nome
print('Prazer em te conhecer {:>20}'.format(nome)) #Alinhar a direita
print('Prazer em te conhecer {:<20}'.format(nome)) #Alinhar a esquerda
print('Prazer em te conhecer {:^20}'.format(nome)) #Centralizar
print('Prazer em te conhecer {:=^20}'.format(nome)) #Sinal de igual 20 vezes


n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
p = n1 ** n2
print('A soma é {}, o produto é {} e a divisão é {:.2f}'.format(s, m, d), end=' >>>>> ')
print('Divisão inteira {} e potência {}'.format(di, p))
