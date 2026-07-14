import customtkinter as ctk


class BasePage(ctk.CTkFrame):
    """
    Base class for all application pages.
    Every page should inherit from this class.
    """

    def __init__(self, parent):

        super().__init__(
            parent,
            fg_color="transparent"
        )

        # Expand to fill available space
        self.pack(
            fill="both",
            expand=True
        )

        # Build page UI
        self.create_page()

    def create_page(self):
        """
        Override this method in child pages.
        """
        pass