class Node:
    def __init__(self,data):
        self.data= data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

def insertion(root,data):
    if root is None:
        root = Node(data)
        return root
    queue = []
    queue.append(root)
    
    while queue:
        temp = queue.pop(0)
        if not temp.left:
            temp.left=Node(data)
            break
        else:
            queue.append(temp.left)
        if not temp.right:
            temp.right = Node(data)
            break
        else:
            queue.append(temp.right)
        
    return root


def bfs(root):
    queue = []
    queue.append(root)
    while queue:
        temp = queue.pop(0)
        print(temp.data)
        if temp.left:
            queue.append(temp.left)
        if temp.right:
            queue.append(temp.right)

def inorder(root):
    if not root is None:
        inorder(root.left)
        print(root.data)
        inorder(root.right)
def preorder(root):
    if not root is None:
        print(root.data)
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if not root is None:
        postorder(root.left)
        postorder(root.right)
        print(root.data)
root = insertion(None,0)
print("one")
insertion(root,1)
print("two")
insertion(root,2)
print(3)
insertion(root,3)
print(4)
insertion(root,4)
print(5)
insertion(root,5)
print(6)
insertion(root,6)
print(7)
insertion(root,7)
print(8)
insertion(root,8)
print(9)
insertion(root,9)
print(10)
insertion(root,10)

# now traversal 
print("bfs")

bfs(root)
print("inorder")

inorder(root)

print("preorder")
preorder(root)

print("postorder")
postorder(root)