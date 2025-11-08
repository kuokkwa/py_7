from dataclasses import dataclass
from collections import deque
from typing import Optional, List

@dataclass
class TreeNode:
    value: int
    left: Optional['TreeNode'] = None
    right: Optional['TreeNode'] = None

n3 = TreeNode(3)
n2 = TreeNode(2, left=None, right=n3)
n4 = TreeNode(4, left=n2, right=None)

n17 = TreeNode(17)
n18 = TreeNode(18, left=None, right=n17)
n13 = TreeNode(13)
n16 = TreeNode(16, left=n13, right=n18)

root = TreeNode(10, left=n4, right=n16)

def dfs_preorder(node: Optional[TreeNode], acc: List[int]):
    if node is None:
        return
    acc.append(node.value)
    dfs_preorder(node.left, acc)
    dfs_preorder(node.right, acc)

def bfs(root: Optional[TreeNode]) -> List[int]:
    if root is None:
        return []
    q = deque([root])
    order = []
    while q:
        node = q.popleft()
        order.append(node.value)
        if node.left is not None:
            q.append(node.left)
        if node.right is not None:
            q.append(node.right)
    return order

dfs_result = []
dfs_preorder(root, dfs_result)
bfs_result = bfs(root)

print("Обхід в глибину:", " -> ".join(map(str, dfs_result)))
print("Обхід в ширину):", " -> ".join(map(str, bfs_result)))