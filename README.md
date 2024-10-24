# Dependencies
+ graphviz
# Installation
First of all, you need to install graphviz and make sure that the executables are in your system path. You can follow
the official documentation https://graphviz.readthedocs.io/en/stable/manual.html.
# Quickstart
You can find the main classes and functions in the tree.py and utils.py files. For example, you can create a binary tree using LeetCode input format by following the example below:
```python
from tree import Tree
from utils import read_nodes
nodes = read_nodes("input.txt")
t = Tree(nodes[0])
root = t.root
```
where the content of .data/input.txt is the following:
```
[1,2,3,4,5,6,null,null,null,7,8]
```
This will produce a **Tree** object which points to the root
of your tree. Then, you can write your algorithm in the functions.py file. For example, you can find below the solution of this problem https://leetcode.com/problems/flip-equivalent-binary-trees/description/ :
```python
def flipEquiv(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
    if (not root1) and (not root2):
        return True    
    if (not root1) or (not root2):
        return False
    if root1.val != root2.val:
        return False
    ll = flipEquiv(root1.left, root2.left)
    lr = flipEquiv(root1.left, root2.right)
    rl = flipEquiv(root1.right, root2.left)
    rr = flipEquiv(root1.right, root2.right)
    return ((ll or lr) and (rl or rr))
```
You can also draw the resulting tree using the print_tree() method of the Tree class, which will produce a .png image:
```python
t.print_tree("example_tree")
```