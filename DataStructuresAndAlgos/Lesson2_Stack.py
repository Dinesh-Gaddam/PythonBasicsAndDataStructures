
class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def insert_first(self, new_element):
        "Insert new element as the head of the LinkedList"
        current = self.head         
        new_element.next = current
        self.head= new_element       

    def delete_first(self):
        "Delete the first (head) element in the LinkedList as return it"
        current = self.head
        if current and current.next:            
            self.head = current.next
            return current
        elif current: 
            self.head= None
            return current
        else:
            return current

    def delete_first_Optimized(self):
        elementToRemove = None
        if(self.head != None ):
            elementToRemove = self.head
            self.head = self.head.next
        return elementToRemove
               

class Stack(object):
    def __init__(self,top=None):
        self.ll = LinkedList(top)

    def push(self, new_element):
        "Push (add) a new element onto the top of the stack"
        self.ll.insert_first(new_element)
        
    def pop(self):
        "Pop (remove) the first element off the top of the stack and return it"
        return self.ll.delete_first()
        #return self.ll.delete_first_Optimized() This will not delete the first element 
        
    
# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a Stack
stack = Stack(e1)

# Test stack functionality
stack.push(e2)
stack.push(e3)
print (stack.pop().value)
print (stack.pop().value)
print (stack.pop().value)
print (stack.pop()) # This is where we need to check null
stack.push(e4)
print (stack.pop().value)