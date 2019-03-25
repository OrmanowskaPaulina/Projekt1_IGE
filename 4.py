# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 12:19:48 2019

@author: paulinka
"""
from def_wczytaj import wczytaj 
import matplotlib.pyplot as plt

x1 = wczytaj('X1: ')
y1 = wczytaj('Y1: ')
x2 = wczytaj('X2: ')
y2 = wczytaj('Y2: ')
x3 = wczytaj('X3: ')
y3 = wczytaj('Y3: ')
x4 = wczytaj('X4: ')
y4 = wczytaj('Y4: ')

dx_ac = x3 - x1
dx_ab = x2 - x1
dx_cd = x4 - x3
dy_ac = y3 - y1
dy_ab = y2 - y1
dy_cd = y4 - y3

mianownik = ((dx_ab*dy_cd)-(dy_ab*dx_cd))
if mianownik == 0:
    print('Proste są równoległe')
else:
    t1 = ((dx_ac*dy_cd)-(dy_ac*dx_cd))/((dx_ab*dy_cd)-(dy_ab*dx_cd))
    t2 = ((dx_ac*dy_ab)-(dy_ac*dx_ab))/((dx_ab*dy_cd)-(dy_ab*dx_cd)) 
    print ('t1',t1,'t2',t2)
    if ((t1 > 0 and t1 < 1 or t2 > 0 and t2 < 1)):
        print('Punkt przecięcia leży do obu odcinkach')
    elif ((t1 >= 0 and t1 <= 1 or t2 >= 0 and t2 <= 1)):
        print('Punkt leży na przedluzeniu jednego odcinka')
    elif ((t1 < 0 and t2 > 1 or t2 < 0 and t1 > 1 )):
        print('Leży na przedłużeniu obu odcinków')
Xp = x1 + t1*(dx_ab)
Yp = y1 + t1*(dy_ab)

Xp1 = x3 + t2*(dx_cd)
Yp1 = y3 + t2*(dy_cd)
print('Współrzędne punktu przecięcia wynoszą: ', 'Xp: ',round(Xp1,3),'Yp: ', round(Yp1,3) )
plik = open('wsp.txt', 'w')
plik.write('Współrzędne punktu przecięcia: Xp: {:.3f} Yp: {:.3f}'.format(Xp1,Yp1))

    
plt.plot([x1,x2,x3,x4,Xp], [y1,y2,y3,y4,Yp], 'ro')
plt.plot([x1, x2], [y1, y2])
plt.plot([x3, x4], [y3, y4])
plt.show()