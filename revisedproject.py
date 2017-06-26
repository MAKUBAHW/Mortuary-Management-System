from tkinter import *
from tkinter import messagebox
import time
import mysql.connector
import hashlib
root=Tk()

##############################################
####           MYSQL CODE                #####
##############################################
try:
    conn = mysql.connector.connect(user='Andrew', password='andy', database='test', host='127.0.0.1', port='3306')
    cursor = conn.cursor()
except:
    raise ValueError("Contact System Admin. Database Offline")

#############################################################################################################
# This function {passencrypt()} reads password entered by user then compares it to the password in the db   #
# The password entered is encrypted and compared to the encrypted password stored in the db                 #
# The function returns a hashed password                                                                    #
#############################################################################################################


# Using sha512()
def passencrypt():
    pent=PasswordLoginEntry.get()
    pent = pent.encode('utf8')
    pword = hashlib.sha512()
    pword.update(pent)
    password = pword.hexdigest()
    print(pword)
    return password

def authentication():
    uname = NameLoginEntry.get()
    pword = PasswordLoginEntry.get()
    andy = passencrypt()

    status = False
    try:
        cursor.execute("SELECT staffid FROM users where staffid ='%s'" % (NameLoginEntry.get()))
        staffid = cursor.fetchone()
        staffid = str(staffid[0])
        print(staffid)

        if staffid is not None:
            print("cursor null")

            if uname == staffid:
                status = True

        cursor.execute("SELECT password FROM users WHERE staffid = '%s'" % (NameLoginEntry.get()))
        password = cursor.fetchone()
        passWord = str(password[0])

        if status == True:
            print("Got password")
            if andy != passWord:
                status = False
                print("Wrong Password")
    except:
        status = False
        print("here")

    if status == True:
        messagebox.showinfo("LOGIN", "Login Successful.")
        try:
            cursor.execute("SELECT enum FROM users WHERE staffid = '%s'" % (NameLoginEntry.get()))
            en=cursor.fetchone()
            enm=str(en[0])
            if enm == "N":
                LoginFrame.pack_forget()
                MenuFrame.pack()
                RegistrationFrame.pack_forget()
                CoffinServicesFrame.pack_forget()
            elif enm == 'Y':
                LoginFrame.pack_forget()
                MenuFrame.pack_forget()
                RegistrationFrame.pack()
                CoffinServicesFrame.pack_forget()
        except:
            status = False

    elif status == False:
        messagebox.showinfo("LOGIN", "WRONG ID / PASSWORD")


#def menupage():
#	if((NameLoginEntry.get()=="Admin") and (PasswordLoginEntry.get()=="12345")):
#		LoginFrame.pack_forget()
#		MenuFrame.pack()
#		RegistrationFrame.pack_forget()
#		CoffinServicesFrame.pack_forget()
def menupage2():
	LoginFrame.pack_forget()
	MenuFrame.pack()
	RegistrationFrame.pack_forget()
	CoffinServicesFrame.pack_forget()


def registrationpage():
	LoginFrame.pack_forget()
	MenuFrame.pack_forget()
	RegistrationFrame.pack()
	CoffinServicesFrame.pack_forget()

def selecttype():
	LoginFrame.pack_forget()
	MenuFrame.pack_forget()
	RegistrationFrame.pack_forget()
	SelectFrame.pack()
	CoffinServicesFrame.pack_forget()
def coffinselect():
	LoginFrame.pack_forget()
	MenuFrame.pack_forget()
	RegistrationFrame.pack_forget()
	SelectFrame.pack_forget()
	CoffinServicesFrame.pack()
def flowerselect():
	LoginFrame.pack_forget()
	MenuFrame.pack_forget()
	RegistrationFrame.pack_forget()
	SelectFrame.pack_forget()
	CoffinServicesFrame.pack_forget()
	MauaFrame.pack()

def eulogy():
	LoginFrame.pack_forget()
	MenuFrame.pack_forget()
	RegistrationFrame.pack_forget()
	SelectFrame.pack_forget()
	CoffinServicesFrame.pack_forget()
	MauaFrame.pack_forget()
	FlowerFrame.pack()
def comppackage():
	LoginFrame.pack_forget()
	MenuFrame.pack_forget()
	RegistrationFrame.pack_forget()
	SelectFrame.pack_forget()
	CoffinServicesFrame.pack_forget()
	MauaFrame.pack_forget()
	FlowerFrame.pack_forget()
	CoffinFrame.pack()



LoginFrame=Frame(root,width=1366,height=768,bd=2,bg='Green',relief='ridge')
LoginFrame.pack()

LoginFrameLeft=Frame(LoginFrame,width=1010,height=768,bd=2,bg='Green',relief='ridge')
LoginFrameLeft.pack(side=LEFT)

LoginFrameRight=Frame(LoginFrame,width=358,height=768,bd=2,bg='Green',relief='ridge')
LoginFrameRight.pack(side=RIGHT)

Date1=StringVar()
Date1.set(time.strftime("%Y/%m/%d"))


DateEntryLogin=Entry(LoginFrameRight,width=10,bg='Green',textvariable=Date1,font=('times',20,'italic'),fg='white',relief='ridge',bd=2)
DateEntryLogin.place(x=100,y=20)

#DateLabel=Label(LoginFrameRight,textvariable=Date1,bd=4,font=('times',15,'italic'),relief='ridge')
#DateLabel.place(x=80,y=200)
#DateEntryLogin.(STATE=DISABLED)



TopLabelLogin=Label(LoginFrameLeft,text="Egerton University Funeral Home Management System",font=('times',16,'italic'),bg='green',fg='white',relief='ridge',bd=2)
TopLabelLogin.place(x=250,y=180)

imageloginleft=PhotoImage(file="logo.gif")

ToppictureLeftLogin=Label(LoginFrameLeft,image=imageloginleft,bd=4,relief='ridge')
ToppictureLeftLogin.place(x=0,y=0)

imageloginright=PhotoImage(file="Egerton.gif")

ToppictureRightLogin=Label(LoginFrameRight,image=imageloginright,bd=4,relief='ridge')
ToppictureRightLogin.place(x=80,y=100)


NameLabel=Label(LoginFrameLeft,text="Name / Staff Number",font=('times',18,'italic'),fg='white',bg='green')
NameLabel.place(x=100,y=350)

PasswordLabel=Label(LoginFrameLeft,text="Password",font=('times',18,'italic'),fg='white',bg='green')
PasswordLabel.place(x=100,y=450)

NameLoginEntry=Entry(LoginFrameLeft,width=40,font=('times',18,'italic'))
NameLoginEntry.place(x=380,y=350)

PasswordLoginEntry=Entry(LoginFrameLeft,width=40,font=('times',18,'italic'), show='*')
PasswordLoginEntry.place(x=380,y=450)

LoginButton=Button(LoginFrameLeft,width=10,height=2,text="Log In",bg='Green',command=authentication,fg='white',font=('times',14,'italic'),relief='ridge')
LoginButton.place(x=750,y=600)
#-----------------------------------------menu page-----------------------------------------------------------------
MenuFrame=Frame(root,width=1366,height=768,bg='Green',bd=2,relief='ridge')
#MenuFrame.pack()


MenuFrameLeft=Frame(MenuFrame,width=1010,height=768,bg='Green',relief='ridge',bd=2)
MenuFrameLeft.pack(side=LEFT)

MenuFrameRight=Frame(MenuFrame,width=356,height=768,bg='Green',relief='ridge',bd=2)
MenuFrameRight.pack(side=RIGHT)

MenuFrameBottomLeft=Frame(MenuFrameLeft,width=1010,height=768,bg='Green',relief='ridge',bd=2)
MenuFrameBottomLeft.pack(side=LEFT)



imagemenutop=PhotoImage(file="logo.gif")

ToppictureLeftLogin=Label(MenuFrameLeft,image=imagemenutop,bd=4,relief='ridge')
ToppictureLeftLogin.place(x=0,y=0)

imagemenuright=PhotoImage(file="Egerton.gif")

ToppictureRightMenu=Label(MenuFrameRight,image=imagemenuright,bd=4,relief='ridge')
ToppictureRightMenu.place(x=80,y=50)

RegisterBodyButton=Button(MenuFrameBottomLeft,text="Register Body",height=2,width=20,relief='ridge',bd=2,fg='green',command=registrationpage,bg='white',font=('times',14,'italic'))
RegisterBodyButton.place(x=50,y=250)

ViewRecordsButton=Button(MenuFrameBottomLeft,text="View Records",height=2,width=20,relief='ridge',bd=2,fg='green',bg='white',font=('times',14,'italic'))
ViewRecordsButton.place(x=50,y=450)

BillBodyButton=Button(MenuFrameBottomLeft,text="Bill Body",height=2,width=20,relief='ridge',bd=2,fg='green',bg='white',font=('times',14,'italic'))
BillBodyButton.place(x=50,y=650)

AdditionalChargesButton=Button(MenuFrameBottomLeft,text="Additional Charges",height=2,width=20,relief='ridge',bd=2,fg='green',bg='white',font=('times',14,'italic'))
AdditionalChargesButton.place(x=350,y=250)

PenaltiesButton=Button(MenuFrameBottomLeft,text="Penalties",relief='ridge',height=2,width=20,bd=2,fg='green',bg='white',font=('times',14,'italic'))
PenaltiesButton.place(x=350,y=450)

CoffinDescriptionButton=Button(MenuFrameBottomLeft,text="Coffin Description",relief='ridge',height=2,width=20,bd=2,fg='green',bg='white',font=('times',14,'italic'))
CoffinDescriptionButton.place(x=350,y=650)

FlowerTypesButton=Button(MenuFrameBottomLeft,text="Flower Types",height=2,width=20,relief='ridge',bd=2,fg='green',bg='white',font=('times',14,'italic'))
FlowerTypesButton.place(x=650,y=250)

PackageDescriptionButton=Button(MenuFrameBottomLeft,text="Package Types",relief='ridge',height=2,width=20,bd=2,fg='green',bg='white',font=('times',14,'italic'))
PackageDescriptionButton.place(x=650,y=450)

AboutButton=Button(MenuFrameBottomLeft,text="About",relief='ridge',height=2,width=20,bd=2,fg='green',bg='white',font=('times',14,'italic'))
AboutButton.place(x=650,y=650)

#-------------------------------------------body registration-------------------------------------------------------
RegistrationFrame=Frame(root,width=1366,height=768,bd=2,relief='ridge')
#RegistrationFrame.pack()

RegistrationFrameLeft=Frame(RegistrationFrame,width=1010,height=768,relief='ridge',bd=2,bg='green')
RegistrationFrameLeft.pack(side=LEFT)

RegistrationFrameRight=Frame(RegistrationFrame,width=356,height=768,relief='ridge',bd=2,bg='green')
RegistrationFrameRight.pack(side=RIGHT)

Registrationleft=PhotoImage(file="logo.gif")
Registrationleftlabel=Label(RegistrationFrameLeft,image=Registrationleft,bd=4,relief='ridge')
Registrationleftlabel.place(x=0,y=0)

Registrationright=PhotoImage(file="Egerton.gif")
Registrationrightlabel=Label(RegistrationFrameRight,image=Registrationright,bd=4,relief='ridge')
Registrationrightlabel.place(x=80,y=50)

RegistrationLabel=Label(RegistrationFrameLeft,text="Body Registration",font=('times',14,'italic'),bd=2,relief='ridge',bg='green',fg='white')
RegistrationLabel.place(x=450,y=180)

NameLabel=Label(RegistrationFrameLeft,text="Name",font=('times',14,'italic'),fg='white',bg='green')
NameLabel.place(x=10,y=250)
NameEntry=Entry(RegistrationFrameLeft,font=('times',14,'italic'),width=30)
NameEntry.place(x=150,y=250)

AgeLabel=Label(RegistrationFrameLeft,text="Age",font=('times',14,'italic'),fg='white',bg='green')
AgeLabel.place(x=10,y=350)
AgeEntry=Entry(RegistrationFrameLeft,font=('times',14,'italic'),width=30)
AgeEntry.place(x=150,y=350)

GenderLabel=Label(RegistrationFrameLeft,text="Gender",font=('times',14,'italic'),fg='white',bg='green')
GenderLabel.place(x=10,y=450)
GenderEntry=Entry(RegistrationFrameLeft,font=('times',14,'italic'),width=30)
GenderEntry.place(x=150,y=450)

IDLabel=Label(RegistrationFrameLeft,text="ID/PP Number",font=('times',14,'italic'),fg='white',bg='green')
IDLabel.place(x=10,y=550)
IDEntry=Entry(RegistrationFrameLeft,font=('times',14,'italic'),width=30)
IDEntry.place(x=150,y=550)

AddressLabel=Label(RegistrationFrameLeft,text="Physcial Address",font=('times',14,'italic'),fg='white',bg='green')
AddressLabel.place(x=10,y=650)
AddressEntry=Entry(RegistrationFrameLeft,font=('times',14,'italic'),width=30)
AddressEntry.place(x=150,y=650)

BroughtByLabel=Label(RegistrationFrameLeft,text="Brought By",font=('times',14,'italic'),fg='white',bg='green')
BroughtByLabel.place(x=500,y=250)
BroughtByEntry=Entry(RegistrationFrameLeft,font=('times',14,'italic'),width=30)
BroughtByEntry.place(x=650,y=250)

KinNameLabel=Label(RegistrationFrameLeft,text="Kin Name",font=('times',14,'italic'),fg='white',bg='green')
KinNameLabel.place(x=500,y=350)
KinNameEntry=Entry(RegistrationFrameLeft,font=('times',14,'italic'),width=30)
KinNameEntry.place(x=650,y=350)

KinNumberLabel=Label(RegistrationFrameLeft,text="Kin Number",font=('times',14,'italic'),fg='white',bg='green')
KinNumberLabel.place(x=500,y=450)
KinNumberEntry=Entry(RegistrationFrameLeft,font=('times',14,'italic'),width=30)
KinNumberEntry.place(x=650,y=450)

DateLabel=Label(RegistrationFrameLeft,text="Date",font=('times',14,'italic'),fg='white',bg='green')
DateLabel.place(x=500,y=550)
DateEntry=Entry(RegistrationFrameLeft,font=('times',14,'italic'),width=30)
DateEntry.place(x=650,y=550)

OptionsRegistrationButton=Button(RegistrationFrameRight,text="Back To Options",bd=2,font=('times',14,'italic'),relief='ridge',bg='green',fg='white',height=2,width=15)
OptionsRegistrationButton.place(x=100,y=500)

NextRegistrationButton=Button(RegistrationFrameRight,text="Next",bd=2,font=('times',14,'italic'),relief='ridge',command=selecttype,bg='green',fg='white',height=2,width=15)
NextRegistrationButton.place(x=100,y=650)

#--------------------------------select package type frame-------------------------

SelectFrame=Frame(root,width=1366,height=768,bd=2,relief='ridge',bg='green')
#SelectFrame.pack()

SelectFrameLeft=Frame(SelectFrame,width=1010,height=768,relief='ridge',bg='green',bd=2)
SelectFrameLeft.pack(side=LEFT)

SelectFrameRight=Frame(SelectFrame,width=356,height=768,relief='ridge',bg='green',bd=2)
SelectFrameRight.pack(side=RIGHT)

imageslectleft=PhotoImage(file="logo.gif")

ToppictureLeftselect=Label(SelectFrameLeft,image=imageslectleft,bd=4,relief='ridge')
ToppictureLeftselect.place(x=0,y=0)

imageselectright=PhotoImage(file="Egerton.gif")

ToppictureRightselect=Label(SelectFrameRight,image=imageselectright,bd=4,relief='ridge')
ToppictureRightselect.place(x=80,y=100)

SelectPackageLabel=Label(SelectFrameLeft,text="Choose either a Comprehesive Package or cutomize your own package",font=('times',14,'italic'),bg='Green',fg='white')
SelectPackageLabel.place(x=50,y=250)

