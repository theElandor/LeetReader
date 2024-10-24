from tree import TreeNode
from typing import Optional
def inorder_dfs_(root: TreeNode):    
    if not root:
        return []
    left = inorder_dfs_(root.left)
    right = inorder_dfs_(root.right)
    return left + [root.val] + right
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
