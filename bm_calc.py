import numpy as np
import matplotlib.pyplot as plt
import math
dm=11    #posta sayısına göre değiştirilir şu an 11 posta
L=11
B=5
T=4
D=1.5*T
x=np.linspace(0,D,7)
DX=L/dm

posta_alanı=[]
denklemler=[]
A=1
fi=1
def formuller(xx,x1):
    if xx==0:
        ksi_alan=denklemler[x1][2]
        #print("check1")
        #print(ksi_alan)
        return ksi_alan
    else:
        ksi_alan=denklemler[x1][0]*xx*xx+denklemler[x1][1]*xx+denklemler[x1][2]
        #print("check2")
        return ksi_alan


offset=np.array([[0.0,0.0,0.0,0.0,0.0890,0.2860,0.4380],
                 [0.0594,0.2445,0.3140,0.4250,0.6140,0.7650,0.8540],
                 [0.2652,0.6038,0.7260,0.8250,0.8970,0.9500,0.9820],
                 [0.5436,0.8852,0.9570,0.9800,0.9910,0.9980,1.0000],
                 [0.7409,0.9870,1.0000,1.0000,1.0000,1.0000,1.0000],
                 [0.7710,0.9980,1.0000,1.0000,1.0000,1.0000,1.0000],
                 [0.7695 ,0.9980 ,1.0000 ,1.0000 ,1.0000 ,1.0000,1.0000],
                 [0.6399 ,0.9401 ,0.9710 ,0.9800 ,0.9850 ,0.9900, 0.9920],
                 [0.3369 ,0.7226, 0.7780, 0.8020, 0.8270, 0.8510 ,0.8770],
                 [0.0771, 0.3493, 0.3890, 0.4070 ,0.4300, 0.4720, 0.5360],
                 [0.0,0.0 ,0.0 ,0.0 ,0.0 ,0.0200 ,0.0510]])

offset_boyutlu=B*offset
for _ in range(dm):
    for i in range(7):
        trapez=2*np.trapz(offset_boyutlu[_][0:i])
        posta_alanı.append(trapez)

posta_alanı=np.reshape(posta_alanı,(dm,7))

#######POSTA ALAN DENKLEMLERİ######
for k in range(dm):
    z=np.polyfit(x,posta_alanı[k],2)
    denklemler.append(z)
denklemler=np.reshape(denklemler,(11,3))
kontrol=[]                                                            #kontrolleri sağlamak için
ksi_alanlar=[]
for s in range(100):
    sin_d=A*math.sin(s*DX+fi)+T                #dalga özellikleri değiştirilebilir
    #formuller(0,1)
    #print(formuller(0,0))
    ksi_alanlar.append(formuller(sin_d,s))
    kontrol.append(sin_d)
ksi_alanlar=np.asarray(ksi_alanlar)

hacim=np.trapz(ksi_alanlar)
print(hacim)
plt.plot(kontrol)
plt.show()