"""A bingo data manager that can randomize the standard set of bingo numbers and 'pull' them one at a time."""

__author__ = "Sean Kraft"

import random


class BingoMachine:
    def __init__(self):
        self.numbers: list[int] = list(range(1, 76))
        self.game_position: int = 0

        random.shuffle(self.numbers)

    def reset_game(self):
        """Re-shuffles the list of bingo numbers and resets the game position index to the start."""
        random.shuffle(self.numbers)
        self.game_position = 0

    def select_number(self, include_letter: bool = False) -> int | str:
        """Pulls a single number (ball) from the list of remaining numbers and then advances the game position."""
        if self.game_position >= len(self.numbers):
            raise UserWarning("All numbers have been pulled. The game is over.")

        selection: int = self.numbers[self.game_position]
        self.game_position += 1

        if include_letter:
            return self.add_letter(selection)
        else:
            return selection

    def get_selected_numbers(self):
        """Returns a list of all numbers that have been pulled so far in the current game."""
        return self.numbers[:self.game_position]

    @staticmethod
    def add_letter(num: int) -> str:
        """Returns the provided number with the correct letter prefix based on its value."""
        if num < 16:
            return f"B-{num}"
        if num < 31:
            return f"I-{num}"
        if num < 46:
            return f"N-{num}"
        if num < 61:
            return f"G-{num}"
        return f"O-{num}"
