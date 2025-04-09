import tkinter as tk
from tkinter import constants

class GameView:
    def __init__(self, root, game, show_result_callback):
        self._frame = tk.Frame(root)
        self.game = game
        self.show_result_callback = show_result_callback

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()