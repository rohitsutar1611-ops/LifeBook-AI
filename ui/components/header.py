import customtkinter as ctk
from datetime import datetime
from ui.themes.colors import *


class Header(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(
            parent,
            height=70,
            fg_color=HEADER,
            corner_radius=0
        )

        self.pack_propagate(False)

        self.create_widgets()

        self.update_clock()

    def create_widgets(self):

        self.title = ctk.CTkLabel(
            self,
            text="Dashboard",
            font=("Segoe UI", 24, "bold"),
            text_color=TEXT
        )

        self.title.pack(
            side="left",
            padx=20
        )

        self.datetime = ctk.CTkLabel(
            self,
            text="",
            font=("Segoe UI", 14),
            text_color=SECONDARY
        )

        self.datetime.pack(
            side="right",
            padx=20
        )

    def set_title(self, title):

        self.title.configure(text=title)

    def update_clock(self):

        now = datetime.now()

        current = now.strftime("%d %B %Y | %I:%M:%S %p")

        self.datetime.configure(text=current)

        self.after(1000, self.update_clock)