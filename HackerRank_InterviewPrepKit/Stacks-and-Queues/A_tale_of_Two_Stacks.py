class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class MyQueue(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.num_elements = 0
    
    def peek(self):
        if self.num_elements == 0:
            return None
        return self.head.value
        
    def pop(self):
        if self.num_elements == 0:
            return None
        value = self.head.value          
        self.head = self.head.next       
        self.num_elements -= 1
        return value
        
    def put(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node    
            self.tail = self.tail.next   
        self.num_elements += 1

queue = MyQueue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])        
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())