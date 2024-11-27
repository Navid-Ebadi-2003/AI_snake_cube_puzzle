import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import snake_cube  
import agents  

class CubeVisualizer:
    def __init__(self, root, puzzle):
        self.root = root
        self.puzzle = puzzle
        self.fig = plt.figure(figsize=(6, 6))
        self.ax = self.fig.add_subplot(111, projection='3d')
        self.canvas = FigureCanvasTkAgg(self.fig, master=root)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.ax.set_box_aspect([1, 1, 1])  
        self.draw_state(self.puzzle.start_state)

    def draw_state(self, state):
        self.ax.clear()
        coordinates = list(state.coordinates.values())

        
        if coordinates:
            x, y, z = zip(*coordinates)
            self.ax.plot(x, y, z, marker='o', color='violet')
            self.ax.set_xlim([-8, 8])
            self.ax.set_ylim([-8, 8])
            self.ax.set_zlim([-8, 8])
            self.ax.set_title("Snake Cube Visualization")
            self.canvas.draw_idle()

    def update(self, state, delay=500):
        self.draw_state(state)
        self.root.after(delay, self.root.update_idletasks)  


class VisualizedIDSAgent(agents.IDS_agent):  
    def __init__(self, puzzle, visualizer):
        super().__init__(puzzle)
        self.visualizer = visualizer

    def DLS(self, state, limit, delay=500):
        frontier = [state]
        while frontier:
            node = frontier.pop()
            if self.puzzle.is_goal(node):
                return node

            if node.depth > limit:
                return None
            else:
                for child in self.puzzle.successor(node):
                    frontier.append(child)
                    self.visualizer.update(child, delay)  
        return False

    def IDS(self, max_depth, delay=500):
        for depth_limit in range(0, max_depth):
            print(f"Searching at depth {depth_limit}...")
            result = self.DLS(self.puzzle.start_state, depth_limit, delay)
            if result is not None:
                return result
        return False


def main():
    puzzle = snake_cube.snake_cube() 

    root = tk.Tk()
    root.title("Snake Cube Visualizer")
    visualizer = CubeVisualizer(root, puzzle)
    agent = VisualizedIDSAgent(puzzle, visualizer)

    solution = agent.IDS(max_depth=20, delay=200) #it is s test faghat  

    if solution:
        print("Solution found:")
        solution.show()  
    else:
        print("No solution found.")

    root.mainloop()


if __name__ == "__main__":
    main()
