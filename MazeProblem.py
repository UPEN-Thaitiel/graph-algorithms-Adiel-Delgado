"""
Insert your code bellow 

our task is to implement an algorithm that can find the way out of a maze.

The maze representation is like this:

    [
      [1,1,1,1,1],
      [1,0,0,1,1],
      [1,1,0,1,1],
      [1,1,0,0,0],
      [1,1,1,1,1],
    ]

So we have a map like this

    integer 0 represents walls

    integer 1 represents valid cells

    cell (0,0) is the starting point (it is the top left corner)

    the bottom right cell is the destination (so this is what we are looking for)

So the solution should be something like this (S represents the states in the solution set):

    [
      [S,-,-,-,-],
      [S,-,-,-,-],
      [S,-,-,-,-],
      [S,-,-,-,-],
      [S,S,S,S,S],
    ]

Good luck!


"""
import queue

def solve(maze):
    #This would let us know if the end or the start are blocked, if this happends the maze can´t be solved.
    n, m = len(maze), len(maze[0])
    if maze [0][0] == 0 or maze[n-1][m-1] == 0:
        return None
    #This would let us know or track the paths that are visited to no loop
    visited = [[False]*m for _ in range(n)]
    visited[0][0] = True
    #This would create or FIFO queue to do our BFS
    q = queue.Queue()
    q.put((0, 0, [(0, 0)]))
    #We define the directions of our path finder, down, up, right, left in that order.
    directions =[(1,0), (-1,0), (0,1), (0,-1)]
    
    while not q.empty():
        x, y, path =q.get()
    #This would mark the short path found
        if (x, y) == (n-1, m-1):
            solved = [row[:] for row in maze]
            for px, py in path:
                solved[px][py] = "S"
            return solved
    #This would explore the neighbors of the paths
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (0 <= nx < n and 0 <= ny < m and maze[nx][ny] == 1 and not visited[nx][ny]):
                visited[nx][ny] = True
    #This would check the limit of every maze
                q.put((nx, ny, path + [(nx, ny)]))
    return None
    #This would help us to print the mazes row per
def print_maze(maze):
    for row in maze:
        print(' '.join(str(cell) for cell in row))
    print()
    
if __name__ == '__main__':
    ### Your code must succesfully solve the following mazes:
    
    m = [[1, 0, 0, 1],
         [1, 0, 0, 1],
         [1, 0, 0, 1],
         [1, 1, 1, 1]
         ]

    easy_maze = [
        [1, 1, 1, 0, 1],
        [1, 0, 1, 0, 1],
        [1, 0, 1, 1, 1],
        [1, 1, 0, 0, 1],
        [0, 1, 1, 1, 1]
    ]

    medium_maze = [
        [1, 1, 0, 1, 1, 0],
        [0, 1, 0, 1, 0, 1],
        [1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1],
        [0, 0, 1, 0, 0, 1]
    ]   
    hard_maze = [
        [1, 0, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1],
        [1, 1, 1, 0, 1, 1, 1],
        [0, 0, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1]
    ]
    for name, maze in [('m', m),
                       ('easy_maze', easy_maze),
                       ('medium_maze', medium_maze),
                       ('hard_maze', hard_maze)]:
        print(f"--- {name} ---")
        sol = solve(maze)
        if sol is None:
            print("There is not a path.\n")
        else:
            print_maze(sol)
