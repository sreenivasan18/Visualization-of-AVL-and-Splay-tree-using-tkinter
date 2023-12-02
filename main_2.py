if __name__ == "__main__":
        
        avl_tree = AVLTree()
    
        while True:
            
            sentences = [
                    "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                    "\n\n\nAVL Tree Menu:"
                    "\nPress 1 to Insert Nodes"
                    "\nPress 2 to Delete a Node"
                    "\nPress 3 to Traverse The AVL Tree"
                    "\nPress 4 to Exit From The AVL Deletion Interface"
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
                    print("\n\nTree is empty. Please insert nodes first.")
                                    
                    print("\n\nPress Enter To Continue")
    
            elif choice == 4:
                print("\n\nYou Have Exited From The AVL TREE Interface, Thank You !!")
                                
                print("\n\nPress Enter To Continue")
                break
    
            else:
                print("\n\nInvalid choice. Please select a valid option.")
                                
                print("\n\nPress Enter To Continue")
                                
            input()
