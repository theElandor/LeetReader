from tree import Tree
from functions import flipEquiv
from utils import read_nodes
import os

nodes = [read_nodes("t1.txt"), read_nodes("t2.txt")]
print(nodes)
t1 = Tree(nodes[0])
t2 = Tree(nodes[1])
t1.print_tree()
    #t2.print_tree()