#Reference: https://eddmann.com/posts/using-iterative-deepening-depth-first-search-in-python/

def print_2ds(solutions):
    for solution in solutions:
        for solu in solution:
            print(solu)
        print()




def num_moves(rows, cols):
    def Available_Move(subject):
        moves = []
        solu = []
        zrow, zcol = next((r, c)
            for r, l in enumerate(subject)
                for c, v in enumerate(l) if v == 0)

        def swap(row, col):
            import copy
            s = copy.deepcopy(subject)
            s[zrow][zcol], s[row][col] = s[row][col], s[zrow][zcol]
            return s

        # north
        if zrow > 0:
            moves.append(swap(zrow - 1, zcol))
            solu.append("UP")
        # east
        if zcol < cols - 1:
            moves.append(swap(zrow, zcol + 1))
            solu.append("RIGHT")

        # south
        if zrow < rows - 1:
            moves.append(swap(zrow + 1, zcol))
            solu.append("DOWN")


        # west
        if zcol > 0:
            moves.append(swap(zrow, zcol - 1))
            solu.append("LEFT")

        return moves, solu
    return Available_Move


big_sol = []
def id_dfs(puzzle, goal, Available_Move):
    import itertools
    def dfs(route, depth):
        udlr = []
        if depth == 0:
            return
        if route[-1] == goal:
            print("this is route", route)
            return route, udlr
        for x in range(len(Available_Move(route[-1])[0])):
            move = Available_Move(route[-1])[0][x]
            step = Available_Move(route[-1])[1][x]

            if move not in route:
                next_route = dfs(route + [move], depth - 1)
                if next_route:
                    print("Move: ", move)
                    print("Action: ", step)
                    big_sol.append(step)
                    return next_route


    for depth in itertools.count():
        route = dfs([puzzle], depth)
        if route:
            return route

puzzle = [[3,1,2],[6,0,8],[7,5,4]]
goal = [[0,1,2],[3,4,5],[6,7,8]]
solutions = id_dfs(puzzle, goal, num_moves(3, 3))
big_sol.reverse()
count =0
for so in solutions:
    for a in so:
        for k in a:
            print(k)
        print()
        print(big_sol[count])
        count += 1
#print_2ds(solutions)
print(big_sol)