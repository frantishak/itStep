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

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def insert_head(self, data):
        self.head = Node(data,next_node=self.head)

    def insert_tail(self,data):
        new_node = Node(data)
        current_node = self.head
        while current_node.next_node:
            current_node = current_node.next_node
        current_node.next_node= new_node

    def print_all(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next_node

    def find_node(self,key):
        current_node = self.head
        while current_node.data != key:
            current_node = current_node.next_node
        return current_node

    def del_node(self, key):
        current_node = self.head
        prev_node = None
        while current_node.data != key:
            prev_node = current_node
            current_node = current_node.next_node
            if current_node.next_node.data == key:
                pass
            pass
        print("Значение prev_node: ", prev_node.data)
        print("До куда дошел цикл: ", current_node.next_node.data)
        prev_node.next_node = current_node.next_node
       # new_next_node = current_node.next_node
        #prev_node = current_node.new_next.node








print("Start test.")
head = Node("")
linked_list = LinkedList(head)
linked_list.insert_tail("qwe1")
linked_list.insert_tail("qwe")
linked_list.insert_head("this is head_first")
linked_list.insert_head("this is head")
linked_list.insert_tail("this is tail second")
linked_list.print_all()
linked_list.del_node("qwe1")
linked_list.print_all()
print("Stop the test.")