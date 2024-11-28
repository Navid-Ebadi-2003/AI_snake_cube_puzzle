import snake_cube
import agents


puzzle = snake_cube.snake_cube(initial_coordinates={
    1: [2, 0, 3],
    2: [2, 0, 2],
    3: [2, 0, 1],
    4: [1, 0, 1],
    5: [1, 1, 1],
    6: [1, 1, 0],
    7: [1, 1, -1],
    8: [1, 2, -1],
    9: [1, 2, 0],
    10: [1, 2, 1],
    11: [0, 2, 1],
    12: [0, 2, 0],
    13: [0, 1, 0],
    14: [0, 0, 0],
    15: [1, 0, 0],
    16: [2, 0, 0],
    17: [2, 1, 0],
    18: [2, 1, 1],
    19: [2, 2, 1],
    20: [2, 2, 0],
    21: [2, 2, -1],
    22: [2, 1, -1],
    23: [2, 0, -1],
    24: [1, 0, -1],
    25: [0, 0, -1],
    26: [0, 0, -2],
    27: [0, 0, -3]
})


# puzzle = snake_cube.snake_cube(initial_coordinates={
#     1: [-5, 2, -6],
#     2: [-5, 2, -5],
#     3: [-5, 2, -4],
#     4: [-4, 2, -4],
#     5: [-3, 2, -4],
#     6: [-3, 2, -3],
#     7: [-3, 2, -2],
#     8: [-2, 2, -2],
#     9: [-1, 2, -2],
#     10: [-1, 2, -1],
#     11: [0, 2, -1],
#     12: [0, 2, 0],
#     13: [0, 1, 0],
#     14: [0, 0, 0],
#     15: [1, 0, 0],
#     16: [2, 0, 0],
#     17: [2, 0, 1],
#     18: [3, 0, 1],
#     19: [3, 0, 2],
#     20: [3, 0, 3],
#     21: [4, 0, 3],
#     22: [4, 0, 4],
#     23: [4, 0, 5],
#     24: [5, 0, 5],
#     25: [5, 0, 6],
#     26: [6, 0, 6],
#     27: [7, 0, 6]
# })

agent = agents.IDS_agent(puzzle)

solution = agent.IDS(max_depth=5)

if solution:
    print("Solution found:")
    for node in solution:
        print("depth :", node.depth ,"------------------------------------")
        node.show()
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
