import customtkinter as ctk
from ui.base.base_page import BasePage


class CalendarPage(BasePage):

    def create_page(self):

        title = ctk.CTkLabel(
            self,
            text="📅 Calendar",
            font=("Segoe UI", 30, "bold")
        )

        title.pack(pady=(40, 10))

        subtitle = ctk.CTkLabel(
            self,
            text="Calendar Module\nComing Soon...",
            font=("Segoe UI", 18)
        )

        subtitle.pack()