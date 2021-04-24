# You will not need to create a ListNode Class here.
class ListNode:
   def __init__(self, data, next = None):
      self.val = data
      self.next = next

def make_linkedlist(elements):
    head = ListNode(elements[0])
    for element in elements[1:]:
        ptr = head
        while ptr.next:
            ptr = ptr.next
        ptr.next = ListNode(element)
    return head

def print_list(head):
    ptr = head
    linkedlist = []
    while ptr:
        linkedlist.append(ptr.val)
        ptr = ptr.next
    print(linkedlist)

def interleave(n1, n2):
    if (not n1): 
        return n2 
    if (not n2): 
        return n1 
    result = n1
    while (n1 and n2): 
        temp1 = n1.next
        temp2 = n2.next
        if (n1.next):
            n2.next = n1.next
        n1.next = n2
        n1 = temp1
        n2 = temp2
    return result
    
n1 = make_linkedlist([1,4,8,7,8])
n2 = make_linkedlist([8,6,9])
print_list(n1)
print_list(interleave(n1, n2))


