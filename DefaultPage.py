from tkinter import *
from PIL import Image,ImageTk
from pymysql import *

class DefaultPage:
    def __init__(self,root):
        self.root=root
        self.root.title('VESIT Library')
        self.root.iconbitmap('images/project_icon_pic.ico')
        self.f=Frame(root,width=1600,height=900)# 900x500 in mainpage
        self.f.pack()
        # The footer at the bottom
        self.footer = Label(self.f, bg="ivory3", height=1, text="@VES Institute of Technology, Since 1962")
        self.footer.pack(side=BOTTOM, fill=X)
        self.b_image = Image.open("images/lib-background-img.jpg")
        self.b_image = self.b_image.resize((1600, 900))
        self.img = ImageTk.PhotoImage(self.b_image)
        self.panel = Label(self.f, image=self.img)
        self.panel.pack()
        self.panel.pack_propagate(0)
        self.img1=Image.open("images/Importance-of-Books.jpg")
        self.img1=self.img1.resize((100, 48))
        self.img_1 = ImageTk.PhotoImage(self.img1)
        self.p1=Label(self.f,image=self.img_1,borderwidth=2,relief=SOLID)
        self.p1.place(x=40,y=20)
        self.img2 = Image.open("images/You_can_read.jpg")
        self.img2 = self.img2.resize((70, 100))
        self.img_2 = ImageTk.PhotoImage(self.img2)
        self.p2 = Label(self.f, image=self.img_2, borderwidth=2, relief=SOLID)
        self.p2.place(x=30, y=600)
        self.m = Message(self.f, width=600, font=("Mongolian Baiti", 25, "bold"), text="VESIT LIBRARY", bg="white",
                         relief=SOLID, borderwidth=2)
        self.m.place(x=144, y=20)
        self.f.pack_propagate(0)

    class LoginButton(Button):
        def __init__(self, parent, text, command, **kwargs):
            super().__init__(parent, text=text, width=30, height=3, bg='#f3f5cb', activebackground="white",
                             activeforeground="white", command=command)
            self.configure(**kwargs)

    class CreamButton(Button):
        def __init__(self, parent, text, command, **kwargs):
            super().__init__(parent, text=text, width=25, height=2, font="Algerian 13 bold", bg="#FFDBAC", fg="black",
                             activebackground="gray", command=command)
            self.configure(**kwargs)

    class ScrolledFrame:
        def __init__(self, master, **kwargs):
            width = kwargs.pop('width', None)
            height = kwargs.pop('height', None)
            self.outer = Frame(master, **kwargs)

            self.vsb = Scrollbar(self.outer, orient=VERTICAL)
            self.vsb.pack(fill=Y, side=RIGHT)
            self.canvas = Canvas(self.outer, highlightthickness=0, width=width, height=height)
            self.canvas.pack(side=LEFT, fill=BOTH, expand=True)
            self.canvas['yscrollcommand'] = self.vsb.set
            self.canvas.bind("<Enter>", self._bind_mouse)
            self.canvas.bind("<Leave>", self._unbind_mouse)
            self.vsb['command'] = self.canvas.yview
            self.inner = Frame(self.canvas)
            self.canvas.create_window(4, 4, window=self.inner, anchor='nw')
            self.inner.bind("<Configure>", self._on_frame_configure)

            self.outer_attr = set(dir(Widget))

        def __getattr__(self, item):
            if item in self.outer_attr:
                return getattr(self.outer, item)
            else:
                return getattr(self.inner, item)

        def _on_frame_configure(self, event=None):
            x1, y1, x2, y2 = self.canvas.bbox("all")
            height = self.canvas.winfo_height()
            self.canvas.config(scrollregion=(0, 0, x2, max(y2, height)))

        def _bind_mouse(self, event=None):
            self.canvas.bind_all("<4>", self._on_mousewheel)
            self.canvas.bind_all("<5>", self._on_mousewheel)
            self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)

        def _unbind_mouse(self, event=None):
            self.canvas.unbind_all("<4>")
            self.canvas.unbind_all("<5>")
            self.canvas.unbind_all("<MouseWheel>")

        def _on_mousewheel(self, event):
            if event.num == 4 or event.delta > 0:
                self.canvas.yview_scroll(-1, "units")
            elif event.num == 5 or event.delta < 0:
                self.canvas.yview_scroll(1, "units")

    class SimpleTable(ScrolledFrame):
        def __init__(self, parent, rows=10, columns=5, colour=None, **kwargs):
            super().__init__(parent, background="#f2efe6", **kwargs)
            self.header_color = colour
            self.even_color = colour
            self.odd_color = colour
            # f2dba0#f06787#bbdbab
            self._widgets = []
            for row in range(rows):
                current_row = []
                if (row == 0):
                    bg = self.header_color
                elif (row % 2 == 0):
                    bg = self.even_color
                else:
                    bg = self.odd_color
                for column in range(columns):
                    label = Label(self, text="-", borderwidth=0, height=3, bg=bg, wraplength=400)
                    label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                    current_row.append(label)
                self._widgets.append(current_row)

            for column in range(columns):
                self.grid_columnconfigure(column, weight=1)

        def set(self, row, column, value, widget=None, **kwargs):
            widget_ref = self._widgets[row][column]
            if (widget is not None):
                if (row % 2 == 0):
                    widget.configure(bg=self.even_color)
                else:
                    widget.configure(bg=self.odd_color)
                widget.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                self._widgets[row][column] = widget
                widget_ref = widget
            widget_ref.configure(text=str(value), **kwargs)

    class DatabaseHelper():
        @staticmethod
        def get_columns(description):
            return tuple(map(lambda x: x[0], description))

        @staticmethod
        def get_data(query, parameters=None):
            conn = connect(host='localhost', database='project', user='root', password='Ra4@246890')
            cur = conn.cursor()
            if parameters is None:
                cur.execute(query)
            else:
                cur.execute(query % parameters)
            result = cur.fetchone()
            cur.close()
            conn.close()
            return result

        @staticmethod
        def get_all_data(query, parameters=None):
            conn = connect(host='localhost', database='project', user='root', password='Ra4@246890')
            cur = conn.cursor()
            if (parameters is None):
                cur.execute(query)
            else:
                cur.execute(query % parameters)
            result = cur.fetchall()
            headers = DefaultPage.DatabaseHelper.get_columns(cur.description)
            cur.close()
            conn.close()
            return (headers,) + result

        @staticmethod
        def execute_query(query, parameters=None):
            conn = connect(host='localhost', database='project', user='root', password='Ra4@246890')
            cur = conn.cursor()
            if parameters is None:
                cur.execute(query)
            else:
                cur.execute(query % parameters)
            conn.commit()
            cur.close()
            conn.close()

if __name__=="__main__":
    root=Tk()
    d=DefaultPage(root)
    root.mainloop()