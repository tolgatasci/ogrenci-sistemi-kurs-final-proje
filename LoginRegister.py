import tkinter as tk
from tkinter import ttk, TOP, messagebox

from tkintermodules.EntryWithPlaceholder import EntryWithPlaceholder

from mylibs.Database import Database
class LoginRegister(tk.Tk):
    def __init__(self):
        super().__init__()
        self.database = Database("ogrenciler.db")
        # users tablesi yok ise oluşturuyoruz.
        # otomatik admin admin oluşturuyor
        self.database.create_table("users", "username TEXT UNIQUE, password TEXT")
        try:

            self.database.insert("insert into users values('admin', 'admin')")
        except:
            pass
        self.title("Login/Register")
        self.geometry("400x300")
        self.tabControl = ttk.Notebook(self)

        self.tab1 = ttk.Frame(self.tabControl)
        self.tab2 = ttk.Frame(self.tabControl)

        self.tabControl.add(self.tab1, text='Giriş')

        login_frame = ttk.Frame(self.tab1)
        login_frame.pack(fill="both", expand=True, padx=50, pady=20)

        self.tabControl.add(self.tab2, text='Kayıt')
        self.tabControl.pack(expand=1, fill="both")

        ttk.Label(login_frame,
                  text="Kullanıcı Adı:", anchor='w').grid(column=0,
                                                          row=0,
                                                          padx=30,
                                                          pady=30, sticky="w")
        self.username = EntryWithPlaceholder(login_frame, placeholder="Kullanıcı Adı")
        self.username.grid(column=1,
                           row=0)

        ttk.Button(login_frame, text="Kayıt Ol", command=self.kayit_ol_gecis).grid(column=0,
                                                                                   row=2,
                                                                                   padx=30,
                                                                                   pady=30,
                                                                                   sticky="e")

        ttk.Label(login_frame,
                  text="Şifre:", anchor='w').grid(column=0,
                                                  row=1,
                                                  padx=30,
                                                  pady=30, sticky="w")
        self.password = EntryWithPlaceholder(login_frame, placeholder="Şifre", show="*")
        self.password.grid(column=1,
                           row=1)

        login_button = ttk.Button(login_frame, text="Giriş Yap", command=self.giris)
        login_button.grid(column=1, row=2, padx=0, pady=0, sticky="e")


        # username, password login buttonu tekrar sıralamaya sokuyoruz. Kullanıcı tab ile diğer input alanına geçiş yapabilsin diye.
        for widget in (self.username, self.password,login_button):
            widget.lift()


        register_frame = ttk.Frame(self.tab2)
        register_frame.pack(fill="both", expand=True, padx=50, pady=20)

        ttk.Label(register_frame,
                  text="Kullanıcı Adı:", anchor='w').grid(column=0,
                                                          row=0,
                                                          padx=10,
                                                          pady=10, sticky="w")
        self.register_username = EntryWithPlaceholder(register_frame, placeholder="Kullanıcı Adı")
        self.register_username.grid(column=1,
                                    row=0)

        ttk.Label(register_frame,
                  text="Şifre:", anchor='w').grid(column=0,
                                                  row=1,
                                                  padx=10,
                                                  pady=10, sticky="w")
        self.register_password = EntryWithPlaceholder(register_frame, placeholder="Şifre", show="*")
        self.register_password.grid(column=1,
                                    row=1)

        ttk.Label(register_frame,
                  text="Şifre Tekrar:", anchor='w').grid(column=0,
                                                         row=2,
                                                         padx=10,
                                                         pady=10, sticky="w")
        self.register_password_again = EntryWithPlaceholder(register_frame, placeholder="Şifre Tekrar", show="*")
        self.register_password_again.grid(column=1,
                                          row=2)

        ttk.Button(register_frame, text="Hesabım VAR!", command=self.giris_gecis).grid(column=0,
                                                                                row=3,
                                                                                padx=30,
                                                                                pady=30,
                                                                                sticky="e")


        ttk.Button(register_frame, text="Kayıt Ol", command=self.kayit_ol).grid(column=1,
                                                                                row=3,
                                                                                padx=30,
                                                                                pady=30,
                                                                                sticky="e")

        for widget in (self.register_username, self.register_password, self.register_password_again):
            widget.lift()


    def giris_gecis(self):
        self.tabControl.select(self.tab1)
        pass

    def kayit_ol_gecis(self):
        self.tabControl.select(self.tab2)
        pass
    def quit(self):
        self.database.db.close()
        self.destroy()
    def giris(self):
        username = self.username.get()
        password = self.password.get()

        query = "SELECT * FROM users WHERE username=? AND password=?"
        result = self.database.run_query(query, (username, password))
        if result:
            messagebox.showinfo("Giriş Başarılı", "Hoşgeldiniz")
            self.logged_in = username
            self.quit()
        else:
            messagebox.showerror('hata', "Giriş Başarısız")

        pass
    def kayit_ol(self):
        username = self.register_username.get()
        password = self.register_password.get()
        password_again = self.register_password_again.get()

        if password != password_again:
            messagebox.showerror("Hata", "Şifreler uyuşmuyor")
            return
        query = "SELECT * FROM users WHERE username=?"
        result = self.database.run_query(query, (username,))
        if result:
            messagebox.showerror("Hata", "Bu kullanıcı adı kullanılıyor")
            return
        query = "INSERT INTO users VALUES(?, ?)"
        self.database.insert_field(query, (username, password))
        self.logged_in = username
        messagebox.showinfo("Başarılı", "Kayıt Başarılı")
        self.quit()
        pass
