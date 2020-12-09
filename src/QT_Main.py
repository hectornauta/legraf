import datetime
import time
import os
import sys
#import logging
#logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

from copy import deepcopy

from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget


from matplotlib import pyplot
from matplotlib import colors

from QT_Main_UI import *
from funciones import *

import numpy as np

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, QRunnable, QThreadPool,pyqtSlot, pyqtSignal
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator

from matplotlib.colors import ListedColormap
from matplotlib.figure import Figure


import time

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        #Inicializando botones y esas weas
        self.threadpool = QThreadPool()
        
        #rx = QRegExp("[0-9]\.?[0-9]*")
        #validator = QRegExpValidator(rx, self)
        #self.lineCelda.setValidator(validator)
        self.lineXPunto.setText('1')
        self.lineYPunto.setText('1')
        
        rx2 = QRegExp("[+-]?[0-9]*\.[0-9]*")
        validator2 = QRegExpValidator(rx2, self)
        self.lineXPunto.setValidator(validator2)
        self.lineYPunto.setValidator(validator2)

        #self.comboSeparador.addItems([';',',','Tab','Espacio'])

        #self.separadores = {',':',',';':';','Tab':'\t','Espacio':' '}

        self.diccionario = {}
        self.datos = None
        self.archivo = None   


        self.grafico2D = pyplot.figure(figsize=(8,8))

        self.canvas = FigureCanvas(self.grafico2D)
        self.toolbar = NavigationToolbar(self.canvas, self)
        
        layout = QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        self.widgetGrafico.setLayout(layout)

        self.colores = list(colors.TABLEAU_COLORS)

        self.btnInsertarPunto.clicked.connect(lambda: self.insertarPunto(self.lineXPunto.text(),self.lineYPunto.text()))

    

    def insertarPunto(self,coordenadax,coordenaday):
        x = float(coordenadax)
        y = float(coordenaday)
        limiteInferiorX = -100
        limiteSuperiorX = 100
        limiteInferiorY = -100
        limiteSuperiorY =100
        #pyplot.clf()
        grafico = self.grafico2D
        ax = grafico.add_subplot()
        ax.plot(limiteInferiorX,limiteInferiorY)
        ax.set_aspect(1)
        pyplot.xlim(limiteInferiorX,limiteSuperiorX)
        pyplot.ylim(limiteInferiorY,limiteSuperiorY)
        pyplot.xlabel('X')
        pyplot.ylabel('Y')
        pyplot.plot(x,y,marker = 'o',color = self.colores[0])

        self.canvas.draw()







                
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
