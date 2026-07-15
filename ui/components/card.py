import customtkinter as ctk

from ui.themes.colors import *


class Card(ctk.CTkFrame):

    def __init__(
        self,
        parent,
        title="",
        width=300,
        height=180
    ):

        super().__init__(

            parent,

            width=width,

            height=height,

            fg_color=CARD,

            corner_radius=18,

            border_width=1,

            border_color=BORDER

        )

        # Fixed Size
        self.pack_propagate(False)

        # -------------------------------
        # Title
        # -------------------------------

        self.title_label = ctk.CTkLabel(

            self,

            text=title,

            font=("Segoe UI", 18, "bold"),

            text_color=TEXT,

            anchor="w"

        )

        self.title_label.pack(

            fill="x",

            padx=20,

            pady=(15, 10)

        )

        # -------------------------------
        # Divider
        # -------------------------------

        self.divider = ctk.CTkFrame(

            self,

            height=1,

            fg_color=BORDER

        )

        self.divider.pack(

            fill="x",

            padx=15,

            pady=(0, 10)

        )

        # -------------------------------
        # Content Area
        # -------------------------------

        self.content = ctk.CTkFrame(

            self,

            fg_color="transparent"

        )

        self.content.pack(

            fill="both",

            expand=True,

            padx=15,

            pady=(0, 15)

        )