import re
import sys

anosList = []
processos = {}
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
parentesEl = {}
global ano
global sec
global anoList
global primeironome
global ultimonome
global completo
global pr
global contador

def saveInfo(anoList, ano, sec, primeironome, ultimonome):

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


def func():
	f = open('processos.xml')
	next(f)

	contador = 1
	iguais = 0
	anoList = sec = ano = None
	primeironome = ultimonome = None

	for line in f:
		m = re.search(r'(<obs\/>)|(<processo id="([0-9]+)">)|(<[a-z]+>)?([^<]*)(<\/[a-z]+>)?',line.strip())
		if m.group(4) == '<processos>' or m.group(6) == '</processos>':
			pass
		if "processo id" in str(m.group(2)):
			pr = m.group(3)		
		contador += 1	
		#print(contador,'->',m.groups())
		for g in m.groups():
			if g is None:
				pass	
			else:
				if g == '<data>':
					ano = re.split(r'-',m.group(5))[0]
					sec = int(ano[0]+(ano[1])) + 1
					anoList = int(ano)				

				if g == '<nome>':
					primeironome = 	re.split(r' ',m.group(5))[0]
					ultimonome = re.split(r' ',m.group(5))[-1]
					completo = m.group(5)	

					if pr in processos and completo in processos[pr]:
						iguais += 1
					else:
						nomecompleto[pr] = completo
						if pr in processos:
							lista = processos[pr]
						else:
							lista = []
						lista.append(completo)
						processos[pr] = lista
						saveInfo(anoList, ano, sec, primeironome, ultimonome)

				if g == '<obs>':
					obsClose = re.search(r'(<\/obs>)',line)
					if obsClose:
						familia = re.findall(r'(?!Doc\.danificado\.| )[,\w\ ]*(?:,Ti.s?(?: .aternos?|\.)*\.|,Irmaos?(?: .aternos?\.|\.|\.)|,Prim.s?(?: .aternos?)*\.|,Sobrinh.(?: .aterno)*\.)(?: *Proc\.\d+\.)*',line) 
						if familia:
							parentesEl[pr+completo] = familia
					else:
						auxF = next(f)
						line = line + auxF
						obsClose = re.search(r'(<\/obs>)',auxF)
						while obsClose == None:
							auxF = next(f)
							obsClose = re.search(r'(<\/obs>)',auxF)
							line = line + auxF
						line = re.sub(r'\n +',' ',line)
						familia = re.findall(r'(?!Doc\.danificado\.| )[,\w\ ]*(?:,Ti.s?(?: .aternos?|\.)*\.|,Irmaos?(?: .aternos?\.|\.|\.)|,Prim.s?(?: .aternos?)*\.|,Sobrinh.(?: .aterno)*\.)(?: *Proc\.\d+\.)*',line) 
						if familia:
							parentesEl[pr+completo] = familia			
	f.close()


def main():
	print("A Ler ficheiro...")
	func()
	menu()

def exA():
	sorted_anos = dict(sorted(anos.items(), key=lambda p:p[0]))
	sorted_seculos = dict(sorted(seculos.items(), key=lambda p:p[0]))
	
	#print(processos)
	print('INTERVALOS SEM INSCRICOES:\n')
	
	i = 0

	while i < len(anosList)-1:
		l = []
		if anosList[i] + 1 < anosList[i+1]:
			while(anosList[i] + 1 < anosList[i+1]):
				l.append(anosList[i] + 1)
				anosList[i] += 1
			if len(l) > 1:	
				print(l[0],'-',l[-1])
			else:
				print(l[0])		
		i+=1

	print('\n\nANOS:')			
	print(sorted_anos)
	print('\n\nSECULOS:')
	print(sorted_seculos)
	print(len(sorted_seculos))

	menu()


def exB():
	sorted_pnome = dict(sorted(pnome.items(), key=lambda p:p[1],reverse = True))
	sorted_unome = dict(sorted(unome.items(), key=lambda p:p[1],reverse = True))
	
	sorted_pnome_secolo17 = dict(sorted(seculo17.items(), key=lambda p:p[1],reverse = True))
	sorted_pnome_secolo18 = dict(sorted(seculo18.items(), key=lambda p:p[1],reverse = True))
	sorted_pnome_secolo19 = dict(sorted(seculo19.items(), key=lambda p:p[1],reverse = True))
	sorted_pnome_secolo20 = dict(sorted(seculo20.items(), key=lambda p:p[1],reverse = True))
	sorted_unome_secolo17 = dict(sorted(seculo17Ultimo.items(), key=lambda p:p[1],reverse = True))
	sorted_unome_secolo18 = dict(sorted(seculo18Ultimo.items(), key=lambda p:p[1],reverse = True))
	sorted_unome_secolo19 = dict(sorted(seculo19Ultimo.items(), key=lambda p:p[1],reverse = True))
	sorted_unome_secolo20 = dict(sorted(seculo20Ultimo.items(), key=lambda p:p[1],reverse = True))
	anosList.sort()

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

	menu()

def exC():
	fam = 0
	irmao = 0
	tio = 0
	primo = 0
	regex = r','
	for nome,familia in parentesEl.items():
		if familia:
			#print(familia)
			fam += 1
		for frase in familia:
			
			regIrmaos = re.search(r'Irmaos',frase)
			regIrmao = re.search(r'Irmao',frase)
			if regIrmaos:
				irmao += len(re.findall(regex,frase)) + 1
			elif regIrmao:
				irmao += 1
			
			regTios = re.search(r'Tios',frase)
			regTio = re.search(r'Tio',frase)
			if regTios:
				tio += len(re.findall(regex,frase)) + 1
			elif regTio:
				tio += 1
			
			regPris = re.search(r'Primos',frase)
			regPri = re.search(r'Primo',frase)
			if regPris:
				primo += len(re.findall(regex,frase)) + 1
			elif regPri:
				primo += 1


	print("Número de candidatos com parentes eclesiásticos: ", fam)
	print("Número de Irmãos eclesiásticos: ", irmao)
	print("Número de Tios eclesiásticos: ", tio)
	print("Número de Primos eclesiásticos: ", primo)

	menu()

def menu():
    print("**Processador de Pessoas listadas nos Róis de Confessados**")
    print()

    choice = input("A: exA \nB: exB\nC: exC \nS: Sair\nPor favor escolha uma opção:")

    if choice == "A" or choice =="a":
        exA()
    elif choice == "B" or choice =="b":
        exB()
    elif choice == "C" or choice =="c":
        exC()
    elif choice=="S" or choice=="s":
        sys.exit
    else:
        print("Opção inválida")
        menu()			 		

main()