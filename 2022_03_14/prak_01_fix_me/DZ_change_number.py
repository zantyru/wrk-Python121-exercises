import tkinter as tk


class Changenum(tk.Frame):  # Цифра не изменяется
    def __init__(self, *args, **kwargs):
        super(Changenum, self).__init__(*args, **kwargs)

        self.entry_text = tk.StringVar()
        # self.entry_text.set("0")
        self.entry = tk.Entry(self, textvariable=self.entry_text)
        self.entry.grid(column=1, columnspan=2, row=2)

        btn_add = tk.Button(self, text="+")
        btn_add.grid(row=2)

        btn_sub = tk.Button(self, text="-")
        btn_sub.grid(column=4, row=2)

        ERROR_TEXT = "Ошибка"

        def get_number_or_none(text_value):
            try:
                x = float(text_value)
            except ValueError:
                x = None
            except TypeError:
                x = None
            return x

        def do_addition(num):
            num = get_number_or_none(num)

            if num is not None:
                result = num + 1
            else:
                result = ERROR_TEXT

            return result

        def do_subtraction(num):
            num = get_number_or_none(num)

            if num is not None:
                result = num - 1
            else:
                result = ERROR_TEXT

            return result

        def action(num, op):
            result = op(num)
            self.entry_text.set(result)

        btn_add.configure(
            command=lambda: action(
                self.entry_text.get(),
                do_addition
            )
        )
        btn_sub.configure(
            command=lambda: action(
                self.entry_text.get(),
                do_subtraction
            )
        )


class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        super(App, self).__init__(*args, **kwargs)
        change = Changenum(self)
        change.pack()

    def run(self):
        self.mainloop()
