from tkinter import *

class generatebill(Toplevel):
	def __init__(self):
		Toplevel.__init__(self)

		self.geometry("650x550+350+200")
		self.title("Bill Generation")
		self.resizable(False, False)