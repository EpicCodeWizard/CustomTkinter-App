import customtkinter as ctk

from .config import LABEL_HEIGHT

class LocalCopy(ctk.CTkButton):
    def __init__(self, master: ctk.CTk, font: tuple) -> None:
        """
        A widget to copy the text in the local URL box.

        Args:
            master (ctk.CTk): where the widget will be placed
            font (tuple): font for the text
        """

        super().__init__(master = master,
                         text = "Copy",
                         command = self.copy,
                         font = (font[0], 16),
                         width = 90,
                         height = LABEL_HEIGHT
                         )

    def copy(self) -> None:
        """
        Copys the value of the local URL box.
        """

class PublicCopy(ctk.CTkButton):
    def __init__(self, master: ctk.CTk, font: tuple) -> None:
        """
        A widget to copy the text in the public URL box.

        Args:
            master (ctk.CTk): where the widget will be placed
            font (tuple): font for the text
        """

        super().__init__(master = master,
                         text = "Copy",
                         command = self.copy,
                         font = (font[0], 16),
                         width = 90,
                         height = LABEL_HEIGHT
                         )

    def copy(self) -> None:
        """
        Copys the value of the public URL box.
        """