ButtonPackages=Button(SelectFrameLeft,width=50,height=5,text="Select Comprehensive Package",font=('times',14,'italic'),command=comppackage,bg='Green',relief='ridge',fg="white",bd=2)
ButtonPackages.place(x=280,y=300)

ButtonCustomize=Button(SelectFrameLeft,width=50,height=5,text="Customize Package",font=('times',14,'italic'),command=coffinselect,bg='Green',relief='ridge',fg="white",bd=2)
ButtonCustomize.place(x=280,y=500)

#-----------------------------------------coffin select------------------------------------------

#---------------------value of checkbox---------------------------
BodyAdmit=IntVar()
DailyCare10=IntVar()
Grooming=IntVar()
PMSuit=IntVar()
PMCare=IntVar()
SampleCare=IntVar()
DailyPMCare=IntVar()
Exhumation=IntVar()
Transfer=IntVar()
TransferDays=IntVar()
TransferPreservation=IntVar()
Transit=IntVar()
BodyAPMAdmission=IntVar()
BodyAPMCustody=IntVar()
BodyAPMGrooming=IntVar()
#----------------------------------------amount to be displayed in entry box--------------------------
BodyWashingAmount=IntVar()
BodyWashingAmount.set(0)


DailyCare10Amount=IntVar()
DailyCare10Amount.set(0)

GroomingAmount=IntVar()
GroomingAmount.set(0)

PMSuitAmount=IntVar()
PMSuitAmount.set(0)

PMCareAmount=IntVar()
PMCareAmount.set(0)

SampleCareAmount=IntVar()
SampleCareAmount.set(0)

DailyPMCareAmount=IntVar()
DailyPMCareAmount.set(0)

ExhumationAmount=IntVar()
ExhumationAmount.set(0)

TransferAmount=IntVar()
TransferAmount.set(0)

TransferDaysAmount=IntVar()
TransferDays.set(0)

TransferPreservationAmount=IntVar()
TransferPreservationAmount.set(0)

TransitAmount=IntVar()
TransitAmount.set(0)

BodyAPMAdmissionAmount=IntVar()
BodyAPMAdmissionAmount.set(0)

BodyAPMCustodyAmount=IntVar()
BodyAPMCustodyAmount.set(0)

BodyAPMGroomingAmount=IntVar()
BodyAPMGroomingAmount.set(0)
#------------------------------------------------------------------------------
CoffinServicesFrame=Frame(root,width=1366,height=768,bg='Green',bd=2,relief='ridge')
#CoffinServicesFrame.pack()
ServicesFrameLeft=Frame(CoffinServicesFrame,width=683,height=768,bg='green',bd=2,relief='ridge')
ServicesFrameLeft.pack(side=LEFT)

ServiceLabel=Label(ServicesFrameLeft,text='Services',font=('times',20,'italic'),bg='green',fg='white')
ServiceLabel.place(x=10,y=10)

MainCheckLabel=Label(ServicesFrameLeft,text='Remains of 10 years and Above',font=('times',16,'italic'),bg='green',fg='white')
MainCheckLabel.place(x=10,y=50)

BodyWashingLabel=Label(ServicesFrameLeft,text='Body admission and Preservation process',font=('times',12,'italic'),bg='green',fg='white')
BodyWashingLabel.place(x=100,y=80)
BodyWashingEntry=Entry(ServicesFrameLeft,textvariable=BodyWashingAmount)
BodyWashingEntry.place(x=500,y=80)
#BodyAdmit.set(0)
BodyWashingEntry.configure(state='readonly')


CustodyLabel=Label(ServicesFrameLeft,text='Daily Custodial Care and Storage',font=('times',12,'italic'),bg='green',fg='white')
CustodyLabel.place(x=100,y=110)
CustodyEntry=Entry(ServicesFrameLeft,textvariable=DailyCare10Amount)
CustodyEntry.place(x=500,y=110)
CustodyEntry.configure(state='readonly')


FinalGroomingLabel=Label(ServicesFrameLeft,text='Final Grooming and Dispatch',font=('times',12,'italic'),bg='green',fg='white')
FinalGroomingLabel.place(x=100,y=140)
FinalGroomingEntry=Entry(ServicesFrameLeft,textvariable=GroomingAmount)
FinalGroomingEntry.place(x=500,y=140)
FinalGroomingEntry.configure(state='readonly')

AncillaryLabel=Label(ServicesFrameLeft,text='Ancillary Services',font=('times',16,'italic'),bg='green',fg='white')
AncillaryLabel.place(x=0,y=170)

PostMortemLabel=Label(ServicesFrameLeft,text='Post Mortem Cases',font=('times',16,'italic'),bg='green',fg='white')
PostMortemLabel.place(x=0,y=200)

PostMortemSuitLabel=Label(ServicesFrameLeft,text='Post Mortem Suit',font=('times',12,'italic'),bg='green',fg='white')
PostMortemSuitLabel.place(x=100,y=230)
PostMortemSuitEntry=Entry(ServicesFrameLeft,textvariable=PMSuitAmount)
PostMortemSuitEntry.place(x=500,y=230)
PostMortemSuitEntry.configure(state='readonly')


PostMortemAutopsyLabel=Label(ServicesFrameLeft,text='Post Autopsy Care',font=('times',12,'italic'),bg='green',fg='white')
PostMortemAutopsyLabel.place(x=100,y=260)
PostMortemAutopsyEntry=Entry(ServicesFrameLeft,textvariable=PMCareAmount)
PostMortemAutopsyEntry.place(x=500,y=260)
PostMortemAutopsyEntry.configure(state='readonly')


PostMortemSamplesLabel=Label(ServicesFrameLeft,text='Samples Recovery and Preservation',font=('times',12,'italic'),bg='green',fg='white')
PostMortemSamplesLabel.place(x=100,y=290)
PostMortemSamplesEntry=Entry(ServicesFrameLeft,textvariable=SampleCareAmount)
PostMortemSamplesEntry.place(x=500,y=290)
PostMortemSamplesEntry.configure(state='readonly')


PostMortemDailyLabel=Label(ServicesFrameLeft,text='Daily Care Before Pm',font=('times',12,'italic'),bg='green',fg='white')
PostMortemDailyLabel.place(x=100,y=320)
PostMortemDailyEntry=Entry(ServicesFrameLeft,textvariable=DailyPMCareAmount)
PostMortemDailyEntry.place(x=500,y=320)
PostMortemDailyEntry.configure(state='readonly')


ExhumationLabel=Label(ServicesFrameLeft,text='Exhumation',font=('times',12,'italic'),bg='green',fg='white')
ExhumationLabel.place(x=100,y=350)
ExhumationEntry=Entry(ServicesFrameLeft,textvariable=ExhumationAmount)
ExhumationEntry.place(x=500,y=350)
ExhumationEntry.configure(state='readonly')


TransferLabel=Label(ServicesFrameLeft,text='Transfer From Other Facilities',font=('times',16,'italic'),bg='green',fg='white')
TransferLabel.place(x=0,y=380)

CustodialTransferLabel=Label(ServicesFrameLeft,text='Custodial Care only less 4 days stay',font=('times',12,'italic'),bg='green',fg='white')
CustodialTransferLabel.place(x=100,y=410)
CustodialTransferEntry=Entry(ServicesFrameLeft,textvariable=TransferAmount)
CustodialTransferEntry.place(x=500,y=410)
CustodialTransferEntry.configure(state='readonly')


ExtraDaysLabel=Label(ServicesFrameLeft,text='Extra Days',font=('times',12,'italic'),bg='green',fg='white')
ExtraDaysLabel.place(x=100,y=440)
ExtraDaysEntry=Entry(ServicesFrameLeft,textvariable=TransferDaysAmount)
ExtraDaysEntry.place(x=500,y=440)
ExtraDaysEntry.configure(state='readonly')


ExtraDaysPreservationLabel=Label(ServicesFrameLeft,text='For Preservation and after care less 4 days stay',font=('times',12,'italic'),bg='green',fg='white')
ExtraDaysPreservationLabel.place(x=100,y=470)
ExtraDaysPreservationEntry=Entry(ServicesFrameLeft,textvariable=TransferPreservationAmount)
ExtraDaysPreservationEntry.place(x=500,y=470)
ExtraDaysPreservationEntry.configure(state='readonly')


OvernightLabel=Label(ServicesFrameLeft,text='Body On Transit Overnight Stay',font=('times',12,'italic'),bg='green',fg='white')
OvernightLabel.place(x=100,y=500)
OvernightEntry=Entry(ServicesFrameLeft,textvariable=TransitAmount)
OvernightEntry.place(x=500,y=500)
OvernightEntry.configure(state='readonly')


SeveralPMLabel=Label(ServicesFrameLeft,text='Bodies with several Post Mortem Changes',font=('times',16,'italic'),bg='green',fg='white')
SeveralPMLabel.place(x=0,y=530)

AdmitPMLabel=Label(ServicesFrameLeft,text='Body Admission and Preservation Process',font=('times',12,'italic'),bg='green',fg='white')
AdmitPMLabel.place(x=100,y=560)
AdmitPMEntry=Entry(ServicesFrameLeft,textvariable=BodyAPMAdmissionAmount)
AdmitPMEntry.place(x=500,y=560)
AdmitPMEntry.configure(state='readonly')


CustodyPMLabel=Label(ServicesFrameLeft,text='Daily Custodial Care And Storage',font=('times',12,'italic'),bg='green',fg='white')
CustodyPMLabel.place(x=100,y=590)
CustodyPMEntry=Entry(ServicesFrameLeft,textvariable=BodyAPMCustodyAmount)
CustodyPMEntry.place(x=500,y=590)
CustodyPMEntry.configure(state='readonly')


GroomPMLabel=Label(ServicesFrameLeft,text='Final Grooming and Dispatch',font=('times',12,'italic'),bg='green',fg='white')
GroomPMLabel.place(x=100,y=620)
GroomPMEntry=Entry(ServicesFrameLeft,textvariable=BodyAPMGroomingAmount)
GroomPMEntry.place(x=500,y=620)
GroomPMEntry.configure(state='readonly')

BackButtonCoffin=Button(ServicesFrameLeft,text="Back",font=('times',14,'italic'),bg='green',width=15,fg='white',relief='ridge',bd=2)
BackButtonCoffin.place(x=100,y=700)


def cmdc():
	if (BodyAdmit.get() == 0):
		BodyWashingEntry.configure(state=DISABLED)
		BodyWashingAmount.set(0)
	elif BodyAdmit.get() == 1:
		BodyWashingEntry.configure(state='readonly')
		BodyWashingAmount.set(3000)

	if DailyCare10.get()==0:
		CustodyEntry.configure(state=DISABLED)
		DailyCare10Amount.set(0)
	elif DailyCare10.get()==1:
		CustodyEntry.configure(state='readonly')
		DailyCare10Amount.set(1000)

	if Grooming.get()==0:
		FinalGroomingEntry.configure(state=DISABLED)
		GroomingAmount.set(0)
	elif Grooming.get()==1:
		FinalGroomingEntry.configure(state='readonly')
		GroomingAmount.set(2000)

	if PMSuit.get()==0:
		PostMortemSuitEntry.configure(state=DISABLED)
		PMSuitAmount.set(0)
	elif PMSuit.get()==1:
		PostMortemSuitEntry.configure(state='readonly')
		PMSuitAmount.set(4000)

	if PMCare.get()==0:
		PostMortemAutopsyEntry.configure(state=DISABLED)
		PMCareAmount.set(0)
	elif PMCare.get()==1:
		PostMortemAutopsyEntry.configure(state='readonly')
		PMCareAmount.set(6000)

	if SampleCare.get()==0:
		PostMortemSamplesEntry.configure(state=DISABLED)
		SampleCareAmount.set(0)
	elif SampleCare.get()==1:
		PostMortemSamplesEntry.configure(state='readonly')
		SampleCareAmount.set(1000)

	if DailyPMCare.get()==0:
		PostMortemDailyEntry.configure(state=DISABLED)
		DailyPMCareAmount.set(0)
	elif DailyPMCare.get()==1:
		PostMortemDailyEntry.configure(state='readonly')
		DailyPMCareAmount.set(1500)

	if Exhumation.get()==0:
		ExhumationEntry.configure(state=DISABLED)
		ExhumationAmount.set(0)
	elif Exhumation.get()==1:
		ExhumationEntry.configure(state='readonly')
		ExhumationAmount.set(150000)

	if Transfer.get()==0:
		CustodialTransferEntry.configure(state=DISABLED)
		TransferAmount.set(0)
	elif Transfer.get()==1:
		CustodialTransferEntry.configure(state='readonly')
		TransferAmount.set(5000)
	if TransferDays.get()==0:
		ExtraDaysEntry.configure(state=DISABLED)
		TransferDaysAmount.set(0)
	elif TransferDays.get()==1:
		ExtraDaysEntry.configure(state='readonly')
		TransferDaysAmount.set(1000)

	if TransferPreservation.get()==0:
		ExtraDaysPreservationEntry.configure(state=DISABLED)
		TransferPreservationAmount.set(0)
	elif TransferPreservation.get()==1:
		ExtraDaysPreservationEntry.configure(state='readonly')
		TransferPreservationAmount.set(8000)

	if Transit.get()==0:
		OvernightEntry.configure(state=DISABLED)
		TransitAmount.set(0)
	elif Transit.get()==1:
		OvernightEntry.configure(state='readonly')
		TransitAmount.set(2000)

	if BodyAPMAdmission.get()==0:
		AdmitPMEntry.configure(state=DISABLED)
		BodyAPMAdmissionAmount.set(0)
	elif BodyAPMAdmission.get()==1:
		AdmitPMEntry.configure(state='readonly')
		BodyAPMAdmissionAmount.set(4000)

	if BodyAPMCustody.get()==0:
		CustodyPMEntry.configure(state=DISABLED)
		BodyAPMCustodyAmount.set(0)
	elif BodyAPMCustody.get()==1:
		CustodyPMEntry.configure(state='readonly')
		BodyAPMCustodyAmount.set(1000)

	if BodyAPMGrooming.get()==0:
		GroomPMEntry.configure(state=DISABLED)
		BodyAPMGroomingAmount.set(0)
	elif BodyAPMGrooming.get()==1:
		GroomPMEntry.configure(state='readonly')
		BodyAPMGroomingAmount.set(2500)
	
	
	
Chkbtn1=Checkbutton(ServicesFrameLeft,offvalue=0,onvalue=1,variable=BodyAdmit,command=cmdc,bg='green')
Chkbtn1.place(x=20,y=80)

Chkbtn2=Checkbutton(ServicesFrameLeft,offvalue=0,onvalue=1,variable=DailyCare10,command=cmdc,bg='green')
Chkbtn2.place(x=20,y=110)

Chkbtn3=Checkbutton(ServicesFrameLeft,offvalue=0,onvalue=1,variable=Grooming,command=cmdc,bg='green')
Chkbtn3.place(x=20,y=140)

Chkbtn4=Checkbutton(ServicesFrameLeft,offvalue=0,onvalue=1,variable=PMSuit,command=cmdc,bg='green')
Chkbtn4.place(x=20,y=230)

Chkbtn5=Checkbutton(ServicesFrameLeft,offvalue=0,onvalue=1,variable=PMCare,command=cmdc,bg='green')
Chkbtn5.place(x=20,y=260)

Chkbtn6=Checkbutton(ServicesFrameLeft,offvalue=0,onvalue=1,variable=SampleCare,command=cmdc,bg='green')
Chkbtn6.place(x=20,y=290)

Chkbtn7=Checkbutton(ServicesFrameLeft,offvalue=0,onvalue=1,variable=DailyPMCare,command=cmdc,bg='green')
Chkbtn7.place(x=20,y=320)

Chkbtn8=Checkbutton(ServicesFrameLeft,offvalue=0,onvalue=1,variable=Exhumation,command=cmdc,bg='green')
Chkbtn8.place(x=20,y=350)

Chkbtn9=Checkbutton(ServicesFrameLeft,offvalue=0,onvalue=1,variable=Transfer,command=cmdc,bg='green')
Chkbtn9.place(x=20,y=410)

