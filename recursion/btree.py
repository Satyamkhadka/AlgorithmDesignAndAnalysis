# we will create and use a binary tree.

class BinaryNode:
    def __init__(self,data=None, left=None, right=None, edge=None):
        self.data=data
        self.left=left
        self.right=right
        self.edge=edge
        
        def is_leaf():
            return left is None and right is None

class BinaryTree:
    def __init__(self,root=None):
        self.root=root

        