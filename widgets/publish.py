import customtkinter as ctk

from .config import LABEL_HEIGHT

class Publish(ctk.CTkSwitch):
    def __init__(self, master: ctk.CTk, font: tuple) -> None:
        """
        A widget to turn on the usage of public network.

        Args:
            master (ctk.CTk): where the widget will be placed
            font (tuple): font for the widget's text
        """

        super().__init__(master = master,
                         text = "Publish",
                         font = (font[0], 16),
                         height = LABEL_HEIGHT,
                         command = self.publish
                         )

    def publish(self) -> None:
        """
        Publishes the URL to view a display/screen
        """

        if self.get() == 1:
            self.configure(text = "Unpublish")
            print("URL sucessfully published.")
        else:
            self.configure(text = "Publish")
            print("URL successfully unpublished.")