Chkbtn10=Checkbutton(ServicesFrameLeft,offvalue=0,onvalue=1,variable=TransferDays,command=cmdc,bg='green')
Chkbtn10.place(x=20,y=440)

Chkbtn11=Checkbutton(ServicesFrameLeft,offvalue=0,onvalue=1,variable=TransferPreservation,command=cmdc,bg='green')
Chkbtn11.place(x=20,y=470)

Chkbtn12=Checkbutton(ServicesFrameLeft,offvalue=0,onvalue=1,variable=Transit,command=cmdc,bg='green')
Chkbtn12.place(x=20,y=500)

Chkbtn13=Checkbutton(ServicesFrameLeft,offvalue=0,onvalue=1,variable=BodyAPMAdmission,command=cmdc,bg='green')
Chkbtn13.place(x=20,y=560)

Chkbtn14=Checkbutton(ServicesFrameLeft,offvalue=0,onvalue=1,variable=BodyAPMCustody,command=cmdc,bg='green')
Chkbtn14.place(x=20,y=590)

Chkbtn15=Checkbutton(ServicesFrameLeft,offvalue=0,onvalue=1,variable=BodyAPMGrooming,command=cmdc,bg='green')
Chkbtn15.place(x=20,y=620)

#------------------------------------------------------------------------------------------------------------------------------------------------
class child():
	BodyAdmit=IntVar()

ServicesFrameRight=Frame(CoffinServicesFrame,width=683,height=768,bg='Green',bd=2,relief='ridge')
ServicesFrameRight.pack(side=RIGHT)

MainChildLabel=Label(ServicesFrameRight,text='Remains of Below 10 Years',font=('times',16,'italic'),bg='green',fg='white')
MainChildLabel.place(x=10,y=50)
#------------------------------------------------------------------ child variables ---------------------------------------------------------------------------
BodyAdmitChild=IntVar()
DailyCareChild=IntVar()
GroomingChild=IntVar()
PMSuitChild=IntVar()
PMCareChild=IntVar()
SampleCareChild=IntVar()
DailyPMCareChild=IntVar()
ExhumationChild=IntVar()
TransferChild=IntVar()
TransferDaysChild=IntVar()
TransferPreservationChild=IntVar()
TransitChild=IntVar()
BodyAPMAdmissionChild=IntVar()
BodyAPMCustodyChild=IntVar()
BodyAPMGroomingChild=IntVar()

#--------------------------------------

BodyWashingAmountChild=IntVar()
BodyWashingAmountChild.set(0)


DailyCareAmountChild=IntVar()
DailyCareAmountChild.set(0)

GroomingAmountChild=IntVar()
GroomingAmountChild.set(0)

PMSuitAmountChild=IntVar()
PMSuitAmountChild.set(0)

PMCareAmountChild=IntVar()
PMCareAmountChild.set(0)

SampleCareAmountChild=IntVar()
SampleCareAmountChild.set(0)

DailyPMCareAmountChild=IntVar()
DailyPMCareAmountChild.set(0)


ExhumationAmountChild=IntVar()
ExhumationAmountChild.set(0)

TransferAmountChild=IntVar()
TransferAmountChild.set(0)

TransferDaysAmountChild=IntVar()
TransferDaysAmountChild.set(0)

TransferPreservationAmountChild=IntVar()
TransferPreservationAmountChild.set(0)

TransitAmountChild=IntVar()
TransitAmountChild.set(0)

BodyAPMAdmissionAmountChild=IntVar()
BodyAPMAdmissionAmountChild.set(0)

BodyAPMCustodyAmountChild=IntVar()
BodyAPMCustodyAmountChild.set(0)

BodyAPMGroomingAmountChild=IntVar()
BodyAPMGroomingAmountChild.set(0)

BodyWashingChildLabel=Label(ServicesFrameRight,text='Body admission and Preservation process',font=('times',12,'italic'),bg='green',fg='white')
BodyWashingChildLabel.place(x=100,y=80)
BodyWashingChildEntry=Entry(ServicesFrameRight,textvariable=BodyWashingAmountChild)
BodyWashingChildEntry.place(x=500,y=80)
BodyWashingChildEntry.configure(state='readonly')

CustodyChildLabel=Label(ServicesFrameRight,text='Daily Custodial Care and Storage',font=('times',12,'italic'),bg='green',fg='white')
CustodyChildLabel.place(x=100,y=110)
CustodyChildEntry=Entry(ServicesFrameRight,textvariable=DailyCareAmountChild)
CustodyChildEntry.place(x=500,y=110)
CustodyChildEntry.configure(state='readonly')


FinalChildGroomingLabel=Label(ServicesFrameRight,text='Final Grooming and Dispatch',font=('times',12,'italic'),bg='green',fg='white')
FinalChildGroomingLabel.place(x=100,y=140)
FinalChildGroomingEntry=Entry(ServicesFrameRight,textvariable=GroomingAmountChild)
FinalChildGroomingEntry.place(x=500,y=140)
FinalChildGroomingEntry.configure(state='readonly')

AncillaryChildLabel=Label(ServicesFrameRight,text='Ancillary Services',font=('times',16,'italic'),bg='green',fg='white')
AncillaryChildLabel.place(x=0,y=170)

PostMortemChildLabel=Label(ServicesFrameRight,text='Post Mortem Cases',font=('times',16,'italic'),bg='green',fg='white')
PostMortemChildLabel.place(x=0,y=200)

PostMortemSuitChildLabel=Label(ServicesFrameRight,text='Post Mortem Suit',font=('times',12,'italic'),bg='green',fg='white')
PostMortemSuitChildLabel.place(x=100,y=230)
PostMortemSuitChildEntry=Entry(ServicesFrameRight,textvariable=PMSuitAmountChild)
PostMortemSuitChildEntry.place(x=500,y=230)
PostMortemSuitChildEntry.configure(state='readonly')


PostMortemAutopsyChildLabel=Label(ServicesFrameRight,text='Post Autopsy Care',font=('times',12,'italic'),bg='green',fg='white')
PostMortemAutopsyChildLabel.place(x=100,y=260)
PostMortemAutopsyChildEntry=Entry(ServicesFrameRight,textvariable=PMCareAmountChild)
PostMortemAutopsyChildEntry.place(x=500,y=260)
PostMortemAutopsyChildEntry.configure(state='readonly')


PostMortemSamplesChildLabel=Label(ServicesFrameRight,text='Samples Recovery and Preservation',font=('times',12,'italic'),bg='green',fg='white')
PostMortemSamplesChildLabel.place(x=100,y=290)
PostMortemSamplesChildEntry=Entry(ServicesFrameRight,textvariable=SampleCareAmountChild)
PostMortemSamplesChildEntry.place(x=500,y=290)
PostMortemSamplesChildEntry.configure(state='readonly')


PostMortemDailyChildLabel=Label(ServicesFrameRight,text='Daily Care Before Pm',font=('times',12,'italic'),bg='green',fg='white')
PostMortemDailyChildLabel.place(x=100,y=320)
PostMortemDailyChildEntry=Entry(ServicesFrameRight,textvariable=DailyPMCareAmountChild)
PostMortemDailyChildEntry.place(x=500,y=320)
PostMortemDailyChildEntry.configure(state='readonly')


ExhumationChildLabel=Label(ServicesFrameRight,text='Exhumation',font=('times',12,'italic'),bg='green',fg='white')
ExhumationChildLabel.place(x=100,y=350)
ExhumationChildEntry=Entry(ServicesFrameRight,textvariable=ExhumationAmountChild)
ExhumationChildEntry.place(x=500,y=350)
ExhumationChildEntry.configure(state='readonly')


TransferChildLabel=Label(ServicesFrameRight,text='Transfer From Other Facilities',font=('times',16,'italic'),bg='green',fg='white')
TransferChildLabel.place(x=0,y=380)

CustodialChildTransferLabel=Label(ServicesFrameRight,text='Custodial Care only less 4 days stay',font=('times',12,'italic'),bg='green',fg='white')
CustodialChildTransferLabel.place(x=100,y=410)
CustodialChildTransferEntry=Entry(ServicesFrameRight,textvariable=TransferAmountChild)
CustodialChildTransferEntry.place(x=500,y=410)
CustodialChildTransferEntry.configure(state='readonly')


ExtraChildDaysLabel=Label(ServicesFrameRight,text='Extra Days',font=('times',12,'italic'),bg='green',fg='white')
ExtraChildDaysLabel.place(x=100,y=440)
ExtraChildDaysEntry=Entry(ServicesFrameRight,textvariable=TransferDaysAmountChild)
ExtraChildDaysEntry.place(x=500,y=440)
ExtraChildDaysEntry.configure(state='readonly')


ExtraChildDaysPreservationLabel=Label(ServicesFrameRight,text='For Preservation and after care less 4 days stay',font=('times',12,'italic'),bg='green',fg='white')
ExtraChildDaysPreservationLabel.place(x=100,y=470)
ExtraChildDaysPreservationEntry=Entry(ServicesFrameRight,textvariable=TransferPreservationAmountChild)
ExtraChildDaysPreservationEntry.place(x=500,y=470)
ExtraDaysPreservationEntry.configure(state='readonly')


OvernightChildLabel=Label(ServicesFrameRight,text='Body On Transit Overnight Stay',font=('times',12,'italic'),bg='green',fg='white')
OvernightChildLabel.place(x=100,y=500)
OvernightChildEntry=Entry(ServicesFrameRight,textvariable=TransitAmountChild)
OvernightChildEntry.place(x=500,y=500)
OvernightChildEntry.configure(state='readonly')


SeveralPMChildLabel=Label(ServicesFrameRight,text='Bodies with several Post Mortem Changes',font=('times',16,'italic'),bg='green',fg='white')
SeveralPMChildLabel.place(x=0,y=530)

AdmitPMChildLabel=Label(ServicesFrameRight,text='Body Admission and Preservation Process',font=('times',12,'italic'),bg='green',fg='white')
AdmitPMChildLabel.place(x=100,y=560)
AdmitPMChildEntry=Entry(ServicesFrameRight,textvariable=BodyAPMAdmissionAmountChild)
AdmitPMChildEntry.place(x=500,y=560)
AdmitPMChildEntry.configure(state='readonly')


CustodyPMChildLabel=Label(ServicesFrameRight,text='Daily Custodial Care And Storage',font=('times',12,'italic'),bg='green',fg='white')
CustodyPMChildLabel.place(x=100,y=590)
CustodyPMChildEntry=Entry(ServicesFrameRight,textvariable=BodyAPMCustodyAmountChild)
CustodyPMChildEntry.place(x=500,y=590)
CustodyPMChildEntry.configure(state='readonly')


GroomPMChildLabel=Label(ServicesFrameRight,text='Final Grooming and Dispatch',font=('times',12,'italic'),bg='green',fg='white')
GroomPMChildLabel.place(x=100,y=620)
GroomPMChildEntry=Entry(ServicesFrameRight,textvariable=BodyAPMGroomingAmountChild)
GroomPMChildEntry.place(x=500,y=620)
GroomPMChildEntry.configure(state='readonly')

NextButtonCoffin=Button(ServicesFrameRight,text="Next",font=('times',14,'italic'),bg='green',command=flowerselect,width=15,fg='white',relief='ridge',bd=2)
NextButtonCoffin.place(x=500,y=700)



def cmdChild():
	if (BodyAdmitChild.get() == 0):
		BodyWashingChildEntry.configure(state=DISABLED)
		BodyWashingAmountChild.set(0)
	elif BodyAdmitChild.get() == 1:
		BodyWashingChildEntry.configure(state='readonly')
		BodyWashingAmountChild.set(2000)

	if DailyCareChild.get()==0:
		CustodyChildEntry.configure(state=DISABLED)
		DailyCareAmountChild.set(0)
	elif DailyCareChild.get()==1:
		CustodyChildEntry.configure(state='readonly')
		DailyCareAmountChild.set(500)

	if GroomingChild.get()==0:
		FinalChildGroomingEntry.configure(state=DISABLED)
		GroomingAmountChild.set(0)
	elif GroomingChild.get()==1:
		FinalChildGroomingEntry.configure(state='readonly')
		GroomingAmountChild.set(1000)

	if PMSuitChild.get()==0:
		PostMortemSuitChildEntry.configure(state=DISABLED)
		PMSuitAmountChild.set(0)
	elif PMSuitChild.get()==1:
		PostMortemSuitChildEntry.configure(state='readonly')
		PMSuitAmountChild.set(4000)

	if PMCareChild.get()==0:
		PostMortemAutopsyChildEntry.configure(state=DISABLED)
		PMCareAmountChild.set(0)
	elif PMCareChild.get()==1:
		PostMortemAutopsyChildEntry.configure(state='readonly')
		PMCareAmountChild.set(6000)
	

	if SampleCareChild.get()==0:
		PostMortemSamplesChildEntry.configure(state=DISABLED)
		SampleCareAmountChild.set(0)
	elif SampleCareChild.get()==1:
		PostMortemSamplesChildEntry.configure(state='readonly')
		SampleCareAmountChild.set(1000)

	if DailyPMCareChild.get()==0:
		PostMortemDailyChildEntry.configure(state=DISABLED)
		DailyPMCareAmountChild.set(0)
	elif DailyPMCareChild.get()==1:
		PostMortemDailyChildEntry.configure(state='readonly')
		DailyPMCareAmountChild.set(1500)

	if ExhumationChild.get()==0:
		ExhumationChildEntry.configure(state=DISABLED)
		ExhumationAmountChild.set(0)
	elif ExhumationChild.get()==1:
		ExhumationChildEntry.configure(state='readonly')
		ExhumationAmountChild.set(150000)

	if TransferChild.get()==0:
		CustodialChildTransferEntry.configure(state=DISABLED)
		TransferAmount.set(0)
	elif TransferChild.get()==1:
		CustodialChildTransferEntry.configure(state='readonly')
		TransferAmountChild.set(5000)
	if TransferDaysChild.get()==0:
		ExtraChildDaysEntry.configure(state=DISABLED)
		TransferDaysAmountChild.set(0)
	elif TransferDaysChild.get()==1:
		ExtraChildDaysEntry.configure(state='readonly')
		TransferDaysAmountChild.set(1000)

	if TransferPreservationChild.get()==0:
		ExtraChildDaysPreservationEntry.configure(state=DISABLED)
		TransferPreservationAmountChild.set(0)
	elif TransferPreservationChild.get()==1:
		ExtraChildDaysPreservationEntry.configure(state='readonly')
		TransferPreservationAmountChild.set(8000)

	if TransitChild.get()==0:
		OvernightChildEntry.configure(state=DISABLED)
		TransitAmountChild.set(0)
	elif TransitChild.get()==1:
		OvernightChildEntry.configure(state='readonly')
		TransitAmountChild.set(2000)

	if BodyAPMAdmissionChild.get()==0:
		AdmitPMChildEntry.configure(state=DISABLED)
		BodyAPMAdmissionAmountChild.set(0)
	elif BodyAPMAdmissionChild.get()==1:
		AdmitPMChildEntry.configure(state='readonly')
		BodyAPMAdmissionAmountChild.set(4000)

	if BodyAPMCustodyChild.get()==0:
		CustodyPMChildEntry.configure(state=DISABLED)
		BodyAPMCustodyAmountChild.set(0)
	elif BodyAPMCustodyChild.get()==1:
		CustodyPMChildEntry.configure(state='readonly')
		BodyAPMCustodyAmountChild.set(1000)

	if BodyAPMGroomingChild.get()==0:
		GroomPMChildEntry.configure(state=DISABLED)
		BodyAPMGroomingAmountChild.set(0)
	elif BodyAPMGroomingChild.get()==1:
		GroomPMChildEntry.configure(state='readonly')
		BodyAPMGroomingAmountChild.set(2500)


Chkbtn1Child=Checkbutton(ServicesFrameRight,offvalue=0,onvalue=1,variable=BodyAdmitChild,command=cmdChild,bg='green')
Chkbtn1Child.place(x=20,y=80)

