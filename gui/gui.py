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

    search_frame = tk.Frame(root, bg="#a9c9ff")
    search_frame.pack(pady=30)

    city_label = tk.Label(
        search_frame,
        text="Ciudad:",
        font=("Helvetica", 14),
        bg="#a9c9ff",
        fg="#1a1a2e"
    )
    city_label.grid(row=0, column=0, padx=(0, 8))

    city_entry = tk.Entry(
        search_frame,
        font=("Helvetica", 14),
        width=20,
        relief="flat",
        bd=4,
        bg="white",
        fg="#1a1a2e"
    )
    city_entry.grid(row=0, column=1, padx=(0, 8))

    # Botón de búsqueda
    def on_search():
        city = city_entry.get().strip()
        if city:
            print(f"Buscando: {city}")

    search_btn = tk.Button(
        search_frame,
        text="Buscar",
        font=("Helvetica", 13, "bold"),
        bg="#4a90d9",
        fg="white",
        relief="flat",
        padx=12,
        pady=4,
        cursor="hand2",
        command=on_search
    )
    search_btn.grid(row=0, column=2)

    root.mainloop()

create_layout()