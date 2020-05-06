# Depth-Firsh Search Algorithm
# ----------------------------
# First Edit: Saturday, April 18,2020
# Second Edit: Sunday, April 19, 2020
# Edit desciption:
#
# Author: Stu.Nguyen Truong An
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
    def __init__(self,filename):
        #read filename
        with open(filename) as f:
            contents = f.read()
        if contents.count('A') != 1:
            raise Exception('Must only one begin Point')
        if contents.count('B') != 1:
            raise Exception('Must only one end Point')
        contents = contents.splitlines()
        self.height = len(contents)
        self.width = max(len(line) for line in contents)

        self.wall = []
        for i in range (self.height):
            row = []
            for j in range (self.width):
                try:
                    if contents[i][j] == 'A':
                        self.start = (i,j)
                        row.append(False)
                    elif contents[i][j] == 'B':
                        self.end = (i,j)
                        row.append(False)
                    elif contents[i][j] == " ":
                        row.append(False)
                    else:
                        row.append(True)
                except IndexError:
                    row.append(False)
            self.wall.append(row)
        self.solution = None

    def print(self):
        #print('Height:',self.height,'Width:',self.width)
        #print(self.wall)
        print('Start Point: ', self.start)
        print('End Point: ', self.end)
        for i in range (self.height):
            if self.solution is not None:
                solution_steps = self.solution[1]
            else:
                solution_steps = None
            print()
            for j in range (self.width):
                if self.wall[i][j] == True:
                    print(' # ', end = '')
                elif self.start == (i,j):
                    print(' A ', end='')
                elif self.end == (i,j):
                    print(' B ', end='')
                elif solution_steps is not None and (i,j) in solution_steps:
                    print(' * ', end='')
                else:
                    print('   ', end = '')
    def Possible_Step(self,state):
        row, col = state
        Possible = [
            ('up',(row-1,col)),
            ('down',(row+1,col)),
            ('left',(row,col-1)),
            ('right',(row,col+1))
        ]
        result = []
        for action, (row,col) in Possible:
            try:
                if not self.wall[row][col]:
                    result.append((action, (row, col)))
            except IndexError:
                continue
        return result

    def Solve(self):
       # self.num_step = 0

        start = Node(state=self.start,parent=None,action=None)
        frontier = StackFrontier()
        frontier.Add(start)

        self.Steps = set()

        while True:
            if frontier.Empty():
                raise Exception('No solution')

            node = frontier.Remove()
            self.num_step += 1

            if node.state == self.end:
                actions = []
                cells = []

                while node.parent is not None:
                    actions.append(node.action)
                    cells.append(node.state)
                    node = node.parent
                actions.reverse()
                cells.reverse()
                self.solution = (actions,cells)
                return
            self.Steps.add(node.state)

            for action, state in self.Possible_Step(node.state):
                if not frontier.Contains_state(state) and state not in self.Steps:
                    child = Node(state=state,parent=node,action=action)
                    frontier.Add(child)

maze = Maze('maze1.txt')
maze.Solve()
print('Steps',maze.Steps)
print('Number of steps',maze.num_step)
#print(maze.solution)
maze.print()
