import tkinter as tk
import matplotlib.pyplot as plt
import snake_cube
import agents


class CubeVisualizer :
    def __init__ (self, root, puzzle):
        self.root = root
        self.puzzle = puzzle
        # to be continued ... =) 


class VisualizedIDSAgent(agents.IDS_agent):
    pass


class VisualizedRBFSAgent(agents.RBFS_agent):
    pass