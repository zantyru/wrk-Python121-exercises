import tkinter as tk


def main():
    root = tk.Tk()
    btn = tk.Button(root, text="###")
    btn.pack()

    def change_text(text):
        btn.configure(text=text)

    def adapter():
        change_text("dsdsfdsf")

    def adapter2():
        change_text("******")

    # btn.configure(command=adapter)
    btn.configure(command=lambda: change_text("Ура!"))

    root.mainloop()


if __name__ == '__main__':
    main()