# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 12:19:48 2019

@author: paulina ormanowska
"""
def polozenie_wsp(x1,y1,x2,y2,x3,y3,x4,y4):

    dx_ac = x3 - x1
    dx_ab = x2 - x1
    dx_cd = x4 - x3
    dy_ac = y3 - y1
    dy_ab = y2 - y1
    dy_cd = y4 - y3

    mianownik = ((dx_ab*dy_cd)-(dy_ab*dx_cd))
    if mianownik == 0:
        komentarz = ('Proste są równoległe')
        Xp = 'brak'
        Yp = 'brak'
    else:
        t1 = ((dx_ac*dy_cd)-(dy_ac*dx_cd))/((dx_ab*dy_cd)-(dy_ab*dx_cd))
        t2 = ((dx_ac*dy_ab)-(dy_ac*dx_ab))/((dx_ab*dy_cd)-(dy_ab*dx_cd)) 

        if (0 <= t1 <= 1) and (0 <= t2 <= 1):
            komentarz = ('Punkt przecięcia leży do obu odcinkach')
        elif (0 <= t1 <= 1) and ((t2 < 0) or (t2 > 1)):
            komentarz = ('Punkt przecięcia leży na przedłużeniu CD')
        elif (0 <= t2 <= 1) and ((t1 < 0) or (t1 > 1)):
            komentarz = ('Punkt przecięcia leży na przedłużeniu AB')
        else:
            komentarz = ('Punkt przecięcia leży przedłużeniu obu odcinków')
        
        Xp = round((x1 + t1*(dx_ab)),3)
        Yp = round((y1 + t1*(dy_ab)),3)
        x1 = round(x1,3)
        y1 = round(y1,3)
        x2 = round(x2,3)
        y2 = round(y2,3)
        x3 = round(x3,3)
        y3 = round(y3,3)
        x4 = round(x4,3)
        y4 = round(y4,3)

        with open ('dane_p1.txt','w') as pp_dane: 
            pp_dane.write('|{:^4}|{:^10}|{:^10}|\n'.format(' ','X','Y')) #zapisywanie danych przy pomocy funkcji format
            pp_dane.write(28*'-')
            pp_dane.write('\n|{:^4}|{:^10}|{:^10}|\n|{:^4}|{:^10}|{:^10}|\n|{:^4}|{:^10}|{:^10}|\n|{:^4}|{:^10}|{:^10}|\n|{:^4}|{:^10}|{:^10}|\n'.format('A',x1,y1,'B',x2,y2,'C',x3,y3,'D',x4,y4,'Pp',Xp,Yp))
    
    return Xp,Yp, komentarz