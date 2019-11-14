#singly linked list


class Node:
  def __init__(self,value):
    self.value=value
    self.next=None

class LinkedList:
    def __init__(self):
        self.head = None
        
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        
        # Move to the tail (the last node)
        node = self.head
        while node.next:
            node = node.next
        
        node.next = Node(value)
        return

linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(4)

node = linked_list.head
while node:
    print(node.value)
    node = node.next


#DOUBLY LINKED LIST

class Node:
  def __init__(self,value):
    self.value=value
    self.next=None
    self.previous=None

class DoublyLinkedList:
  def __init__(self):
    self.head=None
    self.tail=None
  

  def append(self,value):
    if self.head is None:
      self.head=Node(value)
      self.tail=self.head
      return
    else:
      self.tail.next=Node(value)
      self.tail.next.previous=self.tail
      self.tail=self.tail.next
    return


linked_list=DoublyLinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)

node=linked_list.head

while node:
  print(node.value)
  node=node.next

node=linked_list.tail
while node:
  print(node.value)
  node=node.previous

# Linked List Practice
# Implement a linked list class. Your class should be able to:

# Append data to the tail of the list and prepend to the head
# Search the linked list for a value and return the node
# Remove a node
# Pop, which means to return the first node's value and delete the node from the list
# Insert data at some position in the list
# Return the size (length) of the linked list


class Node:
  def __init__(self,value):
    self.value=value
    self.next=None

class LinkedList:
  def __init__(self):
    self.head=None
  
  def prepend(self,value):
    if self.head is None:
      self.head=Node(value)
    else:
      previous_head=self.head
      self.head=Node(value)
      self.head.next=previous_head
    return

  def append(self,value):
    if self.head is None:
      self.head=Node(value)
    else:
      current_node=self.head
      while current_node.next:
        current_node=current_node.next
      
      current_node.next=Node(value)


  def search( self,value):
     current_node=self.head
     while currnet_node.next:
       if(current_node.value==value):
         return current_node
       current_node=current_node.next
     return None

  def remove(self,value):
     current_prev_node=None
     current_node=self.head
     while current_node:
       if current_node==value:
         if current_prev_node is None:
           self.head=current_node.next
         else:
           current_prev_node.next=current_node.next
       current_prev_node=current_node
       current_node=current_node.next

  def pop(self,value):
     first_node=self.head.value
     self.head=self.head.next
     return first_node
     

# Reversed Linked List

class Node:
  def __init__(self,value):
    self.value=value
    self.next=None
  
class LinkedList:
  def __init__(self):
    self.head=None
  
  def append(self,value):
    if self.head is None:
      self.head=Node(value)
    else:
      node=self.head
      while node.next:
        node=node.next
      node.next=Node(value)
  def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.next

def reverse(linked_list):
  trial_position=linked_list.head
  reversed_linked_list=LinkedList()
  while trial_position is not None:
    value=trial_position.value
    reversed_linked_list=insert_at_head(reversed_linked_list,value)
    trial_position=trial_position.next
  return reversed_linked_list

def insert_at_head(linked_list,value):
  position_continuous=linked_list.head
  linked_list.head=Node(value)
  linked_list.head.next=position_continuous
  return linked_list

llist=LinkedList()
for i in [0,1,2,3,4,5]:
  llist.append(i)


flipped = reverse(llist)

flipped=list(flipped)
for i in flipped:
  print(i)
