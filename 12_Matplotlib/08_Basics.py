import matplotlib.pyplot as plt
import numpy as np

xpoints=np.array([10,20,30,40,50])
ypoints=np.array([200,100,90,50,60])

plt.plot(xpoints,ypoints,marker="*",markersize=40,mfc="red",mec="yellow")
plt.show()