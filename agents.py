class IDS_agent:
    def __init__(self, puzzle):
        self.puzzle = puzzle

    def DLS(self, state, limit):
        frontier = [state]
        solution = []
        while frontier:

            #debug
            # print(len(frontier) , "*************************")

            node = frontier.pop()

            if len(solution) > node.depth:
                solution = solution[:node.depth]
            solution.append(node)


            if self.puzzle.is_goal(node):
                return solution

            if node.depth >= limit:
                if len(frontier)== 0:
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
        pass

    def RBFS(self, node, f_limit):
        if self.puzzle.is_goal(node):
            return node, None
        successors = self.puzzle.successor(node)
        if not successors:
            return None, 10**9

        Map = {}
        for s in successors:
            s.f = max((s.depth + self.h(s)), node.f)
            Map[s] = s.f

        while True:
            best = min(Map, key=Map.get)
            if best > f_limit:
                return None, best.f

            Map_without_best = Map.copy()
            Map_without_best.pop(best)
            alternative = min(Map_without_best.values())

            result, best.f = self.RBFS(best, min(f_limit, alternative))
            if result != None:
                return result, best.f

    def RECURSIVE_BEST_FIRST_SEARCH(self):                      # ∞
        solution, f_value = self.RBFS(self.puzzle.start_state, 10**9)
        return solution
