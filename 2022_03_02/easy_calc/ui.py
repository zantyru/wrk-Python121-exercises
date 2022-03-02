import tkinter as tk


class EasyCalcFrame(tk.Frame):
    def __init__(self, *args, **kwargs):
        super(EasyCalcFrame, self).__init__(*args, **kwargs)

        self.output = tk.Entry(self, state=tk.DISABLED)
        self.output.grid(columnspan=4, row=0)

        lbl_left_number = tk.Label(self, text="Число 1")
        lbl_left_number.grid(columnspan=2, row=1)

        lbl_right_number = tk.Label(self, text="Число 2")
        lbl_right_number.grid(column=2, columnspan=2, row=1)

        self.ent_left_number = tk.Entry(self)
        self.ent_left_number.grid(columnspan=2, row=2)

        self.ent_right_number = tk.Entry(self)
        self.ent_right_number.grid(column=2, columnspan=2, row=2)

        btn_plus = tk.Button(self, text="+")
        btn_plus.grid(column=0, row=3)

        btn_minus = tk.Button(self, text="-")
        btn_minus.grid(column=1, row=3)

        btn_mul = tk.Button(self, text="*")
        btn_mul.grid(column=2, row=3)

        btn_div = tk.Button(self, text="/")
        btn_div.grid(column=3, row=3)


class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        super(App, self).__init__(*args, **kwargs)
        easy_calc_frame = EasyCalcFrame(self)
        easy_calc_frame.pack()

    def run(self):
        self.mainloop()


