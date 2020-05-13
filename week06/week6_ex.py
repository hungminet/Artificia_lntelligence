#Reference: https://eddmann.com/posts/using-iterative-deepening-depth-first-search-in-python/

def Available_move(subject):
    moves = []
    solu = []
    #zero location
    zrow, zcol = next((r,c)
        for r,l in enumerate(subject)
            for c,v in enumerate(l) if v==0)

    def swap(row,col):
        import copy
        s = copy.deepcopy(subject)
        s[zrow][zcol], s[row][col] = s[row][col], s[zrow][zcol]
        return s

    if zrow>0:#zero not in first row
        moves.append(swap(zrow-1,zcol))
        solu.append("UP")

    if zcol>0:#zero not in first col
        moves.append(swap(zrow,zcol-1))
        solu.append("LEFT")

    if zcol < 2:#zero not in last col
        moves.append(swap(zrow,zcol+1))
        solu.append("RIGHT")

    if zrow < 2:#zero not in last col
        moves.append(swap(zrow+1,zcol))
        solu.append("DOWN")

    return moves, solu
solution_step = []
def id_dfs(puzzle,goal):
    import itertools
    def dfs(route,depth):
        if depth==0:
            return
        if route[-1] == goal:
            return route
        for x in range(len(Available_move(route[-1])[0])):
            move = Available_move(route[-1])[0][x]
            action = Available_move(route[-1])[1][x]

            if move not in route:
                next_route = dfs(route + [move],depth-1)
                if next_route:
                    solution_step.append(action)
                    return next_route
    for depth in itertools.count():
        route = dfs([puzzle],depth)
        if route:
            return route

puzzle = [[3,1,2],[6,0,8],[7,5,4]]
goal = [[0,1,2],[3,4,5],[6,7,8]]

solutions = id_dfs(puzzle,goal)
solution_step.reverse()
for solution in solutions:
    for row in solution:
        print(row)
    print()

print(solution_step)