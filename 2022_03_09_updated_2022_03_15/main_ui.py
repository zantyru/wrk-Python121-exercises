import tkinter as tk
import cloakroom as cr


class TagsTableFrame(tk.Frame):

    def __init__(self, *args, cloakroom_instance=None, **kwargs):
        super(TagsTableFrame, self).__init__(*args, **kwargs)

        if not isinstance(cloakroom_instance, cr.Cloakroom):
            raise TypeError(
                "Не передан экземпляр класса Cloakroom"
            )

        self.__cloakroom_instance = cloakroom_instance

        free_tags = [*self.__cloakroom_instance.get_free_tags()]
        acquired_tags = [*self.__cloakroom_instance.get_acquired_tags()]
        tags_count = len(free_tags) + len(acquired_tags)

        self.buttons = []
        for tag_number in range(1, tags_count + 1):
            btn = tk.Button(self, width=6, height=1, text=str(tag_number))
            btn.grid(
                column=(tag_number - 1) % 10,
                row=(tag_number - 1) // 10
            )
            self.buttons.append(btn)

        self.refresh()

    def refresh(self):
        """"""
        """Обновляет надписи на кнопках-номерках, показывая, выдан номерок или нет."""

        free_tags = set(self.__cloakroom_instance.get_free_tags())
        acquired_tags = set(self.__cloakroom_instance.get_acquired_tags())
        tags_count = len(free_tags) + len(acquired_tags)

        for tag_number in range(1, tags_count + 1):
            btn = self.buttons[tag_number - 1]
            if tag_number in free_tags:
                btn.configure(fg="#000")
            elif tag_number in acquired_tags:
                btn.configure(fg="#f00")


class CloakroomUI(tk.Tk):

    def __init__(self, cloakroom_instance, *args, **kwargs):
        super(CloakroomUI, self).__init__(*args, **kwargs)

        if not isinstance(cloakroom_instance, cr.Cloakroom):
            raise TypeError(
                "Не передан экземпляр класса Cloakroom"
            )

        self.__cloakroom_instance = cloakroom_instance

        self.geometry("800x600+100+100")
        self.configure(padx=20, pady=20, bg="#ccc")

        self.tags_table_frame = TagsTableFrame(
            self,
            cloakroom_instance=self.__cloakroom_instance
        )
        self.tags_table_frame.grid(
            column=0, row=0, columnspan=4
        )

        btn_acquire_free_tag = tk.Button(
            self,
            text="Выдать номерок посетителю",
            padx=10, pady=10,
            bg="#eeddff", fg="#000000",
            command=self._acquire_free_tag
        )
        btn_acquire_free_tag.grid(column=0, row=1, rowspan=2)

        self._lbl_acquire_free_tag = tk.Label(self, bg="#fff")
        self._lbl_acquire_free_tag.grid(column=1, row=2)

        btn_return_tag = tk.Button(
            self,
            text="Принять возвращаемый номерок",
            padx=10, pady=10,
            bg="#eeddff", fg="#000000"
        )
        btn_return_tag.grid(column=2, row=1, rowspan=2)

        self._ent_tag_string = tk.StringVar()
        ent_tag = tk.Entry(self, textvariable=self._ent_tag_string)
        ent_tag.grid(column=3, row=1)

        self._lbl_return_tag = tk.Label(self, bg="#fff")
        self._lbl_return_tag.grid(column=3, row=2)

    def _acquire_free_tag(self):
        try:
            tag = self.__cloakroom_instance.acquire_free_tag()
            self._lbl_acquire_free_tag.configure(
                text=f"Выдан номерок: {tag}"
            )
        except cr.NotEnoughTagsError:
            self._lbl_acquire_free_tag.configure(
                text="Свободных номерков нет!"
            )

        self.tags_table_frame.refresh()

    def _return_tag(self):
        pass  # решение ДЗ здесь (и в __init__)

        self.tags_table_frame.refresh()

    def run(self):
        self.mainloop()


if __name__ == '__main__':
    cloakroom = cr.Cloakroom(100)
    crui = CloakroomUI(cloakroom)
    crui.run()