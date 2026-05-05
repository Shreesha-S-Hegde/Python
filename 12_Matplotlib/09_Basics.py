import matplotlib.pyplot as plt
import numpy as np

xpoints=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
ypoints=([7,12,22,38,45,54,65,72,78,86,92,100,109,121,129,137,148,159,171,185])

plt.plot(xpoints,ypoints,"*:b",mfc="green",mec="red")
plt.show()