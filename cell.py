class Cell:
    def __init__(self, position: tuple):
        """
        ? Args:
        * * position (tuple): The position to initialize the cell at
        """
        self.alive = False
        self.x, self.y = position

    def swap(self):
        """
        ? Description:
        * * Swap the cells state between dead and alive
        """
        self.alive = not self.alive
