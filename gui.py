from src.game_manager import GameManager
import os
import sys
import tkinter as tk

assets_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))

def start_game():
    hours = int(hours_entry.get())
    minutes = int(minutes_entry.get()) if minutes_entry.get() != "" else 0
    seconds = int(seconds_entry.get()) if seconds_entry.get() != "" else 0
    game = GameManager(hours, minutes, seconds, assets_path)
    game.run()
    root.destroy()

root = tk.Tk()
root.title("Duck Timer!")
root.iconphoto(False, tk.PhotoImage(file=os.path.join(assets_path, "./assets/duck.ico")))

hours_label = tk.Label(root, text="Hours:")
hours_label.pack()
hours_entry = tk.Entry(root)
hours_entry.pack()

minutes_label = tk.Label(root, text="Minutes:")
minutes_label.pack()
minutes_entry = tk.Entry(root)
minutes_entry.pack()

seconds_label = tk.Label(root, text="Seconds:")
seconds_label.pack()
seconds_entry = tk.Entry(root)
seconds_entry.pack()

start_button = tk.Button(root, text="Start Game", command=start_game)
start_button.pack()

root.mainloop()