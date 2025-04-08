import tkinter as tk
from tkinter import constants

class ResultView:
    def __init__(self, root):
        self.root = root

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()