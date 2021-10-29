from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import uic
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
#from numpy import *
import numpy as np
import math

class Grafico:
    numeroPunti = 200                                       #variabile di classe che definisce qunti punti vengono
                                                            #generati per l'asse x del grafico

    def __init__(self, window):                             
        self.window = window                                #variabile di istanza che si riferisce all'oggetto di tipo Ui
                                                            #passato come argomento al patametro window di __init__
        self.figura = plt.figure()                          #crea una figura
        self.ax = self.figura.add_subplot(111)              #aggiunge alla figura un grafico (1 riga, 1 colonna, posizione 1)
        self.canvas = FigureCanvas(self.figura)             #crea un widget che può essere aggiunto alla GUI
        self.window.qvb_grafico.addWidget(self.canvas)      #inserisce il widget nel vertical box predisposto col designer
        self.statoGriglia = False

    def tracciaGrafico(self):
        
        #https://en.wikipedia.org/wiki/NACA_airfoil#Equation_for_a_cambered_4-digit_NACA_airfoil
        def camber_line( x, m, p, c ):
            return np.where((x>=0)&(x<=(c*p)),
                            m * (x / np.power(p,2)) * (2.0 * p - (x / c)),
                            m * ((c - x) / np.power(1-p,2)) * (1.0 + (x / c) - 2.0 * p ))

        def dyc_over_dx( x, m, p, c ):
            return np.where((x>=0)&(x<=(c*p)),
                            ((2.0 * m) / np.power(p,2)) * (p - x / c),
                            ((2.0 * m ) / np.power(1-p,2)) * (p - x / c ))

        def thickness( x, t, c ):
            term1 =  0.2969 * (np.sqrt(x/c))
            term2 = -0.1260 * (x/c)
            term3 = -0.3516 * np.power(x/c,2)
            term4 =  0.2843 * np.power(x/c,3)
            term5 = -0.1015 * np.power(x/c,4)
            return 5 * t * c * (term1 + term2 + term3 + term4 + term5)

        def naca4(x, m, p, t, c=1):
            dyc_dx = dyc_over_dx(x, m, p, c)
            th = np.arctan(dyc_dx)
            yt = thickness(x, t, c)
            yc = camber_line(x, m, p, c)  
            return ((x - yt*np.sin(th), yc + yt*np.cos(th)), 
                    (x + yt*np.sin(th), yc - yt*np.cos(th)))

        eq = self.window.lE_formula.text()
        m = float(eq[0:1])/100
        p = float(eq[1:2])/10
        t = float(eq[2:4])/100

        c = 1.0

        self.ax.clear()
        x = np.linspace(0,1,200)
        for item in naca4(x, m, p, t, c):
            self.ax.plot(item[0], item[1], 'b')
        self.ax.plot(x, camber_line(x, m, p, c), 'r')
        self.ax.axis('equal')
        #self.ax.xlim(-0.05, 1.05)
        #self.ax.title('NACA 2412')
        self.ax.grid(self.statoGriglia)
        self.canvas.draw()



    
    def griglia(self, statoGriglia):
        self.statoGriglia = statoGriglia
        self.ax.grid(statoGriglia)
        self.canvas.draw()


class Ui(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('naca.ui', self)
        self.grafico = Grafico(self)

    def pB_graficoClick(self):
        self.grafico.tracciaGrafico()

    
    def cB_grigliaChange(self):
        self.grafico.griglia(self.cB_griglia.isChecked())
        


app=QApplication([])
window = Ui()
window.show()
app.exec()