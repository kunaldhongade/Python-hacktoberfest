# importing module
import collections

# initialising a deque() of arbitrary length
linked_lst = collections.deque()

# filling deque() with elements
linked_lst.append('first')
linked_lst.append('second')
linked_lst.append('third')

print("elements in the linked_list:")
print(linked_lst)

# adding element at an arbitrary position
linked_lst.insert(1, 'fourth')

print("elements in the linked_list:")
print(linked_lst)

# deleting the last element
linked_lst.pop()

print("elements in the linked_list:")
print(linked_lst)

# removing a specific element
linked_lst.remove('fourth')

print("elements in the linked_list:")
print(linked_lst)
