# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 11:06:20 2019

@author: paulina ormanowska
"""
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLabel, QGridLayout# rozmieszczenia
from PyQt5.QtWidgets import QLineEdit, QPushButton
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
from pol_wz import wzgl_odc
 

class Polozenie(QWidget):
    
    def __init__(self):
        super().__init__()

        self.interfejs()
        self.interfejs_widgets()
        
    def interfejs(self):
        # główne okno
        self.resize(500,500)      # szerokość i wysokość okna;
        self.setWindowTitle("Położenie względem odcinka")    # tytuł okna
        self.show()

    def interfejs_widgets(self):
#
        xaLabel = QLabel("X a:", self)
        yaLabel = QLabel("Y a:", self)
        xbLabel = QLabel("X b:", self)
        ybLabel = QLabel("Y b:", self)
        xcLabel = QLabel("X c:", self)
        ycLabel = QLabel("Y c:", self)
        komLabel = QLabel("Metoda 1:", self)
        kom1Label = QLabel("Metoda 2:", self)
        
        self.xaEdit = QLineEdit()
        self.yaEdit = QLineEdit()
        self.xbEdit = QLineEdit()
        self.ybEdit = QLineEdit()
        self.xcEdit = QLineEdit()
        self.ycEdit = QLineEdit()
        self.komEdit = QLineEdit() 
        self.kom1Edit = QLineEdit()
        
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        
        #wyswietlenie
        grid = QGridLayout()
        grid.addWidget(xaLabel, 1, 0) #1 wiersz 0 kolumna
        grid.addWidget(self.xaEdit, 1, 1)
        grid.addWidget(yaLabel, 2, 0)
        grid.addWidget(self.yaEdit, 2, 1)

         
        grid.addWidget(xbLabel, 3, 0) #1 wiersz 0 kolumna
        grid.addWidget(self.xbEdit, 3, 1)
        grid.addWidget(ybLabel, 4, 0)
        grid.addWidget(self.ybEdit, 4, 1)

        
        grid.addWidget(xcLabel, 5, 0) #1 wiersz 0 kolumna
        grid.addWidget(self.xcEdit, 5, 1)
        grid.addWidget(ycLabel, 6, 0)
        grid.addWidget(self.ycEdit, 6, 1)

        
        grid.addWidget(self.komEdit,3, 2)
        grid.addWidget(komLabel,2, 2)
        grid.addWidget(self.kom1Edit,5, 2)
        grid.addWidget(kom1Label,4, 2) 
        grid.addWidget(self.canvas, 7, 0, -1, -1) #rozciaga od konca i kolumny tez do konca
        self.setLayout(grid)

        polBtn   = QPushButton("Położenie", self)
        grid.addWidget(polBtn, 1, 2, 1, -1)
        polBtn.clicked.connect(self.polozenie)
        
        clearBtn   = QPushButton("Usuń dane", self)
        grid.addWidget(clearBtn, 6, 2, 1, -1)
        clearBtn.clicked.connect(self.czyszczenie)   
        
    def czyszczenie(self):
        self.xaEdit.clear()
        self.yaEdit.clear()
        self.xbEdit.clear()
        self.ybEdit.clear()
        self.xcEdit.clear()
        self.ycEdit.clear()
        self.komEdit.clear()   
        self.kom1Edit.clear() 
        
    def sprawdzLiczbe(self, element):
        if element.text().lstrip('-').replace('.','',1).isdigit():
            return float(element.text())
        else:
            element.setFocus()
            return None
        
    def polozenie(self):
        xa = self.sprawdzLiczbe(self.xaEdit)
        ya = self.sprawdzLiczbe(self.yaEdit)
        xb = self.sprawdzLiczbe(self.xbEdit)
        yb = self.sprawdzLiczbe(self.ybEdit)
        xc = self.sprawdzLiczbe(self.xcEdit)
        yc = self.sprawdzLiczbe(self.ycEdit)
        if None not in [xa, ya, xb, yb, xc, yc]:
            xa = float(self.xaEdit.text())
            ya = float(self.yaEdit.text())
            xb = float(self.xbEdit.text())
            yb = float(self.ybEdit.text())
            xc = float(self.xcEdit.text())
            yc = float(self.ycEdit.text())
            kome1, kome2 = wzgl_odc(xa,ya,xb,yb,xc,yc)
            self.komEdit.setText(kome1)
            self.kom1Edit.setText(kome2)
#wykres                        
            self.figure.clear()
            ax = self.figure.add_subplot(111)
            ax.plot(xa, ya, 'mv')
            ax.plot(xb, yb, 'mo')
            ax.plot(xc, yc, 'r*')
            ax.plot([xa, xb], [ya, yb],'m')
            ax.legend(["A", '\n' + 'B','\n' + 'P'], loc="upper left")
            ax.set_ylabel('Y')
            ax.set_xlabel('X')
            self.canvas.draw()
            
if __name__ == '__main__':
    import sys

    app = Polozenie(sys.argv)    # sys.argv - pozwala applikacji otrzymywać parametry z linii poleceń
    okno = Polozenie()             # utworzenie obiektu reprezentujący okno aplikacji, czyli instancję klasy Kalkulator
    sys.exit(app.exec_())     
    
    
    