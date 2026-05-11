import tkinter as tk
from pathlib import Path

icon_path = Path(__file__).resolve().parent.parent / "source" / "icon.png"

def create_layout():
    root = tk.Tk()
    root.title("Weather App")
    root.geometry("700x700")
    icon = tk.PhotoImage(file=str(icon_path))
    root.iconphoto(False, icon)
    root.configure(bg="#a9c9ff")

    root.mainloop()

create_layout()