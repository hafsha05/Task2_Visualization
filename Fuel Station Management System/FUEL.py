import mysql.connector
from tkinter import*
from tkcalendar import DateEntry
from time import*
from tkinter import messagebox
from PIL import Image,ImageTk

db=mysql.connector.connect(host="localhost",user="root",password="",db="petrol")
cursor=db.cursor()
window=Tk()
window.title("fuel")
img=Image.open("p.png")
img1=ImageTk.PhotoImage(img)
lbl=Label(window,image=img1)
lbl.pack()

l=Label(window,text='FUEL STATION MANAGEMENT SYSTEM',font=("bauhaus 93",40,"bold"))
l.place(x=200,y=50)

time=Label(window,text='Date',font=("comic sans ms",18,"bold"))
time.place(x=950,y=150)
time1=Label(window,font=("comic sans ms",18))
time1.place(x=1050,y=150)
mod=strftime(" %d/%b/%Y")
time1.config(text=mod)
d=DateEntry(window)

l1=Label(window,text='Today price',font=("comic sans ms",18,"bold"))
l1.place(x=950,y=200)
pri=Entry(window,width=10,font=("comic sans ms",18,"bold"))
pri.place(x=1100,y=200)

l2=Label(window,text='Emp Id',font=("Arial",18,"bold"))
l2.place(x=200,y=180)
b=Entry(window,width=20,font=("Arial",18,"bold"))
b.place(x=550,y=180)

l4=Label(window,text='Vehicle type',font=("Arial",18,"bold"))
l4.place(x=200,y=250)
sel=StringVar()
b2=Radiobutton(window,text="2 wheeler",width=14,font=("lucida console",14),value="Two wheeler",variable=sel)
b2.place(x=550,y=250)
b2.deselect()
b21=Radiobutton(window,text="3 wheeler",width=14,font=("lucida console",14),value="Three wheeler",variable=sel)
b21.place(x=550,y=300)
b21.deselect()
b22=Radiobutton(window,text="4 wheeler",width=14,font=("lucida console",14),value="Four wheeler",variable=sel)
b22.place(x=550,y=350)
b22.deselect()

l5=Label(window,text='litre',font=("Arial",18,"bold"))
l5.place(x=200,y=400)
b3=Entry(window,width=20,font=("Arial",18,"bold"))                                                                                                          
b3.place(x=550,y=400)

l6=Label(window,text='Bill Amount',font=("Arial",18,"bold"))
l6.place(x=200,y=450)
en=IntVar()
b4=Entry(window,width=20,textvariable=en,font=("Arial",18,"bold"))
b4.place(x=550,y=450)

def remove():
    b.delete(0,END)
    b3.delete(0,END)
    b4.delete(0,END)
    en.set(0)
def find():
    win=Tk()
    win.geometry("800x700")
    win.config(bg="#C1CDCD")
    inf=Label(win,text="Information",font=("lucida calligraphy",40),bg="#C1CDCD",fg="#9C661F")
    inf.place(x=200,y=10)
    ve=Label(win,text='Emp_Id',font=("Arial",18,"bold"),bg="#C1CDCD")
    ve.place(x=100,y=150)
    Id=Entry(win,width=18,font=("Arial",18,"bold"),bg="#C1CDCD")
    Id.place(x=300,y=150)
    def result():
        global c
        if Id.get()=="":
            c=Label(win,text="Please enter the Emp_Id",font=("Arial",14),bg="#C1CDCD",fg="red")
            c.place(x=300,y=200)
            r=Label(win,text='                                                                                                       ',font=("calibri",18),bg="#C1CDCD")
            r.place(x=100,y=230)
            r2=Label(win,text='                                                                                                     ',font=("calibri",18),bg="#C1CDCD")
            r2.place(x=100,y=280)
            r4=Label(win,text='                                                                                                    ',font=("calibri",18),bg="#C1CDCD")
            r4.place(x=100,y=330)
            r6=Label(win,text='                                                                                                    ',font=("calibri",18),bg="#C1CDCD")
            r6.place(x=100,y=380)
            r8=Label(win,text='                                                                                                      ',font=("calibri",18),bg="#C1CDCD")
            r8.place(x=100,y=430)
        else:    
            c=Label(win,text="                                                                                    ",font=("Arial",14),bg="#C1CDCD",fg="red")
            c.place(x=120,y=200)
            r=Label(win,text='Date :',font=("calibri",18),bg="#C1CDCD")
            r.place(x=100,y=230)
            r1=Label(win,font=("Arial",18,"bold"),bg="#C1CDCD",fg="brown")
            r1.place(x=400,y=230)
            r2=Label(win,text='Today Petrol Price :',font=("calibri",18),bg="#C1CDCD")
            r2.place(x=100,y=280)
            r3=Label(win,font=("Arial",18,"bold"),bg="#C1CDCD")
            r3.place(x=400,y=280)
            r4=Label(win,text='Emp_Id :',font=("calibri",18),bg="#C1CDCD")
            r4.place(x=100,y=330)
            r5=Label(win,font=("Arial",18,"bold"),bg="#C1CDCD")
            r5.place(x=400,y=330)
            r6=Label(win,text=' Total Litre :',font=("calibri",18),bg="#C1CDCD")
            r6.place(x=100,y=380)
            r7=Label(win,font=("Arial",18,"bold"),bg="#C1CDCD")
            r7.place(x=400,y=380)
            r8=Label(win,text='Total Collection Amount:',font=("calibri",18),bg="#C1CDCD")
            r8.place(x=100,y=430)
            r9=Label(win,font=("Arial",18,"bold"),bg="#C1CDCD")
            r9.place(x=400,y=430)
            
            val=int(Id.get()),
            sql=("select date_format(Date,'%d/%b/%Y'),price,empid,sum(litre),sum(total) from submit where empid=%s")
            cursor.execute(sql,val)
            record=cursor.fetchall()
            for i in record:
                r1.config(text=i[0])
                r3.config(text=i[1])
                r5.config(text=i[2])
                r7.config(text=i[3])
                r9.config(text=i[4])
                
    btn2=Button(win,text="Find",width=5,command=result,font=("times new roman",14,"bold"))
    btn2.place(x=600,y=150)
    win.mainloop()
    
def calculate():
    if b.get()=="" or b3.get()=="" or sel.get()=="" or pri.get()=="":
        messagebox.askquestion("error","please enter data")
    else:
        lit= int(b3.get())
        pay=lit*float(pri.get())
        en.set(pay)
def submit():
    if b.get()=="" or b3.get()=="" or sel.get()=="" or pri.get()=="":
        messagebox.askquestion("error","please enter data")
    else:
        sql=("INSERT INTO submit(Date,price,empid,vechicle_type,litre,total)values(%s,%s,%s,%s,%s,%s)")
        val=(d.get_date(),pri.get(),b.get(),sel.get(),b3.get(),b4.get())
        cursor.execute(sql,val)
        db.commit()
        messagebox.askquestion("successfull","Data was Stored")

bt=Button(window,text="Calculate",width=10,command=calculate,font=("times new roman",18,"bold"))
bt.place(x=150,y=600)
bt1=Button(window,text="Submit",width=10,command=submit,font=("times new roman",18,"bold"))
bt1.place(x=350,y=600)
bt2=Button(window,text="Remove",width=10,command=remove,font=("times new roman",18,"bold"))
bt2.place(x=550,y=600)
bt3=Button(window,text="Find",width=10,command=find,font=("times new roman",18,"bold"))
bt3.place(x=750,y=600)
window.mainloop()
