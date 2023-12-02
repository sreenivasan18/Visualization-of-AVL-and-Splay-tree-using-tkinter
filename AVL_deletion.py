def AVL_deletion():
    
    class AVLNode:
        def __init__(self, key):
            self.key = key
            self.left = None
            self.right = None
            self.height = 1
    
    class AVLTree:
        def __init__(self):
            self.root = None
    
        def height(self, node):
            if not node:
                return 0
            return node.height
    
        def balance(self, node):
            if not node:
                return 0
            return self.height(node.left) - self.height(node.right)
    
        def update_height(self, node):
            if not node:
                return
            node.height = 1 + max(self.height(node.left), self.height(node.right))
    
        def rotate_right(self, y):
            x = y.left
            T2 = x.right
    
            x.right = y
            y.left = T2
    
            self.update_height(y)
            self.update_height(x)
    
            return x
    
        def rotate_left(self, x):
            y = x.right
            T2 = y.left
    
            y.left = x
            x.right = T2
    
            self.update_height(x)
            self.update_height(y)
    
            return y
    
        def insert(self, root, key):
            if not root:
                return AVLNode(key)
    
            if key < root.key:
                root.left = self.insert(root.left, key)
            else:
                root.right = self.insert(root.right, key)
    
            self.update_height(root)
    
            balance = self.balance(root)
    
            if balance > 1:
                if key < root.left.key:
                    print(f"Performing LL Rotation on Node {root.key}")
                    old_root = root
                    root = self.rotate_right(root)
                    print(f"Old Root: {old_root.key}, New Root: {root.key}")
                else:
                    print(f"Performing RR Rotation on Node {root.left.key}")
                    root.left = self.rotate_left(root.left)
                    old_root = root
                    print(f"Performing LL Rotation on Node {root.key}")
                    root = self.rotate_right(root)
                    print(f"Old Root: {old_root.key}, New Root: {root.key}")
    
            if balance < -1:
                if key > root.right.key:
                    print(f"Performing RR Rotation on Node {root.key}")
                    old_root = root
                    root = self.rotate_left(root)
                    print(f"Old Root: {old_root.key}, New Root: {root.key}")
                else:
                    print(f"Performing LL Rotation on Node {root.right.key}")
                    root.right = self.rotate_right(root.right)
                    old_root = root
                    print(f"Performing RR Rotation on Node {root.key}")
                    root = self.rotate_left(root)
                    print(f"Old Root: {old_root.key}, New Root: {root.key}")
    
            return root
    
        def delete(self, root, key):
            if not root:
                return root
        
            if key < root.key:
                root.left = self.delete(root.left, key)
            elif key > root.key:
                root.right = self.delete(root.right, key)
            else:
                if not root.left or not root.right:
                    if not root.left:
                        temp = root.right
                    else:
                        temp = root.left
        
                    if not temp:
                        temp = root
                        root = None
                    else:
                        root = temp
                    temp = None
                else:
                    temp = self.get_min_value_node(root.right)
                    root.key = temp.key
                    root.right = self.delete(root.right, temp.key)
        
            if not root:
                return root
        
            self.update_height(root)
            balance = self.balance(root)
        
            if balance > 1:
                if self.balance(root.left) >= 0:
                    print(f"Performing LL Rotation on Node {root.key}")
                    old_root = root
                    root = self.rotate_right(root)
                    print(f"Old Root: {old_root.key}, New Root: {root.key}")
                else:
                    print(f"Performing RR Rotation on Node {root.key}")
                    root.left = self.rotate_left(root.left)
                    old_root = root
                    print(f"Performing LL Rotation on Node {root.key}")
                    root = self.rotate_right(root)
                    print(f"Old Root: {old_root.key}, New Root: {root.key}")
    
            if balance < -1:
                if self.balance(root.right) <= 0:
                    print(f"Performing RR Rotation on Node {root.key}")
                    old_root = root
                    root = self.rotate_left(root)
                    print(f"Old Root: {old_root.key}, New Root: {root.key}")
                else:
                    print(f"Performing LL Rotation on Node {root.key}")
                    root.right = self.rotate_right(root.right)
                    old_root = root
                    print(f"Performing RR Rotation on Node {root.key}")
                    root = self.rotate_left(root)
                    print(f"Old Root: {old_root.key}, New Root: {root.key}")
        
            return root
        
        def get_min_value_node(self, node):
            
            if not node or not node.left:
                return node
            return self.get_min_value_node(node.left)
    
        def inorder(self, node):
            if node:
                self.inorder(node.left)
                print(node.key, end=" ")
                self.inorder(node.right)
    
        def preorder(self, node):
            if node:
                print(node.key, end=" ")
                self.preorder(node.left)
                self.preorder(node.right)
    
        def postorder(self, node):
            if node:
                self.postorder(node.left)
                self.postorder(node.right)
                print(node.key, end=" ")
                
        def insert_multiple(self, root, keys):
            for key in keys:
                root = self.insert(root, key)
            return root
