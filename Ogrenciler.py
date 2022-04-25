import io
import tkinter
from datetime import date
import tkinter as tk
from tkinter import ttk, TOP, messagebox, BOTTOM
from tkinter.messagebox import askyesno

from libs.CreateStutent import CreateStudent
from libs.UpdateStudent import UpdateStudent
from tkintermodules.EntryWithPlaceholder import EntryWithPlaceholder
from PIL import ImageTk, Image
from libs.Database import Database
from tkintermodules.MenuBuilder import MenuBuilder


class Ogrenciler(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Ogrenciler")
        self.database = Database("ogrenciler.db")
        self.database.create_table("ogrenciler",
                                   "id integer primary key,adsoyad text,dyeri text,dtarihi text,ogrenimturu text,il text,ilce text,adres text,fotograf blob text")
        self.resizable(False, False)
        self.geometry("750x500")

        self.w, self.h = self.winfo_screenwidth(), self.winfo_screenheight()
        self.create_widgets()

    def create_widgets(self):
        self.buttons = ttk.Frame(self)
        self.buttons.grid(column=0, row=0, sticky="w", padx=10, pady=10)

        self.listeframe = ttk.Frame(self)
        self.listeframe.grid(column=0, row=1, sticky="NESW", padx=10, pady=10)

        ttk.Button(self.buttons, text="Listeyi Yenile", command=self.ogrenci_listele).grid(column=0,row=0)
        ttk.Button(self.buttons, text="Yeni Öğrenci", command=self.ogrenci_ekle).grid(column=1,row=0)
        style = ttk.Style(self)
        style.configure('Treeview', rowheight=40)  # Treeview'ın satırlarının yüksekliğini ayarlıyoruz.



        # Treeview oluşturuyoruz
        self.ogrenci_listele_tree = ttk.Treeview(self.listeframe, columns=(
        "id", "adsoyad", "dyeri", "dtarihi", "ogrenimturu", "il", "ilce", "adres", "fotograf"))




        # Kolonlara isim veriyoruz.
        self.ogrenci_listele_tree.grid(row=0, column=0, sticky="nsew")
        self.ogrenci_listele_tree.heading("#0", text="Fotoğraf")
        self.ogrenci_listele_tree.heading("id", text="Öğrenci ID")
        self.ogrenci_listele_tree.heading("adsoyad", text="Ad Soyad")
        self.ogrenci_listele_tree.heading("dyeri", text="Doğum Yeri")
        self.ogrenci_listele_tree.heading("dtarihi", text="Doğum Tarihi")
        self.ogrenci_listele_tree.heading("ogrenimturu", text="Öğrenim Türü")
        self.ogrenci_listele_tree.heading("il", text="İl")
        self.ogrenci_listele_tree.heading("ilce", text="İlçe")
        self.ogrenci_listele_tree.heading("adres", text="Adres")

        # Boyut ve özellikleri ayarlanıyor.
        self.ogrenci_listele_tree.column("id", width=int(self.w / 25), anchor="center")
        self.ogrenci_listele_tree.column("adsoyad", width=int(self.w / 25), anchor="center")
        self.ogrenci_listele_tree.column("dyeri", width=int(self.w / 25), anchor="center")
        self.ogrenci_listele_tree.column("dtarihi", width=int(self.w / 25), anchor="e")
        self.ogrenci_listele_tree.column("ogrenimturu", width=int(self.w / 25), anchor="e")
        self.ogrenci_listele_tree.column("il", width=int(self.w / 25), anchor="e")
        self.ogrenci_listele_tree.column("ilce", width=int(self.w / 25), anchor="e")
        self.ogrenci_listele_tree.column("adres", width=int(self.w / 25), anchor="e")
        self.ogrenci_listele_tree.column("#0", width=int(self.w / 25), anchor="center", stretch=True)
        self.ogrenci_listele_tree.column("#9", width=0, anchor="center", stretch="no")

        # Add Scroolbar
        self.scrollbar = ttk.Scrollbar(self.listeframe, orient="vertical", command=self.ogrenci_listele_tree.yview)
        self.scrollbar.grid(row=0, column=1, sticky="nsew")
        self.ogrenci_listele_tree.configure(yscrollcommand=self.scrollbar.set)





        self.ogrenci_listele()

        MenuBuilder(self.ogrenci_listele_tree, selectmode='multiple', app=self)

    def ogrenci_listele(self):
        self.ogrenci_listele_tree.delete(*self.ogrenci_listele_tree.get_children())
        data = self.database.run_query("SELECT * FROM ogrenciler", ())

        for row in data:
            x = (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])

            # direk values row atabiliriz ancak düzenlemek istiyorsak tuple yapıyoruz.
            # row[0] = 1 # hata verir

            img = ImageTk.PhotoImage(Image.open(io.BytesIO(row[8])).resize((25, 25), Image.ANTIALIAS))

            # tree görseli eklemek için garip bug var
            # öncellikle boş bir label oluşturmamız gerekiyor.
            self.Artwork = ttk.Label(self.buttons, image=img)
            self.Artwork.photo = img

            # tree sql çektiğimiz satırları yazdırıyoruz.
            self.ogrenci_listele_tree.insert("", tk.END, text="", values=x, image=img)

    def ogrenci_ekle(self):
        CreateStudent(self)  # CreateStudent classını çağırıyoruz.
        # self.ogrenci_listele_tree.insert('', tk.END, values=[1, 2, 3, 4, 5, 6, 7, 8, 9])

    def delete_selected(self):
        # Seçilmiş olan satırları getirir. Ancak bizim için bu kullanımın mantığı çok basit.
        # Biz sağ tıklandığında zaten tek bir row seçtiriyoruz. Bu yüzden tek satır seçilmiş demektir.
        for item in self.ogrenci_listele_tree.selection():
            # tree'den seçilen satırı siler.

            it = self.ogrenci_listele_tree.item(item).values()
            val = dict(zip(["1", "2", "data"], it))
            get_id = val['data'][0]
            # self.ogrenci_listele_tree.item(item, values=("asd", "asd", "asd", "asd", "asd", "asd", "asd", "asd"))
            answer = askyesno(title='ONAY', message='Silmek istediğinizden emin misiniz?')
            if answer:
                self.database.delete("DELETE FROM ogrenciler WHERE id = {}".format(get_id))

                self.ogrenci_listele_tree.delete(item)
                messagebox.showinfo("Silme İşlemi", "Başarılı!")



    def edit_selected(self):
        for item in self.ogrenci_listele_tree.selection():
            # tree'den seçilen satırı düzenler.
            it = self.ogrenci_listele_tree.item(item).values()
            val = dict(zip(["1", "2", "data"], it))
            get_id = val['data'][0]

            # self.ogrenci_listele_tree.item(item, values=("asd", "asd", "asd", "asd", "asd", "asd", "asd", "asd"))
            UpdateStudent(self,id=get_id,app=self)
    def ogrenci_fotograf_ekle(self):
        pass
