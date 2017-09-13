import numpy as np
import matplotlib.pyplot as plt
plt.figure('Ivan',figsize=(10,10),dpi=100)
x=np.linspace(0,25,25,endpoint=True)
E=1996+x
plt.plot(x,E,color='#B7F24F',linewidth=2,linestyle=':')
plt.xlim(0,25)
plt.xticks(np.arange(0,26,1))
plt.xlabel('Edad')
plt.ylim(1996,2021)
plt.yticks(np.arange(1996,2022,1))
plt.ylabel('Anio')
ax=plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
plt.savefig('Edad.png')
plt.show()
