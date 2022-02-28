import tkinter as tk


def start_demo():

    root = tk.Tk()
    lbl = tk.Label(root, text="Слово.")
    lbl.grid(columnspan=3, row=0)  # Раньше был метод pack()

    frame1 = tk.Frame(root)
    btn1_frame1 = tk.Button(frame1, text="Кнопка")
    btn1_frame1.pack()
    btn2_frame1 = tk.Button(frame1, text="Кнопка")
    btn2_frame1.pack()
    btn3_frame1 = tk.Button(frame1, text="Кнопка")
    btn3_frame1.pack()
    frame1.grid(column=1, row=1)

    root.mainloop()


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

    def run(self):
        self.mainloop()


if __name__ == '__main__':
    # start_demo()

    app = DemoApp()
    app.run()
