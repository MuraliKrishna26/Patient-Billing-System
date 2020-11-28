from tkinter import *
import mysql.connector 

mydb = mysql.connector.connect(host="localhost", user="root", passwd="sunny",auth_plugin="mysql_native_password",database="project")

mycursor = mydb.cursor()



class doctordetails(Toplevel):
	def __init__(self):
		Toplevel.__init__(self)

		self.geometry("650x550+350+200")
		self.title("Doctor Details")
		self.resizable(False, False)

		self.top = Frame(self, height=100,bg='white')
		self.top.pack(fill=X)

		self.buttom = Frame(self, height=550,bg='#cca947')
		self.buttom.pack(fill=X)

		self.top_image = PhotoImage(file='icon.png')
		self.top_image_label = Label(self.top,image=self.top_image, bg='white')
		self.top_image_label.place(x=120, y=19)

		self.heading = Label(self.top, text="Doctor Details",font='arial 15 bold',bg='white',fg='#8a4b27')
		self.heading.place(x=230, y=30)

		self.scroll = Scrollbar(self.buttom, orient=VERTICAL)


		self.listBox = Listbox(self.buttom, width=90, height=32)
		self.listBox.grid(row=0, column=0, padx=(40,10))
		self.scroll.config(command=self.listBox.yview)	
		self.listBox.config(yscrollcommand=self.scroll.set)

		mycursor.execute("select * from doctor")
		
		x = mycursor.fetchall()

		count=0;
		for x_in in x:
			self.listBox.insert(count,"  Doctor Code: "+str(x_in[0])+"|||  Name: "+x_in[1]+"|||   Spl:   "+x_in[2]+"|||  Doctor Fee :"+str(x_in[3]))
			


		self.scroll.grid(row=0, column=1, sticky=N+S)






