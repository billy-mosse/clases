from numpy import *
import time
import math
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import sys
from collections import Counter
import argparse


	#a = sin(t)
	#b = cos(t)
	#c = a + b

	#Grafica la funcion a en el dominio t con el color r
	#plt.plot(t,a,'r') # plotting t,a separately 
	#plt.plot(t,b,'b') # plotting t,b separately 
	#plt.plot(t,c,'g') # plotting t,c separately 



	#Me crea dominios para ls funciones	
	#x12 = linspace(0,10,400)
	#x21 = linspace(0,10,400)

eps = 0.4

up = 12
down = 8

L = Counter()
R = Counter()

def upp():
	global up
	up = up + eps
	return up

def downn():
	global down
	down = down - eps
	return down

def isInverse(node):
	return node < 0


def LL(i):
	global L
	L[i] -= eps/3
	l =L[i]
	return l


def RR(i):
	global R
	R[i] += eps/3
	r =R[i]
	return r



def graph(s, n):
	global L
	global R
	global down
	global up

	#print S
	#print S

	#tambien puedo de a varios


	for i in range(1,n+1):
		plt.plot([3*i], [(n+2)*5], marker='o', markersize=4, color="black")
	


	#C = Counter()


	
	#por ahora no necesito un Center
	for i in range(1,n+1):
		L[i] = 3*i-1
		R[i] = 3*i+1
		#C[i] = 3*i


	px1 = (n+1)
	px2 = 2*(n+1)
	height = (n-1)*5

	up = (n+3)*5
	down = (n+1)*5

	plt.plot([px1], [height], marker='o', markersize=3, color="red")
	plt.plot([px2], [height], marker='o', markersize=3, color="red")

	

	olds = ""
	for index,item in enumerate(s):
		if index == 0:
			plt.plot((px1,L[1]), (height, down), 'b')
			plt.plot((L[1],L[1]), (down, up), 'b')
			plt.plot((L[1],R[1]), (up, up), 'b')
			olds = item
		else:
			runOp(olds,item, plt)
			olds = item
			if index == len(s)-1:
				plt.plot((L[n], L[n]), (up, down), 'b')
				plt.plot((L[n], px2), (down, height), 'b')


	#plt.plot([3,6], [10,10], 'ro')
	plt.axis([0, 3*(n+1), (-1)*height, 2*height + (n+2)*5 + pow(2,n)])

	img=mpimg.imread('images/monalisa.jpg')
	#imgplot = plt.imshow(img)

	myaximage = plt.imshow(img, aspect='auto', extent=(n+1,2*(n+1),(-1)*height,height), alpha=0.5, origin='upper', zorder=-1)

	print "Listo."

	plt.show()

	
