# -*- coding: utf-8 -*-
import io
import uuid
from datetime import date
import tkinter as tk
from tkinter import ttk, TOP, messagebox, BOTTOM, filedialog
from PIL import ImageTk, Image
import locale
from tkcalendar import Calendar, DateEntry

from tkintermodules import tkentrycomplete
from tkintermodules.StringVar import StringVar
import timeit

from tkintermodules.tkentrycomplete import AutocompleteEntry

locale.setlocale(locale.LC_ALL, 'tr_TR.utf8')

class CreateStudent(tk.Toplevel):
    def __init__(self, parent,  **kwargs):
        super().__init__(parent)

        self.transient(parent)
        self.resizable(False, False)
        self.geometry("900x600+500+300")
        self.app = parent
        self.title("Öğrenci Ekle")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.form = ttk.Frame(self, relief='raised', borderwidth=1)
        self.form.grid(column=0, row=0,sticky="news",padx=10, pady=10)
        self.form.columnconfigure(0, weight=1)
        self.form.rowconfigure(0, weight=1)
        self.create_widgets()
    def tarih_sec(self, event=None):
        pass
    def selected_date(self, event=None):
        try:
            tarih = self.ogrenci_dtarihi_entry.selection_get()
            self.ogrenci_dtarihi_entry.delete(0, tk.END)
            self.ogrenci_dtarihi_entry.insert(0, tarih)
        except:
            pass
    def create_widgets(self):
        self.ok_button = ttk.Button(self.form, text="Ekle", command=self.on_ok)
        self.ok_button.pack(side=BOTTOM, fill=tk.X)
        # ("id", "adsoyad", "dyeri", "dtarihi", "ogrenimturu", "il", "ilce", "adres","fotograf")
        self.custom_font = ('calibri', 12, 'bold')
        self.ogrenci_adi_soyadi = StringVar()

        self.ogrenci_dyeri = StringVar()
        self.ogrenci_dtarihi = StringVar()
        self.ogrenci_ogrenimturu = StringVar()
        self.ogrenci_il = StringVar()
        self.ogrenci_ilce = StringVar()
        self.ogrenci_adres = StringVar()
        self.ogrenci_fotograf = tk.StringVar()
        self.ogrenci_adi_soyadi_label = ttk.Label(self.form, text="Öğrenci Adı Soyadı:")
        self.ogrenci_adi_soyadi_label.pack(side=TOP, fill=tk.X)
        self.ogrenci_adi_soyadi_entry = ttk.Entry(self.form, textvariable=self.ogrenci_adi_soyadi)
        self.ogrenci_adi_soyadi_entry.pack(side=TOP, fill=tk.X)



        self.ogrenci_dyeri_label = ttk.Label(self.form, text="Doğum Yeri:")
        self.ogrenci_dyeri_label.pack(side=TOP, fill=tk.X)
        self.ogrenci_dyeri_entry = ttk.Entry(self.form, textvariable=self.ogrenci_dyeri)
        self.ogrenci_dyeri_entry.pack(side=TOP, fill=tk.X)
        self.ogrenci_dtarihi_label = ttk.Label(self.form, text="Doğum Tarihi:")
        self.ogrenci_dtarihi_label.pack(side=TOP, fill=tk.X)
        self.ogrenci_dtarihi_entry = DateEntry(self.form,textvariable=self.ogrenci_dtarihi, width=12, background='darkblue',
                                               foreground='white', borderwidth=2,state="readonly")

        self.ogrenci_dtarihi_entry.pack(side=TOP, fill=tk.X)


        self.ogrenci_ogrenimturu_label = ttk.Label(self.form, text="Öğrenim Türü:")
        self.ogrenci_ogrenimturu_label.pack(side=TOP, fill=tk.X)


        self.ogrenci_ogrenimturu_entry = ttk.Entry(self.form, textvariable=self.ogrenci_ogrenimturu)
        self.ogrenci_ogrenimturu_entry.pack(side=TOP, fill=tk.X)
        #self.ogrenci_dtarihi_entry.bind("<FocusIn>", self.tarih_sec)
        self.ogrenci_dtarihi_entry.bind("<<DateEntrySelected>>",self.selected_date)


        self.ogrenci_il_label = ttk.Label(self.form, text="İl:")
        self.ogrenci_il_label.pack(side=TOP, fill=tk.X)
        options = ['Adana', 'Adıyaman', 'Afyon', 'Ağrı', 'Amasya', 'Ankara', 'Antalya', 'Artvin',
                   'Aydın', 'Balıkesir', 'Bilecik', 'Bingöl', 'Bitlis', 'Bolu', 'Burdur', 'Bursa', 'Çanakkale',
                   'Çankırı', 'Çorum', 'Denizli', 'Diyarbakır', 'Edirne', 'Elazığ', 'Erzincan', 'Erzurum', 'Eskişehir',
                   'Gaziantep', 'Giresun', 'Gümüşhane', 'Hakkari', 'Hatay', 'Isparta', 'Mersin', 'İstanbul', 'İzmir',
                   'Kars', 'Kastamonu', 'Kayseri', 'Kırklareli', 'Kırşehir', 'Kocaeli', 'Konya', 'Kütahya', 'Malatya',
                   'Manisa', 'Kahramanmaraş', 'Mardin', 'Muğla', 'Muş', 'Nevşehir', 'Niğde', 'Ordu', 'Rize', 'Sakarya',
                   'Samsun', 'Siirt', 'Sinop', 'Sivas', 'Tekirdağ', 'Tokat', 'Trabzon', 'Tunceli', 'Şanlıurfa', 'Uşak',
                   'Van', 'Yozgat', 'Zonguldak', 'Aksaray', 'Bayburt', 'Karaman', 'Kırıkkale', 'Batman', 'Şırnak',
                   'Bartın', 'Ardahan', 'Iğdır', 'Yalova', 'Karabük', 'Kilis', 'Osmaniye', 'Düzce']

        self.ogrenci_il_combobox =  AutocompleteEntry(self.form,options, listboxLength=6,stringvar=self.ogrenci_il)

        self.ogrenci_il_combobox.pack(side=TOP, fill=tk.X)
        self.ogrenci_ilce_label = ttk.Label(self.form, text="İlçe:")
        self.ogrenci_ilce_label.pack(side=TOP, fill=tk.X)
        self.ogrenci_ilce_entry = ttk.Entry(self.form, textvariable=self.ogrenci_ilce)
        self.ogrenci_ilce_entry.pack(side=TOP, fill=tk.X)
        self.ogrenci_adres_label = ttk.Label(self.form, text="Adres:")
        self.ogrenci_adres_label.pack(side=TOP, fill=tk.X)
        self.ogrenci_adres_entry = ttk.Entry(self.form, textvariable=self.ogrenci_adres)
        self.ogrenci_adres_entry.pack(side=TOP, fill=tk.X)

        self.Artwork = ttk.Label(self.form, anchor="center")

        self.Artwork.pack(side=TOP, fill=tk.X)

        self.ogrenci_fotograf_button = ttk.Button(self.form, text="Fotoğraf Seç", command=self.on_fotograf_sec)
        self.ogrenci_fotograf_button.pack(side=TOP, fill=tk.X)
        self.ogrenci_fotograf_button.bind("<Return>", self.on_fotograf_sec)



    def on_fotograf_sec(self, event=None):
        self.image_upload = filedialog.askopenfilename(initialdir=".", title="Fotoğraf Seç",
                                                       filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
        image_label = ttk.Label(self.form, text=self.image_upload)
        image_label.pack()

        img = Image.open(self.image_upload)
        img = img.resize((500, 500))
        img = img.convert("RGB")
        with io.BytesIO() as f:
            img.save(f, "JPEG")
            self.image_upload = f.getvalue()
            self.my_img = self.image_upload

        photo2 = ImageTk.PhotoImage(Image.open(io.BytesIO(self.my_img)).resize((150, 150), Image.ANTIALIAS))

        self.Artwork.configure(image=photo2)

        """ self.app.database.db.execute(
        '''INSERT INTO ogrenciler (adsoyad, dyeri, dtarihi, ogrenimturu, il, ilce, adres, fotograf) VALUES (?,?,?,?,?,?,?,?)''',
        ("tolga tasc","uskudar", "04-04-1555", "açık öğretim", "istanbul", "ataşehir","adx", self.image_upload))
        self.app.database.db.commit()"""

    def on_ok(self, event=None):
        if self.ogrenci_adi_soyadi.get() == "":
            messagebox.showwarning("Hata", "Öğrenci Adı Soyadı boş olamaz!")
            return
        if self.ogrenci_dyeri.get() == "":
            messagebox.showwarning("Hata", "Doğum Yeri boş olamaz!")
            return
        if self.ogrenci_dtarihi.get() == "":
            messagebox.showwarning("Hata", "Doğum Tarihi boş olamaz!")
            return
        if self.ogrenci_ogrenimturu.get() == "":
            messagebox.showwarning("Hata", "Öğrenim Türü boş olamaz!")
            return
        if self.ogrenci_il.get() == "":
            messagebox.showwarning("Hata", "İl boş olamaz!")
            return
        if self.ogrenci_ilce.get() == "":
            messagebox.showwarning("Hata", "İlçe boş olamaz!")
            return
        if self.ogrenci_adres.get() == "":
            messagebox.showwarning("Hata", "Adres boş olamaz!")
            return
        if "my_img" not in self.__dict__:
            messagebox.showwarning("Hata", "Fotoğraf boş olamaz!")
            return
        self.app.database.run_query(
            '''INSERT INTO ogrenciler (adsoyad, dyeri, dtarihi, ogrenimturu, il, ilce, adres, fotograf) VALUES (?,?,?,?,?,?,?,?)''',
            (self.ogrenci_adi_soyadi.get(), self.ogrenci_dyeri.get(), self.ogrenci_dtarihi.get(),
             self.ogrenci_ogrenimturu.get(), self.ogrenci_il.get(), self.ogrenci_ilce.get(),
             self.ogrenci_adres.get(), self.my_img))
        self.app.ogrenci_listele()
        messagebox.showinfo("Ekleme İşlemi", "Başarılı!")
        self.destroy()

    def on_cancel(self, event=None):
        self.destroy()
