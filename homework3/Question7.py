#Q.7
class TreeNode(object):
    """ Definition of a binary tree node."""
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Tree_Path:
    def PathSum(self, root, targetSum: int) -> bool:
        if not root:
            return False

        if not root.left and not root.right and root.val == targetSum:
            return True
        
        targetSum -= root.val

        return self.PathSum(root.left, targetSum) or self.PathSum(root.right, targetSum)

a5=TreeNode(5)
a4=TreeNode(4)
a8=TreeNode(8)
a11=TreeNode(11)
a13=TreeNode(13)
a7=TreeNode(7)
a2=TreeNode(2)
a1=TreeNode(1)
a5.left=a4
a5.right=a8
a4.left=a11
a11.right=a2
a11.left=a7
a8.right=a4
a8.left=a13
a13.left=a1
print(Tree_Path().PathSum(a5,22))
#print(Tree_Path(a5))

#Reference: https://leetcode.com/problems/path-sum/discuss/2687057/Faster-than-94.77-or-Petykhon