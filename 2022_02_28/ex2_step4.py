import tkinter as tk


def start_demo():

    root = tk.Tk()
    lbl = tk.Label(root, text="Слово.")
    lbl.grid(columnspan=3, row=0)  # Раньше был метод pack()

    def create_triple_button_frame(base):
        frame = tk.Frame(base)
        btn1 = tk.Button(frame, text="Кнопка")
        btn1.pack()
        btn2 = tk.Button(frame, text="Кнопка")
        btn2.pack()
        btn3 = tk.Button(frame, text="Кнопка")
        btn3.pack()
        return frame

    frame1 = create_triple_button_frame(root)
    frame1.grid(column=1, row=1)
    frame2 = create_triple_button_frame(root)
    frame2.grid(column=2, row=1)
    frame3 = create_triple_button_frame(root)
    frame3.grid(column=3, row=1)

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
        self.frame2 = TripleButton(self)
        self.frame2.grid(column=2, row=1)
        self.frame3 = TripleButton(self)
        self.frame3.grid(column=3, row=1)

    def run(self):
        self.mainloop()


if __name__ == '__main__':
    # start_demo()

    app = DemoApp()
    app.run()
