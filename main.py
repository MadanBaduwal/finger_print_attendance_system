from tkinter import *  
import tkinter as tk 
from tkinter import ttk, messagebox
import sqlite3
import cv2 
import camera 
from tkinter.ttk import *
from PIL import ImageTk,Image  
import tkinter.font as font

def create_db_and_table():
    global connection , TABLE_NAME
    global USER_ID,FLAG,STUDENT_NAME,STUDENT_SYMBOL_NUMBER,CITIZINSHIP_NO,CITIZINSHIP_ISSUE_DATE,CITIZINSHIP_ISSUE_DiSTRICT ,STUDENT_PHONE,GENDER
    connection = sqlite3.connect('management1.db')
    TABLE_NAME = "student_exam_attendance_table"
    USER_ID = "user_id"
    FLAG = "flag"
    STUDENT_NAME = "student_name"
    STUDENT_SYMBOL_NUMBER = "student symbol number"
    CITIZINSHIP_NO = "citizinship_no"
    CITIZINSHIP_ISSUE_DATE = "citizinship_issue_date"
    CITIZINSHIP_ISSUE_DiSTRICT = "citizinship_issue_district"
    STUDENT_PHONE = "student_phone"
    GENDER = "gender"

    connection.execute(" CREATE TABLE IF NOT EXISTS " + TABLE_NAME + " ( " + USER_ID +
                    " INTEGER, " + FLAG +"INTEGER," + 
                    STUDENT_NAME + " TEXT, " + STUDENT_SYMBOL_NUMBER + " TEXT, " + 
                    CITIZINSHIP_NO + " TEXT, " +CITIZINSHIP_ISSUE_DATE + " TEXT, " +CITIZINSHIP_ISSUE_DiSTRICT + " TEXT, " +
                    STUDENT_PHONE + " INTEGER ,"+GENDER+"TEXT);")

create_db_and_table()


def execute_query():


    userid = useridEntry.get()
    useridEntry.delete(0, tk.END)

    flag = flagEntry.get()
    flagEntry.delete(0, tk.END)

    studentname =  studentnameEntry.get()
    studentnameEntry.delete(0, tk.END)
    
    print(studentname)
    print(STUDENT_NAME)
    studentsymbolnumber =  studentsymbolnumberEntry.get()
    studentsymbolnumberEntry.delete(0, tk.END)
    
    citizeshipnumber =  citizinshipnumberEntry.get()
    citizinshipnumberEntry.delete(0, tk.END)
    
    citizinshipissuedate =  citizinshipissuedateEntry.get()
    citizinshipissuedateEntry.delete(0, tk.END)

    citizinshipissuedistrict =  citizinshipissuedistrictEntry.get()
    citizinshipissuedistrictEntry.delete(0, tk.END)


    studentphone = studentphoneEntry.get()
    studentphoneEntry.delete(0, tk.END)
    
    gen = var.get()

    if  gen == 1:
        gender = "MALE"
    elif gen == 2:
        gender = "FEMALE"
    

    connection.execute("INSERT INTO " + TABLE_NAME + " ( " + USER_ID + ", " + FLAG + ", " + STUDENT_NAME + ", " + STUDENT_SYMBOL_NUMBER + ", " + CITIZINSHIP_NO + "," + CITIZINSHIP_ISSUE_DATE + ", " + CITIZINSHIP_ISSUE_DiSTRICT + ", " + STUDENT_PHONE + ", " + GENDER + " ) VALUES ( '"
                       + userid + ", " + flag + ", " + studentname + ", " + studentsymbolnumber + ", " + citizeshipnumber + ", " + citizinshipissuedate + ", " + citizinshipissuedistrict + ", " + studentphone + ", " + gender + ");")
    connection.commit()
    messagebox.showinfo("Success", "Data Saved Successfully.")



