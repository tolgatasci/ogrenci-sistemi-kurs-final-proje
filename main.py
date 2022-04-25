from Ogrenciler import Ogrenciler

from LoginRegister import LoginRegister

login = LoginRegister()

login.mainloop()
from Ogrenciler import Ogrenciler

try:
    if login.logged_in:
        ogrenci = Ogrenciler()
        ogrenci.mainloop()
except:
    pass



#ogrenci = Ogrenciler()
#ogrenci.mainloop()