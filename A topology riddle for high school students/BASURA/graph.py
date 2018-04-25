from numpy import *
import math
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


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





#Para 2 clavos por ahora
def main(nn):
	n = int(nn)


	eps = 0.4
	#tambien puedo de a varios

	#for i in range(1,n):
	plt.plot([3], [10], marker='o', markersize=3, color="red")
	plt.plot([6], [10], marker='o', markersize=3, color="red")


	up = 12
	down = 8


	x1l = 2
	x1r = 4
	
	y1l = 5
	y1r = 7

	px1 = 3
	px2 = 6
	height = 5

	plt.plot([px1], [height], marker='o', markersize=3, color="red")
	plt.plot([px2], [height], marker='o', markersize=3, color="red")

	plt.plot((px1,x1l), (height, up), 'b')
	
	plt.plot((x1l, x1r), (up, up), 'b')
	plt.plot((x1r, y1l), (up, up), 'b')
	plt.plot((y1l, y1r), (up, up), 'b')
	plt.plot((y1r, y1r), (up, down), 'b')
	plt.plot((y1r, y1l), (down, down), 'b')
	plt.plot((y1l, x1r), (down, down), 'b')
	up = up + eps

	plt.plot((x1r, x1r), (down, up), 'b')
	plt.plot((x1r, x1l), (up, up), 'b')
	down = down + eps

	#Tal vez me sirva mantener los puntos visitados y si veo que se va a repetir alguno le sumo epsilon a la coordenada y!!

	#funcion que dadas dos coord me devuelva lo que hay que hacer
	#uso que siempre son "consecutivas" entonces lo que hay que hacer es facil

	down += eps
	plt.plot((x1l, x1l), (up, down), 'b')
	plt.plot((x1l, y1r), (down, down), 'b')
	plt.plot((y1r, y1r), (down, up), 'b')
	plt.plot((y1r, y1l), (up, up), 'b')
	plt.plot((y1l, y1l), (up, down), 'b')
	plt.plot((y1l, px2), (down, height), 'b')

	#plt.plot([3,6], [10,10], 'ro')
	plt.axis([0, 1000, -5, 20])

	img=mpimg.imread('images/monalisa.jpg')
	#imgplot = plt.imshow(img)

	myaximage = plt.imshow(img, aspect='auto', extent=(1,8,-5,5), alpha=0.5, origin='upper', zorder=-1)

	plt.show()



if __name__=="__main__":
	main(argv[1])