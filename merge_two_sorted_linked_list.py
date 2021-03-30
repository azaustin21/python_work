class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next

    def add_to_list(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next

        last.next = new_node


def merge_lists(head1, head2):
    dummy_node = Node(0)

    tail = dummy_node
    while True:
        if head1 is None:
            tail.next = head2
            break
        if head2 is None:
            tail.next = head1
            break
        if head1.data <= head2.data:
            tail.next = head1
            head1 = head1.next
        else:
            tail.next = head2
            head2 = head2.next

        tail = tail.next

    return dummy_node.next

list1 = LinkedList()
list2 = LinkedList()

list1.add_to_list(5)
list1.add_to_list(10)
list1.add_to_list(15)

list2.add_to_list(2)
list2.add_to_list(8)
list2.add_to_list(12)

list1.head = merge_lists(list1.head, list2.head)

print("Merged Linked List is: ")
list1.print_list()
