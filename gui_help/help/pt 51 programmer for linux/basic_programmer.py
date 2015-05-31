#!/usr/bin/python
# -*- coding: utf-8 -*-
#  Author: Narendra

import sys, ctypes #added ctypes
from PyQt4 import QtGui
from ctypes import cdll
from ctypes import *
#mydll = cdll.LoadLibrary('/home/vineeshvs/Dropbox/wel/workspace/Atmel/libhello.so')
#mydll = ctypes.CDLL('/home/vineeshvs/Dropbox/wel/workspace/Atmel/libhello.so') #edited
#mydll = ctypes.CDLL('libhello.so') #edited
class Example(QtGui.QMainWindow):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()

    def initUI(self): 
	
        loadhexfileAction=QtGui.QAction(QtGui.QIcon('load.jpg'), '&Load hex file', self)
        loadhexfileAction.setShortcut('Ctrl+L')
        loadhexfileAction.setStatusTip('Load hex file')
        loadhexfileAction.triggered.connect(self.showDialog)
        exitAction = QtGui.QAction(QtGui.QIcon('exit.jpg'), '&Exit', self)        
        exitAction.setShortcut('Ctrl+X')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(QtGui.qApp.quit)
        programAction=QtGui.QAction(QtGui.QIcon('program.jpeg'), '&Program Target Device Memory', self)
        programAction.setShortcut('Ctrl+P')
        programAction.setStatusTip('Program Target Device Memory')
        programAction.triggered.connect(self.UnderConstructionDialog)
        AboutProgrammerAction = QtGui.QAction(QtGui.QIcon('AboutProgrammer.jpg'), '&About  Programmer', self)
        AboutProgrammerAction.setStatusTip('About') 
        AboutProgrammerAction.triggered.connect(self.OutputDialog)

        self.statusBar()
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(loadhexfileAction)  
        fileMenu.addAction(exitAction)
        helpMenu = menubar.addMenu('&Help')
        helpMenu.addAction(AboutProgrammerAction)
 
        self.toolbar = self.addToolBar('Load hex file')
        self.toolbar.addAction(loadhexfileAction)
       
        self.toolbar = self.addToolBar('Help')
        self.toolbar.addAction(AboutProgrammerAction)

        self.programCb = QtGui.QCheckBox('Program', self)
        self.programCb.move(20, 60)
		
	runb = QtGui.QPushButton('Run', self)
        runb.setCheckable(True)
        runb.move(20, 130)
        runb.clicked[bool].connect(self.run)
        
        self.setGeometry(300, 200, 500, 500)
        self.setWindowTitle('Pt51 Programmer')       
        self.show()
        
    def showDialog(self):
	global fname_arg
        fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file','/home/Downloads')
        print(fname)
        fname_arg = c_char_p(str(fname))
	print(fname_arg)
        
    def UnderConstructionDialog(self):
        
	msgbox = QtGui.QMessageBox()
	msgbox.about(self,'Under construction','Sorry, this section of programmer is under construction :(')
        
    def OutputDialog(self):
        
	msgbox = QtGui.QMessageBox()
	msgbox.about(self,'About','pt51 Programmer\nThis software is used to program the atmega At89c5131 family of ' 
	'microcontrollers\nDeveloper: Narendra (Wadhawani Electronics Laboratory)')
	
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
