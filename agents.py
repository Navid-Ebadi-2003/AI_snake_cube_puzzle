import math


class IDS_agent:
    def __init__(self, puzzle):
        self.puzzle = puzzle

    def DLS(self, state, limit):
        frontier = [state]
        solution = []
        while frontier:

            # debug
            # print(len(frontier) , "*************************")

            node = frontier.pop()

            if len(solution) > node.depth:
                solution = solution[:node.depth]
            solution.append(node)

            if self.puzzle.is_goal(node):
                return solution

            if node.depth >= limit:
                if len(frontier) == 0:
                    return None
            else:
                for child in self.puzzle.successor(node):
                    frontier.append(child)

        return False

    def IDS(self, max_depth):
        for depth_limit in range(0, max_depth):
            print(f"Searching at depth {depth_limit}...")
            result = self.DLS(self.puzzle.start_state, depth_limit)
            if result is not None:
                return result
        else:
            return False


class RBFS_agent:
    def __init__(self, puzzle):
        self.puzzle = puzzle

    def h(self, state):

        manhattan_distance = 0
        for i in range(1, 28):
            manhattan_distance += math.sqrt((self.puzzle.goal_state_Coo[i][0]-state.coordinates[i][0])**2 + (
                self.puzzle.goal_state_Coo[i][1]-state.coordinates[i][1])**2 + (self.puzzle.goal_state_Coo[i][2]-state.coordinates[i][2])**2)
        return manhattan_distance

    def RBFS(self, node, f_limit):
        if self.puzzle.is_goal(node):
            return node, -1
        
        successors = self.puzzle.successor(node)
        for s in successors:
            s.f = s.depth + self.h(s)

        if not successors:
            return None, math.inf

    
        successors.sort(key=lambda s: s.f)

        print("---------------------------")

        while True:
            best = successors[0]

            if best.f > f_limit:
                return None, best.f

            alternative = successors[1].f if len(successors) > 1 else math.inf

            #debug
            print("f:" , best.f)
            print("depth:" , best.depth)

            result, best.f = self.RBFS(best, min(f_limit, alternative))
            successors.sort(key=lambda s: s.f)

            if result != None:
                return result, best.f

    def RECURSIVE_BEST_FIRST_SEARCH(self):                      # ∞
        solution, f_value = self.RBFS(self.puzzle.start_state, math.inf)
        return solution
