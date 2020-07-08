import numpy as np
import matplotlib.pyplot as plt
import csv


x = np.array([])
y = np.array([])
z = np.array([])


with open('total_cases.csv') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    next(plots)
    for row in plots:
        x = np.append(x,row[0])
        y = np.append(y,row[1])        

fig, ax = plt.subplots()


ax.plot(x,y, label = 'World COVID-19 Cases')
# ax.plot(x,z, label= "US COVID-19 Cases")
ax.set_xlabel('Date')
ax.set_ylabel('Cases')
ax.legend()
ax.set_title('COVID-19 Cases')
ax.xaxis.set_major_locator(plt.LinearLocator(12))
ax.yaxis.set_major_locator(plt.AutoLocator())
for tick in ax.get_xticklabels():
    tick.set_rotation(45)
plt.show()
