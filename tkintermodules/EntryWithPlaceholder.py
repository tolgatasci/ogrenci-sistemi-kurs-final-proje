import tkinter as tk

class EntryWithPlaceholder(tk.Entry):
    def __init__(self, master=None, placeholder="Placeholder", placeholder_color="#a3a3a3", **kwargs):
        # Eğer show parametresi girilmemişse, placeholder'ı göstermeyecek.
        # Ancak girilmiş ise, placeholderi göstermesi için show focus in olana kadar show kapalı.
        if 'show' in kwargs:
            self.show = kwargs['show']
            self._password = True
        else:
            self._password = False
        super().__init__(master, **kwargs)
        self.placeholder = placeholder
        self.placeholder_color = placeholder_color
        self.configure(show='')
        self.default_fg_color = self['fg']
        self.bind("<FocusIn>", self.foc_in)
        self.bind("<FocusOut>", self.foc_out)
        self.put_placeholder()

    def put_placeholder(self):
        self.insert(0, self.placeholder)
        self['fg'] = self.placeholder_color
    def foc_in(self, *args):
        if self._password:
            # Eğer _password true ise, şifreli olarak gösterir.
            self.configure(show=self.show)
        if self['fg'] == self.placeholder_color:
            self.delete('0', 'end')
            self['fg'] = self.default_fg_color
    def foc_out(self, *args):
        if not self.get():
            self.put_placeholder()
        if self._password:
            # eğer _password true ise ve placeholder dışında bir şey girilmişse, şifreli olarak gösterir.
            if self.get() == self.placeholder:
                self.configure(show='')