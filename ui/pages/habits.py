import customtkinter as ctk
from ui.base.base_page import BasePage


class HabitsPage(BasePage):

    def create_page(self):

        title = ctk.CTkLabel(
            self,
            text="💪 Habits",
            font=("Segoe UI", 30, "bold")
        )

        title.pack(pady=(40, 10))

        subtitle = ctk.CTkLabel(
            self,
            text="Habit Tracker Module\nComing Soon...",
            font=("Segoe UI", 18)
        )

        subtitle.pack()