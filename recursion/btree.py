from collections import deque

# Node class to define the structure of the node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = self.right = None

# Function to insert nodes
def insert(root, data):
    # If tree is empty, new node becomes the root
    if root is None:
        root = Node(data)
        return root
    
    # Queue to traverse the tree and find the position to insert the node
    q = deque()
    q.append(root)
    while q:
        temp = q.popleft()
        # Insert node as the left child of the parent node
        if temp.left is None:
            temp.left = Node(data)
            break
        # If the left child is not null push it to the queue
        else:
            q.append(temp.left)
        # Insert node as the right child of parent node
        if temp.right is None:
            temp.right = Node(data)
            break
        # If the right child is not null push it to the queue
        else:
            q.append(temp.right)
    return root

# Function to delete the given deepest node (d_node) in binary tree
def deletDeepest(root, d_node):
    q = deque()
    q.append(root)
    # Do level order traversal until last node
    while q:
        temp = q.popleft()
        if temp == d_node:
            temp = None
            del d_node
            return
        if temp.right:
            if temp.right == d_node:
                temp.right = None
                del d_node
                return
            else:
                q.append(temp.right)
        if temp.left:
            if temp.left == d_node:
                temp.left = None
                del d_node
                return
            else:
                q.append(temp.left)

# Function to delete element in binary tree
def deletion(root, key):
    if not root:
        return None
    if root.left is None and root.right is None:
        if root.data == key:
            return None
        else:
            return root
    
    q = deque()
    q.append(root)
    temp = None
    key_node = None
    # Do level order traversal to find deepest node (temp) and node to be deleted (key_node)
    while q:
        temp = q.popleft()
        if temp.data == key:
            key_node = temp
        if temp.left:
            q.append(temp.left)
        if temp.right:
            q.append(temp.right)
    
    if key_node is not None:
        x = temp.data
        key_node.data = x
        deletDeepest(root, temp)
    return root

# Inorder tree traversal (Left - Root - Right)
def inorderTraversal(root):
    if not root:
        return
    inorderTraversal(root.left)
    print(root.data, end=" ")
    inorderTraversal(root.right)

# Preorder tree traversal (Root - Left - Right)
def preorderTraversal(root):
    if not root:
        return
    print(root.data, end=" ")
    preorderTraversal(root.left)
    preorderTraversal(root.right)

# Postorder tree traversal (Left - Right - Root)
def postorderTraversal(root):
    if root is None:
        return
    postorderTraversal(root.left)
    postorderTraversal(root.right)
    print(root.data, end=" ")

# Function for Level order tree traversal
def levelorderTraversal(root):
    if root is None:
        return
    
    # Queue for level order traversal
    q = deque()
    q.append(root)
    while q:
        temp = q.popleft()
        print(temp.data, end=" ")
        # Push left child in the queue
        if temp.left:
            q.append(temp.left)
        # Push right child in the queue
        if temp.right:
            q.append(temp.right)

# Driver function to check the above algorithm
if __name__ == "__main__":
    root = None
    # Insertion of nodes
    root = insert(root, 10)
    root = insert(root, 20)
    root = insert(root, 30)
    root = insert(root, 40)

    print("Preorder traversal:", end=" ")
    preorderTraversal(root)

    print("\nInorder traversal:", end=" ")
    inorderTraversal(root)

    print("\nPostorder traversal:", end=" ")
    postorderTraversal(root)

    print("\nLevel order traversal:", end=" ")
    levelorderTraversal(root)

    # Delete the node with data = 20
    root = deletion(root, 20)

    print("\nInorder traversal after deletion:", end=" ")
    inorderTraversal(root)