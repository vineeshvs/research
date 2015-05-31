#!/usr/bin/python
# -*- coding: utf-8 -*-
#  Author: vineeshvs

import sys, ctypes #added ctypes
from PyQt4 import QtGui, QtCore
from ctypes import cdll
from ctypes import *
#from slicing import *

#mydll = cdll.LoadLibrary('/home/vineeshvs/Dropbox/wel/workspace/Atmel/libhello.so')
#mydll = ctypes.CDLL('/home/vineeshvs/Dropbox/wel/workspace/Atmel/libhello.so') #edited
#mydll = ctypes.CDLL('libhello.so') #edited

class Example(QtGui.QMainWindow):
    
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self): 
        loadVerilogFileAction=QtGui.QAction(QtGui.QIcon('images/upload.png'), '&Load Verilog file', self)
        loadVerilogFileAction.setShortcut('Ctrl+L')
        loadVerilogFileAction.setStatusTip('Load Verilog file')
        loadVerilogFileAction.triggered.connect(self.showDialog)
        viewSlicedFileAction=QtGui.QAction(QtGui.QIcon('images/view.png'), '&View sliced file', self)
        #viewSlicedFileAction.setShortcut('Ctrl+L')
        viewSlicedFileAction.setStatusTip('View sliced file')
        viewSlicedFileAction.triggered.connect(self.showDialog)
        viewLogAction=QtGui.QAction(QtGui.QIcon('images/chat.png'), '&View log', self)
        viewLogAction.setStatusTip('View log')
        viewLogAction.triggered.connect(self.showDialog)
        sliceAction=QtGui.QAction(QtGui.QIcon('images/play.png'), '&Slice the Verilog code', self)
        sliceAction.setShortcut('Ctrl+P')
        sliceAction.setStatusTip('Slice the Verilog code')
        sliceAction.triggered.connect(self.UnderConstructionDialog)
        aboutProgrammerAction = QtGui.QAction(QtGui.QIcon('images/info.png'), '&About  Programmer', self)
        aboutProgrammerAction.setStatusTip('About') 
        aboutProgrammerAction.triggered.connect(self.OutputDialog)
        exitAction = QtGui.QAction(QtGui.QIcon('images/exit.png'), '&Exit', self)        
        exitAction.setShortcut('Ctrl+X')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(QtGui.qApp.quit)

        self.statusBar()
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(loadVerilogFileAction)  
        fileMenu.addAction(exitAction)
        viewMenu = menubar.addMenu('&View')
        viewMenu.addAction(viewSlicedFileAction)  
        viewMenu.addAction(viewLogAction)  
        viewMenu.addAction(exitAction)
        helpMenu = menubar.addMenu('&Help')
        helpMenu.addAction(aboutProgrammerAction)
 
        """Add toolbar buttons"""
        self.toolbar = self.addToolBar('Load Verilog file')
        self.toolbar.addAction(loadVerilogFileAction)
        self.toolbar = self.addToolBar('View sliced file')
        self.toolbar.addAction(viewSlicedFileAction)
        self.toolbar = self.addToolBar('View log')
        self.toolbar.addAction(viewLogAction)
        self.toolbar = self.addToolBar('Help')
        self.toolbar.addAction(aboutProgrammerAction)
        """Checkboxes"""
        self.programCb = QtGui.QCheckBox('Program', self)
        self.programCb.move(20, 60)
        """Buttons"""
	runb = QtGui.QPushButton('Run', self)
        runb.setCheckable(True)
        runb.move(20, 130)
        runb.clicked[bool].connect(self.run)     

        self.setGeometry(300, 200, 500, 500)
        self.setWindowTitle('Verilog slicer')       
        self.show()
        
    def showDialog(self):
	global fname_arg
        #fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file','run/media/vineeth/FUN/trunk/research/work/slicing')
        #slicing_main("/run/media/vineeth/FUN/trunk/research/work/slicing/full_adder.v","u2_half_adder")
        #slicing_main(fname, "u2_half_adder")
        print(fname)
        fname_arg = c_char_p(str(fname))
	print(fname_arg)
        
    def UnderConstructionDialog(self):
	msgbox = QtGui.QMessageBox()
	msgbox.about(self,'Under construction','Sorry, this section of slicer is under construction :(')
        
    def OutputDialog(self):
	msgbox = QtGui.QMessageBox()
	msgbox.about(self,'About','Verilog slicer version1')
	
    def program(self, state):
        if state == QtCore.Qt.Checked:
            self.setWindowTitle('Program')
        else:
            self.setWindowTitle('')
            
    def run(self, pressed):
     	#fname_test = "/home"
	#print(fname_test)
	global fname_arg
        if pressed:
            #if self.programCb.checkState() == 2 & self.eraseCb.checkState() == 1 & self.verifyCb.checkState() == 1: 
	    if self.programCb.checkState() == 2:
            	mydll.program(fname_arg) 
		print("\n\nProgramming Done\n")   
	             
def flags(self, index):
    if not index.isValid():
        return Qt.ItemIsEnabled
    
    if index.column() in self.booleanSet:
        return Qt.ItemIsUserCheckable | Qt.ItemIsSelectable | Qt.ItemIsEnabled
    elif index.column() in self.readOnlySet:
        return Qt.ItemIsSelectable | Qt.ItemIsEnabled
    else:
        return QSortFilterProxyModel.flags(self, index)

def main():
    global fname_arg
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main() 
