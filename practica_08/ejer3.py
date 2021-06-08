import numpy as np

n = -4; f = -8
n_x = 100; n_y = 80
theta = np.radians(60)

#t, b, r, l
t = np.tan(theta/2)*np.abs(n)
r = (n_x/n_y)*t
l = -r
b = -t

e = np.array([0,4,2])
g = np.array([0,-2,-5])
t2 = np.array([0,1,0])

print('valor de t: ',t)
print('valor de b: ',b)
print('valor de r: ',r)
print('valor de l: ',l)
