import sys, enum
from collections import deque
from typing import Tuple, TypeVar, Any


def get_maze_input(f):
    temp = f.readline()
    temp_ij = temp.split(",")
    #  getting length & Width
    row = int(temp_ij[0])
    column = int(temp_ij[1].split("\n")[0].strip())
    temp = f.readlines()
    temp_list = []
    # deleting \n from the
    for item in temp:
        temp_list.append(item.split("\n")[0])
    # creating 2D Array for elements
    new_temp_list = []
    for item_in_row in temp_list:
        new_temp_list.append([char for char in item_in_row])
    for row_index in range(len(temp_list)):
        for column_index in range(len(temp_list[row_index])):
            if temp_list[row_index][column_index] == "S":
                s_index = [row_index, column_index]

    return row, column, new_temp_list, s_index


def expand(node: Any):
    if is_expanded(node): return

    node_index_x, node_index_y = node.get()
    counter = 0

    if (node_index_x + 1) <= row:
        node_position = Position(node_index_x + 1, node_index_y)
        child_node = Node(maze_space_array[node_index_x + 1][node_index_y], node, node_position)
        stack.append(child_node)
        counter += 1

    if (node_index_x - 1) >= 0:
        node_position = Position(node_index_x - 1, node_index_y)
        child_node = Node(maze_space_array[node_index_x - 1][node_index_y], node, node_position)
        stack.append(child_node)
        counter += 1

    if (node_index_y + 1) <= column:
        node_position = Position(node_index_x, node_index_y + 1)
        child_node = Node(maze_space_array[node_index_x][node_index_y + 1], node, node_position)
        stack.append(child_node)
        counter += 1

    if (node_index_y - 1) >= 0:
        node_position = Position(node_index_x, node_index_y - 1)
        child_node = Node(maze_space_array[node_index_x][node_index_y - 1], node, node_position)
        stack.append(child_node)
        counter += 1

    if counter != 0:
        visited.add(node)


def is_expanded(node: Any):
    for item in visited:
        if item.get() == node.get():
            return True
    return False


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Node:
    def __init__(self, state, parent: Any | None, index: Position):
        self.parent = parent
        self.state = state
        self.index = index

    def get(self):
        return self.index.x, self.index.y

    def is_goal(self):
        if self.state == "G":
            return True
        else:
            return False

    def goal_path(self):
        final_path = [(self.index.x, self.index.y)]
        temp_node = self.parent
        while temp_node is not None:
            final_path.append((temp_node.index.x, temp_node.index.y))
            temp_node = temp_node.parent

        goal_path = []
        for i in range(len(final_path) - 1, 0, -1):
            curr_coords = final_path[i]
            prev_coords = final_path[i - 1]
            if curr_coords[0] == prev_coords[0] and curr_coords[1] == prev_coords[1] + 1:
                goal_path.append("L")
            elif curr_coords[0] == prev_coords[0] and curr_coords[1] == prev_coords[1] - 1:
                goal_path.append("R")
            elif curr_coords[0] == prev_coords[0] + 1 and curr_coords[1] == prev_coords[1]:
                goal_path.append("U")
            elif curr_coords[0] == prev_coords[0] - 1 and curr_coords[1] == prev_coords[1]:
                goal_path.append("D")

        return " ".join(goal_path)


with open(file="Input.txt", mode="r") as f:
    row, column, maze_space_array, s_index = get_maze_input(f)

stack = deque()
visited = set()
s_postion = Position(s_index[0], s_index[1])
node = Node("S", None, s_postion)
stack.append(node)

while stack:
    current_node = stack.pop()

    if current_node.is_goal():
        current_node.goal_path()
        break
    expand(current_node)
