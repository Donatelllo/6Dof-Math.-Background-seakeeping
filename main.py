import numpy as np
import matplotlib.pyplot as plt
#SETTING UP PARAMETERS
dt=0.01
ti=0
tf=2
t_sim_lenght=int(((tf-ti)/dt)+1)
saniye_adimi=(tf-ti)/dt
f3=0
f5=0

m=1
a33=114.44
a35=1
I55=1
add_I55=1
c33=1
c35=1
c53=1
c55=1
b33=705.17
b35=1
b53=1
b55=1

ones=np.identity(4)
sonuc=[]

M=np.array([[m+a33  ,a35],                              #[[m+a33  ,a35],
            [a53    ,I55+add_I55] ])                    #[a53    ,I55+add_I55] ])
M=np.invert(M)
R=np.array([[c33,c35],                                  #[[c33,c35],
            [c53,c55]])                                 #[c53,c55]])

D=np.array([[b33,b35],                                  #[[b33,b35],
            [b53,b55]])                                 #[b53,b55]])

r=np.divide(R,M)
d=np.divide(D,M)
#print(d)
#print(r)
AA_coupled35=np.array([[1,0,dt,0],
                       [0,1,0,dt],
                       [-r[0][0]*dt,-r[0][1]*dt,1-d[0][0]*dt,-d[0][1]*dt],
                       [-r[1][0]*dt,-r[1][1]*dt,-d[1][0]*dt,1-d[1][1]*dt]])
##AA_coupled35=AA_coupled35*dt

aa=np.array([[10],
             [1],
             [0],
             [0]])      #####

#AA_coupled35=np.add(AA_coupled35,ones)

FF=np.array([[0,0],
             [0,0],
             [1/(M[0][0]),0],
             [0,1/(M[1][1])]])
ff=np.array([[f3],
             [f5]])

FF_ff=np.matmul(FF,ff)


print(AA_coupled35)


for i in range(t_sim_lenght):


      aa=np.dot(AA_coupled35,aa)+np.dot(FF,ff)                   #
      sonuc.append(aa[0])

      #print(aa)
#print(sonuc)
plt.plot(sonuc)
plt.show()
