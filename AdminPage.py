from tkinter import messagebox
from DefaultPage import *
class AdminPage(DefaultPage):
    def __init__(self,root,admin_details):
        super().__init__(root)
        self.root.state('zoomed')
        self.details = admin_details
        self.dct_IntVar={}
        self.m = Message(self.panel, width=850, font=("Bernard MT Condensed",25,"bold underline"),text=f"Welcome {self.details[1]}", bg="#b5caeb", relief=SOLID, borderwidth=2)
        self.m.place(x=50, y=100)
        self.add_buttons()

    def add_buttons(self):
        self.pending_button = DefaultPage.CreamButton(self.f, "CHECK PENDING LENDS", self.view_pending_lends)
        self.pending_button.place(x=50, y=250)
        self.check_completed_button = DefaultPage.CreamButton(self.f, "CHECK COMPLETED LENDS", self.check_completed_lends)
        self.check_completed_button.place(x=50, y=325)
        self.seeBooks = DefaultPage.CreamButton(self.f,"CHECK AVAILABLE BOOKS",self.see_books)
        self.seeBooks.place(x=50,y=400)
        self.seeStudents = DefaultPage.CreamButton(self.f,"SEE ALL STUDENT DETAILS",self.see_students)
        self.seeStudents.place(x=50,y=475)
        self.addBk = DefaultPage.CreamButton(self.f, "ADD BOOK", self.add_books, bg='#d1a924', width=20)
        self.addBk.place(x=350, y=175)
        self.updateBk = DefaultPage.CreamButton(self.f, "UPDATE/DELETE BOOK", lambda :self.ask_update_or_delete('book'), bg='#d1a924', width=20)
        self.updateBk.place(x=600, y=175)
        self.addStud = DefaultPage.CreamButton(self.f, "ADD STUDENT", self.signup_form, bg='#d1a924', width=20)
        self.addStud.place(x=850, y=175)
        self.updateStud = DefaultPage.CreamButton(self.f, "UPDATE/DELETE STUD", lambda :self.ask_update_or_delete('student'), bg='#d1a924', width=20)
        self.updateStud.place(x=1100, y=175)
        self.logout = DefaultPage.CreamButton(self.f, "LOGOUT", self.admin_logout, width=10, bg='#f3f5cb')
        self.logout.place(x=1200, y=20)

    def view_pending_lends(self):
        query = """select l.OrderId,s.StudentId,s.SName,b.BName,b.Author,b.Category,l.BDate
                       from student s
                       join lending l
                       join book b
                       on b.BookId=l.BId
                       on s.StudentId=l.SId
                       where l.IsReturned=0;"""
        result = DefaultPage.DatabaseHelper.get_all_data(query)
        self.menu_frame = DefaultPage.SimpleTable(self.f, rows=len(result), columns=len(result[0]), height=450, width=680,colour="#f06787")
        self.menu_frame.place(x=500, y=250)
        self.menu_frame.grid_propagate(0)

        for i in range(1, len(result)):
            self.dct_IntVar[result[i][0]] = IntVar()

        for i in range(len(result)):
            for j in range(len(result[0])):
                if i == 0:
                    self.menu_frame.set(row=i, column=j, value=result[i][j], bg="#c9083f", fg="white")
                elif j == 0 and i != 0:
                    self.menu_frame.set(row=i, column=j, value=result[i][j])
                elif j == 2 :
                    self.menu_frame.set(row=i, column=j, value=result[i][j], width=12)
                elif j == 3 :
                    self.menu_frame.set(row=i, column=j, value=result[i][j], width=32)
                elif j == 4 :
                    self.menu_frame.set(row=i, column=j, value=result[i][j], width=18)
                elif j == 6 :
                    self.menu_frame.set(row=i, column=j, value=result[i][j], width=12)
                else:
                    self.menu_frame.set(row=i, column=j, value=result[i][j])

    def check_completed_lends(self):
            query = """select l.OrderId,l.SId,s.SName,b.BName,b.Author,l.BDate,l.Fine
                        from  book b join student s join lending l 
                        on s.StudentId=l.SId
                        on b.BookId=l.BId
                        where l.IsReturned=1;"""

            result = DefaultPage.DatabaseHelper.get_all_data(query)
            self.menu_completed_lends = DefaultPage.SimpleTable(self.f, rows=len(result), columns=len(result[0]), height=450,
                                                    width=680,colour="#bbdbab")
            self.menu_completed_lends.place(x=500, y=250)
            self.menu_completed_lends.grid_propagate(0)

            for i in range(len(result)):
                for j in range(len(result[0])):
                    if i == 0:
                        self.menu_completed_lends.set(row=i, column=j, value=result[i][j], bg="#0aa80c", fg="white")
                    elif j == 0 and i != 0:
                        self.menu_completed_lends.set(row=i, column=j, value=result[i][j])
                    elif j == 2:
                        self.menu_completed_lends.set(row=i, column=j, value=result[i][j], width=12)
                    elif j == 3:
                        self.menu_completed_lends.set(row=i, column=j, value=result[i][j], width=32)
                    elif j == 4:
                        self.menu_completed_lends.set(row=i, column=j, value=result[i][j], width=18)
                    elif j == 5:
                        self.menu_completed_lends.set(row=i, column=j, value=result[i][j], width=12)
                    elif j == 6:
                        self.menu_completed_lends.set(row=i, column=j, value=result[i][j], width=12)
                    else:
                        self.menu_completed_lends.set(row=i, column=j, value=result[i][j])

    def signup_form(self):
        student_signup = Toplevel()
        student_signup.title('Sign-up')
        f = Frame(student_signup, height=250, width=400, bg="gold")
        l1 = Label(f, width=20, text="Enter Student name: ")
        l2 = Label(f, width=20, text="Enter Class: ")
        l3 = Label(f, width=20, text="Enter password: ")
        l4 = Label(f, width=50,text="Enter the details below to add a Student",bg="black",fg="white")
        self.e_studname = Entry(f, width=30, fg='black', bg='white')
        self.e_studname.focus_set()
        self.e_class = Entry(f, width=30, fg='black', bg='white')
        self.e_password = Entry(f, width=30, fg='black', bg='white', show='*')
        l1.grid(row=2, column=1, padx=10, pady=10)
        l2.grid(row=3, column=1, padx=10, pady=10)
        l3.grid(row=4, column=1, padx=10, pady=10)
        l4.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
        self.e_studname.grid(row=2, column=2, padx=10, pady=10)
        self.e_password.grid(row=4, column=2, padx=10, pady=10)
        self.e_class.grid(row=3, column=2, padx=10, pady=10)
        b1 = Button(f, text="Submit", height=2, width=10, command=lambda: self.add_student(student_signup))
        b1.grid(row=5, column=2, padx=10, sticky='w')
        f.pack()
        f.grid_propagate(0)

    def add_student(self,top_level):
        name = self.e_studname.get()
        password = self.e_password.get()
        class_ = self.e_class.get()
        if self.e_studname.get() == '' or self.e_password.get() == '' or self.e_class.get() == '':
            messagebox.showwarning('Incomplete Data','Please Enter all the details')
        else:
            params=(password,name,class_)
            query="insert into project.student(Passwd,SName,Class) values('%s','%s','%s')"
            DefaultPage.DatabaseHelper.execute_query(query,params)
            messagebox.showinfo('New Student Registration',"Student Registered successfully")
        top_level.destroy()

    def add_books(self):
        login_window1 = Toplevel()
        login_window1.title('Book')
        f2 = Frame(login_window1, height=260, width=400, bg='gold')
        lab = Label(f2, width=50, text="Enter below details to add book", bg="black", fg="white")
        lab.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
        Bname = Label(f2, width=20, text="Enter Bookname: ")
        self.e_Bname = Entry(f2, width=30, fg='black', bg='white')
        self.e_Authorname = Entry(f2, width=30, fg='black', bg='white')
        Authorname = Label(f2, width=20, text="Enter Author Name: ")
        Category = Label(f2, width=20, text="Enter Category: ")
        self.e_Category = Entry(f2, width=30, fg='black', bg='white')
        Bname.grid(row=2, column=1, padx=10, pady=10)
        self.e_Bname.grid(row=2, column=2, padx=10, pady=10)
        self.e_Authorname.grid(row=3, column=2, padx=10, pady=10)
        Authorname.grid(row=3, column=1, padx=10, pady=10)
        Category.grid(row=4, column=1, padx=10, pady=10)
        self.e_Category.grid(row=4, column=2, padx=10, pady=10)
        No_of_copies = Label(f2, width=20, text="Enter Available Copies ")
        self.e_Availablecopies = Entry(f2, width=30, fg='black', bg='white')
        No_of_copies.grid(row=5, column=1, padx=10, pady=10)
        self.e_Availablecopies.grid(row=5, column=2, padx=10, pady=10)
        b1 = Button(f2, text="Add book", height=2, width=10, command=lambda: self.Newbk(login_window1))
        b1.grid(row=6, column=2, columnspan=1, padx=10, sticky=W)
        f2.pack()
        f2.grid_propagate(0)

    def Newbk(self, top_level):
        bName = self.e_Bname.get()
        Author = self.e_Authorname.get()
        category = self.e_Category.get()
        copies = self.e_Availablecopies.get()

        if self.e_Bname.get() == '' or self.e_Authorname.get() == '' or self.e_Category.get() == '' or self.e_Availablecopies.get() == '':
            messagebox.showwarning('Incomplete Data', 'Please Enter all the details')
        else:
            params = (bName, Author, category, copies)
            query = "Insert into project.book(BName,Author,Category, AvailableCopies) Values('%s','%s','%s', '%s')"
            DefaultPage.DatabaseHelper.execute_query(query, params)
            messagebox.showinfo('New Book Entry', 'Book added Successfully')
        top_level.destroy()

    def ask_update_or_delete(self, to_whom):
        update_delete = Toplevel()
        update_delete.title('Update OR Delete')
        self.fr = Frame(update_delete, width=250, height=300, bg='brown')
        update_button = Button(self.fr, bg='#f3f5cb', fg='black', width=10, height=2, text='Update', command=lambda: self.get_record(to_whom, 'update', update_delete))
        update_button.place(x=65, y=25)
        delete_button = Button(self.fr, bg='#f3f5cb', fg='black', width=10, height=2, text='Delete', command=lambda: self.get_record(to_whom, 'delete', update_delete))
        delete_button.place(x=65, y=100)
        self.fr.pack()

    def get_record(self, to_whom, event, update_delete):
        if event == 'update':
            lab = Label(self.fr, text='Enter the id: ')
            self.record_entry = Entry(self.fr, width=20)
            lab.place(x=20, y=175)
            self.record_entry.place(x=100, y=175)
            submit_but = Button(self.fr, bg='#f3f5cb', fg='black', width=10, height=1, text='SUBMIT', command=lambda: self.update_record(to_whom, self.record_entry, update_delete))
            submit_but.place(x=75, y=225)
        else:
            lab = Label(self.fr, text='Enter the id: ')
            self.record_entry = Entry(self.fr, width=20)
            lab.place(x=20, y=175)
            self.record_entry.place(x=100, y=175)
            submit_but = Button(self.fr, bg='#f3f5cb', fg='black', width=10, height=1, text='SUBMIT', command=lambda:self.delete_record(to_whom, self.record_entry, update_delete))
            submit_but.place(x=75, y=225)

    def update_record(self, to_whom, id, update_delete):
        if id.get() == '':
            messagebox.showwarning('Incomplete Data', 'Please enter all the details')
            update_delete.destroy()
        elif to_whom == 'book':
            login_window1 = Toplevel()
            login_window1.title('Book')
            f2 = Frame(login_window1, height=260, width=400, bg='gold')
            lab = Label(f2, width=50, text="Enter new details to update book", bg="black", fg="white")
            lab.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
            Bname = Label(f2, width=20, text="Enter Book Name: ")
            self.e_Bname = Entry(f2, width=30, fg='black', bg='white')
            self.e_Authorname = Entry(f2, width=30, fg='black', bg='white')
            Authorname = Label(f2, width=20, text="Enter Author Name: ")
            Category = Label(f2, width=20, text="Enter Category: ")
            self.e_Category = Entry(f2, width=30, fg='black', bg='white')
            Bname.grid(row=2, column=1, padx=10, pady=10)
            self.e_Bname.grid(row=2, column=2, padx=10, pady=10)
            self.e_Authorname.grid(row=3, column=2, padx=10, pady=10)
            Authorname.grid(row=3, column=1, padx=10, pady=10)
            Category.grid(row=4, column=1, padx=10, pady=10)
            self.e_Category.grid(row=4, column=2, padx=10, pady=10)
            No_of_copies = Label(f2, width=20, text="Enter Available Copies ")
            self.e_Availablecopies = Entry(f2, width=30, fg='black', bg='white')
            No_of_copies.grid(row=5, column=1, padx=10, pady=10)
            self.e_Availablecopies.grid(row=5, column=2, padx=10, pady=10)
            b1 = Button(f2, text="Update book", height=2, width=15, command=lambda: self.updateBook(login_window1, id, update_delete))
            b1.grid(row=6, column=2, columnspan=1, padx=10, sticky=W)
            f2.pack()
            f2.grid_propagate(0)
        elif to_whom == 'student':
            student_signup = Toplevel()
            student_signup.title('Student')
            f = Frame(student_signup, height=250, width=400, bg="gold")
            l1 = Label(f, width=20, text="Enter Student name: ")
            l2 = Label(f, width=20, text="Enter Class: ")
            l3 = Label(f, width=20, text="Enter password: ")
            l4 = Label(f, width=50, text="Enter the details below to add a Student", bg="black", fg="white")
            self.e_studname = Entry(f, width=30, fg='black', bg='white')
            self.e_studname.focus_set()
            self.e_class = Entry(f, width=30, fg='black', bg='white')
            self.e_password = Entry(f, width=30, fg='black', bg='white', show='*')
            l1.grid(row=2, column=1, padx=10, pady=10)
            l2.grid(row=3, column=1, padx=10, pady=10)
            l3.grid(row=4, column=1, padx=10, pady=10)
            l4.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
            self.e_studname.grid(row=2, column=2, padx=10, pady=10)
            self.e_password.grid(row=4, column=2, padx=10, pady=10)
            self.e_class.grid(row=3, column=2, padx=10, pady=10)
            b1 = Button(f, text="Submit", height=2, width=10, command=lambda: self.updateStudent(student_signup, id, update_delete))
            b1.grid(row=5, column=2, padx=10, sticky='w')
            f.pack()
            f.grid_propagate(0)

    def updateBook(self, top_level, id, update_delete):
        bName = self.e_Bname.get()
        Author = self.e_Authorname.get()
        category = self.e_Category.get()
        copies = self.e_Availablecopies.get()

        if self.e_Bname.get() == '' or self.e_Authorname.get() == '' or self.e_Category.get() == '' or self.e_Availablecopies.get() == '':
            messagebox.showwarning('Incomplete Data', 'Please Enter all the details')
        else:
            params = (bName, Author, category, copies, int(id.get()))
            query = '''update Book set BName='%s', 
                        Author='%s', Category='%s', AvailableCopies='%s' where BookId='%d';'''
            DefaultPage.DatabaseHelper.execute_query(query, params)
            messagebox.showinfo('Book Updation', 'Book Updated Successfully')
        top_level.destroy()
        update_delete.destroy()

    def updateStudent(self, top_level, id, update_delete):
        name = self.e_studname.get()
        password = self.e_password.get()
        class_ = self.e_class.get()
        if self.e_studname.get() == '' or self.e_password.get() == '' or self.e_class.get() == '':
            messagebox.showwarning('Incomplete Data', 'Please Enter all the details')
        else:
            params = (password, name, class_, int(id.get()))
            query = '''update Student set Passwd='%s', SName='%s', Class='%s' 
                        where StudentId='%d';'''
            DefaultPage.DatabaseHelper.execute_query(query, params)
            messagebox.showinfo('Student Updation', "Student Updated successfully")
        top_level.destroy()
        update_delete.destroy()

    def delete_record(self, to_whom, id, update_delete):
        if id.get() == '':
            messagebox.showwarning('Incomplete Data', 'Please enter all the details')
            update_delete.destroy()
        elif to_whom == 'book':
            params = (int(id.get()),)
            query = '''delete from Book where BookId='%d';'''
            DefaultPage.DatabaseHelper.execute_query(query, params)
            messagebox.showinfo('Book Deletion', "Book Deleted successfully")
            update_delete.destroy()
        elif to_whom == 'student':
            params = (int(id.get()),)
            query = '''delete from Student where StudentId='%d';'''
            DefaultPage.DatabaseHelper.execute_query(query, params)
            messagebox.showinfo('Student Deletion', "Student Deleted successfully")
            update_delete.destroy()

    def see_books(self):
        query = """select * from project.book
                            where AvailableCopies>0;"""
        result = DefaultPage.DatabaseHelper.get_all_data(query)
        self.menu_frame = DefaultPage.SimpleTable(self.f, rows=len(result), columns=len(result[0]), height=450,
                                      width=680, colour="#bbdbab")
        self.menu_frame.place(x=500, y=250)
        self.menu_frame.grid_propagate(0)
        for i in range(len(result)):
            for j in range(len(result[0])):
                if i == 0:
                    self.menu_frame.set(row=i, column=j, value=result[i][j], bg="#0aa80c", fg="white")
                elif j == 0:
                    self.menu_frame.set(row=i, column=j, value=result[i][j], width=14)
                elif j == 3:
                    self.menu_frame.set(row=i, column=j, value=result[i][j], width=12)
                elif j == 4:
                    self.menu_frame.set(row=i, column=j, value=result[i][j], width=14)
                else:
                    self.menu_frame.set(row=i, column=j, value=result[i][j])

    def see_students(self):
        query = """select StudentId,SName,Class from Student"""

        result = DefaultPage.DatabaseHelper.get_all_data(query)
        self.student_details_table = DefaultPage.SimpleTable(self.f, rows=len(result), columns=len(result[0]), height=450,
                                                 width=680, colour="#bbdbab")
        self.student_details_table.place(x=500, y=250)
        self.student_details_table.grid_propagate(0)

        for i in range(len(result)):
            for j in range(len(result[0])):
                if i == 0:
                    self.student_details_table.set(row=i, column=j, value=result[i][j], bg="#0aa80c", fg="white")
                elif j == 0 :
                    self.student_details_table.set(row=i, column=j, value=result[i][j], width=30)
                elif j == 1:
                    self.student_details_table.set(row=i, column=j, value=result[i][j], width=35)
                elif j == 2:
                    self.student_details_table.set(row=i, column=j, value=result[i][j], width=30)
                else:
                    self.student_details_table.set(row=i, column=j, value=result[i][j])


    def admin_logout(self):
        import MainPage
        self.f.destroy()
        self.panel.destroy()
        self.redirect=MainPage.MainPage(self.root)

if __name__=="__main__":
    root=Tk()
    admin_details=(4,'Rohan','rohan')
    a=AdminPage(root,admin_details)
    root.mainloop()