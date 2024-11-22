import snake_cube
import agents

puzzle = snake_cube.snake_cube()
agent = agents.IDS_agent(puzzle)

# Solve the puzzle
solution = agent.IDS(max_depth=50)

if solution:
    print("Solution found:")
    solution.show()
else:
    print("No solution found.")