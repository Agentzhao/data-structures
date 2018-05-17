# data structures

# array (Python list)
# - fast/direct access A[i]
# - requires contiguous storage
# - expensive to insert/delete
# - static memory allocation

# linked list
# - dynamic memory allocation
# - (more) efficient to insert/delete
# - high(er) cost to search (linear)
# - more flexible/efficient storage

class Node:

    def __init__(self, data=None, link=None):
        self.data = data
        self.link = link

#	def get_data(self):
#		return self.data
#	def get_next(self):
#		return self.link
#	def set_next(self, new_next):
#		self.link = new_next
	
class LinkedList:

    def __init__(self):
        self.head = None

    def size(self):
        total = 0
        curr = self.head
        while curr is not None:
            curr = curr.link
            total += 1
        return total

    def insert(self, data, position=0):
        n = Node(data) # new node n with data value = data and link value = None
        if self.head is None: # if empty linked list
            self.head = n
        else: # non-empty linked list
            # insert to front
            if position == 0:
                n.link = self.head
                self.head = n
            # insert to rear
            elif position == self.size():
                curr = self.head
                while curr.link is not None:
                    curr = curr.link
                curr.link = n
            # insert in between
            else:
                prev = self.head
                curr = self.head
                for i in range(position):
                    prev = curr
                    curr = curr.link
                n.link = curr
                prev.link = n

    def search(self, target):
        curr = self.head
        while (curr is not None) and (curr.data != target):
            curr = curr.link
        if curr is not None:
            print("Found!")
        else:
            print("Not found.")

    def delete(self, target=None, position=None):
        if self.head is None: # empty linked list
            print("Cannot delete from empty linked list.")
        else: # non-empty linked list
            if target is not None: # assume distinct values
                prev = self.head
                curr = self.head
                while (curr is not None) and (curr.data != target):
                    prev = curr
                    curr = curr.link
                if curr is not None: # found
                    prev.link = curr.link # delete by bypassing curr
                else:
                    print("Not found.")
            else: # assume position is valid
                prev = self.head
                curr = self.head
                for i in range(position):
                    prev = curr
                    curr = curr.link
                prev.link = curr.link # delete by bypassing curr

    def update(self, old_value, new_value):
        if self.head is None: # empty linked list
            print("Empty linked list")
        else: # non-empty linked list
        curr = self.head
        while (curr is not None) and (curr.data != old_value):
            curr = curr.link
        if curr is not None: # found
            curr.data = new_value
        else:
            print("Not found.")
            
    def display(self):
        if self.head is None: # empty linked list
            print("Empty linked list")
        else: # non-empty linked list
            curr = self.head
            while curr is not None:
                print(curr.data)
                curr = curr.link

# main
ll = LinkedList()
ll.insert(1) # insert to empty linked list
ll.insert(2,0) # insert to front
ll.insert(3,ll.size()) # insert to rear
ll.insert(4,1) # insert in between
ll.display() # show contents after insertion
ll.search(3)
ll.search(5)
ll.delete(3)
ll.display()
ll.delete(5)
ll.update(2,7)
ll.display()
ll.update(5,7)


#agentzhao analysis
class Node:
    def __init__(self, data = None, link = None):
        self.data = data
        self.link = link

class linkedlist:
    def __init__(self):
        self.head = None

    def get_size(self):
        total = 0
        set curr = start of list(self.head)
        while curr is not None:
            go to next node
            add one to total
        return total

    def insert(self, data, position = 0):
        n = Node(data) (make new node with self.data =  data,self.link = None)
        if empty list:
            n = self.head
        else:
            if inserting to head:
                n.link = self.head (link n to current head)
                set current head to n
            elif inserting to rear:
                link end of list to n
            else:
                start from head and go through the whole list
                for i in range(position):
                    set previous to current
                    set current to next
                insert inbetween the 2 nodes
                n.link = curr
                prev.link = n
                
    def search(self, target):
        get current to head opf list
        while current is not None and current.data != target:
            go to next node
        if curr is not None:
            print found
        else:
            print not found
        
    def delete():
        if list empty, print not found
        else:
            if target is defined:
                search for target
                    if found:
                        delete by bypassing the node
                    else:
                        print not found
            else: (position not defined)
                delete the first node by reassigning head of list
                
    def update(self, old_value, new_valule):
        if empty, print empty linkedlist
        else:
            set current to head of list
            while (curr is not None) and (curr.data != old_value):
                go to the next node
            if current is not None, update current data to new_value
            else:
                print not found

    def display(self):
        if empty list:
            print empty
        else:
            set current to self head
            while current data is not None:
                print(currentdata)
                set current to next node
    







    
1
Contact GitHub API Training Shop Blog About
© 2017 GitHub, Inc. Terms Privacy Security Status Help
