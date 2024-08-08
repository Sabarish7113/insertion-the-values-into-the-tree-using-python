class Node:
    def __init__(self,data):
        self.val=data
        self.left=None
        self.right=None
        
def insert(root,data):
    if root is None:
        return Node(data)
    if root.val == data:
        return root
    if root.val<data:
        root.right = insert(root.right,data)
    else:
        root.left = insert(root.left,data)
    return root
        
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val,end=" ")
        inorder(root.right)

def preorder(root):
    if root:
        print(root.val,end=" ")
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val,end=" ")
        
        
r=Node(4)
r=insert(r,2)
r=insert(r,5)
r=insert(r,3)
r=insert(r,7)
r=insert(r,6)
r=insert(r,9)
r=insert(r,8)
r=insert(r,1)

print(inorder(r))
print(preorder(r))
print(postorder(r))
            
    