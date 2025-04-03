class Stack():
    def __init__(self):
        self.data =['','','','','','','']
        self.top =0
    def push(self,value):
        if self.top == len(self.data):
            print("Can't add value to array, arrya is full")
        else:
            self.data[self.top]=value
            self.top=self.top+1
    def pop(self):
        if self.top == 0:
            print("array is empty, popping not possible")
        else:
            self.top =self.top-1
            value=self.data[self.top]
            return value    
print("STACK")
print("==========")
print ("1-Push")
print ("2-Pop")
print ("3-Exit")
stack = Stack()
while True:
    inputChoice = int(input("Choice:"))
    if inputChoice ==1 :
        value=input("enter a value")
        stack.push(value)
    elif inputChoice == 2:
        stack.pop()
    elif inputChoice ==3:
        print("Existing...")
        break 
    else:
        print("Invalid input, try again")
