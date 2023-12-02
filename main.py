if __name__ == "__main__":
        
        avl_tree = AVLTree()
    
        while True:
                 
            sentences = [
                    "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                    "\n\n\nAVL Tree Insertion Menu:"
                    "\nPress 1 to Insert a Node"
                    "\nPress 2 to Traverse The Tree"
                    "\nPress 3 to Exit From the AVL Tree Insertion Interface"
                ]
            
            for sentence in sentences:
                print_letter_by_letter_2(sentence)
                
            choice = int(input("\nEnter your choice: "))
    
            if choice == 1:
                key = int(input("\n\nEnter the key to be inserted: "))
                avl_tree.root = avl_tree.insert(avl_tree.root, key)
                print("Node inserted successfully!")
                
                print("\n\nPress Enter To Continue")
    
            elif choice == 2:
                
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
    
            elif choice == 3:
                
                print("\n\nYou Have Exited From The AVL Tree Insertion Interface, Thank You !!")
                
                                
                print("\n\nPress Enter To Continue")
                break
    
            else:
                print("\n\nInvalid choice. Please select a valid option.")
                
                                
                print("\n\nPress Enter To Continue")
                
            input()
    
