import customtkinter as ctk

from .CTkToolTip import CTkToolTip

class QRCodeTip(CTkToolTip):
    def __init__(self, master: ctk.CTkButton) -> None:
        """
        A tooltip telling you to click to enlarge the QR code.

        Args:
            master (ctk.CTkButton): the widget that will recieve the tooltip
        """

        super().__init__(widget = master,
                         message = "Open QR code...",
                         delay = 0
                         )

class TableTip(CTkToolTip):
    def __init__(self, master: ctk.CTkButton) -> None:
        """
        A tooltip telling you to click to disconnect a device.

        Args:
            master (ctk.CTkButton): the widget that will recieve the tooltip
        """

        super().__init__(widget = master,
                        message = "Disconnect device...",
                        delay = 0
                        )
