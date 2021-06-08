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

# Puntos red plane
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
                
M=np.matmul(Mvp,Morth)
Orthographic = np.matmul(M,plane)
print('Proyeccion Ortografica: \n', Orthographic)


g = np.array([0,-2,-5])
t = np.array([0,1,0])
e = np.array([0,5,2])
# e = (0,2,2)

w = -(g/np.linalg.norm(g))
t_w = np.cross(t,w)
u = t_w / (np.linalg.norm(t_w))
v = np.cross(w,u)

p = np.array([[n,0,0,0],
              [0,n,0,0],
              [0,0,n+f,-n*f],
              [0,0,1,0]])

Mper = np.matmul(Morth,p)
print('Matriz perspectica: \n', Mper)

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

M_ = np.matmul(Mvp,Morth)
M =  np.matmul(M_, Mcam)
M_orth_cam = np.matmul(M,plane)

print('Proyecion ortografica con transformacion de camara:\n',M_orth_cam)

M_ = np.matmul(Mvp,Mper)
M =  np.matmul(M_, Mcam)
M_per_cam = np.matmul(M,plane)

print('Proyecion perspectiva con transformacion de camara:\n',M_per_cam)

M_Homo = np.zeros((3,4))
M_Car = np.zeros((3,4))
Homo = np.zeros((1,4))
M_Homo[0:3,0:4] = M_per_cam[0:3,0:4]
Homo[0,0:4] = M_per_cam[3,0:4]
M_Car[0:3,0:2] = M_Homo[0:3,0:2]/Homo[0,0]
M_Car[0:3,2:4] = M_Homo[0:3,2:4]/Homo[0,2]

print('Proyeccion perspectiva con transformacion de camara (cartesiana):\n',M_Car)
