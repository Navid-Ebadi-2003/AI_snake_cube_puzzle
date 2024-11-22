class IDS_agent:
    def __init__(self, puzzle):
        self.puzzle = puzzle

    def DLS(self, state, limit):
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
        return False

    def IDS(self, max_depth):
        for depth_limit in range(0, max_depth):
            print(f"Searching at depth {depth_limit}...")
            result = self.DLS(self.puzzle.start_state, depth_limit)
            if result is not None:
                return result
        else:
            return False
