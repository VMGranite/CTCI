# Video About Python Data Structures: https://www.youtube.com/watch?v=JlMyYuY1aXU
# Original Github for Code: https://github.com/bfaure/Python3_Data_Structures/blob/master/Linked_List/main.py
# Additional Linked List Info: https://dbader.org/blog/python-linked-list

# Node class
class node:
    # Function to initialise the node object
    def __init__(self, data=None):
        self.data = data
        self.next = None

# Linked List class contains a Node object
class linked_list:
    # Function to initialize head
    def __init__(self):
        self.head = node()

     # Adds new node containing 'data' to the end of the linked list.
    def append(self, data):
        new_node = node(data)
        current = self.head
        while current.next != None:
            current = current.next
        current.next = new_node

    # Returns the length (integer) of the linked list.
    def length(self):
        current = self.head
        total = 0
        while current != None:
            total += 1
            current = current.next
        return total

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

    # Allows for bracket operator syntax (i.e. a[0] to return first item).
    def __getitem__(self, index):
        return self.getByIndex(index)

    # added for probelm 2.1 Remove Duplicates - Displays Matches
    def findEqualTo(self, item): 
        print("Item: " + str(item))
        current_index = 0
        current_node = self.head

        while current_node.next is not None and item is not None:
            current_node = current_node.next
            if current_node.data == item:
                print("MATCH - Node: " + str(current_node.next.data) + " at index " + str(current_index))
            current_index += 1

    # added for probelm 2.1 Remove Duplicates
    # remove all instances of specified item
    def removeAllInstancesOfItem(self, item): 
        current_index = 0
        current_node = self.head

        while current_node.next is not None and item is not None:
            current_node = current_node.next
            if current_node.data == item:
                self.eraseByIndex(current_index)
                current_index -= 1
            current_index += 1

    # added for probelm 2.1 Remove Duplicates
    # Keeps one instance of item, but removes all other instances
    def removeThisDuplicate(self, item): 
        instanceKept = False
        current_index = 0
        current_node = self.head

        while current_node.next is not None and item is not None:
            current_node = current_node.next
            if current_node.data == item and instanceKept:
                self.eraseByIndex(current_index)
                current_index -= 1
            else:
                instanceKept = True
            current_index += 1

    # added for probelm 2.1 Remove Duplicates
    # For List of Duplicates - 
    # Keeps one instance of item, but removes all other instances
    def removeAnyDuplicates(self, items): 
        current_index = 0
        current_node = self.head

        while current_node.next is not None and items is not None:
            current_node = current_node.next
            if any(current_node.data == cnData for cnData in items):
                self.eraseByIndex(current_index)
                current_index -= 1
            current_index += 1
        # add items back into list to keep instances (this could be improved)
        for item in items:
            self.append(item)

    # Finds which numbers repeat and returns list of duplicates
    def findDuplicates(self):
        current_index = 0
        current_node = self.head
        duplicatesDict = {}
        duplicatesList = []

        while current_node.next is not None:
            current_node = current_node.next
            if current_node.data not in duplicatesDict:
                duplicatesDict[current_node.data] = 1
            else:
                duplicatesDict[current_node.data] = duplicatesDict[current_node.data] + 1
            current_index += 1

        for key, value in duplicatesDict.items():
            if value > 1:
                duplicatesList.append(key)

        return duplicatesList

                




