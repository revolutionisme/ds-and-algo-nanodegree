class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    result = LinkedList()
    value_set = set()

    l1_head = llist_1.head
    while l1_head:
        value_set.add(l1_head.value)
        l1_head = l1_head.next
    
    l2_head = llist_2.head
    while l2_head:
        value_set.add(l2_head.value)
        l2_head = l2_head.next

    for value in value_set:
        result.append(value)
    return result

def intersection(llist_1, llist_2):
    result = LinkedList()
    value_set = set()

    l1_head = llist_1.head
    while l1_head:
        value_set.add(l1_head.value)
        l1_head = l1_head.next
    
    l2_head = llist_2.head
    while l2_head:
        if l2_head.value in value_set:
            result.append(l2_head.value)
            value_set.remove(l2_head.value)
        l2_head = l2_head.next

    return result


print("\n==========Test Case 1==========")
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

elements_1 = [3,2,4,35,6,65,6,4,3,21]
elements_2 = [6,32,4,9,6,1,11,21,1]

for i in elements_1:
    linked_list_1.append(i)

for i in elements_2:
    linked_list_2.append(i)


print(union(linked_list_1,linked_list_2))         # Expected elements [32, 65, 2, 35, 3, 4, 6, 1, 9, 11, 21]
print(intersection(linked_list_1,linked_list_2))  # Expected elements [6, 4, 21]


print("\n==========Test Case 2==========")
linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

# lists with completely different elements
elements_3 = [1,2,3,4,5,6,7]
elements_4 = [8,9,10,11,12,13,14]

for i in elements_3:
    linked_list_3.append(i)

for i in elements_4:
    linked_list_4.append(i)

print(union(linked_list_3,linked_list_4))        # Expected elements [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
print(intersection(linked_list_3,linked_list_4)) # Expected elements []


print("\n==========Test Case 3==========")
linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

# lists with same elements
elements_5 = [1,2,3,4,5,6,7]
elements_6 = [1,2,3,4,5,6,7]

for i in elements_5:
    linked_list_5.append(i)

for i in elements_6:
    linked_list_6.append(i)

print(union(linked_list_5,linked_list_6))         # Expected elements [1, 2, 3, 4, 5, 6, 7]
print(intersection(linked_list_5,linked_list_6))  # Expected elements [1, 2, 3, 4, 5, 6, 7]


print("\n==========Test Case 4==========")
linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

# one list empty 
elements_5 = [1,2,3,4,5,6,7]
elements_6 = []

for i in elements_5:
    linked_list_5.append(i)

for i in elements_6:
    linked_list_6.append(i)

print(union(linked_list_5,linked_list_6))         # Expected elements [1, 2, 3, 4, 5, 6, 7]
print(intersection(linked_list_5,linked_list_6))  # Expected elements []



print("\n==========Test Case 5==========")
linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

# both list empty 
elements_5 = []
elements_6 = []

for i in elements_5:
    linked_list_5.append(i)

for i in elements_6:
    linked_list_6.append(i)

print(union(linked_list_5,linked_list_6))         # Expected elements []
print(intersection(linked_list_5,linked_list_6))  # Expected elements []