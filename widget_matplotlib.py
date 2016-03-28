#!/usr/bin/env python
# -*- coding: <encoding name> -*-

"""Insert module docstring here."""

#imports

__author__ = "Sebastian Roll"

# http://scipy-cookbook.readthedocs.org/items/Matplotlib_PySide.html
import sys
import matplotlib
matplotlib.use('Qt4Agg')
matplotlib.rcParams['backend.qt4']='PySide'
import pylab

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from PySide import QtCore, QtGui

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)

    # generate the plot
    fig = Figure(figsize=(600,600), dpi=72, facecolor=(1,1,1), edgecolor=(0,0,0))
    ax = fig.add_subplot(111)
    ax.plot([0,1])
    # generate the canvas to display the plot
    canvas = FigureCanvas(fig)

    win = QtGui.QMainWindow()
    # add the plot canvas to a window
    win.setCentralWidget(canvas)

    win.show()

    sys.exit(app.exec_())



# http://stackoverflow.com/questions/6723527/getting-pyside-to-work-with-matplotlib
# Note: this clears and redraws the entire plot every time (since the shape of my data keeps changing) and so isn't fast.
import matplotlib

matplotlib.use('Qt4Agg')
matplotlib.rcParams['backend.qt4']='PySide'

from matplotlib.figure import Figure
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas

class MatplotlibWidget(FigureCanvas):

    def __init__(self, parent=None,xlabel='x',ylabel='y',title='Title'):
        super(MatplotlibWidget, self).__init__(Figure())

        self.setParent(parent)
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.axes = self.figure.add_subplot(111)

        self.axes.set_xlabel(xlabel)
        self.axes.set_ylabel(ylabel)
        self.axes.set_title(title)

class UseExample:
    def __init__(self):
        # set up main widget here

    def  setupPlot(self):
        # create a matplotlib widget
        self.DataPlot = MatplotlibWidget()
        # create a layout inside the blank widget and add the matplotlib widget
        layout = QtGui.QVBoxLayout(self.ui.widget_PlotArea)
        layout.addWidget(self.DataPlot,1)

    def plotDataPoints(self,x,y):
        self.DataPlot.axes.clear()
        self.DataPlot.axes.plot(x,y,'bo-')
        self.DataPlot.draw()