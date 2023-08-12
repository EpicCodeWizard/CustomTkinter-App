import customtkinter as ctk

from .modal import Modal
from .config import LABEL_HEIGHT

class Enlarge(ctk.CTkButton):
    def __init__(self, master: ctk.CTk, font: tuple) -> None:
        """
        A widget that opens up the modal of the QR code.

        Args:
            master (ctk.CTk): where the widget will be placed
            font (tuple): font for the text
        """

        self.master = master
        super().__init__(master = self.master,
                         text = "Enlarge",
                         font = (font[0], 16),
                         width = 110,
                         height = LABEL_HEIGHT,
                         command = self.open_image
                         )

    def open_image(self) -> None:
        """
        Opens the QR code in the default image viewer.
        """

        Modal(self.master.qr_code.image, 900, 900)
