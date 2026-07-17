from ui.base.base_page import BasePage
from database.repositories.diary_repository import DiaryRepository

import customtkinter as ctk
from datetime import datetime


class DiaryPage(BasePage):

    def create_page(self):

        self.repository = DiaryRepository()
        self.selected_entry_id = None

        self.create_form()

    def create_form(self):
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

        # Left Panel
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

        # Right Panel
        self.right_panel = ctk.CTkFrame(
            self.main_container,
            width=300,
            fg_color="#252525",
            corner_radius=12
        )

        self.right_panel.pack(
            side="right",
            fill="y"
        )

        self.right_panel.pack_propagate(False)

        # ==========================
        # Title
        # ==========================

        title = ctk.CTkLabel(
            self.left_panel,
            text="📝 My Diary",
            font=("Segoe UI", 28, "bold")
        )

        title.pack(
            anchor="w",
            padx=30,
            pady=(20, 15)
        )

        # ==========================
        # Title Entry
        # ==========================

        self.title_entry = ctk.CTkEntry(
            self.left_panel,
            placeholder_text="Diary Title",
            height=40
        )

        self.title_entry.pack(
            fill="x",
            padx=30,
            pady=10
        )

        # ==========================
        # Mood
        # ==========================

        self.mood_menu = ctk.CTkOptionMenu(
            self.left_panel,
            values=[
                "😊 Happy",
                "😐 Normal",
                "😔 Sad",
                "😡 Angry",
                "😍 Excited"
            ]
        )

        self.mood_menu.pack(
            padx=30,
            pady=10,
            anchor="w"
        )
        # ==========================
        # Diary Content
        # ==========================

        self.content_text = ctk.CTkTextbox(
            self.left_panel,
            height=230,
            font=("Segoe UI", 15)
        )

        self.content_text.pack(
            fill="both",
            expand=True,
            padx=30,
            pady=10
        )
        # ==========================
        # Buttons Frame
        # ==========================

        self.button_frame = ctk.CTkFrame(
            self.left_panel,
            fg_color="transparent"
        )

        self.button_frame.pack(
        fill="x",
        padx=30,
        pady=(15,10)
        )
        
        # ==========================
        # Save Button
        # ==========================

        save_button = ctk.CTkButton(
            self.button_frame,
            text="💾 Save Entry",
            height=42,
            command=self.save_entry
        )

        save_button.pack(
        side="left",
        padx=8
        )

        # ==========================
        # Favorite Button
        # ==========================

        self.favorite_button = ctk.CTkButton(
            self.button_frame,
            text="⭐ Mark as Favorite",
            height=40,
            state="disabled",
            command=self.toggle_favorite
        )

        self.favorite_button.pack(
        side="left",
        padx=8
        )

        self.delete_button = ctk.CTkButton(

            self.button_frame,

            text="🗑 Delete Entry",

            fg_color="#C62828",

            hover_color="#B71C1C",

            height=42,

            command=self.delete_entry

        )

        self.delete_button.pack(
        side="left",
        padx=8
        )

       
        print("Delete Button Created")

        self.status_label = ctk.CTkLabel(
            self.left_panel,
        text="",
        text_color="lightgreen",
        font=("Segoe UI", 13)
        )

        self.status_label.pack(pady=(5, 10))

        

        # ==========================
        # Recent Entries
        # ==========================

        entries_title = ctk.CTkLabel(
            self.right_panel,
            text="📚 Recent Entries",
            font=("Segoe UI", 18, "bold")
        )

        entries_title.pack(
            pady=(15, 10)
        )

        self.entries_frame = ctk.CTkScrollableFrame(
            self.right_panel,
            fg_color="transparent"
        )

        self.entries_frame.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=(0, 10)
        )

        # ==========================
        # Search Box
        # ==========================

        self.search_entry = ctk.CTkEntry(
            self.right_panel,
            placeholder_text="🔍 Search entries..."
        )

        self.search_entry.pack(
            fill="x",
            padx=10,
            pady=(0, 10)
        )

        # Live Search
        self.search_entry.bind(
            "<KeyRelease>",
            self.search_entries
        )

        # Load existing entries
        self.load_entries()

    def save_entry(self):

        title = self.title_entry.get().strip()

        content = self.content_text.get("1.0", "end").strip()

        mood = self.mood_menu.get()

        # Validation
        if not title or not content:

            self.status_label.configure(
                text="⚠️ Please enter title and content.",
                text_color="orange"
            )

            return

        now = datetime.now().strftime("%d-%m-%Y %H:%M")

        if self.selected_entry_id is None:

            self.repository.add_entry(

                title=title,
                content=content,
                mood=mood,
                created_at=now,
                updated_at=now

            )

            self.status_label.configure(
                text="✅ Diary Entry Saved",
                text_color="lightgreen"
            )

        else:

            self.repository.update_entry(

                entry_id=self.selected_entry_id,

                title=title,

                content=content,

                mood=mood,

                updated_at=now

            )

            self.status_label.configure(
                text="✏️ Diary Entry Updated",
                text_color="skyblue"
            )

            self.selected_entry_id = None

            self.favorite_button.configure(
            state="disabled",
            text="⭐ Mark as Favorite"
            )


        # Clear Form
        self.title_entry.delete(0, "end")

        self.content_text.delete("1.0", "end")

        self.mood_menu.set("😊 Happy")

        self.selected_entry_id = None

        # Reload Entries
        self.load_entries()

        print("✅ Diary Entry Saved Successfully")

    def load_entries(self):

        entries = self.repository.get_all_entries()

        self.display_entries(entries)

    def search_entries(self, event=None):

        keyword = self.search_entry.get().strip()

        if keyword == "":
            self.load_entries()
            return

        entries = self.repository.search_entries(keyword)

        self.display_entries(entries)

    def display_entries(self, entries):

        # Clear old widgets
        for widget in self.entries_frame.winfo_children():
            widget.destroy()

        if not entries:

            empty = ctk.CTkLabel(
                self.entries_frame,
                text="No entries found.",
                text_color="gray"
            )

            empty.pack(pady=20)

            return

        for entry in entries:

            button = ctk.CTkButton(
                self.entries_frame,
                text=entry[1],
                anchor="w",
                fg_color="transparent",
                hover_color="#3A3A3A",
                height=40,
                command=lambda entry_id=entry[0]: self.load_entry(entry_id)
            )

            button.pack(
                fill="x",
                pady=5
            )


    def load_entry(self, entry_id):

        entry = self.repository.get_entry_by_id(entry_id)

        if not entry:
            return

        self.selected_entry_id = entry[0]

        self.title_entry.delete(0, "end")
        self.title_entry.insert(0, entry[1])

        self.content_text.delete("1.0", "end")
        self.content_text.insert("1.0", entry[2])

        self.mood_menu.set(entry[3])

        self.status_label.configure(
            text="📖 Entry Loaded",
            text_color="skyblue"
        )

        # Enable Favorite Button
        self.favorite_button.configure(state="normal")

        # Update Button Text
        if entry[9] == 1:
            self.favorite_button.configure(
                text="⭐ Remove Favorite"
            )
        else:
            self.favorite_button.configure(
                text="⭐ Mark as Favorite"
            )

    def toggle_favorite(self):

        if self.selected_entry_id is None:
            return

        entry = self.repository.get_entry_by_id(
            self.selected_entry_id
        )

        if not entry:
            return

        current = entry[9]

        new_value = 0 if current == 1 else 1

        self.repository.toggle_favorite(
            self.selected_entry_id,
            new_value
        )

        if new_value == 1:

            self.favorite_button.configure(
                text="⭐ Remove Favorite"
            )

            self.status_label.configure(
                text="⭐ Added to Favorites",
                text_color="gold"
            )

        else:

            self.favorite_button.configure(
                text="⭐ Mark as Favorite"
            )

            self.status_label.configure(
                text="Removed from Favorites",
                text_color="gray"
            )

        self.load_entries()

    def delete_entry(self):

        if self.selected_entry_id is None:

            self.favorite_button.configure(
            state="disabled",
            text="⭐ Mark as Favorite"
            )

            self.status_label.configure(
                text="⚠️ Select an entry first.",
                text_color="orange"
            )

            return

        self.repository.delete_entry(
            self.selected_entry_id
        )

        self.selected_entry_id = None

        self.title_entry.delete(0, "end")

        self.content_text.delete("1.0", "end")

        self.mood_menu.set("😊 Happy")

        self.load_entries()

        self.status_label.configure(
            text="🗑 Diary Entry Deleted",
            text_color="tomato"
        )