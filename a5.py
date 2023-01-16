"""
File: a5.py
Assignment 5

Define a length function.
Define a printStructure function.
Define an insert function.
Test the above functions and the Node class.
"""

from node import Node

def length(head):
    """Returns the number of items in the linked structure
    referred to by head."""
    probe = head
    count = 0

    # ADD CODE HERE: Count the number of nodes in the structure
    node = head
    while True:

        count = count + 1
        if node.next is None:
            break
        node = node.next


    return count
    
def insert(newItem, head):
    """Inserts newItem at the correct position (ascending order) in
    the linked structure referred to by head.
    Returns a reference to the new structure."""

    if head == None or newItem < head.data:
        new_node = Node(newItem)
        new_node.next = head

        return new_node
        # if structure is empty


    else:
        new_node = Node(newItem)
        previous_node, current_node = head, head.next
        while current_node is not None and current_node.data < newItem:
            previous_node = current_node
            current_node = current_node.next

        previous_node.next = new_node
        new_node.next = current_node









        
    return head

def printStructure(head):
    """Prints the items in the structure referred to by head."""
    # ADD CODE HERE
    # ADD CODE HERE


    node = head
    while True:
        print(node.data, end=" ")
        if node.next is None:
            break
        node = node.next




def main():
    """Gets words from the user and inserts in the
    structure referred to by head."""
    
    head = None
    while True:
        userInput = input('Please enter a word (or just hit enter to end): ')
        if userInput == '':
            break
        head = insert(userInput, head)

    print('The structure contains', length(head), 'items:')
    printStructure(head)

if __name__ == "__main__": main()
