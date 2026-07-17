from ui.base.base_page import BasePage
from database.repositories.mood_repository import MoodRepository

import customtkinter as ctk
from datetime import datetime


class MoodPage(BasePage):

    def create_page(self):

        self.repository = MoodRepository()

        self.create_ui()

        self.load_history()

        # self.load_moods()

        # self.load_summary()

    def create_ui(self):

        # ==========================
        # Main Container
        # ==========================

        self.main_container = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        self.main_container.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

        # ==========================
        # Left Panel
        # ==========================

        self.left_panel = ctk.CTkFrame(
            self.main_container,
            fg_color="transparent"
        )

        self.left_panel.pack(
            side="left",
            fill="both",
            expand=True,
            padx=(0, 10)
        )

        # ==========================
        # Right Panel
        # ==========================

        self.right_panel = ctk.CTkFrame(
            self.main_container,
            width=320,
            fg_color="#252525",
            corner_radius=12
        )

        self.right_panel.pack(
            side="right",
            fill="y"
        )

        self.right_panel.pack_propagate(False)

        # ==========================
        # Mood History Title
        # ==========================

        history_title = ctk.CTkLabel(
            self.right_panel,
            text="📅 Mood History",
            font=("Segoe UI", 18, "bold")
        )

        history_title.pack(
            pady=(20, 10)
        )

        # ==========================
        # History Frame
        # ==========================

        self.history_frame = ctk.CTkScrollableFrame(
            self.right_panel,
            fg_color="transparent"
        )

        self.history_frame.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=(0, 10)
        )

        # ==========================
        # Title
        # ==========================

        title = ctk.CTkLabel(
            self.left_panel,
            text="😊 Mood Tracker",
            font=("Segoe UI", 28, "bold")
        )

        title.pack(
            anchor="w",
            padx=30,
            pady=(20, 10)
        )

        subtitle = ctk.CTkLabel(
            self.left_panel,
            text="How are you feeling today?",
            font=("Segoe UI", 15)
        )

        subtitle.pack(
            anchor="w",
            padx=30,
            pady=(0, 20)
        )

        # ==========================
        # Mood Selection
        # ==========================

        self.mood_menu = ctk.CTkOptionMenu(
            self.left_panel,
            values=[
                "😊 Happy",
                "😐 Normal",
                "😔 Sad",
                "😡 Angry",
                "😍 Excited",
                "😴 Tired",
                "😰 Stressed"
            ],
            width=250
        )

        self.mood_menu.pack(
            anchor="w",
            padx=30,
            pady=10
        )

        # ==========================
        # Notes
        # ==========================

        self.note_box = ctk.CTkTextbox(
            self.left_panel,
            height=180,
            font=("Segoe UI", 15)
        )

        self.note_box.pack(
            fill="x",
            padx=30,
            pady=15
        )

        # ==========================
        # Save Button
        # ==========================

        save_btn = ctk.CTkButton(
            self.left_panel,
            text="💾 Save Mood",
            command=self.save_mood
        )

        save_btn.pack(
            pady=(10, 20)
        )

    def save_mood(self):

        mood = self.mood_menu.get()

        note = self.note_box.get("1.0", "end").strip()

        created_at = datetime.now().strftime("%d-%m-%Y %H:%M")

        self.repository.add_mood(
            mood,
            note,
            created_at
        )

        self.note_box.delete("1.0", "end")

        self.mood_menu.set("😊 Happy")

        print("✅ Mood Saved Successfully")

        self.load_history()

        # self.load_moods()

        # self.load_summary()

    def load_history(self):

        moods = self.repository.get_all_moods()

        # Clear old history
        for widget in self.history_frame.winfo_children():
            widget.destroy()

        if not moods:

            label = ctk.CTkLabel(
                self.history_frame,
                text="No mood history yet.",
                text_color="gray"
            )

            label.pack(pady=20)

            return

        for mood in moods:

            card = ctk.CTkFrame(
                self.history_frame,
                fg_color="#2B2B2B",
                corner_radius=10
            )

            card.pack(
                fill="x",
                padx=5,
                pady=5
            )

            mood_label = ctk.CTkLabel(
                card,
                text=f"{mood[1]}",
                font=("Segoe UI", 15, "bold"),
                anchor="w"
            )

            mood_label.pack(
                anchor="w",
                padx=10,
                pady=(8, 0)
            )

            note_label = ctk.CTkLabel(
                card,
                text=mood[2],
                anchor="w",
                justify="left",
                wraplength=220
            )

            note_label.pack(
                anchor="w",
                padx=10,
                pady=(2, 0)
            )

            date_label = ctk.CTkLabel(
                card,
                text=mood[3],
                text_color="gray",
                font=("Segoe UI", 11)
            )

            date_label.pack(
                anchor="e",
                padx=10,
                pady=(0, 8)
            )

    def load_moods(self):

        moods = self.repository.get_all_moods()

        for widget in self.history_frame.winfo_children():
            widget.destroy()

        for mood in moods:

            card = ctk.CTkFrame(
                self.history_frame,
                fg_color="#2B2B2B",
                corner_radius=10
            )

            card.pack(
                fill="x",
                padx=5,
                pady=5
            )

            mood_label = ctk.CTkLabel(
                card,
                text=mood[1],
                font=("Segoe UI", 16, "bold"),
                anchor="w"
            )

            mood_label.pack(
                anchor="w",
                padx=10,
                pady=(8, 0)
            )

            note_label = ctk.CTkLabel(
                card,
                text=mood[2] if mood[2] else "No note",
                anchor="w",
                wraplength=320,
                justify="left"
            )

            note_label.pack(
                anchor="w",
                padx=10,
                pady=(2, 0)
            )

            date_label = ctk.CTkLabel(
                card,
                text=mood[3],
                text_color="gray",
                font=("Segoe UI", 11)
            )

            date_label.pack(
                anchor="e",
                padx=10,
                pady=(0, 8)
            )

    def load_summary(self):

        mood = self.repository.get_latest_mood()

        if mood is None:

            self.summary_mood.configure(
                text="No Mood Yet"
            )

            self.summary_date.configure(
                text=""
            )

            return

        self.summary_mood.configure(
            text=mood[1]
        )

        self.summary_date.configure(
            text=f"Last Updated: {mood[3]}"
        )