import re

def evaluar(entrada):
	arreglo = []
	arreglo2 = []
	arreglo3 = []
	arreglo4 = []

	arreglo = re.split(', |,|', entrada) # separar por comas
#print "PRIMER SPLIT" , arreglo

	if len(arreglo) > 1: 
		for x in arreglo: 
			# remover espacios en blanco
			no_espacio = re.sub('^\s+',"",x) # al principio
			no_espacio = re.sub("\s+\Z","",x) # al final

			split = re.split(" ",no_espacio) # separar por espacios entre palabra e intervalos
			agregar = split if len(split)>1 else no_espacio # guardar arreglo o palabra
			arreglo2.append(agregar)
		#print 'SEGUNDO SPLIT', arreglo2

		for elemento in arreglo2: 
			if type(elemento) == str: #guardar palabra
				arreglo3.append(elemento)
			else: # convertir arreglo  del tipo ['palabra', 'a-b'] a ['palabra', 'a' , 'b']
				nombre = elemento[0]
				numeros = re.split('-', elemento[1])
				arreglo3.append([nombre] + numeros)
	#print "TERCER ARREGLO", arreglo3


		for i in arreglo3: 
			if type(i) == str: # agregar nombre de usuario
				if i != '': #ignorando espacios nulos
					arreglo4.append(i)
			else: # convertir arreglo a lista de usuarios con los indices indicados
				inicio_nombre = i[0]
				lim_inferior = int(i[1])
				lim_superior = int(i[2])+1
				lista = range(  int(lim_inferior), int(lim_superior) )
				for item in lista:
					arreglo4.append(inicio_nombre + str(item))

		return arreglo4
	else:
		arreglo = re.split(" ",entrada) # separar por espacios entre palabra e intervalos
		if len(arreglo)>1:
			nombre = arreglo[0]
			numeros = re.split('-', arreglo[1])
			lim_inferior = int(numeros[0])
			lim_superior = int(numeros[1])+1
			lista = range( lim_inferior,lim_superior)
			for i in lista:
					arreglo2.append(nombre + str(i))
			arreglo = arreglo2
		return arreglo

#a = ',usuarioa , usuariob , usuario 1-5, usuarioc,asdasd, otrousuario 1-3 ,'
#b = 'usuarioa,usuariob,usuario 1-5,usuarioc'
#c = 'usuario1'

#resultado = evaluar_expresion(a)
#print resultado
