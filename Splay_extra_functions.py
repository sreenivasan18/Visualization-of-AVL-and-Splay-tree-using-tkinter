def Splay_extra_functions():
    
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
                        self.right_rotate(n.parent)
                    else:
                        self.left_rotate(n.parent)
                else:
                    p = n.parent
                    g = p.parent
                    if n.parent.left == n and p.parent.left == p:
                        self.right_rotate(g)
                        self.right_rotate(p)
                    elif n.parent.right == n and p.parent.right == p:
                        self.left_rotate(g)
                        self.left_rotate(p)
                    elif n.parent.right == n and p.parent.left == p:
                        self.left_rotate(p)
                        self.right_rotate(g)
                    elif n.parent.left == n and p.parent.right == p:
                        self.right_rotate(p)
                        self.left_rotate(g)
    
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
            if n is None or x == n.data:
                if n:
                    self.splay(n)
                return n
            if x < n.data:
                return self.search(n.left, x) or n
            return self.search(n.right, x) or n
    
        def delete(self, key):
            node = self.search(self.root, key)
            if node:
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
                
        def depth(self, node):
            if not node:
                return 0
            left_depth = self.depth(node.left)
            right_depth = self.depth(node.right)
            return max(left_depth, right_depth)+1
        
        def size(self, node):
            if not node:
                return 0
            left_size = self.size(node.left)
            right_size = self.size(node.right)
            return left_size + right_size + 1
    
        def count_nodes_less_than(self, key):
            def count_less_than_recursive(node, key):
                if node is None:
                    return 0
                count = 0
                if node.data < key:
                    count += 1
                count += count_less_than_recursive(node.left, key)
                count += count_less_than_recursive(node.right, key)
                return count
        
            return count_less_than_recursive(self.root, key)

    
    if __name__ == "__main__":
        
        splay_tree = SplayTree()
    
        while True:
            
            sentences = [
                    "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                    "\n\n\nSplay Tree Menu:"
                    "\nPress 1 to Insert Nodes"
                    "\nPress 2 to Delete a Node"
                    "\nPress 3 to Traverse The Splay Tree"
                    "\nPress 4 to Perform Additional Functions"
                    "\nPress 5 to Exit From The Splay Tree Interface"
                ]
                
            for sentence in sentences:
                print_letter_by_letter_2(sentence)
                
            choice = int(input("\nEnter your choice: "))
    
            if choice == 1:
                num_nodes = int(input("\n\nEnter the number of nodes to be inserted: "))
                keys = []
    
                for i in range(num_nodes):
                    key = int(input(f"Enter key {i + 1}: "))
                    keys.append(key)
    
                splay_tree.insert_multiple(keys)
                print("Nodes are inserted successfully!")
                                
                print("\n\nPress Enter To Continue")
    
            elif choice == 2:
                key = int(input("\n\nEnter the key to delete: "))
                splay_tree.delete(key)
                print("Node deleted successfully!")
                                
                print("\n\nPress Enter To Continue")
    
            elif choice == 3:
                if splay_tree.root:
                    print("\n\nInorder Traversal:")
                    splay_tree.inorder(splay_tree.root)
    
                    print("\nPreorder Traversal:")
                    splay_tree.preorder(splay_tree.root)
    
                    print("\nPostorder Traversal:")
                    splay_tree.postorder(splay_tree.root)
                                    
                    print("\n\nPress Enter To Continue")
                else:
                    print("Tree is empty. Please insert nodes first.")
                                    
                    print("\n\nPress Enter To Continue")
    
            elif choice == 4:
                
                sentences = [
                        "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                        "\n\nAdditional Functions Menu:"
                        "\nPress 1 to Find the Depth of the Tree"
                        "\nPress 2 to Find the Size of the Tree"
                        "\nPress 3 to Find the Height of the Tree"
                        "\nPress 4 to Find the Number of nodes less than the perticular key/data"
                    ]
                    
                for sentence in sentences:
                    print_letter_by_letter_2(sentence)
                    
                additional_choice = int(input("\nEnter your additional choice: "))
    
                if additional_choice == 1:
                    depth = splay_tree.depth(splay_tree.root)
                    print(f"\n\nDepth of the tree: {depth}")
                                    
                    print("\n\nPress Enter To Continue")
    
                elif additional_choice == 2:
                    size = splay_tree.size(splay_tree.root)
                    print(f"\n\nSize of the tree: {size}")
                                    
                    print("\n\nPress Enter To Continue")
    
                elif additional_choice == 3:
                    height = splay_tree.depth(splay_tree.root)
                    print(f"Height of node with key {key}: {height-1}")
                                    
                    print("\n\nPress Enter To Continue")
    
                elif additional_choice == 4:
                    key = int(input("\n\nEnter the key to find the number of nodes less than it: "))
                    count = splay_tree.count_nodes_less_than(key)
                    
                    print(f"Number of nodes with values less than {key}: {count}")
                                    
                    print("\n\nPress Enter To Continue")
    
            elif choice == 5:
                print("\n\nYou have exited from the Splay Tree Interface. Thank you!")
                                
                print("\n\nPress Enter To Continue")
                break
    
            else:
                print("\n\nInvalid choice. Please select a valid option.")
                                
                print("\n\nPress Enter To Continue")
                                
            input()
   