Chkbtn2Child=Checkbutton(ServicesFrameRight,offvalue=0,onvalue=1,variable=DailyCareChild,command=cmdChild,bg='green')
Chkbtn2Child.place(x=20,y=110)

Chkbtn3Child=Checkbutton(ServicesFrameRight,offvalue=0,onvalue=1,variable=GroomingChild,command=cmdChild,bg='green')
Chkbtn3Child.place(x=20,y=140)

Chkbtn4Child=Checkbutton(ServicesFrameRight,offvalue=0,onvalue=1,variable=PMSuitChild,command=cmdChild,bg='green')
Chkbtn4Child.place(x=20,y=230)

Chkbtn5Child=Checkbutton(ServicesFrameRight,offvalue=0,onvalue=1,variable=PMCareChild,command=cmdChild,bg='green')
Chkbtn5Child.place(x=20,y=260)

Chkbtn6Child=Checkbutton(ServicesFrameRight,offvalue=0,onvalue=1,variable=SampleCareChild,command=cmdChild,bg='green')
Chkbtn6Child.place(x=20,y=290)

Chkbtn7Child=Checkbutton(ServicesFrameRight,offvalue=0,onvalue=1,variable=DailyPMCareChild,command=cmdChild,bg='green')
Chkbtn7Child.place(x=20,y=320)

Chkbtn8Child=Checkbutton(ServicesFrameRight,offvalue=0,onvalue=1,variable=ExhumationChild,command=cmdChild,bg='green')
Chkbtn8Child.place(x=20,y=350)

Chkbtn9Child=Checkbutton(ServicesFrameRight,offvalue=0,onvalue=1,variable=TransferChild,command=cmdChild,bg='green')
Chkbtn9Child.place(x=20,y=410)

Chkbtn10Child=Checkbutton(ServicesFrameRight,offvalue=0,onvalue=1,variable=TransferDaysChild,command=cmdChild,bg='green')
Chkbtn10Child.place(x=20,y=440)

Chkbtn11Child=Checkbutton(ServicesFrameRight,offvalue=0,onvalue=1,variable=TransferPreservationChild,command=cmdChild,bg='green')
Chkbtn11Child.place(x=20,y=470)

Chkbtn12Child=Checkbutton(ServicesFrameRight,offvalue=0,onvalue=1,variable=TransitChild,command=cmdChild,bg='green')
Chkbtn12Child.place(x=20,y=500)

Chkbtn13Child=Checkbutton(ServicesFrameRight,offvalue=0,onvalue=1,variable=BodyAPMAdmissionChild,command=cmdChild,bg='green')
Chkbtn13Child.place(x=20,y=560)

Chkbtn14Child=Checkbutton(ServicesFrameRight,offvalue=0,onvalue=1,variable=BodyAPMCustodyChild,command=cmdChild,bg='green')
Chkbtn14Child.place(x=20,y=590)

Chkbtn15Child=Checkbutton(ServicesFrameRight,offvalue=0,onvalue=1,variable=BodyAPMGroomingChild,command=cmdChild,bg='green')
Chkbtn15Child.place(x=20,y=620)

#-----------------------------------------flowers select----------------------------

MauaFrame=Frame(root,width=1366,height=768,bg='green',bd=2,relief='ridge')
#MauaFrame.pack()

MauaFrameLeft=Frame(MauaFrame,width=1010,height=768,bg='green',bd=2,relief='ridge')
MauaFrameLeft.pack(side=LEFT)

MauaFrameRight=Frame(MauaFrame,width=356,height=768,bg='Green',bd=2,relief='ridge')
MauaFrameRight.pack(side=RIGHT)

Cross=IntVar()
Heart=IntVar()
Family=IntVar()
Small=IntVar()
Medium=IntVar()
Big=IntVar()

Cross.set(0)
Heart.set(0)
Family.set(0)
Small.set(0)
Medium.set(0)
Big.set(0)

CrossDefine=StringVar()
HeartDefine=StringVar()
FamilyDefine=StringVar()
SmallDefine=StringVar()
MediumDefine=StringVar()
BigDefine=StringVar()

CrossDefine.set("")
HeartDefine.set("")
FamilyDefine.set("")
SmallDefine.set("")
MediumDefine.set("")
BigDefine.set("")

CrossAmount=IntVar()
HeartAmount=IntVar()
FamilyAmount=IntVar()
SmallAmount=IntVar()
MediumAmount=IntVar()
BigAmount=IntVar()

Maualeft=PhotoImage(file="logo.gif")
Maualeftlabel=Label(MauaFrameLeft,image=Maualeft,bd=4,relief='ridge')
Maualeftlabel.place(x=0,y=0)

Mauaright=PhotoImage(file="Egerton.gif")
Mauarightlabel=Label(MauaFrameRight,image=Mauaright,bd=4,relief='ridge')
Mauarightlabel.place(x=80,y=50)

CrossSetSelectLabel=Label(MauaFrameLeft,text='Cross Set',font=('times',12,'italic'),bg='green',fg='white')
CrossSetSelectLabel.place(x=50,y=200)

CrossSetDefinitionEntry=Entry(MauaFrameLeft,width=30,textvariable=CrossDefine)
CrossSetDefinitionEntry.place(x=300,y=200)
CrossSetDefinitionEntry.configure(state='readonly')

CrossSetSelectEntry=Entry(MauaFrameLeft,textvariable=CrossAmount)
CrossSetSelectEntry.place(x=500,y=200)
CrossSetSelectEntry.configure(state='readonly')

HeartSetSelectLabel=Label(MauaFrameLeft,text='Heart Set',font=('times',12,'italic'),bg='green',fg='white')
HeartSetSelectLabel.place(x=50,y=300)

HeartSetDefinitionEntry=Entry(MauaFrameLeft,width=30,textvariable=HeartDefine)
HeartSetDefinitionEntry.place(x=300,y=300)
HeartSetDefinitionEntry.configure(state='readonly')

HeartSetSelectEntry=Entry(MauaFrameLeft,textvariable=HeartAmount)
HeartSetSelectEntry.place(x=500,y=300)
HeartSetSelectEntry.configure(state='readonly')

FamilySetSelectLabel=Label(MauaFrameLeft,text='Family Set',font=('times',12,'italic'),bg='green',fg='white')
FamilySetSelectLabel.place(x=50,y=400)

FamilySetDefinitionEntry=Entry(MauaFrameLeft,width=30,textvariable=FamilyDefine)
FamilySetDefinitionEntry.place(x=300,y=400)
FamilySetDefinitionEntry.configure(state='readonly')

FamilySetSelectEntry=Entry(MauaFrameLeft,textvariable=FamilyAmount)
FamilySetSelectEntry.place(x=500,y=400)
FamilySetSelectEntry.configure(state='readonly')

SmallBouquetSelectLabel=Label(MauaFrameLeft,text='Small Size Bouquet',font=('times',12,'italic'),bg='green',fg='white')
SmallBouquetSelectLabel.place(x=50,y=500)

SmallBouquetDefinitionEntry=Entry(MauaFrameLeft,width=30,textvariable=SmallDefine)
SmallBouquetDefinitionEntry.place(x=300,y=500)
SmallBouquetDefinitionEntry.configure(state='readonly')

SmallBouquetSelectEntry=Entry(MauaFrameLeft,textvariable=SmallAmount)
SmallBouquetSelectEntry.place(x=500,y=500)
SmallBouquetSelectEntry.configure(state='readonly')

MediumBouquetSelectLabel=Label(MauaFrameLeft,text='Medium Size Bouquet',font=('times',12,'italic'),bg='green',fg='white')
MediumBouquetSelectLabel.place(x=50,y=600)

MediumBouquetDefinitionEntry=Entry(MauaFrameLeft,width=30,textvariable=MediumDefine)
MediumBouquetDefinitionEntry.place(x=300,y=600)
MediumBouquetDefinitionEntry.configure(state='readonly')

MediumBouquetSelectEntry=Entry(MauaFrameLeft,textvariable=MediumAmount)
MediumBouquetSelectEntry.place(x=500,y=600)
MediumBouquetSelectEntry.configure(state='readonly')

BigBouquetSelectLabel=Label(MauaFrameLeft,text='Big Size Bouquet',font=('times',12,'italic'),bg='green',fg='white')
BigBouquetSelectLabel.place(x=50,y=700)

BigBouquetDefinitionEntry=Entry(MauaFrameLeft,width=30,textvariable=BigDefine)
BigBouquetDefinitionEntry.place(x=300,y=700)
BigBouquetDefinitionEntry.configure(state='readonly')

BigBouquetSelectEntry=Entry(MauaFrameLeft,textvariable=BigAmount)
BigBouquetSelectEntry.place(x=500,y=700)
BigBouquetSelectEntry.configure(state='readonly')

def chagua():
        if(Cross.get()==0):
                CrossDefine.set("")
                CrossAmount.set(0)
                CrossSetDefinitionEntry.configure(state=DISABLED)
                CrossSetSelectEntry.configure(state=DISABLED)
        elif(Cross.get()==1):
                CrossDefine.set("Cross Set")
                CrossAmount.set(1500)
                CrossSetDefinitionEntry.configure(state='readonly')
                CrossSetSelectEntry.configure(state='readonly')

        if(Heart.get()==0):
                HeartDefine.set("")
                HeartAmount.set(0)
                HeartSetDefinitionEntry.configure(state=DISABLED)
                HeartSetSelectEntry.configure(state=DISABLED)
        elif(Heart.get()==1):
                HeartDefine.set("Heart Set")
                HeartAmount.set(1500)
                HeartSetDefinitionEntry.configure(state='readonly')
                HeartSetSelectEntry.configure(state='readonly')
        if(Family.get()==0):
                FamilyDefine.set("")
                FamilyAmount.set(0)
                FamilySetDefinitionEntry.configure(state=DISABLED)
                FamilySetSelectEntry.configure(state=DISABLED)
        elif(Family.get()==1):
                FamilyDefine.set("Family Set")
                FamilyAmount.set(1500)
                FamilySetDefinitionEntry.configure(state='readonly')
                FamilySetSelectEntry.configure(state='readonly')
        if(Small.get()==0):
                SmallDefine.set("")
                SmallAmount.set(0)
                SmallBouquetDefinitionEntry.configure(state=DISABLED)
                SmallBouquetSelectEntry.configure(state=DISABLED)
        elif(Small.get()==1):
                SmallDefine.set("Small Size Bouquet")
                SmallAmount.set(2000)
                SmallBouquetDefinitionEntry.configure(state='readonly')
                SmallBouquetSelectEntry.configure(state='readonly')
        if(Medium.get()==0):
                MediumDefine.set("")
                MediumAmount.set(0)
                MediumBouquetDefinitionEntry.configure(state=DISABLED)
                MediumBouquetSelectEntry.configure(state=DISABLED)
        elif(Medium.get()==1):
                MediumDefine.set("Medium Size Bouquet")
                MediumAmount.set(3500)
                MediumBouquetDefinitionEntry.configure(state='readonly')
                MediumBouquetSelectEntry.configure(state='readonly')
        if(Big.get()==0):
                BigDefine.set("")
                BigAmount.set(0)
                BigBouquetDefinitionEntry.configure(state=DISABLED)
                BigBouquetSelectEntry.configure(state=DISABLED)
        elif(Big.get()==1):
                BigDefine.set("Big Size Bouquet")
                BigAmount.set(5000)
                BigBouquetDefinitionEntry.configure(state='readonly')
                BigBouquetSelectEntry.configure(state='readonly')



Chkbtn1Maua=Checkbutton(MauaFrameLeft,offvalue=0,onvalue=1,variable=Cross,command=chagua,bg='green')
Chkbtn1Maua.place(x=20,y=200)

Chkbtn2Maua=Checkbutton(MauaFrameLeft,offvalue=0,onvalue=1,variable=Heart,command=chagua,bg='green')
Chkbtn2Maua.place(x=20,y=300)

Chkbtn3Maua=Checkbutton(MauaFrameLeft,offvalue=0,onvalue=1,variable=Family,command=chagua,bg='green')
Chkbtn3Maua.place(x=20,y=400)

Chkbtn4Maua=Checkbutton(MauaFrameLeft,offvalue=0,onvalue=1,variable=Small,command=chagua,bg='green')
Chkbtn4Maua.place(x=20,y=500)

Chkbtn5Maua=Checkbutton(MauaFrameLeft,offvalue=0,onvalue=1,variable=Medium,command=chagua,bg='green')
Chkbtn5Maua.place(x=20,y=600)

Chkbtn6Maua=Checkbutton(MauaFrameLeft,offvalue=0,onvalue=1,variable=Big,command=chagua,bg='green')
Chkbtn6Maua.place(x=20,y=700)

MauaBackButton=Button(MauaFrameRight,text="Back",relief='ridge',bd=2,bg='Green',fg='white',height=3,width=30)
MauaBackButton.place(x=50,y=400)


MauaNextButton=Button(MauaFrameRight,text="Next",relief='ridge',bd=2,bg='Green',fg='white',height=3,command=eulogy,width=30)
MauaNextButton.place(x=50,y=600)

#--------------------------eulogy---------------------------------------------

FlowerFrame=Frame(root,width=1366,height=768,relief='ridge',bd=2,bg='Green')
#FlowerFrame.pack()

FlowerFrameLeft=Frame(FlowerFrame,width=1010,height=768,relief='ridge',bd=2,bg='Green')
FlowerFrameLeft.pack(side=LEFT)
FlowerFrameRight=Frame(FlowerFrame,width=356,height=768,relief='ridge',bd=2,bg='Green')
FlowerFrameRight.pack(side=RIGHT)

A3One=IntVar()
A3Two=IntVar()
A4One=IntVar()
A4Two=IntVar()
Epson=IntVar()
Black=IntVar()

A3One.set(0)
A3Two.set(0)
A4One.set(0)
A4Two.set(0)
Epson.set(0)
Black.set(0)

A3OneAmount=IntVar()
A3TwoAmount=IntVar()
A4OneAmount=IntVar()
A4TwoAmount=IntVar()
EpsonAmount=IntVar()
BlackAmount=IntVar()

A3OneAmount.set(0)
A3TwoAmount.set(0)
A4OneAmount.set(0)
A4TwoAmount.set(0)
EpsonAmount.set(0)
BlackAmount.set(0)

A3OneDefine=IntVar()
A3TwoDefine=IntVar()
A4OneDefine=IntVar()
A4TwoDefine=IntVar()
EpsonDefine=IntVar()
BlackDefine=IntVar()

A3OneDefine.set("")
A3TwoDefine.set("")
A4OneDefine.set("")
A4TwoDefine.set("")
EpsonDefine.set("")
BlackDefine.set("")

flowerleft=PhotoImage(file="logo.gif")

flowerleftlabel=Label(FlowerFrameLeft,image=flowerleft,bd=4,relief='ridge')
flowerleftlabel.place(x=0,y=0)

flowerright=PhotoImage(file="Egerton.gif")

flowerrightlabel=Label(FlowerFrameRight,image=flowerright,bd=4,relief='ridge')
flowerrightlabel.place(x=80,y=50)


A3OneSelectLabel=Label(FlowerFrameLeft,text='A 3 One Page Colour',font=('times',12,'italic'),bg='green',fg='white')
A3OneSelectLabel.place(x=50,y=200)

A3OneDefinitionEntry=Entry(FlowerFrameLeft,width=30,textvariable=A3OneDefine)
A3OneDefinitionEntry.place(x=300,y=200)
A3OneDefinitionEntry.configure(state='readonly')

A3OneSelectEntry=Entry(FlowerFrameLeft,textvariable=A3OneAmount)
A3OneSelectEntry.place(x=500,y=200)
A3OneSelectEntry.configure(state='readonly')

A3TwoSelectLabel=Label(FlowerFrameLeft,text='A 3 Two Page Colour',font=('times',12,'italic'),bg='green',fg='white')
A3TwoSelectLabel.place(x=50,y=300)

