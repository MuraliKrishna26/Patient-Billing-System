from tkinter import *
from into_patient_connect import patient_diagnosis_filling

class patient_diagnosis_class(Toplevel):
	def __init__(self):
		Toplevel.__init__(self)

		self.geometry("650x550+350+200")
		self.title("Complete Patient Details")
		self.resizable(False, False)

		self.top = Frame(self, height=100,bg='white')
		self.top.pack(fill=X)

		self.buttom = Frame(self, height=550,bg='#367572')
		self.buttom.pack(fill=X)

		self.top_image = PhotoImage(file='icon.png')
		self.top_image_label = Label(self.top,image=self.top_image, bg='white')
		self.top_image_label.place(x=120, y=19)

		self.heading = Label(self.top, text=" Complete Patient Details ",font='arial 15 bold',bg='white',fg='#8a4b27')
		self.heading.place(x=230, y=30)


		self.admit = Button(self.buttom, text="   Fill to Admit   ", font='arial 10 bold',command=self.my_into_patient_connect)	
		self.admit.place(x=100, y=110)


	def my_into_patient_connect(self):
		detail_to_patient_connect = patient_diagnosis_filling()




