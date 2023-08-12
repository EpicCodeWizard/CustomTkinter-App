import customtkinter as ctk

from .config import LABEL_HEIGHT

class LocalURL(ctk.CTkEntry):
    def __init__(self, master: ctk.CTk, font: tuple) -> None:
        """
        A widget that shows the URL for the local network.

        Args:
            master (ctk.CTk): where the widget will be placed
            font (tuple): font for the text
        """

        self.url = ""
        self.font = (font[0], 16)
        super().__init__(master = master,
                         placeholder_text = self.url,
                         font = self.font,
                         height = LABEL_HEIGHT,
                         state = ctk.DISABLED
                         )

    def set_url(self, url: str) -> None:
        """
        Sets the new URL (value) of this widget.

        Args:
            url (str): the URL for the local network
        """

        self.url = url

        self.configure(state = ctk.NORMAL)
        self.configure(require_redraw = True,
                       placeholder_text = self.url
                       )
        self.configure(state = ctk.DISABLED)

class PublicURL(ctk.CTkEntry):
    def __init__(self, master: ctk.CTk, font: tuple) -> None:
        """
        A widget that shows the URL for the public network.

        Args:
            master (ctk.CTk): where the widget will be placed
            font (tuple): font for the text
        """

        self.url = ""
        self.font = (font[0], 16)
        super().__init__(master = master,
                         placeholder_text = self.url,
                         font = self.font,
                         height = LABEL_HEIGHT,
                         state = ctk.DISABLED
                         )

    def set_url(self, url: str) -> None:
        """
        Sets the new URL (value) of this widget.

        Args:
            url (str): the URL for the public network
        """

        self.url = url

        self.configure(state = ctk.NORMAL)
        self.configure(require_redraw = True,
                       placeholder_text = self.url,
                       )
        self.configure(state = ctk.DISABLED)
