import customtkinter as ctk
from PIL import Image

from .config import LABEL_HEIGHT

class Mode(ctk.CTkButton):
    def __init__(self, master: ctk.CTk) -> None:
        """
        A button that allows the user to switch between light an dark mode.

        Args:
            master (ctk.CTk): where the widget will be placed
        """

        self.light = Image.open("./assets/icons/light.png")
        self.dark = Image.open("./assets/icons/dark.png")
        self.image = ctk.CTkImage(light_image = self.dark,
                                  dark_image = self.light,
                                  size = (LABEL_HEIGHT, LABEL_HEIGHT)
                                  )

        super().__init__(master = master,
                         text = "",
                         image = self.image,
                         height = LABEL_HEIGHT,
                         width = LABEL_HEIGHT,
                         command = self.switch_mode
                         )

    def switch_mode(self) -> None:
        """
        Changes the appearance mode.
        """

        if ctk.get_appearance_mode().lower() == "dark":
            ctk.set_appearance_mode("Light")
        elif ctk.get_appearance_mode().lower() == "light":
            ctk.set_appearance_mode("Dark")
