class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_first(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Example usage:
if __name__ == "__main__":
    linked_list = SinglyLinkedList()
    
    # Inserting elements at the beginning
    linked_list.insert_at_first(10)
    linked_list.insert_at_first(20)
    linked_list.insert_at_first(30)
    
    # Printing the linked list
    linked_list.print_list()
