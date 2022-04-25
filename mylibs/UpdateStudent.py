# -*- coding: utf-8 -*-
import io
import uuid
from datetime import date
import tkinter as tk
from tkinter import ttk, TOP, messagebox, BOTTOM, filedialog
from PIL import ImageTk, Image
from tkcalendar import DateEntry

from tkintermodules.StringVar import StringVar
from tkintermodules.tkentrycomplete import AutocompleteEntry


class UpdateStudent(tk.Toplevel):
    def __init__(self, parent,  **kwargs):
        super().__init__(parent)
        if "id" in kwargs:
            self.id = kwargs["id"]
        else:
            raise Exception("id parametresi eksik")
        if "app" in kwargs:
            self.app = kwargs["app"]
        self.ogrenci = self.app.database.run_query("SELECT * FROM ogrenciler WHERE id = ?", (self.id,))
        self.transient(parent)
        self.resizable(False, False)
        self.geometry("900x600+500+300")
        self.app = parent
        self.title("Öğrenci Düzenle")
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
        self.ok_button = ttk.Button(self.form, text="Kaydet", command=self.on_ok)
        self.ok_button.pack(side=BOTTOM, fill=tk.X)
        # ("id", "adsoyad", "dyeri", "dtarihi", "ogrenimturu", "il", "ilce", "adres","fotograf")
        self.ogrenci_adi_soyadi = StringVar(value=self.ogrenci[0][1])
        self.ogrenci_dyeri = StringVar(value=self.ogrenci[0][2])
        self.ogrenci_dtarihi = StringVar(value=self.ogrenci[0][3])
        self.ogrenci_ogrenimturu = StringVar(value=self.ogrenci[0][4])
        self.ogrenci_il = StringVar(value=self.ogrenci[0][5])
        self.ogrenci_ilce = StringVar(value=self.ogrenci[0][6])
        self.ogrenci_adres = StringVar(value=self.ogrenci[0][7])
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
        self.ogrenci_dtarihi_entry = DateEntry(self.form, textvariable=self.ogrenci_dtarihi, width=12,
                                               background='darkblue',
                                               foreground='white', borderwidth=2, state="readonly")

        self.ogrenci_dtarihi_entry.pack(side=TOP, fill=tk.X)

        self.ogrenci_ogrenimturu_label = ttk.Label(self.form, text="Öğrenim Türü:")
        self.ogrenci_ogrenimturu_label.pack(side=TOP, fill=tk.X)

        self.ogrenci_ogrenimturu_entry = ttk.Entry(self.form, textvariable=self.ogrenci_ogrenimturu)
        self.ogrenci_ogrenimturu_entry.pack(side=TOP, fill=tk.X)
        # self.ogrenci_dtarihi_entry.bind("<FocusIn>", self.tarih_sec)
        self.ogrenci_dtarihi_entry.bind("<<DateEntrySelected>>", self.selected_date)

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

        self.ogrenci_il_combobox = AutocompleteEntry(self.form, options, listboxLength=6, stringvar=self.ogrenci_il)

        self.ogrenci_il_combobox.pack(side=TOP, fill=tk.X)
        self.ogrenci_ilce_label = ttk.Label(self.form, text="İlçe:")
        self.ogrenci_ilce_label.pack(side=TOP, fill=tk.X)
        self.ogrenci_ilce_entry = ttk.Entry(self.form, textvariable=self.ogrenci_ilce)
        self.ogrenci_ilce_entry.pack(side=TOP, fill=tk.X)
        self.ogrenci_adres_label = ttk.Label(self.form, text="Adres:")
        self.ogrenci_adres_label.pack(side=TOP, fill=tk.X)
        self.ogrenci_adres_entry = ttk.Entry(self.form, textvariable=self.ogrenci_adres)
        self.ogrenci_adres_entry.pack(side=TOP, fill=tk.X)
        self.my_img = io.BytesIO(self.ogrenci[0][8]).getvalue()

        img = ImageTk.PhotoImage(Image.open(io.BytesIO(self.ogrenci[0][8])).resize((150, 150), Image.ANTIALIAS))

        # tree görseli eklemek için garip bug var
        # öncellikle boş bir label oluşturmamız gerekiyor.
        self.Artwork = ttk.Label(self.form, image=img, anchor="center")
        self.Artwork.photo = img
        self.Artwork.pack(side=TOP, fill=tk.X)
        self.ogrenci_fotograf_button = ttk.Button(self.form, text="Fotoğraf Seç", command=self.on_fotograf_sec)
        self.ogrenci_fotograf_button.pack(side=TOP, fill=tk.X)
        self.ogrenci_fotograf_button.bind("<Return>", self.on_fotograf_sec)



    def on_fotograf_sec(self, event=None):
        self.image_upload = filedialog.askopenfilename(initialdir=".", title="Fotoğraf Seç", filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
        image_label = ttk.Label(self.form, text= self.image_upload)
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
        if self.my_img == "":
            messagebox.showwarning("Hata", "Fotoğraf boş olamaz!")
            return
        self.app.database.run_query("update ogrenciler set adsoyad=?, dyeri=?, dtarihi=?, ogrenimturu=?, il=?, ilce=?, adres=?, fotograf=? where id=?",
                                    (self.ogrenci_adi_soyadi.get(), self.ogrenci_dyeri.get(), self.ogrenci_dtarihi.get(), self.ogrenci_ogrenimturu.get(), self.ogrenci_il.get(), self.ogrenci_ilce.get(), self.ogrenci_adres.get(), self.my_img,self.ogrenci[0][0]))
        self.app.database.db.commit()



        self.app.ogrenci_listele()
        messagebox.showinfo("Güncelleme Başarılı", "Başarılı!")
        self.destroy()

    def on_cancel(self, event=None):
        self.destroy()


