# https://www.geeksforgeeks.org/doubly-linked-list/
# https://www.geeksforgeeks.org/delete-a-node-in-a-doubly-linked-list/
# for Garbage collection 
import gc 

# Node class
class node: 
    def __init__(self, nextNode=None, prev=None, data=None): 
        self.next = nextNode # reference to next node in DLL 
        self.prev = prev # reference to previous node in DLL 
        self.data = data 

# Linked List class contains a Node object
class doubly_linked_list:
    # Function to initialize head
    def __init__(self):
        self.head = node()

   # Add a node at the end of the DLL 
    def append(self, new_data): 
  
        # 1. allocate node 
        # 2. put in the data 
        new_node = node(data = new_data) 
        last = self.head 
  
        # 3. This new node is going to be the last node, so make next of it as NULL 
        new_node.next = None
  
        # 4. If the Linked List is empty, then make the new node as head 
        if self.head is None: 
            new_node.prev = None
            self.head = new_node 
            return
  
        # 5. Else traverse till the last node  
        while (last.next is not None): 
            last = last.next
  
        # 6. Change the next of last node  
        last.next = new_node 

        # 7. Make last node as previous of new node */ 
        new_node.prev = last 


    # Adding a node at the front of the list 
    def push(self, new_data): 
      
        # 1 & 2: Allocate the Node & Put in the data 
        new_node = node(data = new_data) 
      
        # 3. Make next of new node as head and previous as NULL 
        new_node.next = self.head 
        new_node.prev = None
      
        # 4. change prev of head node to new node  
        if self.head is not None: 
            self.head.prev = new_node 
      
        # 5. move the head to point to the new node 
        self.head = new_node  


    # Returns the length (integer) of the linked list.
    def length(self):
        current = self.head
        total = 0
        while current != None:
            total += 1
            current = current.next
        return total - 1

    # Prints out the linked list in traditional Python list format. 
    def display(self):
        elements = []
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
            elements.append(current_node.data)
        print(elements)

    # Returns the value of the node at 'index'.
    def getByIndex(self, index):

        if index >= self.length() or index < 0:
            print("ERROR: 'Get' Index is out of range")
            return None
        current_index = 0
        current_node = self.head
        while True:
            current_node = current_node.next
            if current_index == index:
                return current_node.data
            current_index += 1

     # Deletes the node at index 'index'.
    def eraseByIndex(self, index):
        if index >= self.length() or index < 0:
            print("ERROR: 'Erase' Index is out of range")
            return
        current_index = 0
        current_node = self.head
        while True:
            last_node = current_node
            current_node = current_node.next
            if current_index == index:
                last_node.next = current_node.next
                return
            current_index += 1
        # Call python garbage collector 
        gc.collect()

    def reverseOrder(self):
        new_list = doubly_linked_list()
        new_list.display()
        for index in range(0, self.length()):
            data = self.getByIndex(index)
            new_list.push(data)
            # if index == 0:
            #     new_list.append(self.getByIndex(index))
            #     new_list.display()
            # else:
            #     new_list.push(self.getByIndex(index))
            #     new_list.display()
        new_list.display()
