import numpy as np
import math as m
import matplotlib.pyplot as plt

VERBOSE=[]
L=100
B=5
D=4
T=2
W=0.08
A=1
t=4.2
dx=1
posta_alanı=[]
denklemler=[]
CTRL=[]
Alan=[]                 #drafta göre değişkenlik göstere alanlar
def calc(ksi,x1):
    if ksi==0:
        ksi_alan=denklemler[x1][2]
        #print("check1")
        #print(ksi_alan)
        return ksi_alan
    else:
        ksi_alan=denklemler[x1][0]*ksi*ksi+denklemler[x1][1]*ksi+denklemler[x1][2]
        #print("check2")
        return ksi_alan
#hull=np.array([[0,0,0,0,0,0],
#               [1,1,1,1,1,1],
#               [2,2,2,2,2,2],
#               [3,3,3,3,3,3],
#               [4,4,4,4,4,4],
#               [5,5,5,5,5,5],
#               [6,6,6,6,6,6],
#               [7,7,7,7,7,7],
#               [8,8,8,8,8,8],
#               [9,9,9,9,9,9],
#               [10,10,10,10,10,10]])
hull=np.array([[0.0,0.0,0.0,0.0,0.0890,0.2860,0.4380],                  #seri 60 örnek offset
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




nm=hull.shape  #offsetin boyutlarını saklıyor

dp=L/int(nm[0]-1)
posta_aralığı=np.arange(0,nm[0])*dp
#print(posta_aralığı)
offset=hull*B
#print(offset)
for _ in range(int(nm[0])):
    for __ in range(int(nm[1])):
        trapez=2*np.trapz(offset[_][0:__+1],dx=dp)
        posta_alanı.append(trapez)

posta_alanı=np.reshape(posta_alanı,(int(nm[0]),int(nm[1])))
#print(np.reshape(posta_alanı,(int(nm[0]),int(nm[1]))))                 #posta alanlarını kontrol
dd=np.linspace(0,D,int(nm[1]))
#print(dd)
for q in range(int(nm[0])):
    z=np.polyfit(dd,posta_alanı[q],6)
    denklemler.append(z)
    int
#print(denklemler)

aft_uzaklık_array=[]
dalga_draft_alan=[]

for adım in range(int(L/dx)+1):

    aft_uzaklık=adım*dx
    posta_draft = A * m.sin(W * aft_uzaklık + np.pi * t) + T
    #print(aft_uzaklık)






    if aft_uzaklık==posta_aralığı[0]:
        p0_alan=(np.power(posta_draft,6)*denklemler[0][0]+np.power(posta_draft,5)*denklemler[0][1]+np.power(posta_draft,4)*denklemler[0][2]+
                 np.power(posta_draft,3)*denklemler[0][3]+np.power(posta_draft,2)*denklemler[0][4]+posta_draft*denklemler[0][5]+denklemler[0][6])
        VERBOSE.append(p0_alan)
    if aft_uzaklık==posta_aralığı[1]:
        p1_alan=(np.power(posta_draft,6)*denklemler[1][0]+np.power(posta_draft,5)*denklemler[1][1]+np.power(posta_draft,4)*denklemler[1][2]+
                 np.power(posta_draft,3)*denklemler[1][3]+np.power(posta_draft,2)*denklemler[1][4]+posta_draft*denklemler[1][5]+denklemler[1][6])
        VERBOSE.append(p1_alan)
    if aft_uzaklık==posta_aralığı[2]:
        p2_alan=(np.power(posta_draft,6)*denklemler[2][0]+np.power(posta_draft,5)*denklemler[2][1]+np.power(posta_draft,4)*denklemler[2][2]+
                 np.power(posta_draft,3)*denklemler[2][3]+np.power(posta_draft,2)*denklemler[2][4]+posta_draft*denklemler[2][5]+denklemler[1][6])
        VERBOSE.append(p2_alan)
    if aft_uzaklık==posta_aralığı[3]:
        p3_alan=(np.power(posta_draft,6)*denklemler[3][0]+np.power(posta_draft,5)*denklemler[3][1]+np.power(posta_draft,4)*denklemler[3][2]+
                 np.power(posta_draft,3)*denklemler[3][3]+np.power(posta_draft,2)*denklemler[3][4]+posta_draft*denklemler[3][5]+denklemler[3][6])
        VERBOSE.append(p3_alan)
    if aft_uzaklık==posta_aralığı[4]:
        p4_alan=(np.power(posta_draft,6)*denklemler[4][0]+np.power(posta_draft,5)*denklemler[4][1]+np.power(posta_draft,4)*denklemler[4][2]+
                 np.power(posta_draft,3)*denklemler[4][3]+np.power(posta_draft,2)*denklemler[4][4]+posta_draft*denklemler[4][5]+denklemler[4][6])
        VERBOSE.append(p4_alan)
    if aft_uzaklık==posta_aralığı[5]:
        p5_alan=(np.power(posta_draft,6)*denklemler[5][0]+np.power(posta_draft,5)*denklemler[5][1]+np.power(posta_draft,4)*denklemler[5][2]+
                 np.power(posta_draft,3)*denklemler[5][3]+np.power(posta_draft,2)*denklemler[5][4]+posta_draft*denklemler[5][5]+denklemler[5][6])
        VERBOSE.append(p5_alan)
    if aft_uzaklık==posta_aralığı[6]:
        p6_alan=(np.power(posta_draft,6)*denklemler[6][0]+np.power(posta_draft,5)*denklemler[6][1]+np.power(posta_draft,4)*denklemler[6][2]+
                 np.power(posta_draft,3)*denklemler[6][3]+np.power(posta_draft,2)*denklemler[6][4]+posta_draft*denklemler[6][5]+denklemler[6][6])
        VERBOSE.append(p6_alan)
    if aft_uzaklık==posta_aralığı[7]:
        p7_alan=(np.power(posta_draft,6)*denklemler[7][0]+np.power(posta_draft,5)*denklemler[7][1]+np.power(posta_draft,4)*denklemler[7][2]+
                 np.power(posta_draft,3)*denklemler[7][3]+np.power(posta_draft,2)*denklemler[7][4]+posta_draft*denklemler[7][5]+denklemler[7][6])
        VERBOSE.append(p7_alan)
    if aft_uzaklık==posta_aralığı[8]:
        p8_alan=(np.power(posta_draft,6)*denklemler[8][0]+np.power(posta_draft,5)*denklemler[8][1]+np.power(posta_draft,4)*denklemler[8][2]+
                 np.power(posta_draft,3)*denklemler[8][3]+np.power(posta_draft,2)*denklemler[8][4]+posta_draft*denklemler[8][5]+denklemler[8][6])
        VERBOSE.append(p8_alan)
    if aft_uzaklık==posta_aralığı[9]:
        p9_alan=(np.power(posta_draft,6)*denklemler[9][0]+np.power(posta_draft,5)*denklemler[9][1]+np.power(posta_draft,4)*denklemler[9][2]+
                 np.power(posta_draft,3)*denklemler[9][3]+np.power(posta_draft,2)*denklemler[9][4]+posta_draft*denklemler[9][5]+denklemler[9][6])
        VERBOSE.append(p9_alan)
    if aft_uzaklık==posta_aralığı[10]:
        p10_alan=(np.power(posta_draft,6)*denklemler[10][0]+np.power(posta_draft,5)*denklemler[10][1]+np.power(posta_draft,4)*denklemler[10][2]+
                 np.power(posta_draft,3)*denklemler[10][3]+np.power(posta_draft,2)*denklemler[10][4]+posta_draft*denklemler[10][5]+denklemler[10][6])
        VERBOSE.append(p10_alan)


    aft_uzaklık_array.append(aft_uzaklık)

    #denklemler[x1][0] * ksi * ksi + denklemler[x1][1] * ksi + denklemler[x1][2]
    #draft_alan=(posta_draft**2)*denklemler[posta_n][0]+posta_draft*denklemler[posta_n][1]+denklemler[posta_n][2]




    sayac=1
    #print(posta_draft)



    CTRL.append(posta_draft)

    #Alan.append(draft_alan)

print(VERBOSE)
plt.subplot(2,1,1)
plt.plot(CTRL)
plt.subplot(2,1,2)
plt.plot(VERBOSE)
plt.show()

