class LinkedList:
    class Node:
        def __init__(self, element):
            self.element = element
            self.next = None
    
    def __init__(self):
        self.length = 0
        self.head = None # <-- Acting as reference to First head
    
    def is_empty(self):
        return self.length == 0 # <-- True if list has no nodes, else if greater than 0 return False

    def add(self, element):
        node = self.Node(element) # <-- Creates a new node to be added to the linked list

# Example Usage
my_list = LinkedList()
print(my_list.is_empty()) 