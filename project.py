from tkinter import *
import datetime
from doctor_details import doctordetails
from generatebill_details import generatebill
from bedavailability_details import bedavailability
from treatment_details import treatmentdetails
from register_patient_details import patientdetails
from patient_details import patient_details_toshow
from Admit_Charges import admitchargedetails
from project_diagnosis import patient_diagnosis_class


date = datetime.datetime.now().date()
date = str(date)

class Application(object):
	def __init__(self,master):
		self.master=master

		self.top = Frame(master, height=100,bg='white')
		self.top.pack(fill=X)

		self.buttom = Frame(master, height=550,bg='#367572')
		self.buttom.pack(fill=X)

		self.top_image = PhotoImage(file='icon.png')
		self.top_image_label = Label(self.top,image=self.top_image, bg='white')
		self.top_image_label.place(x=120, y=19)

		self.heading = Label(self.top, text="Patient Billing System",font='arial 15 bold',bg='white',fg='#8a4b27')
		self.heading.place(x=230, y=30)


		self.date_lbl = Label(self.top,text="Date:"+date, font='arial 8 bold',bg='white',fg='#9e821b')
		self.date_lbl.place(x=500,y=80)

		self.generatebill = Button(self.buttom, text="   Generate Bill    ", font='arial 10 bold',command=self.my_generate_bill_details)	
		self.generatebill.place(x=100, y=50)


		self.bedavailble = Button(self.buttom, text="Show Bed Availbility", font='arial 10 bold',command=self.my_availability_bed_details) 		
		self.bedavailble.place(x=100, y=110)

		self.registerpatient = Button(self.buttom, text="  Register Patient  ", font='arial 10 bold',command=self.my_register_patient_details)	
		self.registerpatient.place(x=100, y=170)

		self.treatment = Button(self.buttom, text="   Treatment Details   ", font='arial 10 bold',command=self.my_treatment_details)	
		self.treatment.place(x=100, y=230)

		self.doctorconsult = Button(self.buttom, text="   Doctor Details   ", font='arial 10 bold',command=self.my_doctor_details)	
		self.doctorconsult.place(x=100, y=300)

		self.patient_details = Button(self.buttom, text=" Patient Details ", font='arial 10 bold',command=self.my_patients_details)	
		self.patient_details.place(x=100, y=370)

		self.admit_charges = Button(self.buttom, text=" Admit Charges ", font='arial 10 bold',command=self.my_admit_charges)	
		self.admit_charges.place(x=400, y=110)


		self.Patient_Diagnosis = Button(self.buttom, text=" Patient Diagnosis ", font='arial 10 bold',command=self.my_patient_diagnosis_class)	
		self.Patient_Diagnosis.place(x=400, y=170)
		

	def my_doctor_details(self):
		detail_doctor=doctordetails()

	def my_generate_bill_details(self):
		detail_generate_bill=generatebill()	

	def my_availability_bed_details(self):
		deatil_bed_availability=bedavailability()

	def my_treatment_details(self):
		details_treatment_detail = treatmentdetails()	

	def my_register_patient_details(self):
		details_patient = patientdetails()	

	def my_patients_details(self):
		details_patiet_toshow = patient_details_toshow()

	def my_admit_charges(self):
		details_admit = admitchargedetails()

	def my_patient_diagnosis_class(self):
		details_patient_diagnosis = patient_diagnosis_class()
			
		 

			

def main():
	root = Tk()
	app = Application(root)
	root.title("Hospital Billing System")
	root.geometry("650x550+350+200")
	root.resizable(False, False)
	root.mainloop()

if __name__ == '__main__':
	main()  

