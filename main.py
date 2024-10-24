from tree import Tree
from functions import flipEquiv

with open("input.txt") as f:
    nodes = eval(f.read().split("=")[1].strip().replace("null", "None"))
    t = Tree(nodes)
    t.print_tree()