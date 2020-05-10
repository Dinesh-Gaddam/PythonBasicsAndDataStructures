
class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        self.inserthelper(self.root,new_val)
       
    def inserthelper(self,start,new_val):
        if start:
            if start.value > new_val:                
                if start.left:
                    print('calling left of node value={0}',start.value)
                    self.inserthelper(start.left,new_val)
                else:
                     print('inserting left of node value={0}',start.value)
                     start.left = Node(new_val)
            elif start.value < new_val:
                
                if start.right:
                    print('calling right of node value={0}',start.value)
                    self.inserthelper(start.right,new_val)
                else:
                    print('inserting right of node value={0}',start.value)
                    start.right = Node(new_val)
        else:
            raise Exception('Unable to insert the element:{}'.format(new_val))

    def searchHelper(self,start,find_val):
        if start:
            print(start.value)
            if start.value == find_val:
                return True
            elif start.value < find_val:
                 return self.searchHelper(start.right,find_val)
            else:
                return self.searchHelper(start.left,find_val)
                
        return False
          

    def search(self, find_val):
        return  self.searchHelper(self.root,find_val)




# Set up tree
tree = BinarySearchTree(4)
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)


print(tree.search(3))

print(tree.search(6))

#tree.preorder_print(tree.root.left)