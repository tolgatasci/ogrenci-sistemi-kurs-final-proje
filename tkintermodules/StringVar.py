import tkinter as tk


class StringVar(tk.StringVar):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.trace("w", lambda name, index, mode, sv=self: self.convert(sv))
    def convert(self, sv):
        translate = sv.get().replace("ý", "ı").replace("þ", "ş").replace("Þ", "Ş").replace("Ý", "İ").replace("ð", "ğ").replace("Ð", "Ğ")
        sv.set(translate)


