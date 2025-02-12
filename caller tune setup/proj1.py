import os
import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
import pygame
from pygame import mixer

# Initialize Pygame Mixer
mixer.init()

# Set CustomTkinter Appearance
ctk.set_appearance_mode("dark")  # Dark Mode
ctk.set_default_color_theme("blue")  # Blue Theme

# Dictionaries for Language & Category Paths
LANGUAGES = {"English": "\\English", "Hindi": "\\Hindi", "Bengali": "\\Bengali"}
CATEGORIES = {"Love": "\\Love", "Chill": "\\Chill", "Patriotic": "\\Patriotic", "Emotional": "\\Emotional"}


# Function to Validate Phone Number
def validate_phone():
    phone_number = phone_entry.get()
    if phone_number.isdigit() and len(phone_number) == 10:
        messagebox.showinfo("Success", "✅ Phone Number Verified!")
        language_dropdown.configure(state="normal")
    else:
        messagebox.showerror("Error", "❌ Invalid phone number! Enter a 10-digit number.")


# Function to Enable Category Selection
def enable_category(choice):
    category_dropdown.configure(state="normal")


# Function to Load Songs Dynamically as Buttons
def load_songs():
    selected_lang = language_var.get()
    selected_cat = category_var.get()

    if not selected_lang or not selected_cat:
        messagebox.showerror("Error", "⚠️ Please select both Language and Category!")
        return

    path = os.getcwd() + LANGUAGES[selected_lang] + CATEGORIES[selected_cat] + '\\'

    if not os.path.exists(path):
        messagebox.showerror("Error", "📂 No files found for the selected category.")
        return

    songs = os.listdir(path)

    # Clear previous song buttons
    for widget in song_frame.winfo_children():
        widget.destroy()

    for song in songs:
        song_button = ctk.CTkButton(song_frame, text=song, command=lambda s=song: play_song(s), fg_color="#333",
                                    hover_color="#555")
        song_button.pack(pady=2, fill="x")


# Function to Play Selected Song
def play_song(selected_song):
    selected_lang = language_var.get()
    selected_cat = category_var.get()
    path = os.getcwd() + LANGUAGES[selected_lang] + CATEGORIES[selected_cat] + '\\' + selected_song

    if not os.path.exists(path):
        messagebox.showerror("Error", "🚫 File not found!")
        return

    mixer.music.load(path)
    mixer.music.play()
    messagebox.showinfo("🎵 Playing", f"Now Playing: {selected_song}")


# Function to Stop Music
def stop_music():
    mixer.music.stop()


# Function to Set Caller Tune
def set_caller_tune():
    messagebox.showinfo("📞 Caller Tune Set", "🎶 Your caller tune has been set successfully! 📱✅")
    mixer.music.stop()


# GUI Setup
root = ctk.CTk()
root.title("📞 Caller Tune Setup")
root.geometry("500x650")

# Title Label
title_label = ctk.CTkLabel(root, text="📞 Set Your Caller Tune", font=("Arial", 22, "bold"))
title_label.pack(pady=20)

# Phone Number Input
phone_frame = ctk.CTkFrame(root)
phone_frame.pack(pady=10, padx=20, fill="x")

ctk.CTkLabel(phone_frame, text="📱 Mobile Number:").pack(side="left", padx=10)
phone_entry = ctk.CTkEntry(phone_frame, width=200)
phone_entry.pack(side="left", padx=10)

verify_button = ctk.CTkButton(root, text="✅ Verify", command=validate_phone)
verify_button.pack(pady=5)

# Language Selection
ctk.CTkLabel(root, text="🌍 Select Language:").pack(pady=5)
language_var = ctk.StringVar()
language_dropdown = ctk.CTkOptionMenu(root, variable=language_var, values=list(LANGUAGES.keys()),
                                      command=enable_category)
language_dropdown.configure(state="disabled")
language_dropdown.pack()

# Category Selection
ctk.CTkLabel(root, text="🎵 Select Category:").pack(pady=5)
category_var = ctk.StringVar()
category_dropdown = ctk.CTkOptionMenu(root, variable=category_var, values=list(CATEGORIES.keys()))
category_dropdown.configure(state="disabled")
category_dropdown.pack()

# Load Songs Button
load_button = ctk.CTkButton(root, text="🎼 Load Songs", command=load_songs)
load_button.pack(pady=10)

# Scrollable Song List (Modern Look)
song_scroll_frame = ctk.CTkFrame(root)
song_scroll_frame.pack(pady=10, padx=20, fill="both", expand=True)

song_canvas = tk.Canvas(song_scroll_frame, bg="#222", height=200)
song_canvas.pack(side="left", fill="both", expand=True)

song_scrollbar = tk.Scrollbar(song_scroll_frame, orient="vertical", command=song_canvas.yview)
song_scrollbar.pack(side="right", fill="y")

song_frame = ctk.CTkFrame(song_canvas)
song_canvas.create_window((0, 0), window=song_frame, anchor="nw")

song_canvas.configure(yscrollcommand=song_scrollbar.set)


def update_scroll_region(event):
    song_canvas.configure(scrollregion=song_canvas.bbox("all"))


song_frame.bind("<Configure>", update_scroll_region)

# Play & Stop Buttons
button_frame = ctk.CTkFrame(root)
button_frame.pack(pady=10)

play_button = ctk.CTkButton(button_frame, text="▶ Play", command=lambda: play_song(
    song_frame.winfo_children()[0].cget("text")) if song_frame.winfo_children() else None, width=100)
play_button.grid(row=0, column=0, padx=10)

stop_button = ctk.CTkButton(button_frame, text="⏹ Stop", command=stop_music, width=100)
stop_button.grid(row=0, column=1, padx=10)

# Set Caller Tune Button
caller_tune_button = ctk.CTkButton(root, text="📞 Set as Caller Tune", command=set_caller_tune, fg_color="green",
                                   hover_color="darkgreen", text_color="white")
caller_tune_button.pack(pady=10)

# Run GUI
root.mainloop()
