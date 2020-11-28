from tkinter import *
from tkinter import messagebox
import mysql.connector 

mydb = mysql.connector.connect(host="localhost", user="root", passwd="sunny",auth_plugin="mysql_native_password",database="project")

mycursor = mydb.cursor()


class patientdetails(Toplevel):
	def __init__(self):
		Toplevel.__init__(self)

		self.geometry("650x550+350+200")
		self.title("Register Patient")
		self.resizable(False, False)

		self.top = Frame(self, height=100,bg='white')
		self.top.pack(fill=X)

		self.buttom = Frame(self, height=550,bg='#cca947')
		self.buttom.pack(fill=X)

		self.top_image = PhotoImage(file='icon.png')
		self.top_image_label = Label(self.top,image=self.top_image, bg='white')
		self.top_image_label.place(x=120, y=19)

		self.heading = Label(self.top, text="Register Patient Details",font='arial 15 bold',bg='white',fg='#8a4b27')
		self.heading.place(x=230, y=30)

		#id,name,contact_number,age,gardian,address,martial_status

		self.label_id = Label(self.buttom, text="ID", font='arial 10 bold', fg='white', bg='#fcc324')
		self.label_id.place(x=49,y=40)

		self.entry_id = Entry(self.buttom,width=30,bd=4)
		self.entry_id.insert(0,"Id should be unique")
		self.entry_id.place(x=150, y=40)

		#name

		self.label_name = Label(self.buttom, text="Name", font='arial 10 bold', fg='white', bg='#fcc324')
		self.label_name.place(x=49,y=90)

		self.entry_name = Entry(self.buttom,width=30,bd=4)
		self.entry_name.insert(1,"")
		self.entry_name.place(x=150, y=90)


		#contact number

		self.label_contact = Label(self.buttom, text="Phone Number", font='arial 10 bold', fg='white', bg='#fcc324')
		self.label_contact.place(x=49,y=140)

		self.entry_contact = Entry(self.buttom,width=30,bd=4)
		self.entry_contact.insert(2,"")
		self.entry_contact.place(x=150, y=140)

		#age

		self.label_age = Label(self.buttom, text="Age", font='arial 10 bold', fg='white', bg='#fcc324')
		self.label_age.place(x=49,y=190)

		self.entry_age = Entry(self.buttom,width=30,bd=4)
		self.entry_age.insert(3,"")
		self.entry_age.place(x=150, y=190)

		#gardian 

		self.label_gard = Label(self.buttom, text="Guardian", font='arial 10 bold', fg='white', bg='#fcc324')
		self.label_gard.place(x=49,y=240)

		self.entry_gard = Entry(self.buttom,width=30,bd=4)
		self.entry_gard.insert(4,"")
		self.entry_gard.place(x=150, y=240)

		#address

		self.label_address = Label(self.buttom, text="Address", font='arial 10 bold', fg='white', bg='#fcc324')
		self.label_address.place(x=49,y=290)

		self.entry_address = Entry(self.buttom,width=30,bd=4)
		self.entry_address.insert(5,"")
		self.entry_address.place(x=150, y=290)		

		#martial status

		self.label_marriage = Label(self.buttom, text="Martial Status", font='arial 10 bold', fg='white', bg='#fcc324')
		self.label_marriage.place(x=49,y=340)

		self.entry_marriage = Entry(self.buttom,width=30,bd=4)
		self.entry_marriage.insert(6,"Married/Unmarrried")
		self.entry_marriage.place(x=150, y=340)	

		#button

		self.submitbutton = Button(self.buttom, text="Submit", font='arial 10 bold', command=self.abc)	
		self.submitbutton.place(x=150, y=380)


		#contact_number,age,gardian,address,martial_status

	def abc(self):
		idd = int(self.entry_id.get())
		name = self.entry_name.get()
		contact_number = int(self.entry_contact.get())
		age = self.entry_age.get()
		gardian = self.entry_gard.get()
		address = self.entry_address.get()
		martial_status = self.entry_marriage.get()

		if idd and name and contact_number !="":
			try:
				mycursor.execute('insert into patient_details  values ("%d","%s","%d","%d","%s","%s","%s")' % (idd,name,contact_number,int(age),gardian,address, martial_status))

				mydb.commit()	
				messagebox.showinfo("sucess","Added !!")	
			except Exception as e:
				messagebox.showinfo("Error",str(e))
		else:
			messagebox.showerror("Error","Fill all the feilds",icon='warning')
				

			











	


