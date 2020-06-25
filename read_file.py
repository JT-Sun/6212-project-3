import numpy as np
# read all horizon symbols
horizons = []
with open("dash.txt", "r") as f:
    for line in f.readlines():
        line = line.replace("\n", "")
        horizons.append(line)

# count lines in the maze.txt
# maze_file = open("maze/maze1.txt")
# content = maze_file.read()
# num_lines = len(content.split("\n"))


def read_maze_file(file_path):
    x = []
    with open(file_path, "r") as f:
        line_count = 1
        for line in f.readlines():
            line = line.replace("\n", "")
            line = line.rstrip()
            if line_count < 49:
                cells_self = []
                cells_next = []
                cells_str_self = ""
                cells_str_next = ""
                for i in line:
                    # self cell
                    if i != " ":
                        cells_str_self += "1"
                        cells_self.append(1)
                    else:
                        cells_str_self += "0"
                        cells_self.append(0)
                    # next cell (virtual / not represented in the text file)
                    if i in horizons or i == " ":
                        cells_str_next += "0"
                        cells_next.append(0)
                    else:
                        cells_str_next += "1"
                        cells_next.append(1)
                x.append(cells_self)
                x.append(cells_next)

            elif line_count == 49:
                # cells_str = "1" * len(line)
                cell_49 = []
                for i in line:
                    cell_49.append(1)
                x.append(cell_49)
            line_count += 1
    y = np.array(x)
    return y

# test: write modelled graph into text file
# with open("test.txt", "w") as f:
#     for i in x:
#         f.write(i)
#         f.write("\n")
if __name__ == '__main__':
    import random
    c = np.array([[1,2,3], [1,2,3]])
    maze = read_maze_file("maze/maze1.txt")
    zeros = np.argwhere(maze==0)
    b = np.random.choice(zeros.shape[0], 2)
    start_x = zeros[b[0]][0]
    start_y = zeros[b[0]][1]
    end_x = zeros[b[1]][0]
    end_y = zeros[b[1]][1]
    pass
