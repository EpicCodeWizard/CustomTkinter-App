import customtkinter as ctk

from .publish import Publish
from .enlarge import Enlarge

class PublishEnlargeFrame(ctk.CTkFrame):
    def __init__(self, master: ctk.CTk, **kwargs) -> None:
        """
        A widget to hold a publish and enlarge button.

        Args:
            master (ctk.CTk): where the widget will be placed.
        """

        super().__init__(master = master, 
                         **kwargs
                         )

        self.grid_rowconfigure(0, weight = 1)
        self.grid_columnconfigure(0, weight = 1)
        self.grid_columnconfigure(1, weight = 1)

        self.font = ("DM Mono", 13)

        self.publish = Publish(self, self.font)
        self.publish.grid(row = 1, column = 0, sticky = "ew")

        self.enlarge = Enlarge(self, self.font)
        self.enlarge.grid(row=  1, column = 1, sticky = "se")