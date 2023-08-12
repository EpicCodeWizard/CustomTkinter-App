import customtkinter as ctk

from .config import LABEL_HEIGHT

class LocalNetwork(ctk.CTkLabel):
    def __init__(self, master: ctk.CTk, font: tuple) -> None:
        """
        A widget to explain the textbox below it.
        Hint: run the application.

        Args:
            master (ctk.CTk): where the widget will be placed
            font (tuple): font for the text
        """

        super().__init__(master = master,
                         text = "Local Network URL:",
                         font = (font[0], 16),
                         height = LABEL_HEIGHT
                         )

class PublicNetwork(ctk.CTkLabel):
    def __init__(self, master: ctk.CTk, font: tuple) -> None:
        """
        A widget to explain the textbox below it.
        Hint: run the application.

        Args:
            master (ctk.CTk): where the widget will be placed
            font (tuple): font for the text
        """

        super().__init__(master = master,
                         text = "Public Network URL:",
                         font = (font[0], 16),
                         height = LABEL_HEIGHT
                         )
