import customtkinter as ctk

from .config import PADX, PADY

class Modal(ctk.CTkToplevel):
    def __init__(self, qr_code: ctk.CTkImage, width: int, height: int) -> None:
        """
        A widget to show the QR code in a bigger size.

        Args:
            qr_code (QRCode): the QR code to display
            width (int): width of this window
            height (int): height of this window
        """

        super().__init__()
        self.title("Scan the QR code:")
        self.geometry(f"{width}x{height}")
        self.resizable(False, False)

        self.grid_rowconfigure(0, weight = 1)
        self.grid_columnconfigure(0, weight = 1)

        self.scale = 1.0

        self.image = qr_code
        self.qr_code = ctk.CTkButton(master = self,
                                     text = "",
                                     fg_color = "transparent",
                                     image = qr_code,
                                     state = ctk.ACTIVE,
                                     command = self.close,
                                     # cursor = "X_cursor"
                                     )
        self.qr_code.grid(row = 0,
                          column = 0,
                          padx = PADX,
                          pady = PADY,
                          sticky = "nsew"
                          )

        self.qr_code.bind("<Configure>", self.resize)

    def resize(self, event) -> None:
        """
        Resizes the image to fill up the space of the button.
        """

        self.scale = ctk.ScalingTracker.get_window_dpi_scaling(self.master)

        side = min(event.width, event.height) / self.scale
        self.image.configure(size = (side, side))
        self.qr_code.configure(True, image = self.image)

    def close(self) -> None:
        """
        Closes this window.
        """

        self.destroy()
