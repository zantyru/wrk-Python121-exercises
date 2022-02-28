import tkinter as tk


class TripleButton(tk.Frame):
    def __init__(self, *args, **kwargs):
        super(TripleButton, self).__init__(*args, **kwargs)
        self.btn1 = tk.Button(self, text="Кнопка")
        self.btn1.pack()
        self.btn2 = tk.Button(self, text="Кнопка")
        self.btn2.pack()
        self.btn3 = tk.Button(self, text="Кнопка")
        self.btn3.pack()


class DemoApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        super(DemoApp, self).__init__(*args, **kwargs)
        self.__lbl = tk.Label(self, text="Слово.")
        self.__lbl.grid(columnspan=3, row=0)  # Раньше был pack()
        self.frame1 = TripleButton(self)
        self.frame1.grid(column=1, row=1)
        self.frame2 = TripleButton(self)
        self.frame2.grid(column=2, row=1)
        self.frame3 = TripleButton(self)
        self.frame3.grid(column=3, row=1)

        self.frame1.btn1.configure(
            command=lambda: self.change_label_text("Нажатие!")
        )
        self.frame2.btn2.configure(
            command=lambda: self.change_label_text("Другое нажатие!")
        )

    def change_label_text(self, new_text):
        self.__lbl.configure(text=new_text)

    def run(self):
        self.mainloop()


if __name__ == '__main__':
    app = DemoApp()
    app.run()