A3TwoDefinitionEntry=Entry(FlowerFrameLeft,width=30,textvariable=A3TwoDefine)
A3TwoDefinitionEntry.place(x=300,y=300)
A3TwoDefinitionEntry.configure(state='readonly')

A3TwoSelectEntry=Entry(FlowerFrameLeft,textvariable=A3TwoAmount)
A3TwoSelectEntry.place(x=500,y=300)
A3TwoSelectEntry.configure(state='readonly')

A4OneSelectLabel=Label(FlowerFrameLeft,text='A 4 One Page Colour',font=('times',12,'italic'),bg='green',fg='white')
A4OneSelectLabel.place(x=50,y=400)

A4OneDefinitionEntry=Entry(FlowerFrameLeft,width=30,textvariable=A4OneDefine)
A4OneDefinitionEntry.place(x=300,y=400)
A4OneDefinitionEntry.configure(state='readonly')

A4OneSelectEntry=Entry(FlowerFrameLeft,textvariable=A4OneAmount)
A4OneSelectEntry.place(x=500,y=400)
A4OneSelectEntry.configure(state='readonly')

A4TwoSelectLabel=Label(FlowerFrameLeft,text='A 4 Two Page Colour',font=('times',12,'italic'),bg='green',fg='white')
A4TwoSelectLabel.place(x=50,y=500)

A4TwoDefinitionEntry=Entry(FlowerFrameLeft,width=30,textvariable=A4TwoDefine)
A4TwoDefinitionEntry.place(x=300,y=500)
A4TwoDefinitionEntry.configure(state='readonly')

A4TwoSelectEntry=Entry(FlowerFrameLeft,textvariable=A4TwoAmount)
A4TwoSelectEntry.place(x=500,y=500)
A4TwoSelectEntry.configure(state='readonly')

EpsonNumberLabel=Label(FlowerFrameLeft,text="",font=('times',10,'italic'),fg='white',bg='Green')
EpsonNumberLabel.place(x=300,y=580)

EpsonCostLabel=Label(FlowerFrameLeft,text="20/= Per Copy",font=('times',10,'italic'),fg='white',bg='Green')
EpsonCostLabel.place(x=500,y=580)

EpsonSelectLabel=Label(FlowerFrameLeft,text='Epson Printing',font=('times',12,'italic'),bg='green',fg='white')
EpsonSelectLabel.place(x=50,y=600)

EpsonDefinitionEntry=Entry(FlowerFrameLeft,width=30,textvariable=EpsonDefine)
EpsonDefinitionEntry.place(x=300,y=600)
EpsonDefinitionEntry.configure(state=NORMAL)

EpsonSelectEntry=Entry(FlowerFrameLeft,textvariable=EpsonAmount)
EpsonSelectEntry.place(x=500,y=600)
EpsonSelectEntry.configure(state='readonly')

BlackSelectLabel=Label(FlowerFrameLeft,text='Black and White',font=('times',12,'italic'),bg='green',fg='white')
BlackSelectLabel.place(x=50,y=700)

BlackDefinitionEntry=Entry(FlowerFrameLeft,width=30,textvariable=BlackDefine)
BlackDefinitionEntry.place(x=300,y=700)
BlackDefinitionEntry.configure(state='readonly')

BlackSelectEntry=Entry(FlowerFrameLeft,textvariable=BlackAmount)
BlackSelectEntry.place(x=500,y=700)
BlackSelectEntry.configure(state='readonly')

def eul():
        if(A3One.get()==0):
                A3OneDefine.set("")
                A3OneAmount.set(0)
                A3OneDefinitionEntry.configure(state=DISABLED)
                A3OneSelectEntry.configure(state=DISABLED)
        elif(A3One.get()==1):
                A3OneDefine.set("A 3 One Page Colour")
                A3OneAmount.set(12000)
                A3OneDefinitionEntry.configure(state='readonly')
                A3OneSelectEntry.configure(state='readonly')
        if(A3Two.get()==0):
                A3TwoDefine.set("")
                A3TwoAmount.set(0)
                A3TwoDefinitionEntry.configure(state=DISABLED)
                A3TwoSelectEntry.configure(state=DISABLED)
        elif(A3Two.get()==1):
                A3TwoDefine.set("A 3 Two Pages Colour")
                A3TwoAmount.set(15000)
                A3TwoDefinitionEntry.configure(state='readonly')
                A3TwoSelectEntry.configure(state='readonly')

        if(A4One.get()==0):
                A4OneDefine.set("")
                A4OneAmount.set(0)
                A4OneDefinitionEntry.configure(state=DISABLED)
                A4OneSelectEntry.configure(state=DISABLED)
        elif(A4One.get()==1):
                A4OneDefine.set("A 4 One Page Colour")
                A4OneAmount.set(7500)
                A4OneDefinitionEntry.configure(state='readonly')
                A4OneSelectEntry.configure(state='readonly')
        if(A4Two.get()==0):
                A4TwoDefine.set("")
                A4TwoAmount.set(0)
                A4TwoDefinitionEntry.configure(state=DISABLED)
                A4TwoSelectEntry.configure(state=DISABLED)
        elif(A4Two.get()==1):
                A4TwoDefine.set("A 4 Two Pages Colour")
                A4TwoAmount.set(9000)
                A4TwoDefinitionEntry.configure(state='readonly')
                A4TwoSelectEntry.configure(state='readonly')
        if(Epson.get()==0):
                EpsonDefine.set("")
                EpsonAmount.set(0)
                EpsonDefinitionEntry.configure(state=DISABLED)
                EpsonSelectEntry.configure(state=DISABLED)
        elif(Epson.get()==1):
                EpsonDefine.set("Epson Printed")
                EpsonAmount.set(0)
                EpsonDefinitionEntry.configure(state=NORMAL)
                EpsonSelectEntry.configure(state=NORMAL)
        if(Black.get()==0):
                BlackDefine.set("")
                BlackAmount.set(0)
                BlackDefinitionEntry.configure(state=DISABLED)
                BlackSelectEntry.configure(state=DISABLED)
        elif(Black.get()==1):
                BlackDefine.set("Black And White")
                BlackAmount.set(800)
                BlackDefinitionEntry.configure(state='readonly')
                BlackSelectEntry.configure(state='readonly')

Chkbtn1Eulogy=Checkbutton(FlowerFrameLeft,offvalue=0,onvalue=1,variable=A3One,command=eul,bg='green')
Chkbtn1Eulogy.place(x=20,y=200)

Chkbtn2Eulogy=Checkbutton(FlowerFrameLeft,offvalue=0,onvalue=1,variable=A3Two,command=eul,bg='green')
Chkbtn2Eulogy.place(x=20,y=300)

Chkbtn3Eulogy=Checkbutton(FlowerFrameLeft,offvalue=0,onvalue=1,variable=A4One,command=eul,bg='green')
Chkbtn3Eulogy.place(x=20,y=400)

Chkbtn4Eulogy=Checkbutton(FlowerFrameLeft,offvalue=0,onvalue=1,variable=A4Two,command=eul,bg='green')
Chkbtn4Eulogy.place(x=20,y=500)

Chkbtn5Eulogy=Checkbutton(FlowerFrameLeft,offvalue=0,onvalue=1,variable=Epson,command=eul,bg='green')
Chkbtn5Eulogy.place(x=20,y=600)

Chkbtn5Eulogy=Checkbutton(FlowerFrameLeft,offvalue=0,onvalue=1,variable=Black,command=eul,bg='green')
Chkbtn5Eulogy.place(x=20,y=700)

BackFinalButton=Button(FlowerFrameRight,text="Back",relief='ridge',bd=2,bg='Green',fg='white',height=3,width=20,font=('times',14,'italic'))
BackFinalButton.place(x=80,y=450)

SubmitFinalButton=Button(FlowerFrameRight,text="Submit",relief='ridge',bd=2,bg='Green',fg='white',height=3,width=20,font=('times',14,'italic'))
SubmitFinalButton.place(x=80,y=600)

#----------------------comprehensive package--------------------------------------
CoffinFrame=Frame(root,width=1366,height=768,bg='Green',bd=2,relief='ridge')
#CoffinFrame.pack()

CoffinFrameLeft=Frame(CoffinFrame,width=683,height=768,bg='Green',relief='ridge',bd=2)
CoffinFrameLeft.pack(side=LEFT)

CoffinFrameRight=Frame(CoffinFrame,width=683,height=768,bg='Green',relief='ridge',bd=2)
CoffinFrameRight.pack(side=RIGHT)

StandardDPBrown=IntVar()
StandardDPBrown.set(0)
StandardDPBrownDefine=StringVar()
StandardDPWhite=IntVar()
StandardDPWhiteDefine=StringVar()
StandardGGWhite=IntVar()
StandardGGWhiteDefine=StringVar()
StandardGGBrown=IntVar()
StandardGGBrownDefine=StringVar()
ExecutiveChocolateBrown=IntVar()
ExecutiveChocolateBrownDefine=StringVar()
ExecutiveIvoryWhite=IntVar()
ExecutiveIvoryWhiteDefine=StringVar()
Elegance=IntVar()
EleganceDefine=StringVar()
EleganceM=IntVar()
EleganceMDefine=StringVar()
Vienna=IntVar()
ViennaDefine=StringVar()
BronzeSendOff=IntVar()
BronzeSendOffDefine=StringVar()
SilverSendOff=IntVar()
SilverSendOffDefine=StringVar()
GoldSendOff=IntVar()
GoldSendOffDefine=StringVar()
Platinum=IntVar()
PlatinumDefine=StringVar()
BourneD=IntVar()
BourneDDefine=StringVar()
BourneSupremacy=IntVar()
BourneSupremacyDefine=StringVar()
UnderCover=IntVar()
UnderCoverDefine=StringVar()


StandardDPWhiteAmount=IntVar()
StandardDPWhiteAmount.set(0)

StandardDPWhiteDefine.set("")

StandardDPBrownAmount=IntVar()
StandardDPBrownAmount.set(0)

StandardDPBrownDefine.set("")

StandardGGWhiteAmount=IntVar()
StandardGGWhiteAmount.set(0)

StandardGGWhiteDefine.set("")

StandardGGBrownAmount=IntVar()
StandardGGBrownAmount.set(0)

StandardGGBrownDefine.set("")

ExecutiveChocolateBrownAmount=IntVar()
ExecutiveChocolateBrownAmount.set(0)

ExecutiveChocolateBrownDefine.set("")

ExecutiveIvoryWhiteAmount=IntVar()
ExecutiveIvoryWhiteAmount.set(0)

ExecutiveIvoryWhiteDefine.set("")

EleganceAmount=IntVar()
EleganceAmount.set(0)

EleganceDefine.set("")

EleganceMAmount=IntVar()
EleganceMAmount.set(0)

EleganceMDefine.set("")

ViennaAmount=IntVar()
ViennaAmount.set(0)

ViennaDefine.set("")

BronzeSendOffAmount=IntVar()
BronzeSendOffAmount.set(0)

BronzeSendOffDefine.set("")

SilverSendOffAmount=IntVar()
SilverSendOffAmount.set(0)

SilverSendOffDefine.set("")

GoldSendOffAmount=IntVar()
GoldSendOffAmount.set(0)

GoldSendOffDefine.set("")

PlatinumAmount=IntVar()
PlatinumAmount.set(0)

PlatinumDefine.set("")

BourneDAmount=IntVar()
BourneDAmount.set(0)

BourneDDefine.set("")

BourneSupremacyAmount=IntVar()
BourneSupremacyAmount.set(0)

BourneSupremacyDefine.set("")

UnderCoverAmount=IntVar()
UnderCoverAmount.set(0)

UnderCoverDefine.set("")


ServiceLabel=Label(CoffinFrameLeft,text='Coffin Selection',font=('times',20,'italic'),bg='green',fg='white')
ServiceLabel.place(x=10,y=10)

StandardDPBrownSelectLabel=Label(CoffinFrameLeft,text='Standard Dp Brown',font=('times',12,'italic'),bg='green',fg='white')
StandardDPBrownSelectLabel.place(x=50,y=80)

StandardDPBrownDefinitionEntry=Entry(CoffinFrameLeft,width=30,textvariable=StandardDPBrownDefine)
StandardDPBrownDefinitionEntry.place(x=300,y=80)
StandardDPBrownDefinitionEntry.configure(state='readonly')

StandardDPBrownSelectEntry=Entry(CoffinFrameLeft,textvariable=StandardDPBrownAmount)
StandardDPBrownSelectEntry.place(x=500,y=80)
StandardDPBrownSelectEntry.configure(state='readonly')

StandardDPWhiteSelectLabel=Label(CoffinFrameLeft,text='Standard Dp White',font=('times',12,'italic'),bg='green',fg='white')
StandardDPWhiteSelectLabel.place(x=50,y=160)

StandardDPWhiteDefinitionEntry=Entry(CoffinFrameLeft,width=30,textvariable=StandardDPWhiteDefine)
StandardDPWhiteDefinitionEntry.place(x=300,y=160)
StandardDPWhiteDefinitionEntry.configure(state='readonly')

StandardDPWhiteSelectEntry=Entry(CoffinFrameLeft,textvariable=StandardDPWhiteAmount)
StandardDPWhiteSelectEntry.place(x=500,y=160)
StandardDPWhiteSelectEntry.configure(state='readonly')

StandardGGBrownSelectLabel=Label(CoffinFrameLeft,text='Standard GG Brown',font=('times',12,'italic'),bg='green',fg='white')
StandardGGBrownSelectLabel.place(x=50,y=240)

StandardGGBrownDefinitionEntry=Entry(CoffinFrameLeft,width=30,textvariable=StandardGGBrownDefine)
StandardGGBrownDefinitionEntry.place(x=300,y=240)
StandardGGBrownDefinitionEntry.configure(state='readonly')

StandardGGBrownSelectEntry=Entry(CoffinFrameLeft,textvariable=StandardGGBrownAmount)
StandardGGBrownSelectEntry.place(x=500,y=240)
StandardGGBrownSelectEntry.configure(state='readonly')

StandardGGWhiteSelectLabel=Label(CoffinFrameLeft,text='Standard GG White',font=('times',12,'italic'),bg='green',fg='white')
StandardGGWhiteSelectLabel.place(x=50,y=320)

StandardGGWhiteDefinitionEntry=Entry(CoffinFrameLeft,width=30,textvariable=StandardGGWhiteDefine)
StandardGGWhiteDefinitionEntry.place(x=300,y=320)
StandardGGWhiteDefinitionEntry.configure(state='readonly')

StandardGGWhiteSelectEntry=Entry(CoffinFrameLeft,textvariable=StandardGGWhiteAmount)
StandardGGWhiteSelectEntry.place(x=500,y=320)
StandardGGWhiteSelectEntry.configure(state='readonly')

ExecutiveChocolateBrownSelectLabel=Label(CoffinFrameLeft,text='Executive Brown and Chocolate',font=('times',12,'italic'),bg='green',fg='white')
ExecutiveChocolateBrownSelectLabel.place(x=50,y=400)

ExecutiveChocolateBrownDefinitionEntry=Entry(CoffinFrameLeft,width=30,textvariable=ExecutiveChocolateBrownDefine)
ExecutiveChocolateBrownDefinitionEntry.place(x=300,y=400)
ExecutiveChocolateBrownDefinitionEntry.configure(state='readonly')

ExecutiveChocolateBrownSelectEntry=Entry(CoffinFrameLeft,textvariable=ExecutiveChocolateBrownAmount)
ExecutiveChocolateBrownSelectEntry.place(x=500,y=400)
ExecutiveChocolateBrownSelectEntry.configure(state='readonly')

ExecutiveIvoryWhiteSelectLabel=Label(CoffinFrameLeft,text='Executive Ivory White',font=('times',12,'italic'),bg='green',fg='white')
ExecutiveIvoryWhiteSelectLabel.place(x=50,y=480)

