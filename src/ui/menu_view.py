import tkinter as tk
from tkinter import constants

class MenuView:
    def __init__(self, root, start_game_callback):
        self._frame = tk.Frame(root)
        self.start_game_callback = start_game_callback
    
    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()