def form_fill_up():
    
    global secondWindow
    global useridEntry,flagEntry,studentnameEntry,studentsymbolnumberEntry,citizinshipnumberEntry,citizinshipissuedateEntry,citizinshipissuedistrictEntry,studentphoneEntry,genderEntry
    global var
    root.destroy()
    form_fill_window = Tk()
    form_fill_window.title("Registered")
    
    # For Text
    appLabel = ttk.Label(form_fill_window, text="Student Management System")  
    #Create Panedwindow  
    panedwindow=ttk.Panedwindow(form_fill_window, orient=HORIZONTAL)  
    panedwindow.pack(fill=BOTH, expand=True)  
    #Create Frams  
    fram1=ttk.Frame(panedwindow,width=400,height=400, relief=SUNKEN)  
    fram2=ttk.Frame(panedwindow,width=400,height=400, relief=SUNKEN)  
    panedwindow.add(fram1, weight=4)  
    panedwindow.add(fram2, weight=4)


    
    # For Text
    appLabel = ttk.Label(fram1, text="Personal information")

    # Style for text
    appLabel.config(font=("Helvetica", 20))
    appLabel.grid(row=1, column=0, padx=(0,0),pady=(0,0))
    # For text 
    user_idlabel = tk.Label(fram1, text="User_id", width=30, anchor='w',font=("Verdana 10 bold",20))
    flaglabel = tk.Label(fram1, text="Flag", width=30, anchor='w',font=("Verdana 10 bold",20))
    studentnamelabel = tk.Label(fram1, text="Name", width=30, anchor='w',font=("Verdana 10 bold",20))
    studentsymbolnumberlabel = tk.Label(fram1, text="Symbol number", width=30, anchor='w',font=("Verdana 10 bold",20))
    citizinshipnumberLabel = tk.Label(fram1, text="Citizinship number", width=30, anchor='w',font=("Verdana 10 bold",20))
    citizinshipissuedateLabel = tk.Label(fram1, text="Citizinship issue date", width=30, anchor='w',font=("Verdana 10 bold",20))
    citizinshipissuedistrictrLabel = tk.Label(fram1, text="Citizinship issue district", width=30, anchor='w',font=("Verdana 10 bold",20))
    phonenumberlabel = tk.Label(fram1, text="Phone number", width=30, anchor='w',font=("Verdana 10 bold",20))


    genderlabel = tk.Label(fram1, text="Gender", width=30, anchor='w',font=("Verdana 10 bold",20))
    var = IntVar()
    Radiobutton(fram1, text="Male", variable=var, value=1).grid(row=10, column=2, padx=(0,150), pady = 0)
    Radiobutton(fram1, text="Female", variable=var, value=2).grid(row=10, column=2, padx=(150,10), pady = 0)

    

    #  Style for text
    user_idlabel.grid(row=2, column=0, padx=(40,0),pady=(10,10))
    flaglabel.grid(row=3, column=0, padx=(40,0),pady=(10,10))
    studentnamelabel.grid(row=4, column=0, padx=(40,0),pady=(10,10))
    studentsymbolnumberlabel.grid(row=5, column=0, padx=(40,0),pady=(10,10))
    citizinshipnumberLabel.grid(row=6, column=0, padx=(40,0),pady=(10,10))
    citizinshipissuedateLabel.grid(row=7, column=0, padx=(40,0),pady=(10,10))
    citizinshipissuedistrictrLabel.grid(row=8, column=0, padx=(40,0),pady=(10,10))
    phonenumberlabel.grid(row=9, column=0, padx=(40,0),pady=(10,10))
    genderlabel.grid(row=10, column=0, padx=(40,0),pady=(10,10))

    # Entry box
    useridEntry = tk.Entry(fram1, width = 30)
    flagEntry = tk.Entry(fram1, width = 30)
    studentnameEntry = tk.Entry(fram1, width = 30)
    studentsymbolnumberEntry = tk.Entry(fram1, width = 30)
    citizinshipnumberEntry = tk.Entry(fram1, width = 30)
    citizinshipissuedateEntry = tk.Entry(fram1, width = 30)
    citizinshipissuedistrictEntry = tk.Entry(fram1, width = 30)
    studentphoneEntry = tk.Entry(fram1, width = 30)

    # Style for entry box
    useridEntry.grid(row=2, column=2, padx=(0,10), pady=(0, 0))
    flagEntry.grid(row=3, column=2, padx=(0,10), pady = 0)
    studentnameEntry.grid(row=4, column=2, padx=(0,10), pady = 0)
    studentsymbolnumberEntry.grid(row=5, column=2, padx=(0,10), pady = 0)
    citizinshipnumberEntry.grid(row=6, column=2, padx=(0,10), pady=(0, 0))
    citizinshipissuedateEntry.grid(row=7, column=2, padx=(0,10), pady = 0)
    citizinshipissuedistrictEntry.grid(row=8, column=2, padx=(0,10), pady = 0)
    studentphoneEntry.grid(row=9, column=2, padx=(0,10), pady = 0)
    # For Text


    appLabel = ttk.Label(fram2, text="Bio data")
    # Style for text
    appLabel.config(font=("Helvetica", 20))
    appLabel.grid(row=1, column=0, padx=(0,0),pady=(0,0))

    button = tk.Button(fram2, text="Take picture", command=lambda :camera.main())
    button.grid(row=2, column=0, padx=(200,10), pady=(20,10))

    canvas = Canvas(fram2, width = 100, height = 100)  
    canvas.grid(row=4, column=1)
    img = ImageTk.PhotoImage(Image.open("/home/madan/Desktop/student_managment system/photos/1.jpg"))  
    canvas.create_image(20, 20, anchor=NW, image=img)
    

    # button = tk.Button(fram2, text="Thumb pic", command=lambda :execute_query())
    # button.grid(row=5, column=0, padx=(200,10), pady=(20,10))

    button = tk.Button(fram2, text="Submit", command=lambda :execute_query())
    button.grid(row=5, column=0, padx=(200,10), pady=(20,10))

    form_fill_window.mainloop()




