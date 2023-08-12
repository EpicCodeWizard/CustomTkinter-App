import customtkinter as ctk

from .config import PADX, PADY
from .CTkTable import CTkTable

class Devices(ctk.CTkScrollableFrame):
    def __init__(self, master: ctk.CTk | ctk.CTkToplevel, font: tuple) -> None:
        """
        A list of all currently connected devices.

        Args:
            master (ctk.CTk, ctk.CTkToplevel): where this widget will be placed
        """

        super().__init__(master = master,
                         fg_color = "transparent",
                         scrollbar_button_color = ctk.ThemeManager.theme["CTk"]["fg_color"],
                         )

        self.grid_rowconfigure(0, weight = 0)

        self.grid_columnconfigure(0, weight = 0)

        self.font = font
        self.height = 38
        self.values = [["category1", "category2", "category3", "category4"]]

        header_color = ctk.ThemeManager.theme["CTkTable"]["fg_color"]

        self.table = CTkTable(master = self,
                              font = self.font,
                              values = self.values,
                              command = self.disconnect_device,
                              height = self.height + 10,
                              header_color = header_color
                              )
        self.table.grid(row = 0,
                        column = 0,
                        padx = PADX,
                        pady = PADY,
                        sticky = "nsew"
                        )
        self.table.pack(expand = True, fill = "both")

        for x in range(30):
            self.add_device("data " + str(x), "data " + str(x))

    def remove_dupe(self) -> None:
        """
        Removes all duplicate values from our list.
        """

        self.values = [b for a, b in enumerate(self.values) if b not in self.values[:a]]

    def add_device(self, name: str, ip: str) -> None: # pylint: disable=invalid-name
        """
        Add a display/device to the table.

        Args:
            name (str): name of the device
            ip (str): IP address of the device
        """

        new_row = [name, ip, "", "Button"]
        self.table.add_row(values = new_row,
                           height = self.height
                           )
        self.values.append(new_row)

        self.remove_dupe()

        # row = len(self.values) - 1
        # self.table.insert(row,
        #                   3,
        #                   "Disconnect",
        #                   fg_color = "#A51F21"
        #                   )

    def disconnect_device(self, data: dict) -> None:
        """
        Disconnects any device given a row.

        Args:
            row (int): row in the table with all the devices
        """

        row = data["row"]
        column = data["column"]

        name = self.values[row][0]
        ip = self.values[row][1] # pylint: disable=invalid-name

        if column == 3 and row != 0:
            self.table.delete_row(row)
            self.values.pop(row)