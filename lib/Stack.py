#Deliverables 
#Modify your Stack __init__() method to take an optional limit value and set that as an attribute.
#Update the Stack push() value to only push the passed-in value if there's still room in the Stack.
#Stack size(): returns the number of elements contained in the Stack
#Stack empty(): returns true if the Stack is empty; false otherwise
#Stack full(): returns true if the Stack is full; false otherwise
#Stack search(value): returns the distance between the top of the stack and the target element if it's present; -1 otherwise.

class Stack:

    def __init__(self, items=[], limit=100):
       self.items = items
       self.limit = limit

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, items):
        if len(self.items)  < self.limit:
            self.items.append(items)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
    
    def size(self):
        return len(self.items)

    def full(self):
        return len(self.items) >= self.limit

    def search(self, target):
        try:
            index = self.items.index(target)
            return len(self.items) - index - 1
        except ValueError:
            return -1

        