ExecutiveIvoryWhiteDefintionEntry=Entry(CoffinFrameLeft,width=30,textvariable=ExecutiveIvoryWhiteDefine)
ExecutiveIvoryWhiteDefintionEntry.place(x=300,y=480)
ExecutiveIvoryWhiteDefintionEntry.configure(state='readonly')

ExecutiveIvoryWhiteSelectEntry=Entry(CoffinFrameLeft,textvariable=ExecutiveIvoryWhiteAmount)
ExecutiveIvoryWhiteSelectEntry.place(x=500,y=480)
ExecutiveIvoryWhiteSelectEntry.configure(state='readonly')

EleganceSelectLabel=Label(CoffinFrameLeft,text='Elegance',font=('times',12,'italic'),bg='green',fg='white')
EleganceSelectLabel.place(x=50,y=560)

EleganceDefinitionEntry=Entry(CoffinFrameLeft,width=30,textvariable=EleganceDefine)
EleganceDefinitionEntry.place(x=300,y=560)
EleganceDefinitionEntry.configure(state='readonly')

EleganceSelectEntry=Entry(CoffinFrameLeft,textvariable=EleganceAmount)
EleganceSelectEntry.place(x=500,y=560)
EleganceSelectEntry.configure(state='readonly')

EleganceMSelectLabel=Label(CoffinFrameLeft,text='Elegance M',font=('times',12,'italic'),bg='green',fg='white')
EleganceMSelectLabel.place(x=50,y=640)

EleganceMDefinitionEntry=Entry(CoffinFrameLeft,width=30,textvariable=EleganceMDefine)
EleganceMDefinitionEntry.place(x=300,y=640)
EleganceMDefinitionEntry.configure(state='readonly')

EleganceMSelectEntry=Entry(CoffinFrameLeft,textvariable=EleganceMAmount)
EleganceMSelectEntry.place(x=500,y=640)
EleganceMSelectEntry.configure(state='readonly')

#--------------------------------

ViennaSelectLabel=Label(CoffinFrameRight,text='Vienna',font=('times',12,'italic'),bg='green',fg='white')
ViennaSelectLabel.place(x=50,y=80)

ViennaDefinitionEntry=Entry(CoffinFrameRight,width=30,textvariable=ViennaDefine)
ViennaDefinitionEntry.place(x=300,y=80)
ViennaDefinitionEntry.configure(state='readonly')

ViennaSelectEntry=Entry(CoffinFrameRight,textvariable=ViennaAmount)
ViennaSelectEntry.place(x=500,y=80)
ViennaSelectEntry.configure(state='readonly')

BronzeSelectLabel=Label(CoffinFrameRight,text='Bronze Send Off',font=('times',12,'italic'),bg='green',fg='white')
BronzeSelectLabel.place(x=50,y=160)

BronzeDefinitionEntry=Entry(CoffinFrameRight,width=30,textvariable=BronzeSendOffDefine)
BronzeDefinitionEntry.place(x=300,y=160)
BronzeDefinitionEntry.configure(state='readonly')

BronzeSelectEntry=Entry(CoffinFrameRight,textvariable=BronzeSendOffAmount)
BronzeSelectEntry.place(x=500,y=160)
BronzeSelectEntry.configure(state='readonly')

SilverSelectLabel=Label(CoffinFrameRight,text='Silver Send Off',font=('times',12,'italic'),bg='green',fg='white')
SilverSelectLabel.place(x=50,y=240)

SilverDefinitionEntry=Entry(CoffinFrameRight,width=30,textvariable=SilverSendOffDefine)
SilverDefinitionEntry.place(x=300,y=240)
SilverDefinitionEntry.configure(state='readonly')

SilverSelectEntry=Entry(CoffinFrameRight,textvariable=SilverSendOffAmount)
SilverSelectEntry.place(x=500,y=240)
SilverSelectEntry.configure(state='readonly')

GoldSelectLabel=Label(CoffinFrameRight,text='Gold Send Off',font=('times',12,'italic'),bg='green',fg='white')
GoldSelectLabel.place(x=50,y=320)

GoldDefinitionEntry=Entry(CoffinFrameRight,width=30,textvariable=GoldSendOffDefine)
GoldDefinitionEntry.place(x=300,y=320)
GoldDefinitionEntry.configure(state='readonly')

GoldSelectEntry=Entry(CoffinFrameRight,textvariable=GoldSendOffAmount)
GoldSelectEntry.place(x=500,y=320)
GoldSelectEntry.configure(state='readonly')

PlatinumSelectLabel=Label(CoffinFrameRight,text='Platinum',font=('times',12,'italic'),bg='green',fg='white')
PlatinumSelectLabel.place(x=50,y=400)

PlatinumDefinitionEntry=Entry(CoffinFrameRight,width=30,textvariable=PlatinumDefine)
PlatinumDefinitionEntry.place(x=300,y=400)
PlatinumDefinitionEntry.configure(state='readonly')

PlatinumSelectEntry=Entry(CoffinFrameRight,textvariable=PlatinumAmount)
PlatinumSelectEntry.place(x=500,y=400)
PlatinumSelectEntry.configure(state='readonly')

BourneDSelectLabel=Label(CoffinFrameRight,text='Bourne D',font=('times',12,'italic'),bg='green',fg='white')
BourneDSelectLabel.place(x=50,y=480)

BourneDDefinitionEntry=Entry(CoffinFrameRight,width=30,textvariable=BourneDDefine)
BourneDDefinitionEntry.place(x=300,y=480)
BourneDDefinitionEntry.configure(state='readonly')

BourneDSelectEntry=Entry(CoffinFrameRight,textvariable=BourneDAmount)
BourneDSelectEntry.place(x=500,y=480)
BourneDSelectEntry.configure(state='readonly')

BourneSupremacySelectLabel=Label(CoffinFrameRight,text='Bourne Supremacy',font=('times',12,'italic'),bg='green',fg='white')
BourneSupremacySelectLabel.place(x=50,y=560)

BourneSupremacyDefinitionEntry=Entry(CoffinFrameRight,width=30,textvariable=BourneSupremacyDefine)
BourneSupremacyDefinitionEntry.place(x=300,y=560)
BourneDDefinitionEntry.configure(state='readonly')

BourneSupremacySelectEntry=Entry(CoffinFrameRight,textvariable=BourneSupremacyAmount)
BourneSupremacySelectEntry.place(x=500,y=560)
BourneSupremacySelectEntry.configure(state='readonly')

UnderCoverSelectLabel=Label(CoffinFrameRight,text='UnderCover',font=('times',12,'italic'),bg='green',fg='white')
UnderCoverSelectLabel.place(x=50,y=640)

UnderCoverDefinitionEntry=Entry(CoffinFrameRight,width=30,textvariable=UnderCoverDefine)
UnderCoverDefinitionEntry.place(x=300,y=640)
UnderCoverDefinitionEntry.configure(state='readonly')

UnderCoverSelectEntry=Entry(CoffinFrameRight,textvariable=UnderCoverAmount)
UnderCoverSelectEntry.place(x=500,y=640)
UnderCoverSelectEntry.configure(state='readonly')

Chkbtn1Select=Checkbutton(CoffinFrameLeft,offvalue=0,onvalue=1,bg='green')
Chkbtn1Select.place(x=20,y=80)

Chkbtn2Select=Checkbutton(CoffinFrameLeft,offvalue=0,onvalue=1,variable=StandardDPWhite,bg='green')
Chkbtn2Select.place(x=20,y=160)


#---------------------

