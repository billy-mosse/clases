from numpy import *
import math
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import sys
from collections import Counter


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
	print node
	return "-1" in node

#Hice la operacion now antes y ahora quiero hacer la next
def runOp(now,next,L, R, plt):
	global up

	print now + " " + next
	print "_______"
	
	#Ahora estoy a la derecha o izquierda del nodo i_now
	i_now = int(now[2])
	i_next = int(next[2])
	#assert abs(i_now - i_next) == 1

	if i_next > i_now:
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
				#Entonces primero bajo del NOW y voy por abajo
				plt.plot((L[i_now],L[i_now]), (up,down),'b')
				plt.plot((L[i_now],R[i_now]), (down,down),'b')
				plt.plot((R[i_now],R[i_now]), (down,upp()),'b')

				#up = up + eps
				#Ahora estoy arriba a la derecha del now. Y tengo que ir a la derecha del next
				#Hago lo que hice antes
				plt.plot((R[i_now],R[i_next]), (up,up),'b')

			else:
				#Tengo que ir a la izquierda del next.
				#Como estoy a la izquierda del now, es un quilombo

				#Primero voy por abajo hasta la derecha del next, que esta mas a la derecha
				plt.plot((L[i_now],L[i_now]), (up,down),'b')
				plt.plot((L[i_now],R[i_next]), (down,down),'b')
				plt.plot((R[i_next],R[i_next]), (down,upp()),'b')
				#up = up + eps

				#Y ahora voy para la atras del next
				plt.plot((R[i_next],L[i_next]), (up,up),'b')
	else:
		#Aca el nodo next esta ANTES que el now


		if isInverse(now):
			#Estoy a la izquierda del NOW
			if isInverse(next):
				#Tengo que ir a la derecha del NEXT

				plt.plot((R[i_now],R[i_next]), (up,up),'b')
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
				#Tengo que ir a la izquierda del NEXT, pero esto a la derecha del NOW
				#Entonces primero bajo del NOW y voy por abajo
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

				#Primero voy por abajo hasta la derecha del next, que esta mas a la derecha
				plt.plot((R[i_now],R[i_now]), (up,down),'b')
				plt.plot((R[i_now],L[i_next]), (down,down),'b')
				plt.plot((L[i_next],L[i_next]), (down,upp()),'b')
				#up = up + eps

				#Y ahora voy para la atras del next
				plt.plot((L[i_next],R[i_next]), (up,up),'b')



#Para 2 clavos por ahora
def main(nn):

	s = "a_1*a_2*a_1^(-1)*a_2^(-1)"
	n = int(nn)

	S = s.split("*")
	print S
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




	px1 = 3
	px2 = 6
	height = 5

	plt.plot([px1], [height], marker='o', markersize=3, color="red")
	plt.plot([px2], [height], marker='o', markersize=3, color="red")

	olds = ""
	for index,s in enumerate(S):
		print up
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

	a = 10 + pow(2,n)
	print a

	plt.axis([0, 3*(n+1) + 50, 0, 15])

	img=mpimg.imread('images/monalisa.jpg')
	#imgplot = plt.imshow(img)

	myaximage = plt.imshow(img, aspect='auto', extent=(1,8,-5,5), alpha=0.5, origin='upper', zorder=-1)

	plt.show()



if __name__=="__main__":
	main(sys.argv[1])