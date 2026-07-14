import customtkinter as ctk
from ui.themes.colors import *


MENU_ITEMS = [
    "Dashboard",
    "Diary",
    "Mood",
    "Tasks",
    "Goals",
    "Calendar",
    "Notes",
    "Habits",
    "Statistics",
    "Gallery",
    "Settings"
]


class Sidebar(ctk.CTkFrame):

    def __init__(self, parent, navigation):

        super().__init__(
            parent,
            width=250,
            corner_radius=0,
            fg_color=SIDEBAR
        )

        self.pack_propagate(False)

        self.navigation = navigation

        self.selected_button = None
        self.buttons = {}

        self.create_logo()
        self.create_menu()
        self.create_footer()

    def create_logo(self):

        logo = ctk.CTkLabel(
            self,
            text="📖 LifeBook AI",
            font=("Segoe UI", 15, "bold")
        )

        logo.pack(pady=(30, 5))

        subtitle = ctk.CTkLabel(
            self,
            text="Personal Life Management",
            font=("Segoe UI", 12),
            text_color="gray"
        )

        subtitle.pack(pady=(0, 25))

    def create_menu(self):

        menu_frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        menu_frame.pack(fill="both", expand=True)

        for item in MENU_ITEMS:

            button = ctk.CTkButton(

                menu_frame,

                text=item,

                height=42,

                corner_radius=10,

                anchor="w",

                fg_color="transparent",

                hover_color=PRIMARY_DARK,

                command=lambda name=item: self.select_button(name)

            )

            button.pack(fill="x", padx=15, pady=4)

            self.buttons[item] = button

        

    def create_footer(self):

        footer = ctk.CTkLabel(

            self,

            text="Version 1.0\nMade with Python",

            text_color=SECONDARY,

            font=("Segoe UI", 11)

        )

        footer.pack(pady=20)

    def select_button(self, name):

        for btn in self.buttons.values():

            btn.configure(fg_color="transparent")

        self.buttons[name].configure(
            fg_color=PRIMARY_DARK
        )

        self.navigation.navigate(name)