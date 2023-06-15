import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()


import sys
from typing import Any


# input_file = open(file="Input.txt", mode="r")
# temp = input_file.readlines()
# temp_list = []
# for item in temp:
#     temp_list.append(item.split("\n")[0])
#     # print(item.split("\n"))

# temp_list = [["x", "a"], ["y", "b"], ["z", "c"]]
# for row in temp_list:
#     print(row.pop())
# sys.exit()
# print("final result = ", temp_list)
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


pos1 = Position(0, 0)
pos2 = Position(0, 1)
pos3 = Position(1, 1)
pos4 = Position(2, 1)
tenp_node1 = Node('s', None, pos1)
tenp_node2 = Node('s', tenp_node1, pos2)
tenp_node3 = Node('s', tenp_node2, pos3)
tenp_node4 = Node('s', tenp_node3, pos4)
print(Node.goal_path(tenp_node4))

