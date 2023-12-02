def AVL_extra_functions():
    
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
                    return self.rotate_right(root)
                else:
                    root.left = self.rotate_left(root.left)
                    return self.rotate_right(root)
    
            if balance < -1:
                if key > root.right.key:
                    return self.rotate_left(root)
                else:
                    root.right = self.rotate_right(root.right)
                    return self.rotate_left(root)
    
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
                    return self.rotate_right(root)
                else:
                    root.left = self.rotate_left(root.left)
                    return self.rotate_right(root)
        
            if balance < -1:
                if self.balance(root.right) <= 0:
                    return self.rotate_left(root)
                else:
                    root.right = self.rotate_right(root.right)
                    return self.rotate_left(root)
        
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
    
        def search(self, root, key):
            if not root or root.key == key:
                return root
    
            if root.key < key:
                return self.search(root.right, key)
    
            return self.search(root.left, key)
        
        def find_min(self, root):
            current = root
            while current.left is not None:
                current = current.left
            return current
        
        def find_max(self, root):
            current = root
            while current.right is not None:
                current = current.right
            return current
        
        def count_nodes(self, root):
            if not root:
                return 0
            return 1 + self.count_nodes(root.left) + self.count_nodes(root.right)
    
    if __name__ == "__main__":
        
        avl_tree = AVLTree()
    
        while True:
            
            sentences = [
                    "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                    "\n\n\nAVL Tree Menu:"
                    "\nPress 1 to Insert Nodes"
                    "\nPress 2 to Delete a Node"
                    "\nPress 3 to Traverse The AVL Tree"
                    "\nPress 4 to Perform Additional Functions"
                    "\nPress 5 to Exit From The AVL Deletion Interface"
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
                    
                avl_tree.root = avl_tree.insert_multiple(avl_tree.root, keys)
                print("Nodes are inserted successfully!")
                                
                print("\n\nPress Enter To Continue")
    
            elif choice == 2:
                
                key = int(input("\n\nEnter the key to delete: "))
                avl_tree.root = avl_tree.delete(avl_tree.root, key)
                print("Node deleted successfully!")
                                
                print("\n\nPress Enter To Continue")
    
            elif choice == 3:
                
                if avl_tree.root:
                    
                    print("\n\nInorder Traversal:")
                    avl_tree.inorder(avl_tree.root)
                    
                    print("\nPreorder Traversal:")
                    avl_tree.preorder(avl_tree.root)
                    
                    print("\nPostorder Traversal:")
                    avl_tree.postorder(avl_tree.root)
                                    
                    print("\n\nPress Enter To Continue")
                    
                else:
                    print("Tree is empty. Please insert nodes first.")
                                    
                    print("\n\nPress Enter To Continue")
    
            elif choice == 4:
                
                sentences = [
                        "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                        "\n\nAdditional Functions Menu:"
                        "\nPress 1 to Search for a Node"
                        "\nPress 2 to Find the Minimum Value"
                        "\nPress 3 to Find the Maximum Value"
                        "\nPress 4 to Count Nodes"
                    ]
                
                for sentence in sentences:
                    print_letter_by_letter_2(sentence)
                
                additional_choice = int(input("\nEnter your additional choice: "))
                
                if additional_choice == 1:
                    key = int(input("\n\nEnter the key to search: "))
                    result = avl_tree.search(avl_tree.root, key)
                    if result:
                        print(f"\n\nNode with key {key} found in the AVL tree.")
                                        
                        print("\n\nPress Enter To Continue")
                    else:
                        print(f"\n\nNode with key {key} not found in the AVL tree.")
                                        
                        print("\n\nPress Enter To Continue")
                        
                elif additional_choice == 2:
                    min_node = avl_tree.find_min(avl_tree.root)
                    print(f"\n\nMinimum value node: {min_node.key}")
                                    
                    print("\n\nPress Enter To Continue")
                    
                elif additional_choice == 3:
                    max_node = avl_tree.find_max(avl_tree.root)
                    print(f"\n\nMaximum value node: {max_node.key}")
                                    
                    print("\n\nPress Enter To Continue")
                    
                elif additional_choice == 4:
                    count = avl_tree.count_nodes(avl_tree.root)
                    print(f"\n\nNumber of nodes in the AVL tree: {count}")
                                    
                    print("\n\nPress Enter To Continue")
    
            elif choice == 5:
                print("\n\nYou Have Exited From The AVL TREE Interface, Thank You !!")
                                
                print("\n\nPress Enter To Continue")
                break
    
            else:
                print("\n\nInvalid choice. Please select a valid option.")
                                
                print("\n\nPress Enter To Continue")
                                
            input()
    
