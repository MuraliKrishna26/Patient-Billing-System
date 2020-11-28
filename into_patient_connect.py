from tkinter import *
import mysql.connector 

mydb = mysql.connector.connect(host="localhost", user="root", passwd="sunny",auth_plugin="mysql_native_password",database="project")

mycursor = mydb.cursor()




class patient_diagnosis_filling(Toplevel):
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

		self.heading = Label(self.top, text=" Fill Details ",font='arial 15 bold',bg='white',fg='#8a4b27')
		self.heading.place(x=230, y=30)


		#Diagnosis_Number

		self.label_diagnosis = Label(self.buttom, text="Diagnosis Number", font='arial 10 bold', fg='white', bg='#fcc324')
		self.label_diagnosis.place(x=49,y=40)

		self.entry_diagnosis = Entry(self.buttom,width=30,bd=4)
		self.entry_diagnosis.insert(0,"Id should be unique")
		self.entry_diagnosis.place(x=200, y=40)

		#Patient_Id

		self.label_id_patient = Label(self.buttom, text="Patient Id", font='arial 10 bold', fg='white', bg='#fcc324')
		self.label_id_patient.place(x=49,y=90)

		self.entry_id_patient = Entry(self.buttom,width=30,bd=4)
		self.entry_id_patient.insert(0," ")
		self.entry_id_patient.place(x=200, y=90)

		#Doctor_Code

		self.label_code_doctor = Label(self.buttom, text="Doctor Code", font='arial 10 bold', fg='white', bg='#fcc324')
		self.label_code_doctor.place(x=49,y=140)

		self.entry_code_doctor = Entry(self.buttom,width=30,bd=4)
		self.entry_code_doctor.insert(0," ")
		self.entry_code_doctor.place(x=200, y=140)

		#Bed_Number

		self.label_bed_number = Label(self.buttom, text="Bed Number", font='arial 10 bold', fg='white', bg='#fcc324')
		self.label_bed_number.place(x=49,y=190)

		self.entry_bed_number = Entry(self.buttom,width=30,bd=4)
		self.entry_bed_number.insert(0," ")
		self.entry_bed_number.place(x=200, y=190)


		#button

		self.submitbutton = Button(self.buttom, text="Submit", font='arial 10 bold',command=self.addtodatabase)	
		self.submitbutton.place(x=200, y=250)

	def addtodatabase(self):
		get_diagnosis_number = self.entry_diagnosis.get()
		get_patient_id = self.entry_id_patient.get()
		get_doctor_code = self.entry_code_doctor.get()
		get_bed_number = self.entry_bed_number.get()

		if get_diagnosis_number !="" and get_patient_id !="" and get_doctor_code !="" and get_bed_number !="":
			
			try:

				mycursor.execute('insert into patient_diagnosis values ("%d","%d","%d","%s")' % (int(get_diagnosis_number),int(get_patient_id),int(get_doctor_code),get_bed_number))

				mycursor.execute('update ward_log set availability=("%d") where bed_number=("%s") ' % (1,get_bed_number))

				mydb.commit()
				messagebox.showinfo("sucess","Added !!")




			except Exception as e:
				messagebox.showinfo("Error",str(e))	

		else:
			messagebox.showerror("Error","Fill all the feilds",icon='warning')






