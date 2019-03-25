# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 13:23:04 2019

@author: paulina ormanowska
"""

def wczytaj(wsp):
    komunikat = 'Podaj ' + wsp
    x = input(komunikat)
    
    while x.lstrip('-').replace('.', ' ', 1).isdigit() == 0:
        x = input(komunikat)
        
    return float(x)