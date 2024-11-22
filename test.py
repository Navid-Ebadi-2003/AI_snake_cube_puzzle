import snake_cube
import agents

puzzle = snake_cube.snake_cube()
agent = agents.IDS_agent(puzzle)

solution = agent.IDS(max_depth=200)

if solution:
    print("Solution found:")
    solution.show()
else:
    print("No solution found.")



# puzzle = snake_cube.snake_cube()
# agent = agents.RBFS_agent(puzzle)

# solution = agent.RECURSIVE_BEST_FIRST_SEARCH()

# if solution != None:
#     print("Solution found:")
#     solution.show()
# else:
#     print("No solution found.")