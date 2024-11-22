import copy


class state:
    def __init__(self, coordinates, depth):
        self.coordinates = coordinates
        self.depth = depth
        self.f = 0

    def show(self):
        for i in range(1, 28):
            print(i, ":", self.coordinates[i])


class snake_cube:
    def __init__(self):
        self.start_state = state({
            1: [-5, 2, -6],
            2: [-5, 2, -5],
            3: [-5, 2, -4],
            4: [-4, 2, -4],
            5: [-3, 2, -4],
            6: [-3, 2, -3],
            7: [-3, 2, -2],
            8: [-2, 2, -2],
            9: [-1, 2, -2],
            10: [-1, 2, -1],
            11: [0, 2, -1],
            12: [0, 2, 0],
            13: [0, 1, 0],
            14: [0, 0, 0],
            15: [1, 0, 0],
            16: [2, 0, 0],
            17: [2, 0, 1],
            18: [3, 0, 1],
            19: [3, 0, 2],
            20: [3, 0, 3],
            21: [4, 0, 3],
            22: [4, 0, 4],
            23: [4, 0, 5],
            24: [5, 0, 5],
            25: [5, 0, 6],
            26: [6, 0, 6],
            27: [7, 0, 6]
        }, depth=0)

    goal_state_Coo = {
        1: [2, 0, 1],
        2: [1, 0, 1],
        3: [0, 0, 1],
        4: [0, 1, 1],
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
        26: [0, 1, -1],
        27: [0, 2, -1]
    }

    def is_goal(self, state):
        return list(state.coordinates.values()) == list(self.goal_state_Coo.values())

    def successor(self, state):
        successors = []

        for piece in range(1, 28):
            if piece in [1, 2, 6, 9, 13, 15, 16, 19, 20, 22, 24, 26, 27]:
                continue

            # mehvar x
            if piece in [3, 4, 5, 10, 11, 14, 23, 25]:

                new_state_90 = copy.deepcopy(state)
                new_state_90.depth += 1
                new_state_180 = copy.deepcopy(state)
                new_state_180.depth += 1
                new_state_270 = copy.deepcopy(state)
                new_state_270.depth += 1
                for i in range(piece + 1, 28):
                    new_state_90.coordinates[i][2] = state.coordinates[piece][2] + (
                        state.coordinates[i][1]-state.coordinates[piece][1])
                    new_state_90.coordinates[i][1] = state.coordinates[piece][1] - (
                        state.coordinates[i][2]-state.coordinates[piece][2])

                    new_state_180.coordinates[i][2] = state.coordinates[piece][2] - (
                        state.coordinates[i][1]-state.coordinates[piece][1])
                    new_state_180.coordinates[i][1] = state.coordinates[piece][1] - (
                        state.coordinates[i][2]-state.coordinates[piece][2])

                    new_state_270.coordinates[i][2] = state.coordinates[piece][2] - (
                        state.coordinates[i][1]-state.coordinates[piece][1])
                    new_state_270.coordinates[i][1] = state.coordinates[piece][1] + (
                        state.coordinates[i][2]-state.coordinates[piece][2])

                successors.append(new_state_90)
                successors.append(new_state_180)
                successors.append(new_state_270)

            if piece in [3, 4, 7, 8, 12, 14, 17, 18, 21, 23, 25]:

                new_state_90 = copy.deepcopy(state)
                new_state_90.depth += 1
                new_state_180 = copy.deepcopy(state)
                new_state_180.depth += 1
                new_state_270 = copy.deepcopy(state)
                new_state_270.depth += 1
                for i in range(piece + 1, 28):
                    new_state_90.coordinates[i][0] = state.coordinates[piece][0] + (
                        state.coordinates[i][2]-state.coordinates[piece][2])
                    new_state_90.coordinates[i][2] = state.coordinates[piece][2] - (
                        state.coordinates[i][0]-state.coordinates[piece][0])

                    new_state_180.coordinates[i][0] = state.coordinates[piece][0] - (
                        state.coordinates[i][2]-state.coordinates[piece][2])
                    new_state_180.coordinates[i][2] = state.coordinates[piece][2] - (
                        state.coordinates[i][0]-state.coordinates[piece][0])

                    new_state_270.coordinates[i][0] = state.coordinates[piece][0] - (
                        state.coordinates[i][2]-state.coordinates[piece][2])
                    new_state_270.coordinates[i][2] = state.coordinates[piece][2] + (
                        state.coordinates[i][0]-state.coordinates[piece][0])

                successors.append(new_state_90)
                successors.append(new_state_180)
                successors.append(new_state_270)

            # mehvar z
            if piece in [5, 7, 8, 10, 11, 12, 17, 18, 21]:

                new_state_90 = copy.deepcopy(state)
                new_state_90.depth += 1
                new_state_180 = copy.deepcopy(state)
                new_state_180.depth += 1
                new_state_270 = copy.deepcopy(state)
                new_state_270.depth += 1
                for i in range(piece + 1, 28):
                    new_state_90.coordinates[i][0] = state.coordinates[piece][0] + (
                        state.coordinates[i][1]-state.coordinates[piece][1])
                    new_state_90.coordinates[i][1] = state.coordinates[piece][1] - (
                        state.coordinates[i][0]-state.coordinates[piece][0])

                    new_state_180.coordinates[i][0] = state.coordinates[piece][0] - (
                        state.coordinates[i][1]-state.coordinates[piece][1])
                    new_state_180.coordinates[i][1] = state.coordinates[piece][1] - (
                        state.coordinates[i][0]-state.coordinates[piece][0])

                    new_state_270.coordinates[i][0] = state.coordinates[piece][0] - (
                        state.coordinates[i][1]-state.coordinates[piece][1])
                    new_state_270.coordinates[i][1] = state.coordinates[piece][1] + (
                        state.coordinates[i][0]-state.coordinates[piece][0])

                successors.append(new_state_90)
                successors.append(new_state_180)
                successors.append(new_state_270)

        return successors
