# https://chatgpt.com/c/6906be6b-2cd4-8322-9ae9-ad5c08e0e0e7

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if self.head is None:
            self.head = Node(data)   
            return 
        curr = self.head
        while curr:
            curr = curr.next
        curr.next = Node(data)

    def append_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head  # link new node to current head
        self.head = new_node       # move head to new node

    def del_by_value(self, val):
        curr = self.head
        while curr:
            if curr.next.data == val:
                curr.next = curr.next.next
                break
            curr = curr.next

    def count_ll(self):
        curr = self.head
        count = 0
        while curr:
            count +=1   
            curr = curr.next
        return count 
    
    
    def reverse_linked_list(self):
        prev = None
        curr = self.head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        self.head = prev   # reassign head to new first node
        return self.head
    

    def reversell(self):
        self.head = self._reverse_recursive(self.head)

    def _reverse_recursive(self, node):
        # Base case: if node is None or last node
        if not node or not node.next:
            return node

        # Recursive step: reverse the rest of the list
        new_head = self._reverse_recursive(node.next)

        # Reverse the link
        node.next.next = node
        node.next = None

        return new_head

    def print_list(self):
        curr = self.head
        while curr:
            print(curr.data, end=" -> ")
            curr = curr.next    

ll = LinkedList()
ll.append(23)
ll.append(32)
ll.append(22)
ll.append(33)
ll.append_beginning(100)
ll.append_beginning(200)
ll.del_by_value(32)
print(ll.count_ll())
print(ll.reversell())
print(ll.print_list())