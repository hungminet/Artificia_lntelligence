# Depth-Firsh Search Algorithm
# ----------------------------
# First Edit: Saturday, April 18,2020
# Second Edit: Sunday, April 19, 2020
# Edit desciption:
#
# Author: Stu.Nguyen Truong An
import numpy as np


class Node:
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action


class StackFrontier:
    def __init__(self):
        self.frontier = []

    def Add(self, node):
        self.frontier.append(node)

    def Empty(self):
        return len(self.frontier) == 0

    def Remove(self):
        if self.Empty():
            raise Exception('Empty frontier')
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node

    def Contains_state(self, state):
        return any(node.state == state
                   for node in self.frontier)


class QueryFrontier(StackFrontier):
    def Remove(self):
        if self.Empty():
            raise Exception('Empty frontier')
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node


class Maze:
    def __init__(self):
        # read filename
        self.start = [[3, 1, 2], [6, 0, 8], [7, 5, 4]]
        self.end = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

    def Zero_loc(self, state):
        a = np.array(state)
        for i in range(3):
            for j in range(3):
                if a[i][j] == 0:
                    return (i, j)
        return None

    def Possible_Step(self, state):
        row, col = self.Zero_loc(state)
        Possible = [
            ('up', (row - 1, col)),
            ('down', (row + 1, col)),
            ('left', (row, col - 1)),
            ('right', (row, col + 1))
        ]
        result = []
        for action, (row, col) in Possible:
            try:
                if row >=0 and row <=3 and col >=0 and row <=3:
                    result.append((action, (row, col)))
            except IndexError:
                continue
        return result

    def Solve(self):
        # self.num_step = 0

        start_node = Node(state=self.start, parent=None, action=None)
        frontier = StackFrontier()
        frontier.Add(start_node)

        self.Steps = []

        while True:
            if frontier.Empty():
                raise Exception('No solution')

            node = frontier.Remove()
            #self.num_step += 1

            if node.state == self.end:
                actions = []
                cells = []

                while node.parent is not None:
                    actions.append(node.action)
                    cells.append(node.state)
                    node = node.parent
                actions.reverse()
                cells.reverse()
                self.solution = (actions, cells)
                return
            self.Steps.append(node.state)

            for action, state in self.Possible_Step(node.state):
                if not frontier.Contains_state(state) and state not in self.Steps:
                    child = Node(state=state, parent=node, action=action)
                    frontier.Add(child)


maze = Maze()
maze.Solve()
print('Steps', maze.Steps)
print('Number of steps', maze.num_step)

