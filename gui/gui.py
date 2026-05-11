import tkinter as tk
from pathlib import Path

icon_path = Path(__file__).resolve().parent.parent / "source" / "icon.png"

def create_layout(on_search_callback=None):
    root = tk.Tk()
    root.title("Weather App")
    root.geometry("700x700")
    icon = tk.PhotoImage(file=str(icon_path))
    root.iconphoto(False, icon)
    root.configure(bg="#a9c9ff")

    
    city_display_frame = tk.Frame(
        root,
        bg="#d6eaff",
        relief="flat",
        bd=0,
        padx=24,
        pady=16
    )
    city_display_frame.pack(side="top", anchor="center", pady=(40, 0), ipadx=20, ipady=10)

    city_display_label = tk.Label(
        city_display_frame,
        text="Ingresá una ciudad para ver el clima",
        font=("Helvetica", 18, "bold"),
        bg="#d6eaff",
        fg="#1a1a2e"
    )
    city_display_label.pack()
    
    center_frame = tk.Frame(root, bg="#a9c9ff")
    center_frame.pack(expand=True)

    weather_image_label = tk.Label(center_frame, bg="#a9c9ff")
    weather_image_label.pack(side="left", padx=(20, 30))

    info_frame = tk.Frame(center_frame, bg="#a9c9ff")
    info_frame.pack(side="left")

    temp_label = tk.Label(
        info_frame,
        text="",
        font=("Helvetica", 36, "bold"),
        bg="#a9c9ff",
        fg="#1a1a2e"
    )
    temp_label.pack(anchor="w")

    condition_label = tk.Label(
        info_frame,
        text="",
        font=("Helvetica", 16),
        bg="#a9c9ff",
        fg="#1a1a2e"
    )
    condition_label.pack(anchor="w")

    root._weather_images = {}

    def update_ui(city, temp, condition, image_path=None):
        city_display_label.config(text=city)
        temp_label.config(text=f"{temp}°C")
        condition_label.config(text=condition)

        if image_path and Path(image_path).exists():
            img = tk.PhotoImage(file=str(image_path))
            # Escalar si es muy grande (PhotoImage soporta subsample)
            weather_image_label.config(image=img)
            root._weather_images["current"] = img  # evitar garbage collection
        else:
            weather_image_label.config(image="", text="🌡️", font=("Helvetica", 64))


    search_frame = tk.Frame(root, bg="#a9c9ff")
    search_frame.pack(side="bottom", anchor="center", pady=80)

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
    
    def on_search():
        city = city_entry.get().strip()
        if city and on_search_callback:
            on_search_callback(city, update_ui)
            city_entry.delete(0, tk.END)

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