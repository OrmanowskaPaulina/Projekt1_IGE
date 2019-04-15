# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 11:22:42 2019

@author: paulinka
"""

# główne okno
from PyQt5.QtWidgets import QApplication, QWidget
# widżety
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QLabel, QGridLayout 
from PyQt5.QtWidgets import QLineEdit, QPushButton
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
from polozenie_wsp import polozenie_wsp 
from polozenie_odc import Polozenie

#okno główne
class AppWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.interfejs_widgets()
        self.interfejs()

    def interfejs(self):
        # główne okno
        self.resize(600, 600)                       # szerokość i wysokość okna;
        self.setWindowIcon(QIcon('icon_calc.png'))  # ikona graficzna program
        self.setWindowTitle("Kalkulator")           # tytuł okna
        self.show()                                 # wyświetlenie okna 

    def interfejs_widgets(self):
        
        xaLabel = QLabel("X a:", self) #etykiety 
        yaLabel = QLabel("Y a:", self)
        xbLabel = QLabel("X b:", self)
        ybLabel = QLabel("Y b:", self)
        xcLabel = QLabel("X c:", self)
        ycLabel = QLabel("Y c:", self)
        xdLabel = QLabel("X d:", self)
        ydLabel = QLabel("Y d:", self)
        PxLabel = QLabel("X: ", self)
        PyLabel = QLabel("Y: ", self)
        
        self.xaEdit = QLineEdit() #okna edycji, aby wpisać dane
        self.yaEdit = QLineEdit()
        self.xbEdit = QLineEdit()
        self.ybEdit = QLineEdit()
        self.xcEdit = QLineEdit()
        self.ycEdit = QLineEdit()
        self.xdEdit = QLineEdit()
        self.ydEdit = QLineEdit()
        self.PpxEdit = QLineEdit()
        self.PpyEdit = QLineEdit() 
        self.komEdit = QLineEdit() 
        
        self.figure = plt.figure() #wykres
        self.canvas = FigureCanvas(self.figure)
        
        #wyswietlenie
        grid = QGridLayout() #wybranie układu 
        grid.addWidget(xaLabel, 1, 0) #1 wiersz 0 kolumna
        grid.addWidget(self.xaEdit, 1, 1)
        grid.addWidget(yaLabel, 2, 0)
        grid.addWidget(self.yaEdit, 2, 1)

         
        grid.addWidget(xbLabel, 3, 0) 
        grid.addWidget(self.xbEdit, 3, 1)
        grid.addWidget(ybLabel, 4, 0)
        grid.addWidget(self.ybEdit, 4, 1)

        
        grid.addWidget(xcLabel, 5, 0) 
        grid.addWidget(self.xcEdit, 5, 1)
        grid.addWidget(ycLabel, 6, 0)
        grid.addWidget(self.ycEdit, 6, 1)

        
        grid.addWidget(xdLabel, 7, 0)
        grid.addWidget(self.xdEdit, 7, 1)
        grid.addWidget(ydLabel, 8, 0)
        grid.addWidget(self.ydEdit, 8, 1)
        
        grid.addWidget(self.PpxEdit,10, 1)
        grid.addWidget(PxLabel,10, 0)
        grid.addWidget(self.PpyEdit,11, 1)
        grid.addWidget(PyLabel,11, 0)
        grid.addWidget(self.komEdit,12, 0, 1, 2) 
        grid.addWidget(self.canvas, 1, 2, -1, -1) # 1 wiersz, 2 kolumna, rozciaga do końca 
        self.setLayout(grid) #wyswietlenie naszego layoutu
        
        clearBtn = QPushButton("Usuń dane", self) #przycisk
        grid.addWidget(clearBtn, 14, 0, 1, 2)
        clearBtn.clicked.connect(self.czyszczenie)  #połączenie przycisku z funckją 

        PpBtn = QPushButton('Punkt przecięcia',self)
        grid.addWidget(PpBtn, 9, 0, 1, 2)        
        PpBtn.clicked.connect(self.Pp)
        
        rysujBtn   = QPushButton("Rysuj", self)
        grid.addWidget(rysujBtn, 13, 0, 1, 2)
        rysujBtn.clicked.connect(self.rysuj)
        
        dodBtn   = QPushButton("Położenie punktu względem odcinka", self)
        grid.addWidget(dodBtn, 16, 0, 1, 2)
        dodBtn.clicked.connect(self.Dodatek)
        
        koniecBtn   = QPushButton("Koniec", self)
        grid.addWidget(koniecBtn, 17, 0, -1, -1)
        koniecBtn.clicked.connect(self.koniec)


    def koniec(self): #definicja zamykająca okno
        self.close()    
        
    def oblicz(self):
        self.rysuj()
               
    def sprawdzLiczbe(self, element):
        if element.text().lstrip('-').replace('.','',1).isdigit():
            return float(element.text())
        else:
            element.setFocus()
            return None

    def Pp(self): 
        xa = self.sprawdzLiczbe(self.xaEdit) #sprawdzanie wpisywanej cyfry funkcją sprawdzLiczbe
        ya = self.sprawdzLiczbe(self.yaEdit)
        xb = self.sprawdzLiczbe(self.xbEdit)
        yb = self.sprawdzLiczbe(self.ybEdit)
        xc = self.sprawdzLiczbe(self.xcEdit)
        yc = self.sprawdzLiczbe(self.ycEdit)
        xd = self.sprawdzLiczbe(self.xdEdit)
        yd = self.sprawdzLiczbe(self.ydEdit)    
        if None not in [xa, ya, xb, yb, xc, yc, xd, yd]: #jesli umieszczono dobre dane program przechodzi do obliczania
                xa = float(self.xaEdit.text())
                ya = float(self.yaEdit.text())
                xb = float(self.xbEdit.text())
                yb = float(self.ybEdit.text())
                xc = float(self.xcEdit.text())
                yc = float(self.ycEdit.text())
                xd = float(self.xdEdit.text())
                yd = float(self.ydEdit.text())    
                Ppx, Ppy, komentarz = polozenie_wsp(xa,ya,xb,yb,xc,yc,xd,yd)
                self.PpxEdit.setText(str(Ppx))
                self.PpyEdit.setText(str(Ppy))
                self.komEdit.setText(komentarz)
    
    def czyszczenie(self): #funkcja czyszcząca okna edycji
        self.xaEdit.clear()
        self.yaEdit.clear()
        self.xbEdit.clear()
        self.ybEdit.clear()
        self.xcEdit.clear()
        self.ycEdit.clear()
        self.xdEdit.clear()
        self.ydEdit.clear()
        self.PpxEdit.clear()
        self.PpyEdit.clear()
        self.komEdit.clear()   
     
    def rysuj(self): #rysowanie wykresu
        xa = self.sprawdzLiczbe(self.xaEdit)
        ya = self.sprawdzLiczbe(self.yaEdit)
        xb = self.sprawdzLiczbe(self.xbEdit)
        yb = self.sprawdzLiczbe(self.ybEdit)
        xc = self.sprawdzLiczbe(self.xcEdit)
        yc = self.sprawdzLiczbe(self.ycEdit)
        xd = self.sprawdzLiczbe(self.xdEdit)
        yd = self.sprawdzLiczbe(self.ydEdit)
        if None not in [xa, ya, xb, yb, xc, yc, xd, yd]:
            xa = float(self.xaEdit.text())
            ya = float(self.yaEdit.text())
            xb = float(self.xbEdit.text())
            yb = float(self.ybEdit.text())
            xc = float(self.xcEdit.text())
            yc = float(self.ycEdit.text())
            xd = float(self.xdEdit.text())
            yd = float(self.ydEdit.text())
            Xp, Yp, komentarz = polozenie_wsp(xa,ya,xb,yb,xc,yc,xd,yd)
        
            self.figure.clear() #czyszczenie wykresu
            ax = self.figure.add_subplot(111)
            ax.plot(xa, ya, 'bv') #zaznaczenie punktu A, na kolor niebieski, trójkątem
            ax.plot(xb, yb, 'bo') #zaznaczenie punktu B, na kolor niebieski, kółeczkiem
            ax.plot(xc, yc, 'mv')
            ax.plot(xd, yd, 'mo')
            ax.plot(Xp, Yp, 'k*')
            ax.plot([xa, xb], [ya, yb],'b') #zaznaczenie odcinka AB na niebiesko
            ax.plot([xc, xd], [yc, yd],'m')
            ax.plot([xa, Xp], [ya,Yp],'g:')
            ax.plot([xb, Xp], [yb,Yp],'g:')
            ax.plot([xc, Xp], [yc,Yp],'g:')
            ax.plot([xd, Xp], [yd,Yp],'g:')
            ax.legend(['A', '\n' + 'B','\n' + 'C','\n' + 'D','\n' + 'Pp'], loc="lower right") #legenda
            ax.set_ylabel('Y') #nazwanie osi
            ax.set_xlabel('X')
            self.canvas.draw() #wyswietlenie wykresu
        
    def Dodatek(self):
        nadawca = self.sender()
        if nadawca.text() == "Położenie punktu względem odcinka":
             okno = Polozenie()
             okno.show()
             okno.exec()
        
if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)    # sys.argv - pozwala applikacji otrzymywać parametry z linii poleceń
    okno = AppWindow()             # utworzenie obiektu reprezentujący okno aplikacji, czyli instancję klasy Kalkulator
    sys.exit(app.exec_())           # główna pętla (exit_) - podkreślenie, to dlatego, że jej nazwa pokrywa się z innym kluczem Pythona
