#queue
#first-in-first-out, last-in-last-out (opposite of stack)
#insert is called push
#delete is called pop
#front, rear
#data

class queue:

    MAX = 4

    def __init__(self):
        self.data = []
        for i in range (self.MAX):
            self.data.append(0)
        self.front = 0 # location to delete
        self.rear = 0  # location to insert

    def is_empty(self):
        return self.front == self.rear

    def is_full(self):
        return self.size() == self.MAX-1

    def size(self):
        if self.is_empty():
            return 0
        elif self.front < self.rear:
            return self.rear - self.front
        else: #rear is in front i.e. wrap around
            return self.rear + self.MAX - self.front #minus off the space in between

#wrap around is like 1,2,3 then u delete 1 and 2 and add 4 but only front avail so is 4, ,3 whr rear is in front.


    def enqueue(self,value):
        if self.is_full():
            print("Cannot insert to full queue")
        else:  #includes wrap around
            self.data[self.rear] = value
            self.rear = (self.rear + 1) %self.MAX  #this is to be used to find rear no matter position

    def dequeue(self):
        if self.is_empty():
            print ("Cannot delete from empty queue")
        else: #includes wrap around
            result = self.queue[self.front]
            self.front = (self.front + 1) %self.MAX

    def peek(self):
        if self.is_empty():
            print("Empty queue")
        else:
            return self.data[self.front], self.data[self.front+self.size-1]%self.MAX # the last part self.data[self.rear-1] doesnt work for work around need to make one that works

    def display(self):
        if self.is_empty():
            print("Empty queue")
        else:
            if self.front < self.rear: #no wrap around
                for i in range(self.front,self.rear):
                    print(self.data[i])
            else: #wrap around
                for j in range(self.front, self.MAX):
                    print (self.data[j])
                for k in range(0,self.rear):
                    print (self.data[j])

#main
q = queue()
q.enqueue('a')
q.enqueue('b')
q.enqueue('c')
#print (q.display(),"deleted")  #wrap around test
#q.enqueue('a')
q.display()
print (q.display(),"deleted")
q.display()
        
        
