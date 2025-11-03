class SingleNode:
    def __init__(self, data):
        self.data = data
        self.next = None



class SinglyLinkedList:
    def __init__(self):
        self.head = None 

    def append_beginning(self, data):
        new_node = SingleNode(data)
        new_node.next = self.head # assign None to new_node to make it the last node
        self.head = new_node # assign the new node to head to make it the first node 
        return new_node

    def traverse_forward(self):
        curr = self.head
        while curr:
            print(curr.data, end="------>")
            curr = curr.next

    def traverse_backward(self):
        curr = self.head
        prev = None
        while curr:

            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
                   
        self.head = prev
        return self.head

       
            
        



# sll = SinglyLinkedList()
# sll.append_beginning(20) 
# sll.append_beginning(30)
# sll.append_beginning(40)
# print(sll.traverse_forward())
# print(sll.traverse_backward().data)


class DoubleNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None


    def append_beginning(self, data):
        new_node = DoubleNode(data)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node    
       
    def append_end(self, data):
        new_node = DoubleNode(data)  
        if self.head is None:
            self.head = new_node
            return self.head

        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node #assign the current next point to new node and assign new node prev pointer to curr
        new_node.prev = curr 

    def insert_after_a_node(self, val, data):
        new_node = DoubleNode(data) 
        curr = self.head
        temp = None
        while curr:
            if curr.data == val:
                temp = curr.next 
                curr.next = new_node
                new_node.prev = curr
                new_node.next = temp
            curr = curr.next
            
    def delete_by_value(self, val):
        curr = self.head
        while curr:
            if curr.data == val:
                print(curr.prev.data)
                print(curr.data)
                print(curr.next.data)
                curr.prev.next = curr.next
            curr = curr.next 

                     
    def reverse_dll(self):
        curr = self.head
        temp = None
        while curr: 
            temp = curr.prev
            curr.prev = curr.next
            curr.next = temp
            curr = curr.prev
        if temp:
          self.head = temp.prev


    def find_mid(self):
        fast, slow = self.head, self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        if slow:
            return slow.data
        else:
            return None
        
    def is_palindrome(self):
        left = self.head
        right = self.head
        while right.next:
            right = right.next
        # and right.next != left
        while left != right and right.next != left :
            print(left.data, end="left") 
            print()
            print(right.data, end="right")
            print()

            left = left.next
            right = right.prev


    def traverse_forward(self):
        curr = self.head
        while curr:
            print(curr.data, end=" <-> ")
            curr = curr.next






dll = DoublyLinkedList()
# dll.append_beginning(23)
# dll.append_beginning(24)
# dll.append_beginning(253)
# dll.append_beginning(26)


dll.append_end(23)
dll.append_end(24)
dll.append_end(253)
dll.append_end(26)
# dll.append_end(27)
# print(dll.traverse_forward())
# dll.insert_after_a_node(253, 29)
# print(dll.traverse_forward())
# dll.delete_by_value(29)
# print(dll.traverse_forward())
# print(dll.reverse_dll())
print(dll.traverse_forward())
# dll.find_mid()
dll.is_palindrome()