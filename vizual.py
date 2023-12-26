import matplotlib.pyplot as plt
import numpy as np

ph=[8.5,8.5,8.4,8.4,8.5,8.5,8.5,8.4,8.3,8.3,8.3,8.4,8.3,8.3,0 ,8.6,8.6,8.6,8.6,8.6,8.6,8.6,8.6,8.6,8.6,8.6,8.5,8.6,8.6,8.6,8.6,8.6,8.6,8.5,8.6,8.5,8.4,8.2,8.4,7.9,8.1,7.8,7.9,8.2,8.4,7.9,7.8,7.7,7.9,0,8.7,8.2,8.6,8.2,7.9,8.1,7.8,8.4,8.3,8.6,8.3,8.4,8.3,9.3,8.9,8.8,8.5,8.6,8.2,9,8.7,9,9.1,8.7,8.6,8.8,9.06]
phnorm=[6.5,8.5]

dates=["Yanvar 2018", "Fevral 2018", "Mart 2018", "Aprel 2018","May 2018","Iyun 2018","Iyul 2018","Sentyabr 2018","Oktyabr 2018","Noyabr 2018","Dekabr 2018"]
abc=[]
a=0
av=[]
for i in range(len(dates)):
    abc=ph[i:i+7]
    n=7
    if 0 in abc:
        n=n-abc.count(0)
    a=sum(abc)/n
    av.append(a)
plt.plot(dates,av)
plt.show()
