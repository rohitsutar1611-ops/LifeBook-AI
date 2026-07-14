import customtkinter as ctk
from ui.base.base_page import BasePage


class StatisticsPage(BasePage):

    def create_page(self):

        title = ctk.CTkLabel(
            self,
            text="📊 Statistics",
            font=("Segoe UI", 30, "bold")
        )

        title.pack(pady=(40, 10))

        subtitle = ctk.CTkLabel(
            self,
            text="Statistics Module\nComing Soon...",
            font=("Segoe UI", 18)
        )

        subtitle.pack()