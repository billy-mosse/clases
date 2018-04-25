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


def upp():
	global up
	up = up + eps
	return up


def isInverse(node):
	return "-1" in node

#Hice la operacion now antes y ahora quiero hacer la next
def runOp(now,next,L, R, plt):

	print "Procesando %s luego de %s" % (now, next)
	global up
	global down

	#print now + " " + next
	#print "_______"
	
	#Ahora estoy a la derecha o izquierda del nodo i_now
	i_now = int(now[2])
	i_next = int(next[2])
	#assert abs(i_now - i_next) == 1


	#Estoy usando que depsues de cada movimiento termino arriba.
	if i_next > i_now:
		#Tengo que ir a un clavo que esta a la DERECHA

		#now -----> next
		if not isInverse(now):
			#Estoy a la derecha del NOW
			if not isInverse(next):
				#Tengo que ir a la derecha del NEXT
				plt.plot((R[i_now],R[i_next]), (up,up),'b')
				#up = up + eps
			else:
				#Tengo que ir a la izquierda del next.
				#Entonces voy abajo del now, derecha, arriba, izquierda
				plt.plot((R[i_now],R[i_now]), (up,down),'b')
				plt.plot((R[i_now],R[i_next]), (down,down),'b')
				plt.plot((R[i_next],R[i_next]), (down,upp()),'b')
				#up = up + eps
				plt.plot((R[i_next],L[i_next]), (up,up),'b')
		else:
			#Vengo de la izquierda del nodo NOW
			if not isInverse(next):
				#Tengo que ir a la derecha del NEXT, pero esto a la izquierda del NOW
				#Entonces primero bajo del NOW y voy por abajo a la derecha del NOW,
				#subo, y recien ahi voy a la derecha del next
				plt.plot((L[i_now],L[i_now]), (up,down),'b')
				plt.plot((L[i_now],R[i_now]), (down,down),'b')
				plt.plot((R[i_now],R[i_now]), (down,upp()),'b')

				#Ahora estoy arriba a la derecha del now. Y tengo que ir a la derecha del next
				#Hago lo que hice antes
				plt.plot((R[i_now],R[i_next]), (up,up),'b')

			else:
				#Tengo que ir a la izquierda del next.
				#Como estoy a la izquierda del now, es un quilombo

				#Primero voy por abajo hasta la derecha del next, que esta mas a la derecha
				plt.plot((L[i_now],L[i_now]), (up,down),'b')

				#Aca me estoy moviendo mucho!!
				plt.plot((L[i_now],R[i_next]), (down,down),'b')

				plt.plot((R[i_next],R[i_next]), (down,upp()),'b')
				#up = up + eps

				#Y ahora voy para la atras del next
				plt.plot((R[i_next],L[i_next]), (up,up),'b')
	else:
		#Aca el nodo next esta ANTES que el now

		#next <------ now

		if isInverse(now):
			#Estoy a la izquierda del NOW
			if isInverse(next):
				#Tengo que ir a la izquierda del NEXT
				#entonces, es facil, porque simplemente me muevo para la izquierda

				plt.plot((L[i_now],L[i_next]), (up,up),'b')
				#up = up + eps
			else:
				#Tengo que ir a la derecha del next.
				#Entonces voy abajo del now, derecha, arriba, derecha
				plt.plot((L[i_now],L[i_now]), (up,down),'b')
				plt.plot((L[i_now],L[i_next]), (down,down),'b')
				plt.plot((L[i_next],L[i_next]), (down,upp()),'b')
				#up = up + eps
				plt.plot((L[i_next],R[i_next]), (up,up),'b')
		else:
			#Vengo de la derecha del nodo NOW
			if isInverse(next):
				#Tengo que ir a la izquierda del NEXT, pero estoy a la derecha del NOW
				#Entonces primero bajo del NOW y voy por abajo hasta la derecha del next,
				#y subo
				plt.plot((R[i_now],R[i_now]), (up,down),'b')
				plt.plot((R[i_now],L[i_now]), (down,down),'b')

				plt.plot((L[i_now],L[i_now]), (down,upp()),'b')
				#up = up + eps

				#Ahora estoy arriba a la derecha del now. Y tengo que ir a la derecha del next
				#Hago lo que hice antes
				plt.plot((L[i_now],L[i_next]), (up,up),'b')

			else:
				#Tengo que ir a la derecha del next.
				#Como estoy a la derecha del now, es un quilombo

				#Primero voy por abajo hasta la derecha del next, que esta mas a la izquierda
				plt.plot((R[i_now],R[i_now]), (up,down),'b')
				plt.plot((R[i_now],L[i_next]), (down,down),'b')
				plt.plot((L[i_next],L[i_next]), (down,upp()),'b')
				#up = up + eps

				#Y ahora voy para la atras del next
				plt.plot((L[i_next],R[i_next]), (up,up),'b')

