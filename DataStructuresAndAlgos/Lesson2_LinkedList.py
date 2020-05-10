class Lesson2_LinkedList(object):
    """description of class"""

class Element(object):
    def __init__(self, value):
        self.value= value
        self.next= None

class LinkedList(object):
    def __init__(self,head=None):
        self.head=head

    def append(self,new_element):
        current = self.head
        if self.head:
            while current.next:
                current= current.next
            current.next = new_element
        else:
            self.head=new_element

    # To get element of certain position start position as 1
    # Assumption that given position 
    def get_position(self,position):
        current = self.head
        itr = 0
        if self.head:
            while current:
                itr +=1
                if itr == position:
                    return current
                current =current.next

    """Insert a new node at the given position.
    Assume the first position is "1".
    Inserting at position 3 means between
    the 2nd and 3rd elements."""   
    def insert(self, new_element, position):
        current = self.head
        itr =0
        if self.head:
            while current.next:
                itr +=1
                if itr +1 == position:
                    temp = current.next
                    current.next = new_element
                    new_element.next = temp
                current = current.next

     #Delete the first node with a given value."""
    def delete(self, value):
        current = self.head
        if self.head:
            if current.value== value:
                self.head= current.next
            elif current.next:                
                while current.next:   #plan is to be before element and check for value of next item 
                    if current.next.value == value:
                        current.next=current.next.next
                        break
                    current = current.next



                    
                    
             
                    
        
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

# Test get_position
# Should print 3
print (ll.head.next.next.value)
# Should also print 3
print (ll.get_position(3).value )        


# Test insert
ll.insert(e4,3)
# Should print 4 now
print (ll.get_position(3).value)

# Test delete
ll.delete(1)

# Should print 2 now
print (ll.get_position(1).value)
# Should print 4 now
print (ll.get_position(2).value)
# Should print 3 now
print (ll.get_position(3).value)

e5= Element(5)
e6=Element(6)

ll.append(e5)
ll.append(e6)

ll.delete(5)
# Should print 2 now
print (ll.get_position(2).value)
# Should print 4 now
print (ll.get_position(3).value)
# Should print 3 now
print (ll.get_position(4).value)