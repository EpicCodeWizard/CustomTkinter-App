#     ScreenExtend GUI
#     Copyright (C) 2023  Sarvesh M. (epiccodewizard)
#     <epiccodewizard@gmail.com> and contributors.
#
#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
#
#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
#
#     You should have received a copy of the GNU General Public License
#     along with this program.  If not, see <https://www.gnu.org/licenses/>.

from idlelib.redirector import WidgetRedirector

import customtkinter as ctk

from widgets import *

class CTKApp(ctk.CTk):
    def __init__(self, width: int, height: int) -> None:
        """
        The main application for CTKApp. Create an instance of this class and call the 
        ".mainloop" method on the instance.

        Args:
            width (int): width if the window in pixels
            height (int): height of the window in pixels
        """

        super().__init__()
        self.geometry(f"{width}x{height}")
        self.resizable(True, True)
        self.minsize(600, 450)

        self.title("ScreenExtend")
        ctk.set_default_color_theme("./assets/themes/default.json")
        ctk.set_appearance_mode("System")

        ctk.FontManager.load_font("./assets/fonts/DM Mono.ttf")
        self.font = ("DM Mono", 13)

        self.times1 = []
        self.times2 = []

        self.grid_rowconfigure(0, weight = 1)
        self.grid_rowconfigure(1, weight = 0)
        self.grid_rowconfigure(2, weight = 0)
        self.grid_rowconfigure(3, weight = 0)
        self.grid_rowconfigure(4, weight = 0)
        self.grid_rowconfigure(5, weight = 0)
        self.grid_rowconfigure(6, weight = 0)
        self.grid_rowconfigure(7, weight = 0)

        self.grid_columnconfigure(0, weight = 0)
        self.grid_columnconfigure(2, weight = 1)

        self.devices = Devices(self, self.font)
        self.devices.grid(row = 0,
                          rowspan = 7,
                          column = 2,
                          padx = PADX,
                          pady = PADY,
                          sticky = "nsew"
                          )

        self.qr_code = QRCode(self)
        self.qr_code.set_image("./assets/qr-code.png")
        self.qr_code.grid(row = 0,
                          column = 0,
                          padx = PADX,
                          pady = PADY,
                          sticky = "nsew"
                          )

        self.publish_enlarge = PublishEnlargeFrame(master = self,
                                                   fg_color = "transparent"
                                                   )
        self.publish_enlarge.grid(row = 1,
                                  column = 0,
                                  padx = PADX,
                                  pady = 0,
                                  sticky = "sew",
                                  )

        # filler = ctk.CTkLabel(master = self,
        #                       height = 20,
        #                       text = ""
        #                       )
        # filler.grid(row = 7,
        #             column = 0,
        #             padx = PADX,
        #             pady = PADY,
        #             sticky = "sew"
        #             )

        self.local_net = LocalNetwork(self, self.font)
        self.local_net.grid(row = 2,
                            column = 0,
                            padx = PADX,
                            pady = 0,
                            sticky = "sew"
                            )

        self.local_url = ctk.CTkTextbox(master = self,
                                        height = LABEL_HEIGHT,
                                        activate_scrollbars = False,
                                        border_width = 2,
                                        font = (self.font[0], 16)
                                        )
        self.local_url_redirector = WidgetRedirector(self.local_url._textbox)
        self.local_url_redirector.register("insert", lambda *args, **kw: "break")("0.0", "https://localhost:3000")
        self.local_url_redirector.register("delete", lambda *args, **kw: "break")
        self.local_url.grid(row = 3,
                             column = 0,
                             padx = PADX,
                             pady = PADY,
                             sticky = "sew"
                             )
        self.local_url.bind("<Button-1>", lambda x: self.times1.append(x.time))

        self.public_net = PublicNetwork(self, self.font)
        self.public_net.grid(row = 4,
                             column = 0,
                             padx = PADX,
                             pady = 0,
                             sticky = "sew"
                             )
            
        self.public_url = ctk.CTkTextbox(master = self,
                                         height = LABEL_HEIGHT,
                                         activate_scrollbars = False,
                                         border_width = 2,
                                         font = (self.font[0], 16)
                                         )
        self.public_url_redirector = WidgetRedirector(self.public_url._textbox)
        self.public_url_redirector.register("insert", lambda *args, **kw: "break")("0.0", "https://google.com/")
        self.public_url_redirector.register("delete", lambda *args, **kw: "break")
        self.public_url.grid(row = 5,
                             column = 0,
                             padx = PADX,
                             pady = PADY,
                             sticky = "sew"
                             )
        self.public_url.bind("<Button-1>", lambda x: self.times2.append(x.time))

        self.bind("<Button-1>", lambda x:
                  self.focus() if x.time not in self.times1 and x.time not in self.times2 else None
                  )

if __name__ == "__main__":
    app = CTKApp(1200, 900)
    app.mainloop()
















