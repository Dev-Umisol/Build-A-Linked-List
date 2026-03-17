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
        node = self.Node(element)
        
        if self.is_empty():
            self.head = node # <-- Creates a new node to be added to the linked list
        else:
            current_node = self.head # <- if list isnt empty find the last node and link the new node to its next pointer
            
            while current_node.next is not None: # type: ignore
                current_node = current_node.next # type: ignore
            
            current_node.next = node # type: ignore
        
        self.length += 1
    
    def remove(self, element):
        previous_node = None
        current_node = self.head # <-- Starts the traversal of linked list from the first node
        
        while current_node is not None and current_node.element != element:
            previous_node = current_node
            current_node = current_node.next # <-- moves the current_node pointer to the next node in the list during each iteration of the loop
            
        if current_node is None:
            return
        elif previous_node is not None:
            previous_node.next = current_node.next
        else:
            self.head = current_node.next # <-- handles the case where the element to be removed is found in the head node

        self.length -= 1 # <-- decreases the length of the linked list to reflex the removal of the node
# Example Usage
my_list = LinkedList()
print(my_list.is_empty()) # True

my_list.add(1)
my_list.add(2)

print(my_list.is_empty()) # False
print(my_list.length) # 2

my_list.remove(1)
print(my_list.length) # 1