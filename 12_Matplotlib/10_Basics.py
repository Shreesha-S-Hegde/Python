import matplotlib.pyplot as plt
import numpy as np

fy=np.array([2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026])
revenue=([100000,105000,125000,200000,210000,75000,60000,78000,49000,300000,350000,400000])

plt.plot(fy,revenue,"*:b",mfc="yellow",mec="red")
plt.show()