def comm():
        if(StandardDPBrown.get()==0):
        	
        	Chkbtn2Select.configure(state=NORMAL)
        	Chkbtn3Select.configure(state=NORMAL)
        	Chkbtn4Select.configure(state=NORMAL)
        	Chkbtn5Select.configure(state=NORMAL)
        	Chkbtn6Select.configure(state=NORMAL)
        	Chkbtn7Select.configure(state=NORMAL)
        	Chkbtn8Select.configure(state=NORMAL)
        	Chkbtn9Select.configure(state=NORMAL)
        	Chkbtn10Select.configure(state=NORMAL)
        	Chkbtn11Select.configure(state=NORMAL)
        	Chkbtn12Select.configure(state=NORMAL)
        	Chkbtn13Select.configure(state=NORMAL)
        	Chkbtn14Select.configure(state=NORMAL)
        	Chkbtn15Select.configure(state=NORMAL)
        	Chkbtn16Select.configure(state=NORMAL)
        	StandardDPBrownDefine.set("")
        	StandardDPBrownAmount.set(0)
        	StandardDPBrownDefinitionEntry.configure(state=DISABLED)
        	StandardDPBrownSelectEntry.configure(state=DISABLED)
        	
        elif(StandardDPBrown.get()==1):
        	
        	Chkbtn2Select.configure(state=DISABLED)
        	Chkbtn3Select.configure(state=DISABLED)
        	Chkbtn4Select.configure(state=DISABLED)
        	Chkbtn5Select.configure(state=DISABLED)
        	Chkbtn6Select.configure(state=DISABLED)
        	Chkbtn7Select.configure(state=DISABLED)
        	Chkbtn8Select.configure(state=DISABLED)
        	Chkbtn9Select.configure(state=DISABLED)
        	Chkbtn10Select.configure(state=DISABLED)
        	Chkbtn11Select.configure(state=DISABLED)
        	Chkbtn12Select.configure(state=DISABLED)
        	Chkbtn13Select.configure(state=DISABLED)
        	Chkbtn14Select.configure(state=DISABLED)
        	Chkbtn15Select.configure(state=DISABLED)
        	Chkbtn16Select.configure(state=DISABLED)
        	StandardDPBrownDefine.set("Standard DP Brown")
        	StandardDPBrownAmount.set(6500)
        	StandardDPBrownDefinitionEntry.configure(state='readonly')
        	StandardDPBrownSelectEntry.configure(state='readonly')

        if(StandardDPWhite.get()==0):
        	StandardDPWhiteDefine.set("")
        	StandardDPWhiteAmount.set(0)
        	StandardDPWhiteDefinitionEntry.configure(state=DISABLED)
        	StandardDPWhiteSelectEntry.configure(state=DISABLED)
        	Chkbtn1Select.configure(state=NORMAL)
        	Chkbtn3Select.configure(state=NORMAL)
        	Chkbtn4Select.configure(state=NORMAL)
        	Chkbtn5Select.configure(state=NORMAL)
        	Chkbtn6Select.configure(state=NORMAL)
        	Chkbtn7Select.configure(state=NORMAL)
        	Chkbtn8Select.configure(state=NORMAL)
        	Chkbtn9Select.configure(state=NORMAL)
        	Chkbtn10Select.configure(state=NORMAL)
        	Chkbtn11Select.configure(state=NORMAL)
        	Chkbtn12Select.configure(state=NORMAL)
        	Chkbtn13Select.configure(state=NORMAL)
        	Chkbtn14Select.configure(state=NORMAL)
        	Chkbtn15Select.configure(state=NORMAL)
        	Chkbtn16Select.configure(state=NORMAL)
        elif(StandardDPWhite.get()==1):
        	StandardDPWhiteDefine.set("Standard DP White")
        	StandardDPWhiteAmount.set(6500)
        	StandardDPWhiteDefinitionEntry.configure(state='readonly')
        	StandardDPWhiteSelectEntry.configure(state='readonly')
        	Chkbtn1Select.configure(state=DISABLED)
        	Chkbtn3Select.configure(state=DISABLED)
        	Chkbtn4Select.configure(state=DISABLED)
        	Chkbtn5Select.configure(state=DISABLED)
        	Chkbtn6Select.configure(state=DISABLED)
        	Chkbtn7Select.configure(state=DISABLED)
        	Chkbtn8Select.configure(state=DISABLED)
        	Chkbtn9Select.configure(state=DISABLED)
        	Chkbtn10Select.configure(state=DISABLED)
        	Chkbtn11Select.configure(state=DISABLED)
        	Chkbtn12Select.configure(state=DISABLED)
        	Chkbtn13Select.configure(state=DISABLED)
        	Chkbtn14Select.configure(state=DISABLED)
        	Chkbtn15Select.configure(state=DISABLED)
        	Chkbtn16Select.configure(state=DISABLED)

        if(StandardGGBrown.get()==0):
        	StandardGGBrownDefine.set("")
        	StandardGGBrownAmount.set(0)
        	StandardGGBrownDefinitionEntry.configure(state=DISABLED)
        	StandardGGBrownSelectEntry.configure(state='readonly')
        	Chkbtn1Select.configure(state=NORMAL)
        	Chkbtn2Select.configure(state=NORMAL)
        	Chkbtn4Select.configure(state=NORMAL)
        	Chkbtn5Select.configure(state=NORMAL)
        	Chkbtn6Select.configure(state=NORMAL)
        	Chkbtn7Select.configure(state=NORMAL)
        	Chkbtn8Select.configure(state=NORMAL)
        	Chkbtn9Select.configure(state=NORMAL)
        	Chkbtn10Select.configure(state=NORMAL)
        	Chkbtn11Select.configure(state=NORMAL)
        	Chkbtn12Select.configure(state=NORMAL)
        	Chkbtn13Select.configure(state=NORMAL)
        	Chkbtn14Select.configure(state=NORMAL)
        	Chkbtn15Select.configure(state=NORMAL)
        	Chkbtn16Select.configure(state=NORMAL)
        elif(StandardGGBrown.get()==1):
        	StandardGGBrownDefine.set("Standard GG Brown")
        	StandardGGBrownAmount.set(7000)
        	StandardGGBrownDefinitionEntry.configure(state='readonly')
        	StandardGGBrownSelectEntry.configure(state='readonly')
        	Chkbtn2Select.configure(state=DISABLED)
        	Chkbtn1Select.configure(state=DISABLED)
        	Chkbtn4Select.configure(state=DISABLED)
        	Chkbtn5Select.configure(state=DISABLED)
        	Chkbtn6Select.configure(state=DISABLED)
        	Chkbtn7Select.configure(state=DISABLED)
        	Chkbtn8Select.configure(state=DISABLED)
        	Chkbtn9Select.configure(state=DISABLED)
        	Chkbtn10Select.configure(state=DISABLED)
        	Chkbtn11Select.configure(state=DISABLED)
        	Chkbtn12Select.configure(state=DISABLED)
        	Chkbtn13Select.configure(state=DISABLED)
        	Chkbtn14Select.configure(state=DISABLED)
        	Chkbtn15Select.configure(state=DISABLED)
        	Chkbtn16Select.configure(state=DISABLED)

        if(StandardGGWhite.get()==0):
        	StandardGGWhiteDefine.set("")
        	StandardGGWhiteAmount.set(0)
        	StandardGGWhiteDefinitionEntry.configure(state=DISABLED)
        	StandardGGWhiteSelectEntry.configure(state='readonly')
        	Chkbtn1Select.configure(state=NORMAL)
        	Chkbtn2Select.configure(state=NORMAL)
        	Chkbtn3Select.configure(state=NORMAL)
        	Chkbtn5Select.configure(state=NORMAL)
        	Chkbtn6Select.configure(state=NORMAL)
        	Chkbtn7Select.configure(state=NORMAL)
        	Chkbtn8Select.configure(state=NORMAL)
        	Chkbtn9Select.configure(state=NORMAL)
        	Chkbtn10Select.configure(state=NORMAL)
        	Chkbtn11Select.configure(state=NORMAL)
        	Chkbtn12Select.configure(state=NORMAL)
        	Chkbtn13Select.configure(state=NORMAL)
        	Chkbtn14Select.configure(state=NORMAL)
        	Chkbtn15Select.configure(state=NORMAL)
        	Chkbtn16Select.configure(state=NORMAL)
        elif(StandardGGWhite.get()==1):
        	StandardGGWhiteDefine.set("Standard GG White")
        	StandardGGWhiteAmount.set(7000)
        	StandardGGWhiteDefinitionEntry.configure(state='readonly')
        	StandardGGWhiteSelectEntry.configure(state='readonly')
        	Chkbtn2Select.configure(state=DISABLED)
        	Chkbtn3Select.configure(state=DISABLED)
        	Chkbtn1Select.configure(state=DISABLED)
        	Chkbtn5Select.configure(state=DISABLED)
        	Chkbtn6Select.configure(state=DISABLED)
        	Chkbtn7Select.configure(state=DISABLED)
        	Chkbtn8Select.configure(state=DISABLED)
        	Chkbtn9Select.configure(state=DISABLED)
        	Chkbtn10Select.configure(state=DISABLED)
        	Chkbtn11Select.configure(state=DISABLED)
        	Chkbtn12Select.configure(state=DISABLED)
        	Chkbtn13Select.configure(state=DISABLED)
        	Chkbtn14Select.configure(state=DISABLED)
        	Chkbtn15Select.configure(state=DISABLED)
        	Chkbtn16Select.configure(state=DISABLED)

        if(ExecutiveChocolateBrown.get()==0):
        	ExecutiveChocolateBrownDefine.set("")
        	ExecutiveChocolateBrownAmount.set(0)
        	ExecutiveChocolateBrownDefinitionEntry.configure(state=DISABLED)
        	ExecutiveChocolateBrownSelectEntry.configure(state='readonly')
        	Chkbtn1Select.configure(state=NORMAL)
        	Chkbtn2Select.configure(state=NORMAL)
        	Chkbtn3Select.configure(state=NORMAL)
        	Chkbtn4Select.configure(state=NORMAL)
        	Chkbtn6Select.configure(state=NORMAL)
        	Chkbtn7Select.configure(state=NORMAL)
        	Chkbtn8Select.configure(state=NORMAL)
        	Chkbtn9Select.configure(state=NORMAL)
        	Chkbtn10Select.configure(state=NORMAL)
        	Chkbtn11Select.configure(state=NORMAL)
        	Chkbtn12Select.configure(state=NORMAL)
        	Chkbtn13Select.configure(state=NORMAL)
        	Chkbtn14Select.configure(state=NORMAL)
        	Chkbtn15Select.configure(state=NORMAL)
        	Chkbtn16Select.configure(state=NORMAL)
        elif(ExecutiveChocolateBrown.get()==1):
        	ExecutiveChocolateBrownDefine.set("Executive Chocolate Brown")
        	ExecutiveChocolateBrownAmount.set(8500)
        	ExecutiveChocolateBrownDefinitionEntry.configure(state='readonly')
        	ExecutiveChocolateBrownSelectEntry.configure(state='readonly')
        	Chkbtn2Select.configure(state=DISABLED)
        	Chkbtn3Select.configure(state=DISABLED)
        	Chkbtn4Select.configure(state=DISABLED)
        	Chkbtn1Select.configure(state=DISABLED)
        	Chkbtn6Select.configure(state=DISABLED)
        	Chkbtn7Select.configure(state=DISABLED)
        	Chkbtn8Select.configure(state=DISABLED)
        	Chkbtn9Select.configure(state=DISABLED)
        	Chkbtn10Select.configure(state=DISABLED)
        	Chkbtn11Select.configure(state=DISABLED)
        	Chkbtn12Select.configure(state=DISABLED)
        	Chkbtn13Select.configure(state=DISABLED)
        	Chkbtn14Select.configure(state=DISABLED)
        	Chkbtn15Select.configure(state=DISABLED)
        	Chkbtn16Select.configure(state=DISABLED)

        if(ExecutiveIvoryWhite.get()==0):
        	ExecutiveIvoryWhiteDefine.set("")
        	ExecutiveIvoryWhiteAmount.set(0)
        	ExecutiveIvoryWhiteDefintionEntry.configure(state=DISABLED)
        	ExecutiveIvoryWhiteSelectEntry.configure(state='readonly')
        	Chkbtn1Select.configure(state=NORMAL)
        	Chkbtn2Select.configure(state=NORMAL)
        	Chkbtn3Select.configure(state=NORMAL)
        	Chkbtn4Select.configure(state=NORMAL)
        	Chkbtn5Select.configure(state=NORMAL)
        	Chkbtn7Select.configure(state=NORMAL)
        	Chkbtn8Select.configure(state=NORMAL)
        	Chkbtn9Select.configure(state=NORMAL)
        	Chkbtn10Select.configure(state=NORMAL)
        	Chkbtn11Select.configure(state=NORMAL)
        	Chkbtn12Select.configure(state=NORMAL)
        	Chkbtn13Select.configure(state=NORMAL)
        	Chkbtn14Select.configure(state=NORMAL)
        	Chkbtn15Select.configure(state=NORMAL)
        	Chkbtn16Select.configure(state=NORMAL)
        elif(ExecutiveIvoryWhite.get()==1):
        	ExecutiveIvoryWhiteDefine.set("Executive Ivory White")
        	ExecutiveIvoryWhiteAmount.set(9000)
        	ExecutiveIvoryWhiteDefintionEntry.configure(state='readonly')
        	ExecutiveIvoryWhiteSelectEntry.configure(state='readonly')
        	Chkbtn2Select.configure(state=DISABLED)
        	Chkbtn3Select.configure(state=DISABLED)
        	Chkbtn4Select.configure(state=DISABLED)
        	Chkbtn5Select.configure(state=DISABLED)
        	Chkbtn1Select.configure(state=DISABLED)
        	Chkbtn7Select.configure(state=DISABLED)
        	Chkbtn8Select.configure(state=DISABLED)
        	Chkbtn9Select.configure(state=DISABLED)
        	Chkbtn10Select.configure(state=DISABLED)
        	Chkbtn11Select.configure(state=DISABLED)
        	Chkbtn12Select.configure(state=DISABLED)
        	Chkbtn13Select.configure(state=DISABLED)
        	Chkbtn14Select.configure(state=DISABLED)
        	Chkbtn15Select.configure(state=DISABLED)
        	Chkbtn16Select.configure(state=DISABLED)

        if(Elegance.get()==0):
        	EleganceDefine.set("")
        	EleganceAmount.set(0)
        	EleganceMDefinitionEntry.configure(state=DISABLED)
        	EleganceSelectEntry.configure(state='readonly')
        	Chkbtn2Select.configure(state=NORMAL)
        	Chkbtn3Select.configure(state=NORMAL)
        	Chkbtn4Select.configure(state=NORMAL)
        	Chkbtn5Select.configure(state=NORMAL)
        	Chkbtn6Select.configure(state=NORMAL)
        	Chkbtn1Select.configure(state=NORMAL)
        	Chkbtn8Select.configure(state=NORMAL)
        	Chkbtn9Select.configure(state=NORMAL)
        	Chkbtn10Select.configure(state=NORMAL)
        	Chkbtn11Select.configure(state=NORMAL)
        	Chkbtn12Select.configure(state=NORMAL)
        	Chkbtn13Select.configure(state=NORMAL)
        	Chkbtn14Select.configure(state=NORMAL)
        	Chkbtn15Select.configure(state=NORMAL)
        	Chkbtn16Select.configure(state=NORMAL)
        elif(Elegance.get()==1):
        	EleganceDefine.set("Elegance")
        	EleganceAmount.set(18000)
        	EleganceMDefinitionEntry.configure(state='readonly')
        	EleganceSelectEntry.configure(state='readonly')
        	Chkbtn2Select.configure(state=DISABLED)
        	Chkbtn3Select.configure(state=DISABLED)
        	Chkbtn4Select.configure(state=DISABLED)
        	Chkbtn5Select.configure(state=DISABLED)
        	Chkbtn6Select.configure(state=DISABLED)
        	Chkbtn1Select.configure(state=DISABLED)
        	Chkbtn8Select.configure(state=DISABLED)
        	Chkbtn9Select.configure(state=DISABLED)
        	Chkbtn10Select.configure(state=DISABLED)
        	Chkbtn11Select.configure(state=DISABLED)
        	Chkbtn12Select.configure(state=DISABLED)
        	Chkbtn13Select.configure(state=DISABLED)
        	Chkbtn14Select.configure(state=DISABLED)
        	Chkbtn15Select.configure(state=DISABLED)
        	Chkbtn16Select.configure(state=DISABLED)

        if(EleganceM.get()==0):
        	EleganceMDefine.set("")
        	EleganceMAmount.set(0)
        	EleganceMDefinitionEntry.configure(state=DISABLED)
        	EleganceMSelectEntry.configure(state='readonly')
        	Chkbtn2Select.configure(state=NORMAL)
        	Chkbtn3Select.configure(state=NORMAL)
        	Chkbtn4Select.configure(state=NORMAL)
        	Chkbtn5Select.configure(state=NORMAL)
        	Chkbtn6Select.configure(state=NORMAL)
        	Chkbtn7Select.configure(state=NORMAL)
        	Chkbtn1Select.configure(state=NORMAL)
        	Chkbtn9Select.configure(state=NORMAL)
        	Chkbtn10Select.configure(state=NORMAL)
        	Chkbtn11Select.configure(state=NORMAL)
        	Chkbtn12Select.configure(state=NORMAL)
        	Chkbtn13Select.configure(state=NORMAL)
        	Chkbtn14Select.configure(state=NORMAL)
        	Chkbtn15Select.configure(state=NORMAL)
        	Chkbtn16Select.configure(state=NORMAL)
        elif(EleganceM.get()==1):
        	EleganceMDefine.set("Elegance M")
        	EleganceMAmount.set(26000)
        	EleganceMDefinitionEntry.configure(state='readonly')
        	EleganceMSelectEntry.configure(state='readonly')
        	Chkbtn2Select.configure(state=DISABLED)
        	Chkbtn3Select.configure(state=DISABLED)
        	Chkbtn4Select.configure(state=DISABLED)
        	Chkbtn5Select.configure(state=DISABLED)
        	Chkbtn6Select.configure(state=DISABLED)
        	Chkbtn7Select.configure(state=DISABLED)
        	Chkbtn1Select.configure(state=DISABLED)
        	Chkbtn9Select.configure(state=DISABLED)
        	Chkbtn10Select.configure(state=DISABLED)
        	Chkbtn11Select.configure(state=DISABLED)
        	Chkbtn12Select.configure(state=DISABLED)
        	Chkbtn13Select.configure(state=DISABLED)
        	Chkbtn14Select.configure(state=DISABLED)
        	Chkbtn15Select.configure(state=DISABLED)
        	Chkbtn16Select.configure(state=DISABLED)

        if(Vienna.get()==0):
        	ViennaDefine.set("")
        	ViennaAmount.set(0)
        	ViennaDefinitionEntry.configure(state=DISABLED)
        	ViennaSelectEntry.configure(state='readonly')
        	Chkbtn2Select.configure(state=NORMAL)
        	Chkbtn3Select.configure(state=NORMAL)
        	Chkbtn4Select.configure(state=NORMAL)
        	Chkbtn5Select.configure(state=NORMAL)
        	Chkbtn6Select.configure(state=NORMAL)
        	Chkbtn7Select.configure(state=NORMAL)
        	Chkbtn8Select.configure(state=NORMAL)
        	Chkbtn1Select.configure(state=NORMAL)
        	Chkbtn10Select.configure(state=NORMAL)
        	Chkbtn11Select.configure(state=NORMAL)
        	Chkbtn12Select.configure(state=NORMAL)
        	Chkbtn13Select.configure(state=NORMAL)
        	Chkbtn14Select.configure(state=NORMAL)
        	Chkbtn15Select.configure(state=NORMAL)
        	Chkbtn16Select.configure(state=NORMAL)
        elif(Vienna.get()==1):
        	ViennaDefine.set("Vienna")
        	ViennaAmount.set(28000)
        	ViennaDefinitionEntry.configure(state='readonly')
        	ViennaSelectEntry.configure(state='readonly')
        	Chkbtn2Select.configure(state=DISABLED)
        	Chkbtn3Select.configure(state=DISABLED)
        	Chkbtn4Select.configure(state=DISABLED)
        	Chkbtn5Select.configure(state=DISABLED)
        	Chkbtn6Select.configure(state=DISABLED)
        	Chkbtn7Select.configure(state=DISABLED)
        	Chkbtn8Select.configure(state=DISABLED)
        	Chkbtn1Select.configure(state=DISABLED)
        	Chkbtn10Select.configure(state=DISABLED)
        	Chkbtn11Select.configure(state=DISABLED)
        	Chkbtn12Select.configure(state=DISABLED)
        	Chkbtn13Select.configure(state=DISABLED)
        	Chkbtn14Select.configure(state=DISABLED)
        	Chkbtn15Select.configure(state=DISABLED)
        	Chkbtn16Select.configure(state=DISABLED)

        if(BronzeSendOff.get()==0):
        	BronzeSendOffDefine.set("")
        	BronzeSendOffAmount.set(0)
        	BronzeDefinitionEntry.configure(state=DISABLED)
        	BronzeSelectEntry.configure(state='readonly')
        	Chkbtn2Select.configure(state=NORMAL)
        	Chkbtn3Select.configure(state=NORMAL)
        	Chkbtn4Select.configure(state=NORMAL)
        	Chkbtn5Select.configure(state=NORMAL)
        	Chkbtn6Select.configure(state=NORMAL)
        	Chkbtn7Select.configure(state=NORMAL)
        	Chkbtn8Select.configure(state=NORMAL)
        	Chkbtn9Select.configure(state=NORMAL)
        	Chkbtn1Select.configure(state=NORMAL)
        	Chkbtn11Select.configure(state=NORMAL)
        	Chkbtn12Select.configure(state=NORMAL)
        	Chkbtn13Select.configure(state=NORMAL)
        	Chkbtn14Select.configure(state=NORMAL)
        	Chkbtn15Select.configure(state=NORMAL)
        	Chkbtn16Select.configure(state=NORMAL)
        elif(BronzeSendOff.get()==1):
        	BronzeSendOffDefine.set("Bronze Send Off")
        	BronzeSendOffAmount.set(32000)
        	BronzeDefinitionEntry.configure(state='readonly')
        	BronzeSelectEntry.configure(state='readonly')
        	Chkbtn2Select.configure(state=DISABLED)
        	Chkbtn3Select.configure(state=DISABLED)
        	Chkbtn4Select.configure(state=DISABLED)
        	Chkbtn5Select.configure(state=DISABLED)
        	Chkbtn6Select.configure(state=DISABLED)
        	Chkbtn7Select.configure(state=DISABLED)
        	Chkbtn8Select.configure(state=DISABLED)
        	Chkbtn9Select.configure(state=DISABLED)
        	Chkbtn1Select.configure(state=DISABLED)
        	Chkbtn11Select.configure(state=DISABLED)
        	Chkbtn12Select.configure(state=DISABLED)
        	Chkbtn13Select.configure(state=DISABLED)
        	Chkbtn14Select.configure(state=DISABLED)
        	Chkbtn15Select.configure(state=DISABLED)
        	Chkbtn16Select.configure(state=DISABLED)

        if(SilverSendOff.get()==0):
        	SilverSendOffDefine.set("")
        	SilverSendOffAmount.set(0)
        	SilverDefinitionEntry.configure(state=DISABLED)
        	SilverSelectEntry.configure(state='readonly')
        	Chkbtn2Select.configure(state=NORMAL)
        	Chkbtn3Select.configure(state=NORMAL)
        	Chkbtn4Select.configure(state=NORMAL)
        	Chkbtn5Select.configure(state=NORMAL)
        	Chkbtn6Select.configure(state=NORMAL)
        	Chkbtn7Select.configure(state=NORMAL)
        	Chkbtn8Select.configure(state=NORMAL)
        	Chkbtn9Select.configure(state=NORMAL)
        	Chkbtn10Select.configure(state=NORMAL)
        	Chkbtn1Select.configure(state=NORMAL)
        	Chkbtn12Select.configure(state=NORMAL)
        	Chkbtn13Select.configure(state=NORMAL)
        	Chkbtn14Select.configure(state=NORMAL)
        	Chkbtn15Select.configure(state=NORMAL)
        	Chkbtn16Select.configure(state=NORMAL)
        elif(SilverSendOff.get()==1):
        	SilverSendOffDefine.set("Silver Send Off")
        	SilverSendOffAmount.set(33000)
        	SilverDefinitionEntry.configure(state='readonly')
        	SilverSelectEntry.configure(state='readonly')
        	Chkbtn2Select.configure(state=DISABLED)
        	Chkbtn3Select.configure(state=DISABLED)
        	Chkbtn4Select.configure(state=DISABLED)
        	Chkbtn5Select.configure(state=DISABLED)
        	Chkbtn6Select.configure(state=DISABLED)
        	Chkbtn7Select.configure(state=DISABLED)
        	Chkbtn8Select.configure(state=DISABLED)
        	Chkbtn9Select.configure(state=DISABLED)
        	Chkbtn10Select.configure(state=DISABLED)
        	Chkbtn1Select.configure(state=DISABLED)
        	Chkbtn12Select.configure(state=DISABLED)
        	Chkbtn13Select.configure(state=DISABLED)
        	Chkbtn14Select.configure(state=DISABLED)
        	Chkbtn15Select.configure(state=DISABLED)
        	Chkbtn16Select.configure(state=DISABLED)

        if(GoldSendOff.get()==0):
        	GoldSendOffDefine.set("")
        	GoldSendOffAmount.set(0)
        	GoldDefinitionEntry.configure(state=DISABLED)
        	GoldSelectEntry.configure(state='readonly')
        	Chkbtn2Select.configure(state=NORMAL)
        	Chkbtn3Select.configure(state=NORMAL)
        	Chkbtn4Select.configure(state=NORMAL)
        	Chkbtn5Select.configure(state=NORMAL)
        	Chkbtn6Select.configure(state=NORMAL)
        	Chkbtn7Select.configure(state=NORMAL)
        	Chkbtn8Select.configure(state=NORMAL)
        	Chkbtn9Select.configure(state=NORMAL)
        	Chkbtn10Select.configure(state=NORMAL)
        	Chkbtn11Select.configure(state=NORMAL)
        	Chkbtn1Select.configure(state=NORMAL)
        	Chkbtn13Select.configure(state=NORMAL)
        	Chkbtn14Select.configure(state=NORMAL)
        	Chkbtn15Select.configure(state=NORMAL)
        	Chkbtn16Select.configure(state=NORMAL)
        elif(GoldSendOff.get()==1):
        	GoldSendOffDefine.set("Gold Send Off")
        	GoldSendOffAmount.set(35000)
        	GoldDefinitionEntry.configure(state='readonly')
        	GoldSelectEntry.configure(state='readonly')
        	Chkbtn2Select.configure(state=DISABLED)
        	Chkbtn3Select.configure(state=DISABLED)
        	Chkbtn4Select.configure(state=DISABLED)
        	Chkbtn5Select.configure(state=DISABLED)
        	Chkbtn6Select.configure(state=DISABLED)
        	Chkbtn7Select.configure(state=DISABLED)
        	Chkbtn8Select.configure(state=DISABLED)
        	Chkbtn9Select.configure(state=DISABLED)
        	Chkbtn10Select.configure(state=DISABLED)
        	Chkbtn11Select.configure(state=DISABLED)
        	Chkbtn1Select.configure(state=DISABLED)
        	Chkbtn13Select.configure(state=DISABLED)
        	Chkbtn14Select.configure(state=DISABLED)
        	Chkbtn15Select.configure(state=DISABLED)
        	Chkbtn16Select.configure(state=DISABLED)

        if(Platinum.get()==0):
        	PlatinumDefine.set("")
        	PlatinumAmount.set(0)
        	PlatinumDefinitionEntry.configure(state=DISABLED)
        	PlatinumSelectEntry.configure(state='readonly')
        	Chkbtn2Select.configure(state=NORMAL)
        	Chkbtn3Select.configure(state=NORMAL)
        	Chkbtn4Select.configure(state=NORMAL)
        	Chkbtn5Select.configure(state=NORMAL)
        	Chkbtn6Select.configure(state=NORMAL)
        	Chkbtn7Select.configure(state=NORMAL)
        	Chkbtn8Select.configure(state=NORMAL)
        	Chkbtn9Select.configure(state=NORMAL)
        	Chkbtn10Select.configure(state=NORMAL)
        	Chkbtn11Select.configure(state=NORMAL)
        	Chkbtn12Select.configure(state=NORMAL)
        	Chkbtn1Select.configure(state=NORMAL)
        	Chkbtn14Select.configure(state=NORMAL)
        	Chkbtn15Select.configure(state=NORMAL)
        	Chkbtn16Select.configure(state=NORMAL)
        elif(Platinum.get()==1):
        	PlatinumDefine.set("Platinum")
        	PlatinumAmount.set(40000)
        	PlatinumDefinitionEntry.configure(state='readonly')
        	PlatinumSelectEntry.configure(state='readonly')
        	Chkbtn2Select.configure(state=DISABLED)
        	Chkbtn3Select.configure(state=DISABLED)
        	Chkbtn4Select.configure(state=DISABLED)
        	Chkbtn5Select.configure(state=DISABLED)
        	Chkbtn6Select.configure(state=DISABLED)
        	Chkbtn7Select.configure(state=DISABLED)
        	Chkbtn8Select.configure(state=DISABLED)
        	Chkbtn9Select.configure(state=DISABLED)
        	Chkbtn10Select.configure(state=DISABLED)
        	Chkbtn11Select.configure(state=DISABLED)
        	Chkbtn12Select.configure(state=DISABLED)
        	Chkbtn1Select.configure(state=DISABLED)
        	Chkbtn14Select.configure(state=DISABLED)
        	Chkbtn15Select.configure(state=DISABLED)
        	Chkbtn16Select.configure(state=DISABLED)

        if(BourneD.get()==0):
        	BourneDDefine.set("")
        	BourneDAmount.set(0)
        	BourneDDefinitionEntry.configure(state=DISABLED)
        	BourneDSelectEntry.configure(state='readonly')
        	Chkbtn2Select.configure(state=NORMAL)
        	Chkbtn3Select.configure(state=NORMAL)
        	Chkbtn4Select.configure(state=NORMAL)
        	Chkbtn5Select.configure(state=NORMAL)
        	Chkbtn6Select.configure(state=NORMAL)
        	Chkbtn7Select.configure(state=NORMAL)
        	Chkbtn8Select.configure(state=NORMAL)
        	Chkbtn9Select.configure(state=NORMAL)
        	Chkbtn10Select.configure(state=NORMAL)
        	Chkbtn11Select.configure(state=NORMAL)
        	Chkbtn12Select.configure(state=NORMAL)
        	Chkbtn13Select.configure(state=NORMAL)
        	Chkbtn1Select.configure(state=NORMAL)
        	Chkbtn15Select.configure(state=NORMAL)
        	Chkbtn16Select.configure(state=NORMAL)
        elif(BourneD.get()==1):
        	BourneDDefine.set("Bourne D")
        	BourneDAmount.set(2500)
        	BourneDDefinitionEntry.configure(state='readonly')
        	BourneDSelectEntry.configure(state='readonly')
        	Chkbtn2Select.configure(state=DISABLED)
        	Chkbtn3Select.configure(state=DISABLED)
        	Chkbtn4Select.configure(state=DISABLED)
        	Chkbtn5Select.configure(state=DISABLED)
        	Chkbtn6Select.configure(state=DISABLED)
        	Chkbtn7Select.configure(state=DISABLED)
        	Chkbtn8Select.configure(state=DISABLED)
        	Chkbtn9Select.configure(state=DISABLED)
        	Chkbtn10Select.configure(state=DISABLED)
        	Chkbtn11Select.configure(state=DISABLED)
        	Chkbtn12Select.configure(state=DISABLED)
        	Chkbtn13Select.configure(state=DISABLED)
        	Chkbtn1Select.configure(state=DISABLED)
        	Chkbtn15Select.configure(state=DISABLED)
        	Chkbtn16Select.configure(state=DISABLED)

        if(BourneSupremacy.get()==0):
        	BourneSupremacyDefine.set("")
        	BourneSupremacyAmount.set(0)
        	BourneSupremacyDefinitionEntry.configure(state=DISABLED)
        	BourneSupremacySelectEntry.configure(state='readonly')
        	Chkbtn2Select.configure(state=NORMAL)
        	Chkbtn3Select.configure(state=NORMAL)
        	Chkbtn4Select.configure(state=NORMAL)
        	Chkbtn5Select.configure(state=NORMAL)
        	Chkbtn6Select.configure(state=NORMAL)
        	Chkbtn7Select.configure(state=NORMAL)
        	Chkbtn8Select.configure(state=NORMAL)
        	Chkbtn9Select.configure(state=NORMAL)
        	Chkbtn10Select.configure(state=NORMAL)
        	Chkbtn11Select.configure(state=NORMAL)
        	Chkbtn12Select.configure(state=NORMAL)
        	Chkbtn13Select.configure(state=NORMAL)
        	Chkbtn14Select.configure(state=NORMAL)
        	Chkbtn1Select.configure(state=NORMAL)
        	Chkbtn16Select.configure(state=NORMAL)
        elif(BourneSupremacy.get()==1):
        	Chkbtn2Select.configure(state=DISABLED)
        	Chkbtn3Select.configure(state=DISABLED)
        	Chkbtn4Select.configure(state=DISABLED)
        	Chkbtn5Select.configure(state=DISABLED)
        	Chkbtn6Select.configure(state=DISABLED)
        	Chkbtn7Select.configure(state=DISABLED)
        	Chkbtn8Select.configure(state=DISABLED)
        	Chkbtn9Select.configure(state=DISABLED)
        	Chkbtn10Select.configure(state=DISABLED)
        	Chkbtn11Select.configure(state=DISABLED)
        	Chkbtn12Select.configure(state=DISABLED)
        	Chkbtn13Select.configure(state=DISABLED)
        	Chkbtn14Select.configure(state=DISABLED)
        	Chkbtn1Select.configure(state=DISABLED)
        	Chkbtn15Select.configure(state=NORMAL)
        	Chkbtn16Select.configure(state=DISABLED)
        	BourneSupremacyDefine.set("Bourne Supremacy")
        	BourneSupremacyAmount.set(4000)
        	BourneSupremacyDefinitionEntry.configure(state='readonly')
        	BourneSupremacySelectEntry.configure(state='readonly')

        if(UnderCover.get()==0):
        	UnderCoverDefine.set("")
        	UnderCoverAmount.set(0)
        	UnderCoverDefinitionEntry.configure(state=DISABLED)
        	UnderCoverSelectEntry.configure(state='readonly')
        	Chkbtn2Select.configure(state=NORMAL)
        	Chkbtn3Select.configure(state=NORMAL)
        	Chkbtn4Select.configure(state=NORMAL)
        	Chkbtn5Select.configure(state=NORMAL)
        	Chkbtn6Select.configure(state=NORMAL)
        	Chkbtn7Select.configure(state=NORMAL)
        	Chkbtn8Select.configure(state=NORMAL)
        	Chkbtn9Select.configure(state=NORMAL)
        	Chkbtn10Select.configure(state=NORMAL)
        	Chkbtn11Select.configure(state=NORMAL)
        	Chkbtn12Select.configure(state=NORMAL)
        	Chkbtn13Select.configure(state=NORMAL)
        	Chkbtn14Select.configure(state=NORMAL)
        	Chkbtn15Select.configure(state=NORMAL)
        	Chkbtn1Select.configure(state=NORMAL)
        elif(UnderCover.get()==1):
        	UnderCoverDefine.set("Undercover")
        	UnderCoverAmount.set(5000)
        	UnderCoverDefinitionEntry.configure(state='readonly')
        	UnderCoverSelectEntry.configure(state='readonly')
        	Chkbtn2Select.configure(state=DISABLED)
        	Chkbtn3Select.configure(state=DISABLED)
        	Chkbtn4Select.configure(state=DISABLED)
        	Chkbtn5Select.configure(state=DISABLED)
        	Chkbtn6Select.configure(state=DISABLED)
        	Chkbtn7Select.configure(state=DISABLED)
        	Chkbtn8Select.configure(state=DISABLED)
        	Chkbtn9Select.configure(state=DISABLED)
        	Chkbtn10Select.configure(state=DISABLED)
        	Chkbtn11Select.configure(state=DISABLED)
        	Chkbtn12Select.configure(state=DISABLED)
        	Chkbtn13Select.configure(state=DISABLED)
        	Chkbtn14Select.configure(state=DISABLED)
        	Chkbtn15Select.configure(state=DISABLED)
        	Chkbtn1Select.configure(state=DISABLED)


