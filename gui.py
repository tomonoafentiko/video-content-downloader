import os
import sys
import json
import tkinter as tk
from tkinter import messagebox, filedialog, ttk
from utils.batch_downloader import batch_download

# ----- Persistent settings -----
SETTINGS_FILE = "settings.json"

def save_settings():
    settings = {"dark_mode": dark_mode}
    with open(SETTINGS_FILE, "w") as f:
        json.dump(settings, f)

def load_settings():
    global dark_mode
    if os.path.exists(SETTINGS_FILE):
        with open(SETTINGS_FILE, "r") as f:
            settings = json.load(f)
            dark_mode = settings.get("dark_mode", False)
    else:
        dark_mode = False

# ----- For PyInstaller to find resources (like icon) -----
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller stores temp files in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

icon_path = resource_path("icon.ico")

# Global variables
download_path = ""
dark_mode = False

# ----- Functionality -----
def select_download_folder():
    global download_path
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        download_path = folder_selected
        path_label.config(text=f"📂 Download Path: {download_path}", foreground=highlight_color)

def start_download():
    if not download_path:
        messagebox.showwarning("Path Error", "Please select a download folder first.")
        return

    urls = entry.get("1.0", "end-1c").splitlines()
    if not urls:
        messagebox.showwarning("Input Error", "Please enter at least one link.")
        return

    progress_bar["value"] = 0
    status_var.set("🚀 Downloading...")
    root.update_idletasks()

    total = len(urls)
    results = []

    for i, url in enumerate(urls, start=1):
        result = batch_download([url], download_path)
        results.extend(result)
        progress_bar["value"] = (i / total) * 100
        status_var.set(f"Downloading... ({i}/{total})")
        root.update_idletasks()

    messagebox.showinfo("Results", "\n".join(results))
    status_var.set("✅ Download complete.")
    progress_bar["value"] = 100

def toggle_dark_mode():
    global dark_mode, bg_color, text_color, highlight_color
    dark_mode = not dark_mode
    save_settings()  # Save when toggled

    if dark_mode:
        bg_color = "#1e1e1e"
        text_color = "#f5f5f5"
        highlight_color = "#66b3ff"
    else:
        bg_color = "#eaf4ff"
        text_color = "#000000"
        highlight_color = "#007acc"

    apply_theme()

def apply_theme():
    root.configure(bg=bg_color)
    style.configure("TLabel", background=bg_color, foreground=text_color)
    style.configure("Header.TLabel", background=bg_color, foreground=highlight_color)
    style.configure("TButton", background=highlight_color, foreground="white")
    style.configure("TProgressbar", troughcolor=bg_color)

    entry.configure(bg="white" if not dark_mode else "#333333", fg=text_color)
    status_bar.configure(background=bg_color, foreground=text_color)
    path_label.configure(background=bg_color, foreground=highlight_color)

# --------------------- GUI Layout ---------------------
root = tk.Tk()
root.iconbitmap(icon_path)
root.title("🎬 Video Content Downloader")
root.geometry("640x580")

# Set icon using resource path
root.iconbitmap(resource_path("icon.ico"))

# Load settings and apply theme
load_settings()

# Theme-related colors
if dark_mode:
    bg_color = "#1e1e1e"
    text_color = "#f5f5f5"
    highlight_color = "#66b3ff"
else:
    bg_color = "#eaf4ff"
    text_color = "#000000"
    highlight_color = "#007acc"

# --------- Style Setup ----------
style = ttk.Style(root)
style.theme_use("clam")

style.configure("TButton", font=("Helvetica", 10, "bold"), padding=6)
style.map("TButton", background=[("active", "#3399ff"), ("pressed", "#005f99")])

style.configure("TLabel", background=bg_color, font=("Helvetica", 10))
style.configure("Header.TLabel", font=("Helvetica", 18, "bold"), foreground=highlight_color)
style.configure("TProgressbar", thickness=18)

# -------- Header --------
header_frame = ttk.Frame(root)
header_frame.pack(pady=10)

header = ttk.Label(header_frame, text="📥 Video Content Downloader", style="Header.TLabel")
header.pack(side="left", padx=10)

theme_button = ttk.Button(header_frame, text="Change Theme Mode", command=toggle_dark_mode)
theme_button.pack(side="right", padx=10)

# -------- Input Frame --------
input_frame = ttk.Frame(root)
input_frame.pack(pady=5, padx=12, fill="x")

label = ttk.Label(input_frame, text="Paste video URLs/links you want to download below, one per line:")
label.pack(anchor="w")

text_frame = ttk.Frame(input_frame)
text_frame.pack(fill="both", expand=True)

entry = tk.Text(text_frame, height=10, font=("Consolas", 10), wrap="word", relief="sunken")
entry.pack(side="left", fill="both", expand=True)

scrollbar = ttk.Scrollbar(text_frame, command=entry.yview)
scrollbar.pack(side="right", fill="y")
entry.config(yscrollcommand=scrollbar.set)

# -------- Path Selection --------
path_button = ttk.Button(root, text="📁 Select Download Folder", command=select_download_folder)
path_button.pack(pady=10)

path_label = ttk.Label(root, text="📂 No folder selected", foreground="gray")
path_label.pack()

# -------- Download Button --------
button = ttk.Button(root, text="⬇️ Start Download", command=start_download)
button.pack(pady=15)

# -------- Progress Bar --------
progress_bar = ttk.Progressbar(root, length=460, mode="determinate")
progress_bar.pack(pady=10)

# -------- Status Bar --------
status_var = tk.StringVar()
status_var.set("✅ Ready.")
status_bar = ttk.Label(root, textvariable=status_var, relief="sunken", anchor="w", font=("Helvetica", 9))
status_bar.pack(side="bottom", fill="x")

# Apply the theme from settings
apply_theme()

# Start the main loop
root.mainloop()
