from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left: Optional['TreeNode'] = None
        self.right: Optional['TreeNode'] = None

# TODO: Implement the max_depth function
def max_depth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    queue = deque([root])
    depth = 0
    while queue:
        level = len(queue)
        for x in range(level):
            current = queue.popleft()
            print(current.value)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        depth +=1
    return depth

# TODO: Implement the lowest_common_ancestor function
def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    pass
