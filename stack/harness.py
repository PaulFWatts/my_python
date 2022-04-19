import Stack


s = Stack.MyStack()       # Create a stack using inheritance
print(dir(s))
s.push('Dave')           # Push some things onto it
s.push(42)
s.swap()
s.push([3, 4, 5])
print("Length is: ", len(s))            # Prints 3
x = s.pop()              # x gets [3,4,5]
y = s.pop()              # y gets 42
z = s.pop()              # z gets 'Dave'
print(x, y, z)           # Prints [3,4,5] 42 'Dave'
print("Length is: ",len(s))            # Prints 0
print(s)                 # Prints <Stack at 0x10c8b0, size=0>
