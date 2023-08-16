import customtkinter as ctk
from PIL import Image
import tkinter as tk
import time

from .modal import Modal

def get_screen_size():
    """
    Workaround to get the size of the current screen in a multi-screen setup.

    Returns:
        geometry (List[int]): A list containing the width and height of the screen.
            [width, height]
    """
    root = tk.Tk()
    root.update_idletasks()
    root.attributes("-fullscreen", True)
    root.state("iconic")
    geometry = root.winfo_geometry()
    root.destroy()
    return [int(x) for x in geometry.split("+")[0].split("x")]

class QRCode(ctk.CTkButton):
    def __init__(self, master: ctk.CTk) -> None:
        """
        A widget to display the QR code (a .png image)

        Args:
            master (ctk.CTk): where the widget will be placed
        """

        self.image = None
        self.raw_image = None
        self.master = master
        self.scale = ctk.ScalingTracker.get_window_dpi_scaling(self.master)
        self.last_resize_time = 0  # Add this line to initialize a variable to track the last resize time

        super().__init__(master = self.master,
                         text = "",
                         fg_color = "transparent",
                         command = self.open_image,
                         state = ctk.ACTIVE,
                         # cursor = "cross"
                         )

        self.bind("<Configure>", self.dynamic_resize)

    def open_image(self) -> None:
        """
        Opens the QR code in the default image viewer.
        """

        Modal(self.image, 900, 900)

    def dynamic_resize(self, event) -> None:
        """
        Dynamically resizes the image to fill up the space of the button.
        """

        current_time = time.time()
        if current_time - self.last_resize_time < 0.1:  # Throttle the resize operation to once every 0.1 seconds
            return

        self.last_resize_time = current_time

        self.scale = ctk.ScalingTracker.get_window_dpi_scaling(self.master)
        side = min(event.width, event.height) / self.scale
        if not self.raw_image is None:
            self.image = ctk.CTkImage(light_image=self.raw_image,
                                      size=(side, side)
                                      )
        self.configure(True, image=self.image)

    def set_image(self,
                  path: str
                  ) -> None:
        """
        Change the QR code being displayed.

        Args:
            path (str): the path to the QR code (.png image)
            width (int | None, optional): width of the image in pixels. defaults to 140.
            height (int | None, optional): height of the image in pixels. defaults to 140.
        """

        self.raw_image = Image.open(path)
        self.image = ctk.CTkImage(light_image = self.raw_image,
                                  size = get_screen_size()
                                  )
        self.configure(True, image = self.image)
