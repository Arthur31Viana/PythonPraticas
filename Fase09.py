frase = '  Curso em video python  '
print(frase[9:13])
print(frase[9:13:2])
print(frase[:15])
print(frase[9:])
print(frase[9::3])

print(len(frase))
print(frase.count('o'))
print(frase.count('o', 0, 13))
print(frase.find('deo'))
print('curso' in frase)
print(frase.replace('python', 'Android'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
print(frase.strip())
print(frase.rstrip())
print(frase.lstrip())
print(frase.split())
print('-'.join(frase))
