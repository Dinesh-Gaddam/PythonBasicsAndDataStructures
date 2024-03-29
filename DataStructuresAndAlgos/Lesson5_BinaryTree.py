
class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def preorder_print(self,start):
        if start:
            if start.left and start.right:
                print(start.value)
                
                self.preorder_print(start.left)
                self.preorder_print(start.right)
            elif start.left:
                print(start.value)
                self.preorder_print(start.left)                
            elif start.right:
                print(start.value)
                self.preorder_print(start.right)
            else:
                print(start.value)
                return
        else:            
            return

    #Return collection 
    def preorder_print(self,start,traversal=list):
        if start:
            traversal.append(start.value)
            traversal.append("-")           
            self.preorder_print(start.left,traversal)
            self.preorder_print(start.right,traversal)

    def preorder_print(self,start,traversal):
        if start:
            traversal += (str(start.value) + "-")
            print(traversal)
            self.preorder_print(start.left,traversal)
            self.preorder_print(start.right,traversal)
            
          

    def preorder_searchMyTry(self,start,find_val):
        if start:
            if start.left and start.right:
                print("Node left and Right,Node current value=",start.value)
                if start.value == find_val:
                    return 1
                else:
                    self.preorder_search(start.left,find_val)
                    self.preorder_search(start.right,find_val)

            elif start.left:
                print("Node left only ,Node current value=",start.value)
                if start.value == find_val:
                    return 1
                else:
                    self.preorder_search(start.left,find_val)
                    
            elif start.right:
                print("Node Right only ,Node current value=",start.value)
                if start.value == find_val:
                    return 1
                else:
                    self.preorder_search(start.right,find_val)
            else:
                if start.value == find_val:
                    return 1
                else:
                    return
        else:            
            return

    def preorder_search(self,start,find_val):
        if start:
            print(start.value)
            if start.value == find_val:
                return True
            else:
                return self.preorder_search(start.left,find_val) or self.preorder_search(start.right,find_val)
            print("Last element")
        return False

    def print_tree(self):
       # treeList=[]
       # self.preorder_print(self.root,treeList)
        #print(treeList)
       stringformat=""
       self.preorder_print(self.root,stringformat)
       print(stringformat)


          

    def search(self, find_val):
        """if self.preorder_search(self.root,find_val) == 1:
            return True
        else:
            return False"""
        return  self.preorder_search(self.root,find_val)




# Set up tree
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

#tree.print_tree()


print(tree.search(4))

print(tree.search(6))

#tree.preorder_print(tree.root.left)