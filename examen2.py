import numpy as np
import matplotlib.pyplot as plt
plt.figure('Grafica',figsize=(10,10),dpi=100)
x=np.linspace(-np.pi,np.pi,100,endpoint=True)
E=3*np.cos(x) + 2014
plt.plot(x,E,color='#FF4000',linewidth=2,linestyle=':') 
plt.xlim(-4,4)                                          
plt.xticks(np.arange(-4,4,1))                          
plt.xlabel('ABC')                                      
plt.ylim(2011,2018)                                     
plt.yticks(np.arange(2011,2017,1))                      
plt.ylabel('DEF')                                      
ax=plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',2014))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))
plt.savefig('Cos.png')
plt.show()

