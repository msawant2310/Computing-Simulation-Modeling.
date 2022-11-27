#Q.2
class TreeNode(object):
    """ Definition of a binary tree node."""
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
def depth(root):
    if root is None:
        return 0
    else:
        left_depth=solution(root.left)
        #print(left_depth,"a")
        right_depth=solution(root.right)
        #print(right_depth,"b")
        
        if(left_depth>right_depth):
            return left_depth+1
        else:
            return right_depth+1

a15=TreeNode(15)
a7=TreeNode(7)
a20=TreeNode(20)
a9=TreeNode(9)
a3=TreeNode(3)
a20.left=a15
a20.right=a7
a3.left=a9
a3.right=a20
print(depth(a3))

#Reference:https://www.geeksforgeeks.org/write-a-c-program-to-find-the-maximum-depth-or-height-of-a-tree/