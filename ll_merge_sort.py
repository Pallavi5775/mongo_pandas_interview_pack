# 1️⃣ Dividing the list into halves
# 2️⃣ Sorting each half recursively
# 3️⃣ Merging the two sorted halves into one sorted list

# find the middle
# break the ll across the middle
# sort each half 
# merge each half to one


class DoubleNode():
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def traverse(self):
        curr = self.head
        while curr:
            print(curr.data, end="----->")
            curr = curr.next
    def append(self, data):
        new_node = DoubleNode(data)
        if self.head is None:
            self.head = new_node
            return self.head
        
        curr= self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node
        new_node.prev = curr

    def find_middle(self, head):
        if not head:
            return head
        fast, slow = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow if slow else None
    

    def sort(self):
        self.head = self.sort_ll(self.head)

    def sort_ll(self, head):

        # if head empty or only one node return the head
        if not head or not head.next:
            return head
        # divide the ll into two halves
        mid_element = self.find_middle(head)
        next_to_mid = mid_element.next
        mid_element.next = None

        left = self.sort_ll(head)
        right = self.sort_ll(next_to_mid)

        merge_sorted_list = self.merge_sorted_list(left, right)
        return merge_sorted_list
    
    def merge_sorted_list(self, left, right):
        if not left:
            return right
        if not right:
            return left
        
        if left.data <= right.data:
            result = left
            result.next = self.merge_sorted_list(left.next, right)

        else:
            result = right
            result.next = self.merge_sorted_list(left, right.next)    

        return result
        
dll = DoublyLinkedList()
dll.append(20)
dll.append(21)
dll.append(23)
dll.append(24)
dll.append(25)
dll.sort()
dll.traverse()                