import math
import tkinter.messagebox
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql

class Students:
    def __init__(self, window):
        self.window = window
        self.window.title("სტუდენტთა ქულათა სისტემა")
        self.window.geometry('1250x700+50+0')  # width x height + x position + y position
        self.window.resizable(False, False)
        titlelabel = Label(self.window, text="სტუდენტთა ქულათა სისტემა", font=('Helvetica', 30, 'bold'), bg='#864879',
                           fg='black', bd=5, relief=GROOVE)
        titlelabel.pack(side=TOP, fill=X)

        # frame1 - გამოიყენება სტუდენტის მონაცემების განსასაზღვრად მაგ: სტუდენტის ID, სახელი, გვარი, ჯფუფის ნომერი
        # მისი საგნები და ასევე მისი ქულები.
        frame1 = Frame(self.window, bg="#219F94", relief=RIDGE, bd=3)
        frame1.place(x=410, y=58, width=830, height=350)

        # frame2 გამოიყენება სტუდენტის შედეგების საჩვენებლად.
        frame2 = Frame(self.window, relief=RIDGE, bd=3)
        frame2.place(x=10, y=58, width=400, height=400)

        # frame3 გამოიყენება ღილაკების დასასმელად.
        frame3 = Frame(self.window, bg='#C8F2EF', relief=RIDGE, bd=2)
        frame3.place(x=410, y=410, width=830, height=40)

        # frame4 გამოიყენება მონაცემთა ბაზის გამოსატანად
        frame4 = Frame(self.window, relief=RIDGE, bd=3)
        frame4.place(x=10, y=450, width=1230, height=350)

        # ---------------------------------Entry - ის ცვლადები---------------------------------
        self.student_id = StringVar()
        self.saxeli = StringVar()
        self.gvari = StringVar()
        self.kursis_saxeli = StringVar()
        self.qulata_jami = IntVar()
        self.procenti = StringVar()
        self.statusi = StringVar()

        self.python = IntVar()
        self.csharp = IntVar()
        self.cplusplus = IntVar()
        self.java = IntVar()
        self.javascript = IntVar()
        self.inf_usf = IntVar()
        self.qselebi = IntVar()

        # ---------------------------------ღილაკების ლოგიკა--------------------------------------

        # ---------------------------------ინფორმაცია სტუდენტზე---------------------------------
        frame1_label = Label(frame1, text="სტუდენტის ID:", bg="#219F94", font=('cooper black', 15, 'bold'))
        frame1_label.grid(row=0, column=0, padx=0, pady=7, sticky='w')
        frame1_entry = Entry(frame1, bd=5, relief=RIDGE, width=20, textvariable=self.student_id)
        frame1_entry.grid(row=0, column=1, padx=0, pady=5)
        frame1_label1 = Label(frame1, text="სახელი:", bg="#219F94", font=('cooper black', 15, 'bold'))
        frame1_label1.grid(row=1, column=0, padx=0, pady=7, sticky='w')
        frame1_entry1 = Entry(frame1, bd=5, relief=RIDGE, width=20, textvariable=self.saxeli)
        frame1_entry1.grid(row=1, column=1, padx=0, pady=5)
        frame1_label2 = Label(frame1, text="გვარი:", bg="#219F94", font=('cooper black', 15, 'bold'))
        frame1_label2.grid(row=2, column=0, padx=0, pady=7, sticky='w')
        frame1_entry2 = Entry(frame1, bd=5, relief=RIDGE, width=20, textvariable=self.gvari)
        frame1_entry2.grid(row=2, column=1, padx=0, pady=5)
        frame1_label3 = Label(frame1, text="მიმართულება:", bg="#219F94", font=('cooper black', 15, 'bold'))
        frame1_label3.grid(row=3, column=0, padx=0, pady=7, sticky='w')
        frame1_combobox = ttk.Combobox(frame1, font=('cooper black', 12, 'bold'), width=25,
                                           textvariable=self.kursis_saxeli)
        frame1_combobox['values'] = (
        'Software Engieniring', 'Computer Engienering', "Artifical Intelligent")
        frame1_combobox.grid(row=3, column=1, padx=5, pady=5)
        frame1_label4 = Label(frame1, text="ქულათა ჯამი:", bg="#219F94", font=('cooper black', 15, 'bold'))
        frame1_label4.grid(row=4, column=0, padx=0, pady=7, sticky='w')
        frame1_entry4 = Entry(frame1, bd=5, relief=RIDGE, width=20, state = DISABLED, textvariable=self.qulata_jami)
        frame1_entry4.grid(row=4, column=1, padx=0, pady=5)
        frame1_label5 = Label(frame1, text="პროცენტი:", bg="#219F94", font=('cooper black', 15, 'bold'))
        frame1_label5.grid(row=5, column=0, padx=0, pady=6, sticky='w')
        frame1_entry5 = Entry(frame1, bd=5, relief=RIDGE, width=20, state = DISABLED, textvariable=self.procenti)
        frame1_entry5.grid(row=5, column=1, padx=0, pady=5)
        frame1_label6 = Label(frame1, text="სტატუსი:", bg="#219F94", font=('cooper black', 15, 'bold'))
        frame1_label6.grid(row=6, column=0, padx=0, pady=6, sticky='w')
        frame1_entry6 = Entry(frame1, bd=5, relief=RIDGE, width=20, state=DISABLED, textvariable=self.statusi)
        frame1_entry6.grid(row=6, column=1, padx=0, pady=5)
            # ---------------------------------ინფორმაცია საგნებზე---------------------------------
        frame1_label6 = Label(frame1, text="Python :", bg="#219F94", font=('cooper black', 15, 'bold'))
        frame1_label6.grid(row=0, column=2, padx=40, pady=10, sticky='w')
        frame1_entry6 = Entry(frame1, bd=5, relief=RIDGE, width=20, textvariable=self.python)
        frame1_entry6.grid(row=0, column=3, padx=10, pady=5)
        frame1_label7 = Label(frame1, text="C#:", bg="#219F94", font=('cooper black', 15, 'bold'))
        frame1_label7.grid(row=1, column=2, padx=40, pady=10, sticky='w')
        frame1_entry7 = Entry(frame1, bd=5, relief=RIDGE, width=20, textvariable=self.csharp)
        frame1_entry7.grid(row=1, column=3, padx=10, pady=5)
        frame1_label8 = Label(frame1, text="Java:", bg="#219F94", font=('cooper black', 15, 'bold'))
        frame1_label8.grid(row=2, column=2, padx=40, pady=10, sticky='w')
        frame1_entry8 = Entry(frame1, bd=5, relief=RIDGE, width=20, textvariable=self.java)
        frame1_entry8.grid(row=2, column=3, padx=10, pady=5)
        frame1_label9 = Label(frame1, text="JavaScript:", bg="#219F94", font=('cooper black', 15, 'bold'))
        frame1_label9.grid(row=3, column=2, padx=40, pady=10, sticky='w')
        frame1_entry9 = Entry(frame1, bd=5, relief=RIDGE, width=20, textvariable=self.javascript)
        frame1_entry9.grid(row=3, column=3, padx=10, pady=5)
        frame1_label10 = Label(frame1, text="C++:", bg="#219F94", font=('cooper black', 15, 'bold'))
        frame1_label10.grid(row=4, column=2, padx=40, pady=6, sticky='w')
        frame1_entry10 = Entry(frame1, bd=5, relief=RIDGE, width=20, textvariable=self.cplusplus)
        frame1_entry10.grid(row=4, column=3, padx=10, pady=5)
        frame1_label11 = Label(frame1, text="კომპ.ქსელები:", bg="#219F94", font=('cooper black', 15, 'bold'))
        frame1_label11.grid(row=5, column=2, padx=40, pady=6, sticky='w')
        frame1_entry11 = Entry(frame1, bd=5, relief=RIDGE, width=20, textvariable=self.qselebi)
        frame1_entry11.grid(row=5, column=3, padx=10, pady=5)
        frame1_label12 = Label(frame1, text="ინფ. უსაფ:", bg="#219F94", font=('cooper black', 15, 'bold'))
        frame1_label12.grid(row=6, column=2, padx=40, pady=10, sticky='w')
        frame1_entry12 = Entry(frame1, bd=5, relief=RIDGE, width=20, textvariable=self.inf_usf)
        frame1_entry12.grid(row=6, column=3, padx=10, pady=5)
            # --------------------------------
            # frame2 - ის კომპონენტებზე მუშაობა
            # --------------------------------
        frame2_label = Label(frame2, text="სტუდენტის შედეგები", font='arial 15 bold', fg='black', relief=GROOVE, bd=5)
        frame2_label.pack(side=TOP, fill=X)
        frame2_scroll = Scrollbar(frame2, orient=VERTICAL)
        frame2_scroll.pack(side=RIGHT, fill=Y)
        self.textarea = Text(frame2, font='arial 12 bold', yscrollcommand=frame2_scroll)
        self.textarea.pack(fill=BOTH)
        frame2_scroll.config(command=self.textarea.yview)
            # --------------------------------
            # frame3 - ის კომპონენტებზე მუშაობა
            # --------------------------------
        frame3_button = Button(frame3, text='შედეგის შექმნა', font='arial 11 bold', bg="#D1D1D1", fg="black",command=self.bazashidamateba)
        frame3_button.grid(row=0, column=0, padx=40)
        frame3_button1 = Button(frame3, text='შედეგის განახლება', font='arial 11 bold', bg="#D1D1D1", fg="black")
        frame3_button1.grid(row=0, column=1)
        frame3_button2 = Button(frame3, text='გასუფთავება', font='arial 11 bold', bg="#D1D1D1", fg="black",command=self.gasuftaveba)
        frame3_button2.grid(row=0, column=2, padx=40)
        frame3_button3 = Button(frame3, text='შედეგის წაშლა', font='arial 11 bold', bg="#D1D1D1", fg="black", command=self.delete)
        frame3_button3.grid(row=0, column=3)
        frame3_button3 = Button(frame3, text='დახურვა', font='arial 11 bold', bg="#D1D1D1", fg="black", command=self.daxurva)
        frame3_button3.grid(row=0, column=4, padx = 40)
        # --------------------------------
        # frame4 - ის კომპონენტებზე მუშაობა
        # --------------------------------
        frame3_scroll = Scrollbar(frame4, orient=VERTICAL)
        self.studentis_cxrili = ttk.Treeview(frame4, columns=(
            'სტუდენტის ID', 'კურსის სახელი',
            'Python', 'C#', 'Java', 'JavaScript',"C++", 'ინფ. უსაფ',
            "კომპ.ქსელები",'ქულათა ჯამი','პროცენტი',"სტატუსი"))
        frame3_scroll.pack(side=RIGHT, fill=Y)
        frame3_scroll.config(command=self.studentis_cxrili.yview)
        self.studentis_cxrili.heading('სტუდენტის ID', text='სტუდენტის ID')
        self.studentis_cxrili.heading('კურსის სახელი', text='კურსის სახელი')
        self.studentis_cxrili.heading('Python', text='Python')
        self.studentis_cxrili.heading('C#', text='C#')
        self.studentis_cxrili.heading('Java', text='Java')
        self.studentis_cxrili.heading('JavaScript', text='JavaScript')
        self.studentis_cxrili.heading('C++', text='C++')
        self.studentis_cxrili.heading('ინფ. უსაფ', text='ინფ. უსაფ')
        self.studentis_cxrili.heading('კომპ.ქსელები', text='კომპ.ქსელები')
        self.studentis_cxrili.heading('სტატუსი', text='სტატუსი')
        self.studentis_cxrili.heading('ქულათა ჯამი', text='ქულათა ჯამი')
        self.studentis_cxrili.heading('პროცენტი', text='პროცენტი')
        self.studentis_cxrili['show'] = 'headings'
        self.studentis_cxrili.column('სტუდენტის ID', width=100)
        self.studentis_cxrili.column('კურსის სახელი', width=105)
        self.studentis_cxrili.column('ქულათა ჯამი', width=100)
        self.studentis_cxrili.column('პროცენტი', width=100)
        self.studentis_cxrili.column('Python', width=100)
        self.studentis_cxrili.column('კომპ.ქსელები', width=100)
        self.studentis_cxrili.column('C#', width=100)
        self.studentis_cxrili.column('Java', width=100)
        self.studentis_cxrili.column('JavaScript', width=100)
        self.studentis_cxrili.column('ინფ. უსაფ', width=100)
        self.studentis_cxrili.column('C++', width=100)
        self.studentis_cxrili.column('სტატუსი', width=100)
        self.studentis_cxrili.pack()
        self.studentis_cxrili.bind("<ButtonRelease-1>",self.ganaxleba)
        self.DataGamotana()

    def jami(self):
        jami = (self.python.get() +
                self.csharp.get() +
                self.java.get() +
                self.javascript.get() +
                self.cplusplus.get() +
                self.inf_usf.get() +
                self.qselebi.get())
        procenti = (jami / 700) * 100
        procenti = math.floor(procenti)
        self.qulata_jami.set(str(jami))
        self.procenti.set(str(procenti) + "%")
        if self.python.get() >= 51:
            self.statusi.set("Pass")
        else:
            self.statusi.set("Fail In Python")

    def bazashidamateba(self):
        if self.student_id.get() == "" or self.kursis_saxeli.get() == "" or self.python.get() == "" or self.csharp.get() == "" or self.csharp.get() == "" or self.java.get() == "" or self.javascript == "" or self.cplusplus.get() == "" or self.qselebi == "" or self.inf_usf == "":
            tkinter.messagebox.showerror("Error", "გთხოვთ შეავსოთ ყველა ველი.")
        else:
            self.shedegi()
            self.jami()
            con = pymysql.connect(host='localhost', user='root', password='', database='students')
            cur = con.cursor()
            cur.execute("Select * from students")
            rows = cur.fetchall()
            try:
                for row in rows:
                    if row[0]==self.student_id.get():
                        messagebox.showerror('Error', "დაფიქსირდა ერთნაირი ID !")
                cur.execute("Insert into students values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                    self.student_id.get(),
                    self.kursis_saxeli.get(),
                    self.python.get(),
                    self.csharp.get(),
                    self.java.get(),
                    self.javascript.get(),
                    self.cplusplus.get(),
                    self.inf_usf.get(),
                    self.qselebi.get(),
                    self.qulata_jami.get(),
                    self.procenti.get(),
                    self.statusi.get(),
                    self.saxeli.get(),
                    self.gvari.get()
                ))
                con.commit()
                self.DataGamotana()
                con.close()
                self.gasuftaveba()
            except:
                messagebox.showerror('Error', "დაფიქსირდა ერთნაირი ID !")

    def daxurva(self):
        daxurva = tkinter.messagebox.askyesno("გასვლა გსურთ?", "გრურთ პროგრამის დახურვა ?")
        if daxurva > 0:
            self.window.destroy()
            return

    def gasuftaveba(self):
        self.student_id.set("")
        self.saxeli.set("")
        self.gvari.set("")
        self.kursis_saxeli.set("")
        self.qulata_jami.set("")
        self.procenti.set("")
        self.statusi.set("")
        self.python.set("")
        self.csharp.set("")
        self.cplusplus.set("")
        self.java.set("")
        self.javascript.set("")
        self.inf_usf.set("")
        self.qselebi.set("")

    def cleartextarea(self):
        self.textarea.delete("1.0", END)


    def DataGamotana(self):
        con = pymysql.connect(host='localhost', user='root', password='', database='students')
        cur = con.cursor()
        cur.execute("Select * from students")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.studentis_cxrili.delete(*self.studentis_cxrili.get_children())
            for row in rows:
                self.studentis_cxrili.insert('',END,values=row)
            con.commit()
        con.close()

    def shedegi(self):
        self.textarea.insert(1.0,END)
        self.textarea.insert(END, f"\n სტუდენტის ID: \t\t {self.student_id.get()}")
        self.textarea.insert(END, f"\n სტუდენტის სახელი: \t\t {self.saxeli.get()}")
        self.textarea.insert(END, f"\n სტუდენტი: \t\t {self.saxeli.get()} {self.gvari.get()}")
        self.textarea.insert(END, f"\n კურსის სახელი: \t\t {self.kursis_saxeli.get()}")
        self.textarea.insert(END, f"\n Python: \t\t {self.python.get()}")
        self.textarea.insert(END, f"\n C#: \t\t {self.csharp.get()}")
        self.textarea.insert(END, f"\n Java: \t\t {self.java.get()}")
        self.textarea.insert(END, f"\n JavaScript: \t\t {self.javascript.get()}")
        self.textarea.insert(END, f"\n C++: \t\t {self.cplusplus.get()}")
        self.textarea.insert(END, f"\n ინფორმაციული უსაფრთხოება: \t\t {self.inf_usf.get()}")
        self.textarea.insert(END, f"\n ქსელები: \t\t {self.qselebi.get()}")
        self.textarea.insert(END, f"\n ქულათა ჯამი: \t\t {self.qulata_jami.get()}")
        self.textarea.insert(END, f"\n ქულათა პროცენტი: \t\t {self.procenti.get()}")
        self.textarea.insert(END, f"\n სტატუსი: \t\t {self.statusi.get()}")

    def delete(self):
        if self.student_id.get() == "":
            messagebox.showerror("Error", 'გთხოვთ შემოიტანოთ წასაშლელი Student-ის ID')
        else:
            con = pymysql.connect(host='localhost', user='root', password='', database='students')
            cur = con.cursor()
            cur.execute("delete from students where სტუდენტის_ID=%s",self.student_id.get())
            con.commit()
            con.close()
            self.DataGamotana()
    def ganaxleba(self,ev):
        ganaxleba = self.studentis_cxrili.focus()
        content = self.studentis_cxrili.item(ganaxleba)
        row = content['values']
        self.student_id.set(row[0])
        self.kursis_saxeli.set(row[1])
        self.python.set(row[2])
        self.csharp.set(row[3])
        self.java.set(row[4])
        self.cplusplus.set(row[5])
        self.javascript.set(row[6])
        self.inf_usf.set(row[7])
        self.qselebi.set(row[8])
        self.qulata_jami.set(row[9])
        self.procenti.set(row[10])
        self.statusi.set(row[11])
        self.saxeli.set(row[12])
        self.gvari.set(row[13])




window=Tk()
student = Students(window)
window.mainloop()