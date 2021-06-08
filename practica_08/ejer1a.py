import numpy as np

nx=100
ny=80

#Matriz Mvp
Mvp=np.array([
 [nx/2, 0,0,(nx-1)/2],
 [0,ny/2,0,(ny-1)/2],
 [0,0,1,0],
 [0,0,0,1]
 ])

# Puntos del plano rojo
plane = np.array([[-1,1,1,-1],
                  [2,2,0,0],
                  [-6,-6,-6,-6],
                  [1,1,1,1]])

#valores de l,b,n,r,t y f
l=-2; b=0; n=-4
r=2; t=3; f=-8

#Creacion de la matriz ortogonal
Morth=np.array([[2/(r-l),0,0,-((r+l)/(r-l))],
                [0,2/(t-b),0,-((t+b)/(t-b))],
                [0,0,2/(n-f),-((n+f)/(n-f))],
                [0,0,0,1]])
print('Matriz MVP: \n',Mvp)

#Proyeccion de transformacion ortografica
M=np.matmul(Mvp,Morth)
Orthographic = np.matmul(M,plane)
print('Proyeccion Ortografica: \n', Orthographic)

# e = (0,2,2)
e = np.array([0,5,2])
g = np.array([0,-2,-5])
t = np.array([0,1,0])

w = -(g/np.linalg.norm(g))
t_w = np.cross(t,w)
u = t_w / (np.linalg.norm(t_w))
v = np.cross(w,u)

print('vector U: \n',u)
print('vector V: \n',v)
print('vector W: \n',w)

#Construccion de la Mcam
Mcam_ = np.zeros((4,4))
Mcam_[0:3,0] = u
Mcam_[0:3,1] = v
Mcam_[0:3,2] = w
Mcam_[0:3,3] = e
Mcam_[3,3] = 1
#print(Mcam_)
Mcam = np.linalg.inv(Mcam_)
print('matriz Mcam:\n ',Mcam)

#Proyecion de transformacion de camara: Ortografica
M_ = np.matmul(Mvp,Morth)
M =  np.matmul(M_, Mcam)
M_orth_cam = np.matmul(M,plane)
print('Proyecion ortografica con transformacion de camara:\n',M_orth_cam)

