# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()
        res = []
        if root:
            q.append(root)

        while q:
            right = None
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    right = node
                    q.append(right.left)
                    q.append(right.right)
            if right:
                res.append(right.val)
        return res








