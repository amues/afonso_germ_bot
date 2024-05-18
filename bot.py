# SPDX-License-Identifier: BSD-3-Clause

import random
from typing import Optional, Tuple

import numpy as np

from cholerama import Positions, helpers

AUTHOR = "Histeria"  # This is your team name
SEED = None  # Set this to a value to make runs reproducible


class Bot:
    """
    This is the bot that will be instantiated for the competition.

    The pattern can be either a numpy array or a path to an image (white means 0,
    black means 1).
    """

    def __init__(
            self,
            number: int,
            name: str,
            patch_location: Tuple[int, int],
            patch_size: Tuple[int, int],
    ):
        """
        Parameters:
        ----------
        number: int
            The player number. Numbers on the board equal to this value mark your cells.
        name: str
            The player's name
        patch_location: tuple
            The i, j row and column indices of the patch in the grid
        patch_size: tuple
            The size of the patch
        """
        self.number = number  # Mandatory: this is your number on the board
        self.name = name  # Mandatory: player name
        self.color = None  # Optional
        self.patch_location = patch_location
        self.patch_size = patch_size

        self.rng = np.random.default_rng(SEED)

        # If we make the pattern too sparse, it just dies quickly
        xy = self.rng.integers(0, 12, size=(2, 100))
        # self.pattern = Positions(
        #     x=xy[1] + patch_size[1] // 2, y=xy[0] + patch_size[0] // 2
        # )
        self.pattern = Positions(
            x=np.array([0, 1, 1, 1, 2, 2, 3, 4, 5, 5]) + patch_size[1] // 2, y=np.array([6, 4, 6, 7, 4, 6, 4, 2, 0, 2]) + patch_size[0] // 2
        )
        # The pattern can also be just an image (0=white, 1=black)
        # self.pattern = "mypattern.png"

        self.options = [self.glider, self.loafer, self.paul_callahan_infinite, self.lwss]
        self.weights = [10, 5, 12, 20]
        self.next_choice = self.space_rake

    def glider(self, patch: np.ndarray, tokens: int) -> Optional[Positions]:
        if tokens < 5:
            return None
        else:
            empty_regions = helpers.find_empty_regions(patch, (3, 3))
            nregions = len(empty_regions)
            if nregions == 0:
                return None
            ind = self.rng.integers(0, nregions)
            x = np.array([1, 2, 0, 1, 2]) + empty_regions[ind, 1]
            y = np.array([2, 1, 0, 0, 0]) + empty_regions[ind, 0]
            return Positions(x=x, y=y)

    def loafer(self, patch: np.ndarray, tokens: int) -> Optional[Positions]:
        if tokens < 20:
            return None
        else:
            empty_regions = helpers.find_empty_regions(patch, (9, 9))
            nregions = len(empty_regions)
            if nregions == 0:
                return None
            ind = self.rng.integers(0, nregions)
            x = np.array([0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8]) + empty_regions[ind, 1]
            y = np.array([1, 2, 5, 7, 8, 0, 3, 6, 7, 1, 3, 2, 8, 6, 7, 8, 5, 6, 7, 8]) + empty_regions[ind, 0]
            return Positions(x=x, y=y)

    def paul_callahan_infinite(self, patch: np.ndarray, tokens: int) -> Optional[Positions]:
        if tokens < 10:
            return None
        else:
            empty_regions = helpers.find_empty_regions(patch, (8, 8))
            nregions = len(empty_regions)
            if nregions == 0:
                return None
            ind = self.rng.integers(0, nregions)
            x = np.array([0, 1, 1, 1, 2, 2, 3, 4, 5, 5]) + empty_regions[ind, 1]
            y = np.array([6, 4, 6, 7, 4, 6, 4, 2, 0, 2]) + empty_regions[ind, 0]
            return Positions(x=x, y=y)

    def lwss(self, patch: np.ndarray, tokens: int) -> Optional[Positions]:
        if tokens < 9:
            return None
        else:
            empty_regions = helpers.find_empty_regions(patch, (5, 5))
            nregions = len(empty_regions)
            if nregions == 0:
                return None
            ind = self.rng.integers(0, nregions)
            x = np.array([0, 0, 1, 2, 2, 3, 3, 3, 3]) + empty_regions[ind, 1]
            y = np.array([1, 4, 0, 0, 4, 0, 1, 2, 3]) + empty_regions[ind, 0]
            return Positions(x=x, y=y)

    def space_rake(self, patch: np.ndarray, tokens: int) -> Optional[Positions]:
        if tokens < 65:
            return None
        else:
            empty_regions = helpers.find_empty_regions(patch, (22, 22))
            nregions = len(empty_regions)
            if nregions == 0:
                return None
            ind = self.rng.integers(0, nregions)
            x = np.array([0,
                          0,
                          0,
                          0,
                          0,
                          0,
                          1,
                          1,
                          1,
                          1,
                          1,
                          1,
                          2,
                          2,
                          2,
                          2,
                          2,
                          3,
                          3,
                          3,
                          3,
                          5,
                          6,
                          6,
                          6,
                          6,
                          7,
                          7,
                          7,
                          8,
                          8,
                          8,
                          8,
                          8,
                          8,
                          8,
                          9,
                          9,
                          9,
                          9,
                          9,
                          9,
                          9,
                          9,
                          10,
                          10,
                          10,
                          14,
                          14,
                          14,
                          14,
                          15,
                          15,
                          15,
                          15,
                          16,
                          16,
                          17,
                          17,
                          17,
                          17,
                          18,
                          18,
                          18,
                          18]) + empty_regions[ind, 1]
            y = np.array([11,
                          12,
                          18,
                          19,
                          20,
                          21,
                          9,
                          10,
                          12,
                          13,
                          17,
                          21,
                          9,
                          10,
                          11,
                          12,
                          21,
                          10,
                          11,
                          17,
                          20,
                          8,
                          7,
                          8,
                          17,
                          18,
                          6,
                          16,
                          19,
                          7,
                          8,
                          9,
                          10,
                          11,
                          16,
                          19,
                          8,
                          9,
                          10,
                          11,
                          15,
                          16,
                          18,
                          19,
                          11,
                          16,
                          17,
                          18,
                          19,
                          20,
                          21,
                          0,
                          3,
                          17,
                          21,
                          4,
                          21,
                          0,
                          4,
                          17,
                          20,
                          1,
                          2,
                          3,
                          4]) + empty_regions[ind, 0]
            return Positions(x=x, y=y)

    def iterate(
            self, iteration: int, board: np.ndarray, patch: np.ndarray, tokens: int
    ) -> Optional[Positions]:
        """
        This method will be called by the game engine on each iteration.

        Parameters:
        ----------
        iteration : int
            The current iteration number.
        board : numpy array
            The current state of the entire board.
        patch : numpy array
            The current state of the player's own patch on the board.
        tokens : list
            The list of tokens on the board.

        Returns:
        -------
        An object containing the x and y coordinates of the new cells.
        """
        r = self.next_choice(patch, tokens)
        if r is not None:
            self.next_choice = random.choices(self.options, self.weights)[0]

        return r
