#!/usr/bin/python3


import sys
from module_test import *

from random import seed
from random import random

# 
# --------- Initial values go here ---------------- #
seed()
rnum = random() + 1.0
srnum = str(rnum)

# 
# ----------- Program starts here ------------------ #
# This Class can have any name
# Ui_MainWindow is the Classfound in module_test.py

class Test(Ui_MainWindow): 
	def __init__(self, window):
		self.setupUi(window)
# 
# ============= Signals go here ===================== #
		
		
		# Connect signals to methode
		self.pushButton.clicked.connect(self.hello)
		
		self.newRanButton.clicked.connect(self.newRand)
		
		self.exitButton.clicked.connect(self.exit)
		#
# 
# ============== Methods go here ============= #

	

	def hello(self):
		self.textEdit.setText("Hello Cruel World\n" + srnum)
	
	def exit(self):
		 sys.exit(app.exec_())
			
	def newRand(self):
		global srnum
		seed()
		rnum = random() + 1.0
		srnum = str(rnum)

# ============================================ #
		
app = QtWidgets.QApplication(sys.argv)  # Not used in this Script
MainWindow = QtWidgets.QMainWindow()

# Creat instance of the GUI
ui = Test(MainWindow)   # Same as Class
 
# Show the window
MainWindow.show()
app.exec_()
