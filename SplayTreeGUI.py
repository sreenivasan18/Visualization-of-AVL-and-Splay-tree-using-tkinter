class SplayTreeGUI:
        def __init__(self, root):
            self.root = root
            self.root.title("Splay Tree")
            self.root.geometry("800x600")
            self.root.configure(bg="black")
    
            self.tree = SplayTree()
    
            self.label = tk.Label(root, text="Enter a number:", bg="black", fg="white")
            self.label.pack()
    
            self.entry = tk.Entry(root)
            self.entry.pack()
    
            self.insert_button = tk.Button(root, text="Insert", command=self.insert, bg="black", fg="white")
            self.insert_button.pack()
    
            self.delete_button = tk.Button(root, text="Delete", command=self.delete, bg="black", fg="white")
            self.delete_button.pack()
    
            self.splay_button = tk.Button(root, text="Splay Node", command=self.splay_node, bg="black", fg="white")
            self.splay_button.pack()
    
            self.canvas = tk.Canvas(root, width=800, height=400, bg="black")
            self.canvas.pack()
    
            self.draw_tree()
    
        def animate_insert(self, node, x, y, dx):
            self.canvas.delete("all")
            self.draw_tree_recursive(self.tree.root, 400, 50, 200)
            if not node:
                return
            self.canvas.create_oval(x - 20, y - 20, x + 20, y + 20, fill="white")
            self.canvas.create_text(x, y, text=str(node.data))
            if node.left:
                x_left = x - dx
                y_left = y + 50
                self.canvas.create_line(x, y, x_left, y_left, arrow=tk.LAST)
                time.sleep(0.5)
                self.root.update()
                self.animate_insert(node.left, x_left, y_left, dx / 2)
            if node.right:
                x_right = x + dx
                y_right = y + 50
                self.canvas.create_line(x, y, x_right, y_right, arrow=tk.LAST)
                time.sleep(0.5)
                self.root.update()
                self.animate_insert(node.right, x_right, y_right, dx / 2)
    
        def animate_delete(self, node, x, y, dx):
            self.canvas.delete("all")
            self.draw_tree_recursive(self.tree.root, 400, 50, 200)
            if not node:
                return
            self.canvas.create_oval(x - 20, y - 20, x + 20, y + 20, fill="white")
            self.canvas.create_text(x, y, text=str(node.data))
            if node.left:
                x_left = x - dx
                y_left = y + 50
                self.canvas.create_line(x, y, x_left, y_left, arrow=tk.LAST)
                time.sleep(0.5)
                self.root.update()
                self.animate_delete(node.left, x_left, y_left, dx / 2)
            if node.right:
                x_right = x + dx
                y_right = y + 50
                self.canvas.create_line(x, y, x_right, y_right, arrow=tk.LAST)
                time.sleep(0.5)
                self.root.update()
                self.animate_delete(node.right, x_right, y_right, dx / 2)
    
        def insert(self):
            try:
                key = int(self.entry.get())
                node = Node(key)
                self.tree.insert(node)
                self.draw_tree()
                self.animate_insert(self.tree.root, 400, 50, 200)
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid integer.")
    
        def delete(self):
            try:
                key = int(self.entry.get())
                node = self.tree.search(self.tree.root, key)
                if node:
                    self.tree.delete(key)
                    self.draw_tree()
                    self.animate_delete(self.tree.root, 400, 50, 200)
                else:
                    messagebox.showerror("Error", "Node not found in the tree.")
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid integer.")
    
        def splay_node(self):
            try:
                key = int(self.entry.get())
                node = self.tree.search(self.tree.root, key)
                if node:
                    self.tree.splay(node)
                    self.draw_tree()
                else:
                    messagebox.showerror("Error", "Node not found in the tree.")
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid integer.")
    
        def draw_tree(self):
            self.canvas.delete("all")
            self.draw_tree_recursive(self.tree.root, 400, 50, 200)
    
        def draw_tree_recursive(self, node, x, y, dx):
            if not node:
                return
            line_color = "white"
            self.canvas.create_oval(x - 20, y - 20, x + 20, y + 20, fill="white")
            self.canvas.create_text(x, y, text=str(node.data))
            if node.left:
                x_left = x - dx
                y_left = y + 50
                self.canvas.create_line(x, y, x_left, y_left, arrow=tk.LAST, fill=line_color)
                self.draw_tree_recursive(node.left, x_left, y_left, dx / 2)
            if node.right:
                x_right = x + dx
                y_right = y + 50
                self.canvas.create_line(x, y, x_right, y_right, arrow=tk.LAST, fill=line_color)
                self.draw_tree_recursive(node.right, x_right, y_right, dx / 2)
    
    root = tk.Tk()
    SplayTreeGUI(root)
    root.mainloop()
