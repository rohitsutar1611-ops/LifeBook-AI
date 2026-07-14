import customtkinter as ctk


class NavigationManager:
    """
    Handles page navigation inside the main content area.
    """

    def __init__(self, app):
        self.app = app

        # Dictionary to store registered pages
        self.pages = {}

        # Currently active page
        self.current_page = None

    # ----------------------------------------
    # Register a page
    # ----------------------------------------
    def register_page(self, page_name, page_class):
        """
        Register a page class.

        Example:
            register_page("Dashboard", DashboardPage)
        """
        self.pages[page_name] = page_class

    # ----------------------------------------
    # Remove current page
    # ----------------------------------------
    def clear_content(self):

        for widget in self.app.content_frame.winfo_children():
            widget.destroy()

        self.current_page = None

    # ----------------------------------------
    # Navigate to page
    # ----------------------------------------
    def navigate(self, page_name):

        # Check page exists
        if page_name not in self.pages:
            print(f"[Navigation Error] '{page_name}' page not registered.")
            return

        # Update Header Title
        self.app.header.set_title(page_name)

        # Clear old page
        self.clear_content()

        # Create new page
        page_class = self.pages[page_name]

        self.current_page = page_class(self.app.content_frame)

        self.current_page.pack(
            fill="both",
            expand=True
        )

        print(f"Opened: {page_name}")

    # ----------------------------------------
    # Get Current Page
    # ----------------------------------------
    def get_current_page(self):

        return self.current_page

    # ----------------------------------------
    # Check if page exists
    # ----------------------------------------
    def page_exists(self, page_name):

        return page_name in self.pages