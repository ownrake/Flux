from customtkinter import *
from PIL import Image

from db.db_manager import DatabaseManager

db = DatabaseManager()

wid = 1300
hei = 700

class App(CTk):
    def __init__(self):
        super().__init__()
        self.geometry(f"{wid}x{hei}")
        
        self.tabview = CTkTabview(self, width=700, height=450, )
        self.tabview.pack(expand=True)

        self.tabview.add("login")
        self.tabview.add("register")

        self.login_frame = self.tabview.tab("login")

        self.frame_welcome_login = CTkLabel(self.login_frame, text="Welcome to Flux!")
        self.frame_welcome_login.pack(padx=40, pady=20)

        self.frame_username_login = CTkLabel(self.login_frame, text="username")
        self.frame_username_login.pack(padx=40, pady=20)

        self.entry_username_login = CTkEntry(self.login_frame, placeholder_text="введите username")
        self.entry_username_login.pack(padx=40, pady=20)

        self.frame_passwd_login = CTkLabel(self.login_frame, text="passwd")
        self.frame_passwd_login.pack(padx=40, pady=20)

        self.entry_passwd_login = CTkEntry(self.login_frame, placeholder_text="введите passwd")
        self.entry_passwd_login.pack(padx=40, pady=20)

        self.button_continie_login = CTkButton(self.login_frame, text="Далее", command=self.login)
        self.button_continie_login.pack(padx=40, pady=20)



        self.register_frame = self.tabview.tab("register")

        self.frame_welcome = CTkLabel(self.register_frame, text="Welcome to Flux!")
        self.frame_welcome.pack(padx=40, pady=20)

        self.frame_username = CTkLabel(self.register_frame, text="username")
        self.frame_username.pack(padx=40, pady=20)

        self.entry_username = CTkEntry(self.register_frame, placeholder_text="введите username")
        self.entry_username.pack(padx=40, pady=20)

        self.entry_email = CTkLabel(self.register_frame, text="email")
        self.entry_email.pack(padx=40, pady=20)

        self.entry_email = CTkEntry(self.register_frame, placeholder_text="введите email")
        self.entry_email.pack(padx=40, pady=20)

        self.frame_passwd = CTkLabel(self.register_frame, text="passwd")
        self.frame_passwd.pack(padx=40, pady=20)

        self.entry_passwd = CTkEntry(self.register_frame, placeholder_text="введите passwd")
        self.entry_passwd.pack(padx=40, pady=20)

        self.button_continie = CTkButton(self.register_frame, text="Далее", command=self.register)
        self.button_continie.pack(padx=40, pady=20)

    
    def login(self):
        user = self.entry_username_login.get()
        passwd = self.entry_passwd_login.get()

        db.login_user(user, passwd)


    
    def register(self):
        user = self.entry_username.get()
        email = self.entry_email.get()
        passwd = self.entry_passwd.get()

        db.add_user(user, email, passwd)

        print(user, passwd)
        

        

app = App()
app.mainloop()
