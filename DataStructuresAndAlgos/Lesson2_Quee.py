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

    def getFirstInsertedElement(self):
        if self.head:
          return  self.head.value
        else:
            return "Queue empty"

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

    #Delete the first node with a given value."""
    def delete(self):
        current = self.head
        if self.head:
            if self.head.next:
            # How to delete element
                self.head= self.head.next
                return current.value
            else:
                self.head=None
                return current.value;
        else:
            return None


class Queue:
    def __init__(self, head=None):
        self.ll = LinkedList(head)

    def enqueue(self, new_element):
        self.ll.append(new_element)

    def peek(self):
        return self.ll.getFirstInsertedElement()

    def dequeue(self):
        return self.ll.delete()
    
# Setup
q = Queue(Element(1))
q.enqueue(Element(2))
q.enqueue(Element(3))

# Test peek
# Should be 1
print (q.peek())

# Test dequeue
# Should be 1
print (q.dequeue())

# Test enqueue
q.enqueue(Element(4))
# Should be 2
print (q.dequeue())
# Should be 3
print (q.dequeue())
# Should be 4
print (q.dequeue())
q.enqueue(Element(5))
# Should be 5
print (q.peek())