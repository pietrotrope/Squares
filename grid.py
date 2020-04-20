import numpy as np


class Point():
    """
    Represent a point in a bidimensional space
    """

    def __init__(self, x, y):
        """
        Initialize point with the given coordinates

        Parameters
        ----------
        x : x value of the point
        y : y value of the point
        """
        self.x = x
        self.y = y


class Grid():
    """
    Handles the board of the game
    """

    width = 0
    height = 0

    matrix = np.zeros((0, 0))
    def __init__(self, width=20, height=20):
        """
        create a grid

        Parameters
        ----------
        width : width of the grid
        height : height of the grid
        """
        self.width = width*2
        self.height = height*2
        # Assure the corners are enveloped in a padding
        self.matrix = np.zeros((self.width +2, self.height +2))


"""
ATTENTION
There will be no more updates to the project until the product 
backlog is created.
"""