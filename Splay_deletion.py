def Splay_deletion():
    
    class Node:
        def __init__(self, data):
            self.data = data
            self.parent = None
            self.left = None
            self.right = None
    
    class SplayTree:
        def __init__(self):
            self.root = None
    
        def maximum(self, x):
            while x.right:
                x = x.right
            return x
    
        def left_rotate(self, x):
            y = x.right
            x.right = y.left
            if y.left:
                y.left.parent = x
    
            y.parent = x.parent
            if not x.parent:
                self.root = y
            elif x == x.parent.left:
                x.parent.left = y
            else:
                x.parent.right = y
    
            y.left = x
            x.parent = y
    
        def right_rotate(self, x):
            y = x.left
            x.left = y.right
            if y.right:
                y.right.parent = x
    
            y.parent = x.parent
            if not x.parent:
                self.root = y
            elif x == x.parent.right:
                x.parent.right = y
            else:
                x.parent.left = y
    
            y.right = x
            x.parent = y
    
        def splay(self, n):
            while n.parent:
                if n.parent == self.root:
                    if n == n.parent.left:
                        print(f"Performing Zig Rotation on Node {n.parent.data}")
                        old_root = self.root
                        self.right_rotate(n.parent)
                        print(f"Old Root: {old_root.data}, New Root: {self.root.data}")
                    else:
                        print(f"Performing Zag Rotation on Node {n.parent.data}")
                        old_root = self.root
                        self.left_rotate(n.parent)
                        print(f"Old Root: {old_root.data}, New Root: {self.root.data}")
                else:
                    p = n.parent
                    g = p.parent
                    if n.parent.left == n and p.parent.left == p:
                        print(f"Performing Zig-Zig Rotation on Node {g.data}")
                        old_root = self.root
                        self.right_rotate(g)
                        self.right_rotate(p)
                        print(f"Old Root: {old_root.data}, New Root: {self.root.data}")
                    elif n.parent.right == n and p.parent.right == p:
                        print(f"Performing Zag-Zag Rotation on Node {g.data}")
                        old_root = self.root
                        self.left_rotate(g)
                        self.left_rotate(p)
                        print(f"Old Root: {old_root.data}, New Root: {self.root.data}")
                    elif n.parent.right == n and p.parent.left == p:
                        print(f"Performing Zig-Zag Rotation on Node {g.data}")
                        old_root = self.root
                        self.left_rotate(p)
                        self.right_rotate(g)
                        print(f"Old Root: {old_root.data}, New Root: {self.root.data}")
                    elif n.parent.left == n and p.parent.right == p:
                        print(f"Performing Zag-Zig Rotation on Node {g.data}")
                        old_root = self.root
                        self.right_rotate(p)
                        self.left_rotate(g)
                        print(f"Old Root: {old_root.data}, New Root: {self.root.data}")
    
        def insert(self, n):
            y = None
            temp = self.root
            while temp:
                y = temp
                if n.data < temp.data:
                    temp = temp.left
                else:
                    temp = temp.right
    
            n.parent = y
    
            if not y:
                self.root = n
            elif n.data < y.data:
                y.left = n
            else:
                y.right = n
    
            self.splay(n)
    
        def search(self, n, x):
            if x == n.data:
                self.splay(n)
                return n
            elif x < n.data:
                return self.search(n.left, x)
            elif x > n.data:
                return self.search(n.right, x)
            else:
                return None
    
        def delete(self, key):
            node = self.search(self.root, key)
            if node:
                print(f"Deleting Node {node.data}")
                old_root = self.root
                self.splay(node)
                
                left_subtree = SplayTree()
                left_subtree.root = self.root.left
                
                if left_subtree.root:
                    left_subtree.root.parent = None
                    
                right_subtree = SplayTree()
                right_subtree.root = self.root.right
                
                if right_subtree.root:
                    right_subtree.root.parent = None
                    
                if left_subtree.root:
                    m = left_subtree.maximum(left_subtree.root)
                    left_subtree.splay(m)
                    left_subtree.root.right = right_subtree.root
                    self.root = left_subtree.root
                    if right_subtree.root:
                        right_subtree.root.parent = left_subtree.root
                        
                else:
                    self.root = right_subtree.root
                    
                if self.root:
                    self.root.parent = None
                    
                print(f"Old Root: {old_root.data}, New Root: {self.root.data}")
    
    
        def inorder(self, node):
            if node:
                self.inorder(node.left)
                print(node.data, end=" ")
                self.inorder(node.right)
    
        def preorder(self, node):
            if node:
                print(node.data, end=" ")
                self.preorder(node.left)
                self.preorder(node.right)
    
        def postorder(self, node):
            if node:
                self.postorder(node.left)
                self.postorder(node.right)
                print(node.data, end=" ")
                
        def insert_multiple(self, keys):
            for key in keys:
                new_node = Node(key)
                self.insert(new_node)
