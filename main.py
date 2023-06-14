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


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Node:
    def __init__(self, state, parent: Any | None, index: Position):
        self.parent = parent
        self.state = state
        self.index = index

    def is_goal(self):
        if self.state == "G":
            return True
        else:
            return False

    def goal_path(self):
        final_path = [(self.index.x, self.index.y)]
        temp_node = self.parent
        while True:
            final_path.append((temp_node.index.x, temp_node.index.y))
            if temp_node.parent is None:
                break
            temp_node = temp_node.parent
        while True:

            if final_path[0][0] == final_path[1][0] and final_path[1][1]+1 == final_path[0][1]:
                goal_path = "R , "
            if final_path[0][0] == final_path[1][0] and final_path[1][1] == final_path[0][1] + 1 :
                goal_path = "L , "
            if final_path[0][1] == final_path[1][1] and final_path[0][0] + 1 == final_path[1][0]:
                goal_path = "U , "
            if final_path[0][0] == final_path[1][0] and final_path[1][1] == final_path[0][1] + 1 :
                goal_path = "D , "
            if final_path[]


    # def expand(self, )


with open(file="Input.txt", mode="r") as f:
    row, column, maze_space_array, s_index = get_maze_input(f)

stack = deque()
visited = set()
s_postion = Position(s_index[0], s_index[1])

node = Node("S", )

stack.insert(node)

while stack:
    current_node = stack.pop()

    # if Node.is_goal(current_node): Node_path(current_node)

    # expand(current_node)