def inv(s, debug_messages):

	if debug_messages: print "Obteniendo la inversa de %s..." % s
	temp = ""
	ret = ""
	for index,c in enumerate(reversed(s)):
		#print temp
		if c != "*":
			temp = c + temp
			if "a_" in temp:
				if "^(-1)" in temp:
					t = temp[:-5]
				else:
					t = temp + "^(-1)"
				if index == len(s) - 1:
					ret += t
				else:
					ret += t + "*"
				temp=""

	if debug_messages: print "Es: %s" % ret
	return ret




def formula(n, debug_messages):
	if n==2:
		return "a_1*a_2*a_1^(-1)*a_2^(-1)"
	else:
		s = formula(n-1, debug_messages)
		return s + "*a_%d*" % n + inv(s, debug_messages) + "*a_%d^(-1)" % n

def iteradas(n):

	for i in range(2,n+1):
		print "Para %s clavos:" % i
		print formula(i, False)
		print('\n' * 3)
		time.sleep(1)


def graph(s, n):
	S = s.split("*")
	#print S
	#print S

	#tambien puedo de a varios


	for i in range(1,n+1):
		plt.plot([3*i], [10], marker='o', markersize=3, color="red")
	


	L = Counter()
	R = Counter()
	#C = Counter()

	#por ahora no necesito un Center
	for i in range(1,n+1):
		L[i] = 3*i-1
		R[i] = 3*i+1
		#C[i] = 3*i




	px1 = (n+1)
	px2 = 2*(n+1)
	height = 5

	plt.plot([px1], [height], marker='o', markersize=3, color="red")
	plt.plot([px2], [height], marker='o', markersize=3, color="red")

	olds = ""
	for index,s in enumerate(S):
		if 1:
			if index == 0:
				plt.plot((px1,L[1]), (height, down), 'b')
				plt.plot((L[1],L[1]), (down, up), 'b')
				plt.plot((L[1],R[1]), (up, up), 'b')
				olds = s
			else:
				runOp(olds,s,L, R, plt)
				olds = s
				if index == len(S)-1:
					plt.plot((L[n], L[n]), (up, down), 'b')
					plt.plot((L[n], px2), (down, height), 'b')

	'''	plt.plot((px1,L[1]), (height, up), 'b')
	
	plt.plot((L[1], R[1]), (up, up), 'b')
	plt.plot((R[1], L[2]), (up, up), 'b')
	plt.plot((L[2], R[2]), (up, up), 'b')
	plt.plot((R[2], R[2]), (up, down), 'b')
	plt.plot((R[2], L[2]), (down, down), 'b')
	plt.plot((L[2], R[1]), (down, down), 'b')
	up = up + eps

	plt.plot((R[1], R[1]), (down, up), 'b')
	plt.plot((R[1], L[1]), (up, up), 'b')
	down = down + eps

	#Tal vez me sirva mantener los puntos visitados y si veo que se va a repetir alguno le sumo epsilon a la coordenada y!!

	#funcion que dadas dos coord me devuelva lo que hay que hacer
	#uso que siempre son "consecutivas" entonces lo que hay que hacer es facil

	down += eps
	plt.plot((L[1], L[1]), (up, down), 'b')
	plt.plot((L[1], R[2]), (down, down), 'b')
	plt.plot((R[2], R[2]), (down, up), 'b')
	plt.plot((R[2], L[2]), (up, up), 'b')
	plt.plot((L[2], L[2]), (up, down), 'b')
	plt.plot((L[2], px2), (down, height), 'b')'''

	#plt.plot([3,6], [10,10], 'ro')
	plt.axis([0, 3*(n+1), -5, 10 + 0.75 * pow(2,n)])

	img=mpimg.imread('images/monalisa.jpg')
	#imgplot = plt.imshow(img)

	myaximage = plt.imshow(img, aspect='auto', extent=(n+1,2*(n+1),-5,5), alpha=0.5, origin='upper', zorder=-1)

	print "Listo."

	plt.show()


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
		s = formula(n, False)

		print s
		if args.graficar:
			graph(s, n)


if __name__=="__main__":
	main()
