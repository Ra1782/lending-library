from AdminPage import *
from StudentPage import *

class MainPage(DefaultPage):
    def __init__(self,root):
        super().__init__(root)
        self.root.geometry('900x550')
        self.root.state('normal')
        self.add_widgets()


    def add_widgets(self):
        self.admin_button = DefaultPage.LoginButton(self.panel, "Admin login" ,lambda: self.getLoginScreen("Admin"),relief='raised',borderwidth=4,)
        self.admin_button.place(x=210, y=220)
        self.user_button = DefaultPage.LoginButton(self.panel, "Student login", lambda: self.getLoginScreen("User"),relief='raised',borderwidth=4)
        self.user_button.place(x=500, y=220)
    def reset(self):
        self.e_username.delete(0,END)
        self.e_password.delete(0, END)

    def getLoginScreen(self,login_type):
        login_window = Toplevel()
        login_window.title(login_type)
        f = Frame(login_window, height=200, width=400,bg="gold")
        l1 = Label(f, width=20, text="Enter username: ")
        self.e_username = Entry(f, width=30, fg='black', bg='white')
        self.e_username.focus_set()
        self.e_password = Entry(f, width=30, fg='black', bg='white', show='*')
        l2 = Label(f, width=20, text="Enter password: ")
        l1.grid(row=1, column=1, padx=10, pady=10)
        l2.grid(row=2, column=1, padx=10, pady=10)
        self.e_username.grid(row=1, column=4, padx=10, pady=10)
        self.e_password.grid(row=2, column=4, padx=10, pady=10)
        b1 = Button(f, text="Submit", height=2, width=10,command=lambda: self.validate(login_window, login_type))
        b1.grid(row=3, column=1, padx=10, sticky='e')
        b2 = Button(f, text="Reset", height=2, width=10, command=lambda: self.reset())
        b2.grid(row=3, column=4, padx=10, sticky='w')
        f.pack()
        f.grid_propagate(0)

    def validate(self,login_window,login_type):
        username=self.e_username.get()
        pwd = self.e_password.get()
        if login_type=="Admin":
            query = "Select * from project.Admin where AName= '%s' and Passwd='%s'"
        else:
            query = "Select * from project.Student where SName= '%s' and Passwd='%s'"
        parameters=(username,pwd)
        result = DefaultPage.DatabaseHelper.get_data(query,parameters)
        if result is None or len(result)==0 :
            messagebox.showerror("Login Failed","Incorrect credentials")
        else:
            messagebox.showinfo('Login Success',"Login successfuly completed")
            login_window.destroy()
            self.f.destroy()
            self.panel.destroy()
            if login_type=="Admin":
                self.redirect=AdminHomePage(self.root, result)
            else:
                self.redirect=StudentPage(self.root,result)

if __name__=="__main__":
    root=Tk()
    m=MainPage(root)
    root.mainloop()