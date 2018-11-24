import random as rand
import math as m
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mt
from mpl_toolkits.mplot3d import Axes3D

plt.rcParams['agg.path.chunksize']=20000

def PART_A():
    total = 10
    for j in range (1, 8):
        inside_point_x=[]
        inside_point_y=[]
        outside_point_x=[]
        outside_point_y=[]
        inside = 0
        for i in range(0, total):
            #generating random points, with each coordinate lying between [-1, 1]
            x = rand.random()-0.5
            y = rand.random()-0.5
            x=x*2
            y=y*2
            #checking whether the point lies within the circle
            if m.sqrt(x**2 + y**2) < 1.0:
                inside += 1
                inside_point_x.append(x)
                inside_point_y.append(y)
            else:
                outside_point_y.append(x)
                outside_point_x.append(y)

        #calculating the value of pi
        pi = (float(inside) / total) * 4

        print (total)
        print(pi)
        
        total = total*10
        plt.clf()
        #plotting points 
        plt.scatter(inside_point_x,inside_point_y,c='b')
        plt.scatter(outside_point_x,outside_point_y,c='r')

        plt.savefig('Iteration_'+str(j)+'.png')
        print ("Over")

def PART_B():
	print ("start")
	total = 10

	for j in range (1, 8):
		inside = 0
		inside_point_x=[]
		inside_point_y=[]
		inside_point_z=[]
		outside_point_x=[]
		outside_point_y=[]
		outside_point_z=[]
		for i in range(0, total):
			#generating random points, with each coordinate lying between [-1, 1]
			x = rand.random()-0.5
			y = rand.random()-0.5
			z = rand.random()-0.5
			x=x*2
			y=y*2
			z=z*2
			#checking whether the point lies within the sphere
			if m.sqrt(x**2 + y**2 + z**2) < 1.0:
				inside += 1
				inside_point_x.append(x)
				inside_point_y.append(y)
				inside_point_z.append(z)
			else:
				outside_point_x.append(x)
				outside_point_y.append(y)
				outside_point_z.append(z)

		#calculating the value of pi
		pi = (float(inside) / total) * 6

		print (total)
		print(pi)
	    
		total = total*10

		plt.clf()

		fig=plt.figure()
		ax=fig.add_subplot(111,projection='3d')
		#plotting points that lie within the sphere
		ax.scatter(inside_point_x,inside_point_y,inside_point_z,c='b',marker='o')
		
		ax.set_xlabel('X')
		ax.set_ylabel('Y')
		ax.set_zlabel('Z')
		plt.savefig('Iteration_'+str(j)+".png")

if __name__=="__main__":
	PART_A()
	PART_B()
