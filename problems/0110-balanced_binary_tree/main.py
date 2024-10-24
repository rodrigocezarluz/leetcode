from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return [True, 0]

            left, right = dfs(root.left), dfs(root.right)
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
            return [balanced, 1 + max(left[1], right[1])]

        return dfs(root)[0]


class MySolution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check_height_dfs(
            node: Optional[TreeNode],
        ):
            if not node:
                return 0
            h_left = check_height_dfs(node.left)
            r_left = check_height_dfs(node.right)

            if h_left == -1 or r_left == -1 or abs(h_left - r_left) > 1:
                return -1
            else:
                return 1 + max(h_left, r_left)

        return check_height_dfs(root) != -1


test = MySolution()
print(
    test.isBalanced(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7))))
    == True
)
print(
    test.isBalanced(
        TreeNode(
            1,
            TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(4)), TreeNode(3)),
            TreeNode(2),
        )
    )
    == False
)
print(test.isBalanced(TreeNode()) == True)
print(test.isBalanced(TreeNode(1)) == True)
print(test.isBalanced(TreeNode(1, TreeNode(2))) == True)
