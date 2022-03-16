import tkinter as tk


class MinusPlusButtonsFrame(tk.Frame):

    def __init__(self, *args, **kwargs):
        super(MinusPlusButtonsFrame, self).__init__(*args, **kwargs)
        self.__btn_minus = tk.Button(
            self, text="-", padx=4, pady=4,
            width=2, height=1, font=(None, 18)
        )
        self.__btn_plus = tk.Button(
            self, text="+", padx=4, pady=4,
            width=2, height=1, font=(None, 18)
        )
        self.__btn_minus.grid(column=0, row=0)
        self.__btn_plus.grid(column=1, row=0)

        self.configure(padx=10, pady=10)

    def setup_minus_command(self, func):
        self.__btn_minus.configure(command=func)

    def setup_plus_command(self, func):
        self.__btn_plus.configure(command=func)


class CounterFrame(tk.Frame):

    def __init__(self, *args, label="Счётчик", **kwargs):
        super(CounterFrame, self).__init__(*args, **kwargs)

        self.__value = 0
        self.__input_text = tk.StringVar(value="0")
        entry = tk.Entry(
            self, textvariable=self.__input_text,
            font=(None, 20)
        )
        mpbuttons = MinusPlusButtonsFrame(self)
        lbl = tk.Label(self, text=str(label))

        entry.grid(column=0, row=0)
        mpbuttons.grid(column=0, row=1)
        lbl.grid(column=0, row=2)

        self.configure(padx=10, pady=10)

        mpbuttons.setup_minus_command(self._decrease)
        mpbuttons.setup_plus_command(self._increase)

    def _increase(self):
        try:
            n = int(float(self.__input_text.get()))
            self.__value = n
            self.__value += 1
        except TypeError:
            pass
        except ValueError:
            pass

        self.__input_text.set(str(self.__value))

    def _decrease(self):
        try:
            n = int(float(self.__input_text.get()))
            self.__value = n
            self.__value -= 1
        except TypeError:
            pass
        except ValueError:
            pass

        self.__input_text.set(str(self.__value))

    @property
    def value(self):
        return self.__value


class ProbeControlFrame(tk.Frame):

    def __init__(self, *args, **kwargs):
        super(ProbeControlFrame, self).__init__(*args, **kwargs)

        mpbutton = MinusPlusButtonsFrame(self)
        label = tk.Label(
            self, text="Управление зондом",
            font=(None, 18)
        )

        mpbutton.grid(column=0, row=0)
        label.grid(column=1, row=0)

        self.configure(padx=10, pady=20)


class App(tk.Tk):

    def __init__(self, *args, **kwargs):
        super(App, self).__init__(*args, **kwargs)

        probecontrol = ProbeControlFrame(self)
        probecontrol.grid(column=0, columnspan=3, row=1)

        counter_1 = CounterFrame(self, label="Давление")
        counter_2 = CounterFrame(self, label="Температура")
        counter_3 = CounterFrame(self, label="Освещённость")

        counter_1.grid(column=0, row=0)
        counter_2.grid(column=1, row=0)
        counter_3.grid(column=2, row=0)

        copy_button = tk.Button(self, text="Скопировать давление")
        copy_button.grid(column=0, row=2)

        copy_label = tk.Label(self)
        copy_label.grid(column=1, row=2)

        def do_copy():
            copy_label.configure(
                text=str(counter_1.value)
            )

        copy_button.configure(command=do_copy)