def verify_student():

    root.destroy()
    verify_student_window = Tk()
    verify_student_window.title("verify_student")
    
    # For Text
    appLabel = ttk.Label(verify_student_window, text="Student Management System")  
    #Create Panedwindow  
    panedwindow=ttk.Panedwindow(verify_student_window, orient=HORIZONTAL)  
    panedwindow.pack(fill=BOTH, expand=True)  
    #Create Frams  
    fram1=ttk.Frame(panedwindow,width=400,height=400, relief=SUNKEN)  
    fram2=ttk.Frame(panedwindow,width=400,height=400, relief=SUNKEN)  
    panedwindow.add(fram1, weight=4)  
    panedwindow.add(fram2, weight=4)



    
    # For Text
    appLabel = ttk.Label(fram1, text="Personal information")

    # Style for text
    appLabel.config(font=("Helvetica", 20))
    appLabel.grid(row=1, column=0, padx=(0,0),pady=(0,0))
    # For text 
    user_idlabel = tk.Label(fram1, text="User_id", width=30, anchor='w',font=("Verdana 10 bold",20))
    flaglabel = tk.Label(fram1, text="Flag", width=30, anchor='w',font=("Verdana 10 bold",20))
    studentnamelabel = tk.Label(fram1, text="Name", width=30, anchor='w',font=("Verdana 10 bold",20))
    studentsymbolnumberlabel = tk.Label(fram1, text="Symbol number", width=30, anchor='w',font=("Verdana 10 bold",20))
    citizinshipnumberLabel = tk.Label(fram1, text="Citizinship number", width=30, anchor='w',font=("Verdana 10 bold",20))
    citizinshipissuedistrictrLabel = tk.Label(fram1, text="Citizinship issue district", width=30, anchor='w',font=("Verdana 10 bold",20))
    genderlabel = tk.Label(fram1, text="Gender", width=30, anchor='w',font=("Verdana 10 bold",20))
    
    # genderlabel = Label(secondWindow, text="Gender", width=30, anchor='w',font=("Sylfaen", 12))
    var = IntVar()
    Radiobutton(fram1, text="Male", variable=var, value=1).grid(row=9, column=2, padx=(0,150), pady = 0)
    Radiobutton(fram1, text="Female", variable=var, value=2).grid(row=9, column=2, padx=(150,10), pady = 0)


    phonenumberlabel = tk.Label(fram1, text="Phone number", width=30, anchor='w',font=("Verdana 10 bold",20))
    

    #  Style for text
    user_idlabel.grid(row=2, column=0, padx=(40,0),pady=(10,10))
    flaglabel.grid(row=3, column=0, padx=(40,0),pady=(10,10))
    studentnamelabel.grid(row=4, column=0, padx=(40,0),pady=(10,10))
    studentsymbolnumberlabel.grid(row=5, column=0, padx=(40,0),pady=(10,10))
    citizinshipnumberLabel.grid(row=6, column=0, padx=(40,0),pady=(10,10))
    citizinshipissuedistrictrLabel.grid(row=7, column=0, padx=(40,0),pady=(10,10))
    phonenumberlabel.grid(row=8, column=0, padx=(40,0),pady=(10,10))
    genderlabel.grid(row=9, column=0, padx=(40,0),pady=(10,10))

    # Entry box
    useridEntry = tk.Entry(fram1, width = 30)
    flagEntry = tk.Entry(fram1, width = 30)
    studentnameEntry = tk.Entry(fram1, width = 30)
    studentsymbolnumberEntry = tk.Entry(fram1, width = 30)
    citizinshipnumberEntry = tk.Entry(fram1, width = 30)
    citizinshipissuedateEntry = tk.Entry(fram1, width = 30)
    studentphoneEntry = tk.Entry(fram1, width = 30)

    # Style for entry box
    useridEntry.grid(row=2, column=2, padx=(0,10), pady=(0, 0))
    flagEntry.grid(row=3, column=2, padx=(0,10), pady = 0)
    studentnameEntry.grid(row=4, column=2, padx=(0,10), pady = 0)
    studentsymbolnumberEntry.grid(row=5, column=2, padx=(0,10), pady = 0)
    citizinshipnumberEntry.grid(row=6, column=2, padx=(0,10), pady=(0, 0))
    citizinshipissuedateEntry.grid(row=7, column=2, padx=(0,10), pady = 0)
    #genderEntry.grid(row=8, column=2, padx=(0,10), pady = 0)
    studentphoneEntry.grid(row=8, column=2, padx=(0,10), pady = 0)
    # For Text


    appLabel = ttk.Label(fram2, text="Bio data")
    # Style for text
    appLabel.config(font=("Helvetica", 20))
    appLabel.grid(row=1, column=0, padx=(0,0),pady=(0,0))

    button = tk.Button(fram2, text="Take picture", command=lambda :camera.main())
    button.grid(row=2, column=0, padx=(200,10), pady=(20,10))

    canvas = Canvas(fram2, width = 100, height = 100)  
    canvas.grid(row=4, column=1)
    img = ImageTk.PhotoImage(Image.open("/home/madan/Desktop/student_managment system/photos/1.jpg"))  
    canvas.create_image(20, 20, anchor=NW, image=img)
    

    button = tk.Button(fram2, text="Thumb pic", command=lambda :execute_query())
    button.grid(row=5, column=0, padx=(200,10), pady=(20,10))

    verify_student_window.mainloop()


