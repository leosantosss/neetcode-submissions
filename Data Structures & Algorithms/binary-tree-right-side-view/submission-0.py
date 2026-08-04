# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = collections.deque()

        if not root:
            return res

        q.append(root)
        while q:
            qLen = len(q)
            for i in range (qLen):
                node = q.popleft()
                if node and i == (qLen - 1):
                    res.append(node.val)
                    if node.left is not None:
                        q.append(node.left)
                    if node.right is not None:
                        q.append(node.right) 
                elif node:
                    if node.left is not None:
                        q.append(node.left)
                    if node.right is not None:
                        q.append(node.right)
                else:
                    continue

        return res
            

            