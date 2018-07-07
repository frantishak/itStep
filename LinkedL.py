class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data
    def set_data(self,data=None):
        self.data = data

    def get_next_node(self):
        return self.next_node
    def set_next_node(self,next_node=None):
        self.next_node = next_node

class LinkedList(Node):
    def __init__(self, head=None):
        self.head = head

    def insert_head(self, data):
        new_node = Node(data)
        self.head = new_node
        self.next_node = self.head

    def print_all(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next_node

linked_list = LinkedList("12dw")
linked_list.print_all()