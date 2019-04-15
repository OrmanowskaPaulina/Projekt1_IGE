# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 12:18:23 2019

@author: paulina ormanowska
"""

import numpy as np 

def wzgl_odc(x1,y1,x2,y2,x3,y3):
    x = np.array([(x1), (x2), (x3)])
    y = np.array([(y1), (y2), (y3)])
    z = np.array([1,1,1])

    for (x1,y1,z1) in zip(x,y,z):
        det_xyz = (x[0]*y[1])+(x[1]*y[2])+(x[2]*y[0])-(x[2]*y[1])-(x[0]*y[2])-(x[1]*y[0])

    if det_xyz > 0:
        komentarz1 = 'Punkt C leży po prawej stronie odcinka AB'
    if det_xyz == 0:
        komentarz1 = 'Punkty ABC są współliniowe'
    if det_xyz < 0:
        komentarz1 = 'Punkt C leży po lewej stronie odcinka AB'

    for (x1,y1,z1) in zip(x,y,z):
        d_xab = x[0] - x[1]
        d_yap = y[0] - y[2]
        d_xap = x[0] - x[2]
        d_yab = y[0] - y[1]
        iloczyn = d_xab*d_yap - d_xap*d_yab
    
    if iloczyn > 0:
        komentarz2 = 'Punkt C leży po prawej stronie odcinka AB'
    if iloczyn == 0:
        komentarz2 = 'Punkty ABC są współliniowe'
    if iloczyn < 0:
        komentarz2 = 'Punkt C leży po lewej stronie odcinka AB'
            
    return komentarz1, komentarz2