
class LinkedList:
    """
    A Linked List is a collection of nodes where each node
    stores a value and a reference to the next node.
    """

    class Node:
        """
        Represents a single node in the Linked List.
        Each node contains data (element) and a link (next).
        """

        def __init__(self, element):
            self.element = element  # Store the value inside the node
            self.next = None        # Point to the next node (None initially)

    def __init__(self):
        """Initialize an empty Linked List."""

        self.length = 0  # Keep track of the total number of nodes
        self.head = None  # Head points to the first node

    def is_empty(self):
        """Check whether the Linked List is empty."""

        return self.length == 0

    def add(self, element):
        """
        Add a new element at the end of the Linked List.
        """

        # Create a new node with the given element
        node = self.Node(element)

        # If the list is empty, make the new node the head
        if self.is_empty():
            self.head = node

        else:
            # Start from the first node
            current_node = self.head

            # Move through the list until we reach the last node
            while current_node.next is not None:
                current_node = current_node.next

            # Connect the last node to the new node
            current_node.next = node

        # Increase the total number of nodes
        self.length += 1

    def remove(self, element):
        """
        Remove the first node that matches the given element.
        If the element is not found, do nothing.
        """

        # Keep track of the previous and current nodes
        previous_node = None
        current_node = self.head

        # Search for the node containing the element
        while current_node is not None and current_node.element != element:
            previous_node = current_node
            current_node = current_node.next

        # If we reach the end, the element was not found
        if current_node is None:
            return

        # If the node is not the first node,
        # connect the previous node to the next node
        elif previous_node is not None:
            previous_node.next = current_node.next

        # If the first node needs to be removed,
        # move the head to the next node
        else:
            self.head = current_node.next

        # Decrease the total number of nodes
        self.length -= 1


# Create an empty Linked List
my_list = LinkedList()

# Check whether the list is empty
print(my_list.is_empty())  # True

# Add elements to the Linked List
my_list.add(1)
my_list.add(2)

# Check whether the list is empty
print(my_list.is_empty())  # False

# Check the total number of nodes
print(my_list.length)  # 2

# Remove the element 1
my_list.remove(1)

# Check the updated number of nodes
print(my_list.length)  # 1
