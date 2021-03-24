import re

f = open('processos.xml')

anosList = []
anos = {}
seculos = {}
pnome = {}
unome = {}
nomecompleto = {}
seculo17 = {}
seculo18 = {}
seculo19 = {}
seculo20 = {}
seculo17Ultimo = {}
seculo18Ultimo = {}
seculo19Ultimo = {}
seculo20Ultimo = {}

for line in f:

	m = re.search(r'(<obs/>)|(<processo id="([0-9]+)">)|(<[a-z]+>)?([^<]*)(</[a-z]+>)?',line.strip())

	for g in m.groups():
		if g is None:
			pass
		elif g == '<data>':

			ano = re.split(r'-',m.group(5))[0]
			sec = int(ano[0]+(ano[1])) + 1
			anoList = int(ano)

			if anoList in anosList:
				pass
			else:
				anosList.append(anoList)	

			if ano in anos:
				anos[ano] += 1
			else:
				anos[ano] = 1

			if sec in seculos:
				seculos[sec] += 1
			else:
				seculos[sec] = 1				

		elif g == '<nome>':
			primeironome = 	re.split(r' ',m.group(5))[0]
			ultimonome = re.split(r' ',m.group(5))[-1]
			completo = m.group(5)	

			if primeironome in pnome:
				pnome[primeironome] += 1
			else:
				pnome[primeironome] = 1

			if ultimonome in unome:
				unome[ultimonome] += 1
			else:
				unome[ultimonome] = 1

			if sec == 17 :
				if primeironome in seculo17:
					seculo17[primeironome] += 1
				else:
					seculo17[primeironome] = 1

				if ultimonome in seculo17Ultimo:
					seculo17Ultimo[ultimonome] += 1
				else:
					seculo17Ultimo[ultimonome] = 1		
			if sec == 18 :
				if primeironome in seculo18:
					seculo18[primeironome] += 1
				else:
					seculo18[primeironome] = 1

				if ultimonome in seculo18Ultimo:
					seculo18Ultimo[ultimonome] += 1
				else:
					seculo18Ultimo[ultimonome] = 1	
			if sec == 19 :
				if primeironome in seculo19:
					seculo19[primeironome] += 1
				else:
					seculo19[primeironome] = 1

				if ultimonome in seculo19Ultimo:
					seculo19Ultimo[ultimonome] += 1
				else:
					seculo19Ultimo[ultimonome] = 1	
			if sec == 20 :
				if primeironome in seculo20:
					seculo20[primeironome] += 1
				else:
					seculo20[primeironome] = 1

				if ultimonome in seculo20Ultimo:
					seculo20Ultimo[ultimonome] += 1
				else:
					seculo20Ultimo[ultimonome] = 1									


sorted_pnome = dict(sorted(pnome.items(), key=lambda p:p[1],reverse = True))
sorted_unome = dict(sorted(unome.items(), key=lambda p:p[1],reverse = True))
sorted_anos = dict(sorted(anos.items(), key=lambda p:p[0]))
sorted_seculos = dict(sorted(seculos.items(), key=lambda p:p[0]))
sorted_pnome_secolo17 = dict(sorted(seculo17.items(), key=lambda p:p[1],reverse = True))
sorted_pnome_secolo18 = dict(sorted(seculo18.items(), key=lambda p:p[1],reverse = True))
sorted_pnome_secolo19 = dict(sorted(seculo19.items(), key=lambda p:p[1],reverse = True))
sorted_pnome_secolo20 = dict(sorted(seculo20.items(), key=lambda p:p[1],reverse = True))
sorted_unome_secolo17 = dict(sorted(seculo17Ultimo.items(), key=lambda p:p[1],reverse = True))
sorted_unome_secolo18 = dict(sorted(seculo18Ultimo.items(), key=lambda p:p[1],reverse = True))
sorted_unome_secolo19 = dict(sorted(seculo19Ultimo.items(), key=lambda p:p[1],reverse = True))
sorted_unome_secolo20 = dict(sorted(seculo20Ultimo.items(), key=lambda p:p[1],reverse = True))
anosList.sort()

print('Intervalos sem inscricoes')
i = 0

while i < len(anosList)-1:
	l = []
	if anosList[i] + 1 < anosList[i+1]:
		while(anosList[i] + 1 < anosList[i+1]):
			l.append(anosList[i] + 1)
			anosList[i] += 1
		print(l)	
	i+=1

print('ANOS:')			
print(sorted_anos)
print('\n\nSECULOS:')
print(sorted_seculos)
print(len(sorted_seculos))
print('\n\nPRIMEIROS NOMES:')
print(sorted_pnome)
print('\n\nULTIMOS NOMES:')
print(sorted_unome)
print('\n\nMAX PRIMEIRO NOME')
print(max(sorted_pnome,key = pnome.get))
print('\n\nMAX ULTIMO NOME')
print(max(sorted_unome,key = unome.get))
print('\n\nMAX 5 PRIMEIRO NOME')
print(list(sorted_pnome.keys())[:5])
print('\n\nMAX 5 ULTIMO NOME')
print(list(sorted_unome.keys())[:5])
print('\n\nMAX 5 PRIMEIRO NOME SECULO 17')
print(list(sorted_pnome_secolo17.keys())[:5])
print('\n\nMAX 5 PRIMEIRO NOME SECULO 18')
print(list(sorted_pnome_secolo18.keys())[:5])
print('\n\nMAX 5 PRIMEIRO NOME SECULO 19')
print(list(sorted_pnome_secolo19.keys())[:5])
print('\n\nMAX 5 PRIMEIRO NOME SECULO 20')
print(list(sorted_pnome_secolo20.keys())[:5])
print('\n\nMAX 5 ULTIMO NOME SECULO 17')
print(list(sorted_unome_secolo17.keys())[:5])
print('\n\nMAX 5 ULTIMO NOME SECULO 18')
print(list(sorted_unome_secolo18.keys())[:5])
print('\n\nMAX 5 ULTIMO NOME SECULO 19')
print(list(sorted_unome_secolo19.keys())[:5])
print('\n\nMAX 5 ULTIMO NOME SECULO 20')
print(list(sorted_unome_secolo20.keys())[:5])

print('\n\n',anosList)

f.close()			 		