# -*- coding: utf-8 -*-
"""
@author: Satyanarayana
"""
#import numpy as np
import matplotlib.pyplot as plt
#from mpl_toolkits import mplot3d
#plt =pyplot.Circle((0,0),5)

fig, ax = plt.subplots()

ax.set_xlim((0, 8))
ax.set_ylim((0, 6))
#ax.set(xlim=(-1, 1), ylim = (-1, 1))
ax.set_aspect('equal', adjustable='box')
a_circle = plt.Circle((2, 3), 1,color="black", fill=False)
ax.add_artist(a_circle)
ax.grid()

ax.set_title('Circle Tangent') 
ax.scatter(7,4,label='p (7,4)') 
ax.scatter(2,3,label='c (2,3)')
ax.scatter(2,4,label='q (2,4)') 
plt.annotate("p", (7.2, 4))
plt.annotate("c", (2, 2.6))
plt.annotate("q", (2, 4.2))
ax.plot((7,2),(4,3))
ax.plot((7,2),(4,4))
ax.plot((2,2),(3,4))
ax.legend()
plt.show()