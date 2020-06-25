"""
0,0,1,0,0
0,0,0,0,0
0,0,0,1,0
1,1,0,1,1
0,0,0,0,0

"""
from read_file import read_maze_file
import numpy as np
import time
import matplotlib.pyplot as plt
from numpy.polynomial.polynomial import polyfit
import seaborn as sns


def dfs_maze(maze, start, end):
    """

    :param maze: two dimensional array with ones and zeros
    :param start: tuple as (x, y)
    :param end: tuple as (x, y)
    :return: path if found and searching steps
    """
    # maze is represented as cells
    # each cell is either 1 or 0, where 1 is wall, 0 is path
    # each cell has a coordinate (x, y)

    # check if start and end are valid positions

    #
    if start[0] == end[0] and start[1] == end[1]:
        return True

    # directions: right, left, up, down
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    x, y = start[0], start[1]
    for dx, dy in dirs:
        nx = x
        ny = y
        while 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] != 1:
            nx += dx
            ny += dy
            global a
            a += 1
            if nx == end[0] and ny == end[1]:
                return True
        nx -= dx
        ny -= dy
        # visited position
        if maze[nx][ny] != 0:
            continue

        maze[nx][ny] = 2

        if dfs_maze(maze, (nx, ny), end):
            return True
    return False


if __name__ == '__main__':
    count = 0
    search_steps = []
    time_cost = []
    maze = read_maze_file("maze2.txt")
    zeros = np.argwhere(maze == 0)

    for start_x, start_y in zeros:
        if count < 1000:
            break_count = 0
            for end_x, end_y in zeros:
                a = 0
                if break_count < 30:
                    if start_x != end_x or start_y != end_y:
                        maze = read_maze_file("maze2.txt")
                        time1 = time.time_ns()
                        result = dfs_maze(maze, (start_x, start_y), (end_x, end_y))
                        time2 = time.time_ns()
                        time3 = time2 - time1
                        if result:
                            count += 1
                            print("********", count)
                            print("start:", (start_x, start_y))
                            print("end:", (end_x, end_y))
                            print("total search steps:", a)
                            print("total time cost:", time3)

                            print("successful search time:", count)
                            search_steps.append(a)
                            time_cost.append(time3)
                        else:
                            break_count += 1
                else:
                    break
        else:
            break

    ax = sns.regplot(x=search_steps, y=time_cost,line_kws={'color': 'red'})
    plt.xlabel("search steps")
    plt.ylabel("time cost in ns")
    plt.show()
