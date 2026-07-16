from ui.base.base_page import BasePage
from ui.components.card import Card
from ui.themes.colors import *

import customtkinter as ctk


class DashboardPage(BasePage):

    def __init__(self, parent):

        super().__init__(parent)

    def create_page(self):

        self.create_layout()

        self.create_welcome_card()

        self.create_mood_streak_cards()

        self.create_entries_tasks_cards()

        self.create_statistics_card()

        self.create_quote_card()

    def create_layout(self):

        self.container = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        self.container.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

        # =============================
        # Grid Configuration
        # =============================

        self.container.grid_columnconfigure(0, weight=1)
        self.container.grid_columnconfigure(1, weight=1)

        self.container.grid_rowconfigure(0, weight=0)
        self.container.grid_rowconfigure(1, weight=1)
        self.container.grid_rowconfigure(2, weight=1)
        self.container.grid_rowconfigure(3, weight=1)
        self.container.grid_rowconfigure(4, weight=0)

        # =============================
        # Grid Frames
        # =============================

        self.row1 = ctk.CTkFrame(
            self.container,
            fg_color="transparent"
        )

        self.row1.grid(
            row=0,
            column=0,
            columnspan=2,
            sticky="ew",
            pady=(0,15)
        )

        self.row2_left = ctk.CTkFrame(
            self.container,
            fg_color="transparent"
        )

        self.row2_left.grid(
            row=1,
            column=0,
            sticky="nsew",
            padx=(0,10),
            pady=(0,15)
        )

        self.row2_right = ctk.CTkFrame(
            self.container,
            fg_color="transparent"
        )

        self.row2_right.grid(
            row=1,
            column=1,
            sticky="nsew",
            pady=(0,15)
        )

        self.row3_left = ctk.CTkFrame(
            self.container,
            fg_color="transparent"
        )

        self.row3_left.grid(
            row=2,
            column=0,
            sticky="nsew",
            padx=(0,10),
            pady=(0,15)
        )

        self.row3_right = ctk.CTkFrame(
            self.container,
            fg_color="transparent"
        )

        self.row3_right.grid(
            row=2,
            column=1,
            sticky="nsew",
            pady=(0,15)
        )

        self.row4 = ctk.CTkFrame(
            self.container,
            fg_color="transparent"
        )

        self.row4.grid(
            row=3,
            column=0,
            columnspan=2,
            sticky="nsew",
            pady=(0,15)
        )

        self.row5 = ctk.CTkFrame(
            self.container,
            fg_color="transparent"
        )

        self.row5.grid(
            row=4,
            column=0,
            columnspan=2,
            sticky="ew"
        )


    def create_welcome_card(self):

        self.welcome_card = Card(

            self.row1,

            title="👋 Welcome",

            height=160

        )

        self.welcome_card.pack(

            fill="x"

        )

        # ---------------- Welcome Text ----------------

        welcome_label = ctk.CTkLabel(

            self.welcome_card.content,

            text="Welcome to LifeBook AI",

            font=("Segoe UI", 28, "bold")

        )

        welcome_label.pack(

            anchor="w",

            padx=10,

            pady=(10,5)

        )

        # ---------------- Subtitle ----------------

        subtitle = ctk.CTkLabel(

            self.welcome_card.content,

            text="Your Personal AI Life Management System",

            font=("Segoe UI",16),

            text_color=SECONDARY

        )

        subtitle.pack(

            anchor="w",

            padx=10

        )

    def create_mood_streak_cards(self):

        # ==========================
        # Mood Card
        # ==========================

        self.mood_card = Card(
            self.row2_left,
            title="😊 Today's Mood"
        )

        self.mood_card.pack(
            fill="both",
            expand=True
        )

        mood = ctk.CTkLabel(
            self.mood_card.content,
            text="😀 Happy",
            font=("Segoe UI", 26, "bold")
        )

        mood.pack(pady=(20, 5))

        mood_text = ctk.CTkLabel(
            self.mood_card.content,
            text="Keep Smiling!",
            font=("Segoe UI", 15),
            text_color=SECONDARY
        )

        mood_text.pack()

        # ==========================
        # Writing Streak Card
        # ==========================

        self.streak_card = Card(
            self.row2_right,
            title="🔥 Writing Streak"
        )

        self.streak_card.pack(
            fill="both",
            expand=True
        )

        streak = ctk.CTkLabel(
            self.streak_card.content,
            text="🔥 7 Days",
            font=("Segoe UI", 26, "bold")
        )

        streak.pack(pady=(20, 5))

        streak_text = ctk.CTkLabel(
            self.streak_card.content,
            text="Keep Writing Daily",
            font=("Segoe UI", 15),
            text_color=SECONDARY
        )

        streak_text.pack()

    def create_entries_tasks_cards(self):

        # ==========================
        # Recent Entries Card
        # ==========================

        self.entries_card = Card(
            self.row3_left,
            title="📝 Recent Entries"
        )

        self.entries_card.pack(
            fill="both",
            expand=True
        )

        entries = [
            "• First Diary Entry",
            "• Started LifeBook AI",
            "• Planning New Features"
        ]

        for entry in entries:

            label = ctk.CTkLabel(
                self.entries_card.content,
                text=entry,
                anchor="w",
                font=("Segoe UI", 15)
            )

            label.pack(
                anchor="w",
                padx=10,
                pady=5
            )

        # ==========================
        # Today's Tasks Card
        # ==========================

        self.tasks_card = Card(
            self.row3_right,
            title="✅ Today's Tasks"
        )

        self.tasks_card.pack(
            fill="both",
            expand=True
        )

        tasks = [
            "☐ Complete Dashboard UI",
            "☑ Push Code to GitHub",
            "☐ Start Diary Module"
        ]

        for task in tasks:

            label = ctk.CTkLabel(
                self.tasks_card.content,
                text=task,
                anchor="w",
                font=("Segoe UI", 15)
            )

            label.pack(
                anchor="w",
                padx=10,
                pady=5
            )

    def create_statistics_card(self):

        self.stats_card = Card(
            self.row4,
            title="📊 Statistics",
            height=220
        )

        self.stats_card.pack(fill="x")

        stats_frame = ctk.CTkFrame(
            self.stats_card.content,
            fg_color="transparent"
        )

        stats_frame.pack(
            fill="both",
            expand=True,
            padx=5,
            pady=10
        )

        stats = [
            ("25", "Entries"),
            ("12,450", "Words"),
            ("8", "Goals"),
            ("15", "Habits")
        ]

        for value, title in stats:

            stat_card = ctk.CTkFrame(
                stats_frame,
                fg_color="#3B82F6",
                corner_radius=12
            )

            stat_card.pack(
                side="left",
                expand=True,
                fill="both",
                padx=8,
                pady=5
            )

            value_label = ctk.CTkLabel(
                stat_card,
                text=value,
                font=("Segoe UI", 26, "bold"),
                text_color=TEXT
            )

            value_label.pack(
                pady=(30, 5)
            )

            title_label = ctk.CTkLabel(
                stat_card,
                text=title,
                font=("Segoe UI", 14),
                text_color=SECONDARY
            )

            title_label.pack()

    def create_quote_card(self):

        self.quote_card = Card(
            self.row5,
            title="💬 Quote of the Day",
            height=150
        )

        self.quote_card.pack(
            fill="x"
        )

        quote = ctk.CTkLabel(
            self.quote_card.content,
            text='"Small progress every day adds up to big results."',
            font=("Segoe UI", 18, "italic"),
            wraplength=900,
            justify="center"
        )

        quote.pack(
            expand=True,
            pady=(15, 5)
        )

        author = ctk.CTkLabel(
            self.quote_card.content,
            text="— LifeBook AI",
            font=("Segoe UI", 14),
            text_color=SECONDARY
        )

        author.pack(
            pady=(0, 10)
        )
        