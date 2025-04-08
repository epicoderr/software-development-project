import tkinter as tk
from tkinter import constants

class GameView:
    def __init__(self, root, game, show_result_callback):
        #used AI for help here
        self._frame = tk.Frame(root)
        self.game = game
        self.show_result_callback = show_result_callback

        test_game_text = self.game.test_game() if callable(self.game.test_game) else self.game.test_game
        self.game_label = tk.Label(self._frame, text=test_game_text, font=("Courier", 12))
        self.game_label.pack(pady=10)

        end_button = tk.Button(self._frame, text="End Game", command=self.show_result_callback)
        end_button.pack(pady=10)

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()