Chkbtn1Select=Checkbutton(CoffinFrameLeft,offvalue=0,onvalue=1,variable=StandardDPBrown,command=comm,bg='green')
Chkbtn1Select.place(x=20,y=80)

Chkbtn2Select=Checkbutton(CoffinFrameLeft,offvalue=0,onvalue=1,variable=StandardDPWhite,command=comm,bg='green')
Chkbtn2Select.place(x=20,y=160)

Chkbtn3Select=Checkbutton(CoffinFrameLeft,offvalue=0,onvalue=1,variable=StandardGGBrown,command=comm,bg='green')
Chkbtn3Select.place(x=20,y=240)

Chkbtn4Select=Checkbutton(CoffinFrameLeft,offvalue=0,onvalue=1,variable=StandardGGWhite,command=comm,bg='green')
Chkbtn4Select.place(x=20,y=320)

Chkbtn5Select=Checkbutton(CoffinFrameLeft,offvalue=0,onvalue=1,variable=ExecutiveChocolateBrown,command=comm,bg='green')
Chkbtn5Select.place(x=20,y=400)

Chkbtn6Select=Checkbutton(CoffinFrameLeft,offvalue=0,onvalue=1,variable=ExecutiveIvoryWhite,command=comm,bg='green')
Chkbtn6Select.place(x=20,y=480)

Chkbtn7Select=Checkbutton(CoffinFrameLeft,offvalue=0,onvalue=1,variable=Elegance,command=comm,bg='green')
Chkbtn7Select.place(x=20,y=560)

Chkbtn8Select=Checkbutton(CoffinFrameLeft,offvalue=0,onvalue=1,variable=EleganceM,command=comm,bg='green')
Chkbtn8Select.place(x=20,y=640)

Chkbtn9Select=Checkbutton(CoffinFrameRight,offvalue=0,onvalue=1,variable=Vienna,command=comm,bg='green')
Chkbtn9Select.place(x=20,y=80)

Chkbtn10Select=Checkbutton(CoffinFrameRight,offvalue=0,onvalue=1,variable=BronzeSendOff,command=comm,bg='green')
Chkbtn10Select.place(x=20,y=160)

Chkbtn11Select=Checkbutton(CoffinFrameRight,offvalue=0,onvalue=1,variable=SilverSendOff,command=comm,bg='green')
Chkbtn11Select.place(x=20,y=240)

Chkbtn12Select=Checkbutton(CoffinFrameRight,offvalue=0,onvalue=1,variable=GoldSendOff,command=comm,bg='green')
Chkbtn12Select.place(x=20,y=320)

Chkbtn13Select=Checkbutton(CoffinFrameRight,offvalue=0,onvalue=1,variable=Platinum,command=comm,bg='green')
Chkbtn13Select.place(x=20,y=400)

Chkbtn14Select=Checkbutton(CoffinFrameRight,offvalue=0,onvalue=1,variable=BourneD,command=comm,bg='green')
Chkbtn14Select.place(x=20,y=480)

Chkbtn15Select=Checkbutton(CoffinFrameRight,offvalue=0,onvalue=1,variable=BourneSupremacy,command=comm,bg='green')
Chkbtn15Select.place(x=20,y=560)

Chkbtn16Select=Checkbutton(CoffinFrameRight,offvalue=0,onvalue=1,variable=UnderCover,command=comm,bg='green')
Chkbtn16Select.place(x=20,y=640)


SubmitPackageButton=Button(CoffinFrameRight,text="Submit",bd=2,bg='Green',font=('times',14,'italic'),relief='ridge',fg='white')
SubmitPackageButton.place(x=600,y=700)

root.mainloop()
