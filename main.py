from tree import Tree
from utils import read_nodes
from functions import flipEquiv
import os

nodes = [read_nodes("t1.txt"), read_nodes("t2.txt")]
print(nodes)
t1 = Tree(nodes[0])
t2 = Tree(nodes[1])
t1.print_tree("t1")
t2.print_tree("t2")
root1 = t1.root
root2 = t2.root
print(flipEquiv(root1=root1, root2=root2))