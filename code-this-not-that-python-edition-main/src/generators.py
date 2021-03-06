from sys import getsizeof 

# Inefficent way 💩: Using a list ❌
L = [n for n in range(42_000)]
sum(L) # 881979000
getsizeof(L) # 351064 bytes

# Efficient way 🔥: Use a generator ✅
G = (n for n in range(42_000))
sum(G) # 881979000 bytes
getsizeof(G) # 112 bytes
print(G) # <generator object <genexpr> at 0x7f8b8b8b8b90>
