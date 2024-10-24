from collections import deque
import graphviz

class Tree:
    def __init__(self, nodes):        
        self.nodes = nodes
        self.root = None        
        if not nodes:
            return
        if len(nodes) % 2 == 0:
            nodes.append(None)
        q = deque()
        n = len(nodes)        
        root = TreeNode(nodes[0])
        self.root = root
        q.append(root)
        i = 1
        while i != n:
            current = q.popleft()
            left = nodes[i]
            right = nodes[i+1]
            lnode = TreeNode(left) if left else None
            rnode = TreeNode(right) if right else None
            current.left = lnode
            current.right = rnode
            q.append(lnode)
            q.append(rnode)
            i+=2
    def print_tree(self):
        root = self.root
        dot = graphviz.Digraph()
        dot.node(str(root.val))

        def add_nodes_edges(node):
            if node.left:
                dot.node(str(node.left.val))
                dot.edge(str(node.val), str(node.left.val))
                add_nodes_edges(node.left)
            if node.right:
                dot.node(str(node.right.val))
                dot.edge(str(node.val), str(node.right.val))
                add_nodes_edges(node.right)
        add_nodes_edges(root)
        dot.render('binary_tree', view=True, format='png')

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right