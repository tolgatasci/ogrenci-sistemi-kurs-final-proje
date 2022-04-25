import tkinter


class MenuBuilder(tkinter.Listbox):

    def __init__(self, parent, *args, **kwargs):
        self.app = kwargs['app']


        del kwargs['app']
        tkinter.Listbox.__init__(self, parent, *args, **kwargs)

        self.popup_menu = tkinter.Menu(parent, tearoff=0)
        self.popup_menu.add_command(label="Düzenle", command=self.app.edit_selected)
        self.popup_menu.add_command(label="Sil",
                                    command=self.app.delete_selected)

        self.parent = parent
        parent.bind("<Button-3>", self.popup)

    def popup(self, event):
        try:
            iid = self.parent.identify_row(event.y)
            if iid:
                self.app.selected_row = iid
                self.parent.selection_set(iid)
            self.popup_menu.tk_popup(event.x_root, event.y_root, 0)


        finally:
            self.popup_menu.grab_release()

    def delete_selected(self):
        for i in self.curselection()[::-1]:
            self.delete(i)

    def select_all(self):
        self.selection_set(0, 'end')