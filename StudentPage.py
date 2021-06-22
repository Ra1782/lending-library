from DefaultPage import *
from tkinter import messagebox
import datetime

class StudentPage(DefaultPage):
    def __init__(self, root, student_details):
        super().__init__(root)
        self.details = student_details
        self.root.state('zoomed')
        self.dct_StringVar = {}
        self.dct_StringVar1 = {}
        self.m = self.m = Message(self.f, width=850, font=("Bernard MT Condensed",25,"bold underline"),text=f"Welcome {self.details[2]}\nClass: {self.details[3]}", bg="#b5caeb", relief=SOLID, borderwidth=2)
        self.m.place(x=100, y=100)
        self.add_buttons()

    def add_buttons(self):
        self.logout = DefaultPage.CreamButton(self.f, "LOGOUT", self.student_logout, width=10, bg='#f3f5cb')
        self.logout.place(x=1200, y=20)
        self.ch_pass = DefaultPage.CreamButton(self.f, "CHANGE PASSWORD", self.check_stud, width=20,  bg='#f3f5cb')
        self.ch_pass.place(x=950, y=20)
        self.Issue_Books = DefaultPage.CreamButton(self.f, text="ISSUE BOOKS",
                                       command=lambda: self.show_issue_details("<Button-1>"))
        self.Issue_Books.place(x=250, y=220)
        self.Issue_Books.bind("<Button-1>", self.show_issue_details)
        self.book_status_button = DefaultPage.CreamButton(self.f, text="CHECK YOUR PENDING BOOKS", command=self.book_status)
        self.book_status_button.place(x=550, y=220)
        self.previous_books_button = DefaultPage.CreamButton(self.f, text="VIEW YOUR PREVIOUS BOOKS ", command=self.previous_books)
        self.previous_books_button.place(x=850, y=220)

    def show_issue_details(self, event):
        self.radio_frame = Frame(self.f, bg="#FFDBAC", width=25, height=16)
        self.var = StringVar(self.radio_frame, value='0')
        self.r1 = Radiobutton(self.radio_frame, text='Sem 1', variable=self.var, value='SEM-I', width=25, height=2, bg="#FFDBAC")
        self.r1.grid(row=0,column=0)
        self.r2 = Radiobutton(self.radio_frame, text='Sem 2', variable=self.var, value='SEM-II', width=25, height=2, bg="#FFDBAC")
        self.r2.grid(row=1,column=0)
        self.r3 = Radiobutton(self.radio_frame, text='Sem 3', variable=self.var, value='SEM-III', width=25, height=2, bg="#FFDBAC")
        self.r3.grid(row=2,column=0)
        self.r4 = Radiobutton(self.radio_frame, text='Sem 4', variable=self.var, value='SEM-IV', width=25, height=2, bg="#FFDBAC")
        self.r4.grid(row=3,column=0)
        self.r5 = Radiobutton(self.radio_frame, text='Sem 5', variable=self.var, value='SEM-V', width=25, height=2, bg="#FFDBAC")
        self.r5.grid(row=4,column=0)
        self.r6 = Radiobutton(self.radio_frame, text='Sem 6', variable=self.var, value='SEM-VI', width=25, height=2, bg="#FFDBAC")
        self.r6.grid(row=5,column=0)
        self.r7 = Radiobutton(self.radio_frame, text='Sem 7', variable=self.var, value='SEM-VII', width=25, height=2, bg="#FFDBAC")
        self.r7.grid(row=6,column=0)
        self.r8 = Radiobutton(self.radio_frame, text='Sem 8', variable=self.var, value='SEM-VIII', width=25, height=2, bg="#FFDBAC")
        self.r8.grid(row=7,column=0)
        self.b1 = DefaultPage.CreamButton(self.f, text="SHOW BOOKS", command=lambda: self.show_books(self.var.get()), width=20)
        self.b1.place(x=180, y=630)
        self.radio_frame.place(x=200, y=300)

    def show_books(self, var='SEM-I'):
        params = (var,)
        query = """select BookId,BName,Author 
                from project.Book
                where Category='%s';"""
        result = DefaultPage.DatabaseHelper.get_all_data(query, params)
        self.menu_frame = DefaultPage.SimpleTable(self.f, rows=len(result), columns=len(result[0]),
                                      height=400, width=680, colour="#bbdbab")
        self.menu_frame.place(x=440, y=300)
        self.menu_frame.grid_propagate(0)

        for i in range(1, len(result)):
            self.dct_StringVar[result[i][0]] = IntVar()

        for i in range(len(result)):
            for j in range(len(result[0])):
                if i == 0:
                    self.menu_frame.set(row=i, column=j, value=result[i][j], bg="#0aa80c", fg="white")
                elif j == 0 and i != 0:
                    c = Checkbutton(self.menu_frame, text=result[i][j],
                                    variable=self.dct_StringVar.get(result[i][j]))
                    self.menu_frame.set(row=i, column=j, value=result[i][j], widget=c)
                elif j == 1:
                    self.menu_frame.set(row=i, column=j, value=result[i][j], width=35)
                else:
                    self.menu_frame.set(row=i, column=j, value=result[i][j], width=30)
        self.submit = Button(self.menu_frame, text="Issue Book", width=30, height=2, bg="gold", fg="black", command=lambda: self.issue_books())
        self.submit.grid(row=len(result) + 2, column=len(result[0]) - 3, rowspan=10)
        self.avial_copies = Button(self.menu_frame, text="Check Available Copies", width=30, height=2, bg="gold", fg="black",
                           command=lambda: self.show_message(self.check_available_copies(self.get_selected_books())))
        self.avial_copies.grid(row=len(result) + 2, column=len(result[0]) - 2, rowspan=10)

    def issue_books(self):
        selected_books = self.get_selected_books()
        if len(selected_books) == 0:
            messagebox.showwarning("No Book Selected", "Please select one book to Issue")
        elif len(selected_books) > 1:
            messagebox.showwarning("Many books", "Please do not select more than one book to Issue")
        else:
            for book_id in selected_books:
                no_of_copies = self.check_available_copies(book_id)
                if no_of_copies == 0:
                    messagebox.showinfo('No book','We are Sorry, the book you are looking for is unavailable at the moment. Please try again later.')
                    break
            else:
                response = messagebox.askyesno('Confirm issue','Confirm your Book Issue')
                if response:  # If the answer was "Yes" response is True
                    self.let_student_issue(selected_books)
                else:  # If the answer was "No" response is False
                    self.show_books(self.var.get())

    def let_student_issue(self, selected_books):
        for book_id in selected_books:
            params = (self.details[0], book_id, datetime.datetime.today().date())
            query = """insert into project.Lending(SId,BId,BDate) 
                        values('%s','%s','%s');"""
            DefaultPage.DatabaseHelper.execute_query(query, params)
            params = (book_id,)
            query = """update book set AvailableCopies=AvailableCopies-1 where BookId=%s;"""
            DefaultPage.DatabaseHelper.execute_query(query, params)
        for key, value in self.dct_StringVar.items():
            if value.get() == 1:
                self.dct_StringVar[key].set(0)
        messagebox.showinfo('Book Issued', 'Congratulations!! Book have been Issued to you')
        self.show_books(self.var.get())

    def get_selected_books(self):
        selected_books = []
        for key, value in self.dct_StringVar.items():
            if value.get() == 1:
                selected_books.append(key)
        return selected_books

    def check_available_copies(self, book_id):
        if len(self.get_selected_books()) == 0:
            pass
        elif len(self.get_selected_books()) > 1:
            messagebox.showwarning('Many books', 'Please do not select more than one book')
        else:
            if type(book_id) == list:
                if len(book_id) == 0:
                    return
                else:
                    book_id = book_id[0]
            params = (book_id,)
            query = """select AvailableCopies from project.Book where BookId='%s'"""
            result = DefaultPage.DatabaseHelper.get_data(query, params)
            return result[0]

    def show_message(self,copies):
        if len(self.get_selected_books()) == 0:
            messagebox.showwarning('No Book Selected', 'Please select a book from the list')
        elif copies is None:
            pass
        else :
            messagebox.showinfo('Book Count', f'Available copies of Selected book are {copies}')

    def book_status(self):
        params = (self.details[0],)
        query = """select l.OrderId,b.BookId,b.BName,b.Author,l.BDate
                        from lending l inner join book b 
                        on b.BookId=l.BId
                        where isReturned=0 and l.SId=%s;"""
        result = DefaultPage.DatabaseHelper.get_all_data(query, params)

        self.book_status_table = DefaultPage.SimpleTable(self.f, rows=len(result), columns=len(result[0]), width=680, height=400,
                                             colour="#f06787")
        self.book_status_table.grid_propagate(0)
        self.book_status_table.place(x=440, y=300)
        for i in range(1, len(result)):
            self.dct_StringVar1[result[i][0]] = IntVar()
        for i in range(len(result)):
            for j in range(len(result[0])):
                if i == 0:
                    self.book_status_table.set(row=i, column=j, value=result[i][j], bg="#c9083f", fg="white")
                elif j == 0 and i!=0:
                    c = Checkbutton(self.book_status_table, text=result[i][j],
                                    variable=self.dct_StringVar1.get(result[i][j]))
                    self.book_status_table.set(row=i, column=j, value=result[i][j], widget=c, width=6)
                elif j == 2:
                    self.book_status_table.set(row=i, column=j, value=result[i][j], width=32)
                elif j == 3:
                    self.book_status_table.set(row=i, column=j, value=result[i][j], width=30)
                elif j == 4:
                    self.book_status_table.set(row=i, column=j, value=result[i][j], width=12)
                else:
                    self.book_status_table.set(row=i, column=j, value=result[i][j], width=10)
        self.submit = Button(self.book_status_table, text="Return Book", width=30, height=2, bg="gold", fg="black",
                             command=lambda: self.return_books(self.get_selected_books_status()))
        self.submit.grid(row=len(result) + 2, column=len(result[0]) - 3)
        self.fine = Button(self.book_status_table, text="Check Fine", width=30, height=2, bg="gold", fg="black",
                             command=lambda: self.fine_message(self.check_fine(self.get_selected_books_status())))
        self.fine.grid(row=len(result) + 2, column=len(result[0]) - 2)

    def return_books(self, selected_books):
        if len(selected_books) == 0:
            messagebox.showwarning('No Book Selected','Please select a book from the list')
        elif len(self.get_selected_books_status()) > 1:
            messagebox.showwarning('Many books', 'Please do not select more than one book')
        else:
            fine = self.check_fine(selected_books)
            response = messagebox.askyesno('Return Confirmation',f'Please click Yes to proceed. Your Fine is {fine}')
            if response:  # If the answer was "Yes" response is True
                if len(selected_books) == 0:
                    messagebox.showwarning('No selected book','Please select a book to continue')
                else:

                    params = (datetime.datetime.today().date(), fine, selected_books[0])
                    query = """update project.Lending 
                                        set RDate='%s', Fine='%s', IsReturned=1 
                                        where OrderId='%s'"""
                    DefaultPage.DatabaseHelper.execute_query(query, params)
                    params = (selected_books[0],)
                    query = """update book set AvailableCopies=AvailableCopies+1 
                                        where BookId=
                                        (select BId from Lending where OrderId=%s);"""
                    DefaultPage.DatabaseHelper.execute_query(query, params)
                    messagebox.showinfo('Succesfully book Returned', f'Book Returned. Thankyou')
                    for key, value in self.dct_StringVar1.items():
                        if value.get() == 1:
                            self.dct_StringVar1[key].set(0)
                    self.book_status()
            else:  # If the answer was "No" response is False
                self.book_status()

    def fine_message(self,fine):
        if len(self.get_selected_books_status()) == 0:
            messagebox.showwarning('No Book Selected','Please select a book from the list')
            for key, value in self.dct_StringVar1.items():
                if value.get() == 1:
                    self.dct_StringVar1[key].set(0)
        elif fine is None:
            pass
        else:
            messagebox.showinfo('Book Fine',f'Your Applicable Fine is Rs.{fine}')
            for key, value in self.dct_StringVar1.items():
                if value.get() == 1:
                    self.dct_StringVar1[key].set(0)

    def get_selected_books_status(self):
        selected_books = []
        for key, value in self.dct_StringVar1.items():
            if value.get() == 1:
                selected_books.append(key)
        return selected_books

    def check_fine(self,order_id):
        if len(self.get_selected_books_status()) == 0:
            pass
        elif len(self.get_selected_books_status()) > 1:
            messagebox.showwarning('Many books', 'Please do not select more than one book')
        else:
            if type(order_id) == list:
                if len(order_id) == 0:
                    return
                else:
                    order_id = order_id[0]
            params = (order_id,)
            query = """select BDate from project.Lending where OrderId='%s'"""
            result = DefaultPage.DatabaseHelper.get_data(query, params)
            borrowDate = result[0]
            returnDate = datetime.datetime.today().date()
            days = (returnDate - borrowDate).days
            # According to Rs.2 per day fine applicable after a week
            if days > 7:
                fine = 2 * (days - 7)
            else:
                fine = 0
            return fine

    def previous_books(self):
        query = """Select BName, Author,BDate,RDate,Fine
                from Book b join Lending l
                on b.BookId=l.BId
                where l.IsReturned=1 and l.SId='%d'
                order by OrderId DESC"""
        parameters = (self.details[0])
        result = DefaultPage.DatabaseHelper.get_all_data(query, parameters)

        self.recent_orders_table = DefaultPage.SimpleTable(self.f, rows=len(result), columns=len(result[0]), width=680,
                                               height=400,colour="#bbdbab")
        self.recent_orders_table.grid_propagate(0)
        self.recent_orders_table.place(x=440, y=300)
        for i in range(len(result)):
            for j in range(len(result[0])):
                if i == 0:
                    self.recent_orders_table.set(row=i, column=j, value=result[i][j], bg="#0aa80c", fg="white")
                elif j == 0:
                    self.recent_orders_table.set(row=i, column=j, value=result[i][j], width=40)
                elif j == 1:
                    self.recent_orders_table.set(row=i, column=j, value=result[i][j], width=25)
                else:
                    self.recent_orders_table.set(row=i, column=j, value=result[i][j], width=10)

    def check_stud(self):
        old_check_pass = Toplevel()
        old_check_pass.title('Authenticate')
        fr = Frame(old_check_pass, width=200, height=200, bg='gold')
        info_label = Label(fr, width=50, bg='black', fg='white', text="To change password let's verify it's you" )
        info_label.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
        lab = Label(fr, width=20, text='Enter your Old Password: ')
        self.old_pass = Entry(fr, width=30)
        lab.grid(row=1, column=0, padx=10, pady=10)
        self.old_pass.grid(row=1, column=1, padx=10, pady=10)
        sub = Button(fr, text="Submit", height=2, width=10, command=lambda: self.check_pass(old_check_pass))
        sub.grid(row=2, column=1, padx=10, pady=10)
        fr.pack()

    def check_pass(self, parent_frame):
        old_pass = self.old_pass.get()
        query = """select Passwd from Student where StudentId='%d'"""
        params = (self.details[0],)
        pass_from_db = DefaultPage.DatabaseHelper.get_data(query, params)
        if old_pass == pass_from_db[0]:
            messagebox.showinfo('Authentication Successful', 'Password found correct')
            parent_frame.destroy()
            self.update_pass()
        else:
            messagebox.showwarning('Authentication Failed', 'Incorrect Password')

    def update_pass(self):
        new_pass = Toplevel()
        new_pass.title('Password Update')
        fr = Frame(new_pass, width=200, height=200, bg='gold')
        info_label = Label(fr, width=50, bg='black', fg='white', text="After Entering password click Submit")
        info_label.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
        lab = Label(fr, width=20, text='Enter your New Password: ')
        self.new_passwd = Entry(fr, width=30)
        lab.grid(row=1, column=0, padx=10, pady=10)
        self.new_passwd.grid(row=1, column=1, padx=10, pady=10)
        sub = Button(fr, text="Submit", height=2, width=10, command=lambda: self.update_pass_db(new_pass))
        sub.grid(row=2, column=1, padx=10, pady=10)
        fr.pack()

    def update_pass_db(self, parent_frame):
        new_pass = self.new_passwd.get()
        query = """update Student set Passwd='%s' where StudentId='%d'"""
        params = (new_pass, self.details[0])
        DefaultPage.DatabaseHelper.execute_query(query, params)
        messagebox.showinfo('Password Updation', 'Password Updated Successfully')
        parent_frame.destroy()

    def student_logout(self):
        import MainPage
        messagebox.showinfo('Logout', 'Thank You. We hope to see you again')
        self.f.destroy()
        self.panel.destroy()
        self.redirect = MainPage.MainPage(self.root)

if __name__ == '__main__':
    root = Tk()
    c = StudentPage(root, (6, 'rohit', 'Rohit', 'D15'))
    root.mainloop()