# Python Kurs bitirme projesi
 Kursumuz için tkinter ile aşağıda bulunan özelliklere sahip bir projemiz var.
- Sqlite veritabanı ve tkinter ile kullanıcı arayüzü
- Giriş ve Kayıt ol formu ile başlar. 
- Kullanıcı girişi yapılırsa, kullanıcı ana ekrana yönlendirilir.
- Treeview ile listelenmiş öğrenci listesi ile karşılaşır.
- Öğrenci ekleme, düzenleme ve silme işlemleri yapılır.


### Aldığım hatalar ve çözümlerim

Kullanıcı input girişlerinde StringVar ı ş gibi harfler girdiğinde Ý ý gözüküyor. 
Bunu çözmek için StringVar kalıtı kullanarak girilen harfleri replace ile çözdük.

    class StringVar(tk.StringVar):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self.trace("w", lambda name, index, mode, sv=self: self.convert(sv))
        def convert(self, sv):
            translate = sv.get().replace("ý", "ı").replace("þ", "ş").replace("Þ", "Ş").replace("Ý", "İ").replace("ð", "ğ").replace("Ð", "Ğ")
            sv.set(translate)

Placeholder için bir metod buldum ancak ondada şifre alanı yani show kullanılınca placeholder'de *** böyle gözüküyordu.
EntryWithPlaceholder ile placeholder'ı göstermek için kullandım. 