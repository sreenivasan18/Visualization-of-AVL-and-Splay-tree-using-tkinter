if __name__ == "__main__":
        
        splay_tree = SplayTree()
    
        while True:
            
            sentences = [
                    "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                    "\n\n\nSplay Tree Menu:"
                    "\nPress 1 to Insert a Node"
                    "\nPress 2 to Traverse The Tree"
                    "\nPress 3 to Exit From the Splay Tree Interface"
                ]
                
            for sentence in sentences:
                print_letter_by_letter_2(sentence)
                
            choice = int(input("\nEnter Your Choice: "))
    
            if choice == 1:
                
                key = int(input("\n\nEnter the key to be inserted: "))
                node = Node(key)
                splay_tree.insert(node)
                print("Node inserted successfully!")
                                
                print("\n\nPress Enter To Continue")
    
            elif choice == 2:
                
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
    
            elif choice == 3:
                
                print("\n\nYou have exited from the Splay Tree Insertion Interface. Thank you!")
                                
                print("\n\nPress Enter To Continue")
                break
    
            else:
                print("\n\nInvalid choice. Please select a valid option.")
                                
                print("\n\nPress Enter To Continue")
                                
            input()
    
