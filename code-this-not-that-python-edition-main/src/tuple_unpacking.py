# Tuple unpacking
some_tuple = (1, 2, 3)

# OK version 🤔 - Unpack elements by index ❌
x = some_tuple[0]
y = some_tuple[1]
z = some_tuple[2]
print(x, y, z)


# Pythonic way 🐍 - Unpack elements directly ✅
x, y, z = some_tuple
print(x, y, z)