#Hice la operacion now antes y ahora quiero hacer la next
def runOp(now,next, plt):

	global up
	global down
	global L
	global R

	#print now + " " + next
	#print "_______"
	
	#Ahora estoy a la derecha o izquierda del nodo i_now
	i_now = abs(int(now))
	i_next = abs(int(next))
	#assert abs(i_now - i_next) == 1


	#Estoy usando que depsues de cada movimiento termino arriba.
	if i_next > i_now:
		#Tengo que ir a un clavo que esta a la DERECHA

		#now -----> next
		if not isInverse(now):
			#Estoy a la derecha del NOW
			if not isInverse(next):
				#Tengo que ir a la derecha del NEXT
				plt.plot((R[i_now],RR(i_next)), (up,up),'b')
				#up = up + eps
			else:
				#Tengo que ir a la izquierda del next.
				#Entonces voy abajo del now, derecha, arriba, izquierda
				plt.plot((R[i_now],R[i_now]), (up,downn()),'b')
				plt.plot((R[i_now],RR(i_next)), (down,down),'b')
				plt.plot((R[i_next],R[i_next]), (down,upp()),'b')
				#up = up + eps
				plt.plot((R[i_next],LL(i_next)), (up,up),'b')
		else:
			#Vengo de la izquierda del nodo NOW
			if not isInverse(next):
				#Tengo que ir a la derecha del NEXT, pero esto a la izquierda del NOW
				#Entonces primero bajo del NOW y voy por abajo a la derecha del NOW,
				#subo, y recien ahi voy a la derecha del next
				plt.plot((L[i_now],L[i_now]), (up,downn()),'b')
				plt.plot((L[i_now],RR(i_now)), (down,down),'b')
				plt.plot((R[i_now],R[i_now]), (down,upp()),'b')

				#Ahora estoy arriba a la derecha del now. Y tengo que ir a la derecha del next
				#Hago lo que hice antes
				plt.plot((R[i_now],RR(i_next)), (up,up),'b')

			else:
				#Tengo que ir a la izquierda del next.
				#Como estoy a la izquierda del now, es un quilombo

				#Primero voy por abajo hasta la derecha del next, que esta mas a la derecha
				plt.plot((L[i_now],L[i_now]), (up,downn()),'b')

				#Aca me estoy moviendo mucho!!
				plt.plot((L[i_now],RR(i_next)), (down,down),'b')

				plt.plot((R[i_next],R[i_next]), (down,upp()),'b')
				#up = up + eps

				#Y ahora voy para la atras del next
				plt.plot((R[i_next],LL(i_next)), (up,up),'b')

	else:
		#Aca el nodo next esta ANTES que el now

		if isInverse(now):
			#Estoy a la izquierda del NOW
			if isInverse(next):
				#Tengo que ir a la izquierda del NEXT
				#entonces, es facil, porque simplemente me muevo para la izquierda

				plt.plot((L[i_now],LL(i_next)), (up,up),'b')

				#up = up + eps
			else:
				#Tengo que ir a la derecha del next.
				#Entonces voy abajo del now, derecha, arriba, derecha
				plt.plot((L[i_now],L[i_now]), (up,downn()),'b')
				plt.plot((L[i_now],LL(i_next)), (down,down),'b')
				plt.plot((L[i_next],L[i_next]), (down,upp()),'b')
				#up = up + eps
				plt.plot((L[i_next],RR(i_next)), (up,up),'b')
		else:
			#Vengo de la derecha del nodo NOW
			if isInverse(next):
				#Tengo que ir a la izquierda del NEXT, pero estoy a la derecha del NOW
				#Entonces primero bajo del NOW y voy por abajo hasta la derecha del next,
				#y subo
				plt.plot((R[i_now],R[i_now]), (up,downn()),'b')
				plt.plot((R[i_now],L[i_now]), (down,down),'b')

				plt.plot((L[i_now],L[i_now]), (down,upp()),'b')
				#up = up + eps

				#Ahora estoy arriba a la derecha del now. Y tengo que ir a la derecha del next
				#Hago lo que hice antes
				plt.plot((L[i_now],LL(i_next)), (up,up),'b')

			else:
				#Tengo que ir a la derecha del next.
				#Como estoy a la derecha del now, es un quilombo

				#Primero voy por abajo hasta la derecha del next, que esta mas a la izquierda
				plt.plot((R[i_now],R[i_now]), (up,downn()),'b')
				plt.plot((R[i_now],LL(i_next)), (down,down),'b')
				plt.plot((L[i_next],L[i_next]), (down,upp()),'b')
				#up = up + eps

				#Y ahora voy para la atras del next
				plt.plot((L[i_next],RR(i_next)), (up,up),'b')










################ Conseguir la formulita ################

#Invierto una formulita que puede ser larga
def inv(l):
	inv_l = []
	for item in reversed(l):
		inv_l.append(-item)

	return inv_l


#Obtengo la solucion para n
def formula(n):
	if n==2:
		sol = [1,2,-1,-2]
		return sol
	else:
		sol = formula(n-1)

		#Calculo la solucion para n a partir de la solucion para n-1
		ret = sol + [n] + inv(sol) + [-n]
		return ret


################ Conseguir la formulita ################





def printlist(sol):
	str_sol = ""
	for index, item in enumerate(sol):
		s = str(item)
		if index==0:
			str_sol += "X" + s
		else:
			if '-' in s:
				str_sol += "-X" + s[1:]
			else:
				str_sol += "+X%s" % s
	print str_sol



def iteradas(n):

	for i in range(2,n+1):
		print "Para %s clavos:" % i
		printlist(formula(i))
		print('\n' * 3)
		time.sleep(1)




class MyParser(argparse.ArgumentParser):
    def error(self, message):
        sys.stderr.write('error: %s\n' % message)
        self.print_help()
        sys.exit(2)


#Para 2 clavos por ahora
def main():

	parser = MyParser()
	parser.add_argument('--graficar', help='Graficar la formula obtenida', action='store_true')	
	parser.add_argument('--iteradas', help='Solo dar las formulas iteradas hasta n', action='store_true')	

	parser.add_argument("-n", "--clavos", help="La cantidad de clavos del problema. Ojo, no zarparse porque se cuelga")

	if len(sys.argv)==1:
	    parser.print_help()
	    sys.exit(1)
    
	args = parser.parse_args()

	n = int(args.clavos)
	if args.iteradas:
		iteradas(n)
	else:
		sol = formula(n)
		printlist(sol)
		if args.graficar:
			graph(sol, n)


if __name__=="__main__":
	main()
