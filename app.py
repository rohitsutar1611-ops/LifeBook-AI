import customtkinter as ctk

# =========================
# UI Components
# =========================
from ui.components.sidebar import Sidebar
from ui.components.header import Header

# =========================
# Navigation
# =========================
from core.navigation import NavigationManager

# =========================
# Pages
# =========================
from ui.pages.dashboard import DashboardPage
from ui.pages.diary import DiaryPage
from ui.pages.mood import MoodPage
from ui.pages.tasks import TasksPage
from ui.pages.goals import GoalsPage
from ui.pages.calendar import CalendarPage
from ui.pages.notes import NotesPage
from ui.pages.habits import HabitsPage
from ui.pages.statistics import StatisticsPage
from ui.pages.gallery import GalleryPage
from ui.pages.reminder import ReminderPage
from ui.pages.settings import SettingsPage

# =========================
# Theme
# =========================
from ui.themes.colors import *

# =========================
# Database
# =========================
from database.models import DatabaseModels


# -------------------------
# Application Theme
# -------------------------

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


class LifeBookAI(ctk.CTk):

    def __init__(self):

        super().__init__()

        # -------------------------
        # Window
        # -------------------------

        self.title("LifeBook AI")

        self.geometry("1400x800")

        self.minsize(1200, 700)

        self.configure(fg_color=BACKGROUND)

        self.initialize_database()

        # -------------------------
        # Main Frame
        # -------------------------

        self.main_frame = ctk.CTkFrame(
            self,
            fg_color=BACKGROUND,
            corner_radius=0
        )

        self.main_frame.pack(
            side="right",
            fill="both",
            expand=True
        )

        # -------------------------
        # Header
        # -------------------------

        self.header = Header(self.main_frame)

        self.header.pack(fill="x")

        # -------------------------
        # Content Frame
        # -------------------------

        self.content_frame = ctk.CTkFrame(
            self.main_frame,
            fg_color=CONTENT,
            corner_radius=15
        )

        self.content_frame.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

        # -------------------------
        # Navigation Manager
        # -------------------------

        self.navigation = NavigationManager(self)

        # -------------------------
        # Register Pages
        # -------------------------

        self.navigation.register_page("Dashboard", DashboardPage)
        self.navigation.register_page("Diary", DiaryPage)
        self.navigation.register_page("Mood", MoodPage)
        self.navigation.register_page("Tasks", TasksPage)
        self.navigation.register_page("Goals", GoalsPage)
        self.navigation.register_page("Calendar", CalendarPage)
        self.navigation.register_page("Notes", NotesPage)
        self.navigation.register_page("Habits", HabitsPage)
        self.navigation.register_page("Statistics", StatisticsPage)
        self.navigation.register_page("Gallery", GalleryPage)
        self.navigation.register_page("Reminder", ReminderPage)
        self.navigation.register_page("Settings", SettingsPage)

        # -------------------------
        # Sidebar
        # -------------------------

        self.sidebar = Sidebar(
            self,
            self.navigation
        )

        self.sidebar.pack(
            side="left",
            fill="y"
        )

        self.sidebar.select_button("Dashboard")

        

    def initialize_database(self):
        """
        Initialize application database.
        """

        models = DatabaseModels()

        models.create_all_tables()

        models.close()

        print("✅ Database Initialized")


# -------------------------
# Run Application
# -------------------------

if __name__ == "__main__":

    app = LifeBookAI()

    app.mainloop()