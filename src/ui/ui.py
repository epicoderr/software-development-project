from ui.menu_view import MenuView
from ui.game_view import GameView
from ui.result_view import ResultView
from game.solitaire import Solitaire

class UI:
    def __init__(self, root, game: Solitaire):
        self._root = root
        self._current_view = None
        self._game = game

    def start(self):
        self._show_menu_view()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()
        self._current_view = None

    def _show_menu_view(self):
        self._hide_current_view()
        self._current_view = MenuView(self._root, self._show_game_view)
        self._current_view.pack()

    def _show_game_view(self):
        self._hide_current_view()
        self._current_view = GameView(self._root, self._game, self._show_result_view)
        self._current_view.pack()

    def _show_result_view(self):
        self._hide_current_view()
        self._current_view = ResultView(self._root, self._show_menu_view)
        self._current_view.pack()