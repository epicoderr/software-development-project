import tkinter as tk
from tkinter import constants

class MenuView:
    def __init__(self, root, start_game_callback):
        #used AI for help here
        self._frame = tk.Frame(root)
        self.start_game_callback = start_game_callback

        label = tk.Label(self._frame, text="Welcome to Solitaire!")
        label.pack(pady=10)

        start_button = tk.Button(self._frame, text="Start Game", command=self.start_game_callback)
        start_button.pack(pady=10)
    
    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()