def main_window():
    global root
    root = tk.Tk()
    root.title("Student exam attendance Management system")

    # For Text 
    appLabel = tk.Label(root, text="Student exam attendance Management system", fg="#0a0329")
    # For text style
    appLabel.config(font=("Helvetica", 30))
    appLabel.grid(row=0, columnspan=2, padx=(40,0),pady=(0,0))
    
    # For responsible
    n_rows =1
    n_columns =2
    for i in range(n_rows):
        root.grid_rowconfigure(i,  weight =1)
    for i in range(n_columns):
        root.grid_columnconfigure(i,  weight =1)
    
    myFont = font.Font(family='Helvetica', size=10, weight='bold')


    button = tk.Button(root, text="Form fill up",height=10,width=50, command=lambda :form_fill_up())
    button.grid(row=1, column=0, padx=(10,10),pady=(5,150))
    button['font'] = myFont

    button = tk.Button(root, text="Verify student",height=10,width=50, command=lambda :verify_student())
    button.grid(row=1, column=1, padx=(10,10),pady=(5,150))
    button['font'] = myFont

    button = tk.Button(root, text="Display all student",height=10,width=50,command=lambda :display_all_student())
    button.grid(row=1, column=2, padx=(10,10),pady=(5,150))
    button['font'] = myFont
    root.mainloop()
main_window()


