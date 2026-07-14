from ui.base.base_page import BasePage
import customtkinter as ctk


class DiaryPage(BasePage):

    def create_page(self):

        title = ctk.CTkLabel(
            self,
            text="📝 Diary",
            font=("Segoe UI", 28, "bold")
        )

        title.pack(pady=30)

        label = ctk.CTkLabel(
            self,
            text="Coming Soon..."
        )

        label.pack()