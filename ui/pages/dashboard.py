import customtkinter as ctk

from ui.base.base_page import BasePage


class DashboardPage(BasePage):

    def create_page(self):

        title = ctk.CTkLabel(

            self,

            text="🏠 Dashboard",

            font=("Segoe UI", 30, "bold")

        )

        title.pack(pady=25)

        welcome = ctk.CTkLabel(

            self,

            text="Welcome to LifeBook AI",

            font=("Segoe UI", 18)

        )

        welcome.pack()