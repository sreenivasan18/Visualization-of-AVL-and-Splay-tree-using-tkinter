if __name__ == "__main__":
        
        splay_tree = SplayTree()
    
        while True:
            
            sentences = [
                    "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                    "\n\n\nSplay Tree Menu:"
                    "\nPress 1 to Insert Nodes"
                    "\nPress 2 to Delete a Node"
                    "\nPress 3 to Traverse The Splay Tree"
                    "\nPress 4 to Exit From The Splay Tree Interface"
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
                    print("T\n\nree is empty. Please insert nodes first.")
                                    
                    print("\n\nPress Enter To Continue")
    
            elif choice == 4:
                
                print("\n\nYou have exited from the Splay Tree Deletion Interface. Thank you!")
                                
                print("\n\nPress Enter To Continue")
                break
    
            else:
                print("\n\nInvalid choice. Please select a valid option.")
                
                print("\n\nPress Enter To Continue")
                                
            input()
