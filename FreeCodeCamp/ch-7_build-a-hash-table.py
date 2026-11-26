

# Build a Hash Table
#
# In this lab, you will build a hash table from scratch.
# A hash table is a data structure that stores key-value pairs.
#
# A hash table works by taking the key as input and hashing
# it using a specific hashing function.
#
# For this lab, the hashing function will:
# - Sum the Unicode code points of each character in the key.
# - Use the resulting hash value as the index to store the value.
#
# Objective:
# Fulfill all the user stories below and pass all tests.
#
# USER STORIES:
#
# 1. Create a class named HashTable.
#
# 2. The HashTable class should have a collection attribute
#    initialized to an empty dictionary when a new instance
#    is created.
#
# 3. The collection dictionary should store key-value pairs
#    based on the hashed value of the key.
#
# 4. The HashTable class should have four instance methods:
#    - hash
#    - add
#    - remove
#    - lookup
#
# HASH METHOD:
#
# - Take a string as a parameter.
# - Return a hash value calculated by summing the Unicode
#   code points of each character in the string.
# - Use the ord() function to get the Unicode code point.
#
# ADD METHOD:
#
# - Take two arguments: key and value.
# - Calculate the hash of the key.
# - Use the hash value as a key in the collection dictionary.
# - Store the original key-value pair inside a nested dictionary.
# - If multiple keys produce the same hash value,
#   store all their key-value pairs in the existing
#   nested dictionary under the same hash value.
#
# REMOVE METHOD:
#
# - Take a key as its argument.
# - Calculate the hash of the key.
# - Check whether the key exists in the collection.
# - Remove only the corresponding key-value pair.
# - If the key does not exist, do not raise an error.
# - If multiple keys have the same hash value,
#   remove only the requested key, not the entire dictionary.
#
# LOOKUP METHOD:
#
# - Take a key as its argument.
# - Calculate the hash of the key.
# - Find the corresponding value in the collection.
# - Return the value if the key exists.
# - Return None if the key does not exist.
#
# EXAMPLES:
#
# Example 1:
# ht.hash('golf') should return 424.
#
# Example 2:
# ht.add('golf', 'sport')
#
# Expected collection:
# {
#     424: {
#         'golf': 'sport'
#     }
# }
#
# Example 3:
# ht.add('dear', 'friend')
# ht.add('read', 'book')
#
# Expected collection:
# {
#     412: {
#         'dear': 'friend',
#         'read': 'book'
#     }
# }
#
# Example 4:
# ht.add('rose', 'flower')
#
# Expected collection:
# {
#     441: {
#         'rose': 'flower'
#     }
# }
#
# Example 5:
# ht.add('fcc', 'coding')
# ht.add('cfc', 'chemical')
#
# Expected collection:
# {
#     300: {
#         'fcc': 'coding',
#         'cfc': 'chemical'
#     }
# }
#
# Example 6:
# If the hash table contains 'fcc' and 'cfc',
# removing 'fcc' should only remove 'fcc'.
#
# Expected collection:
# {
#     300: {
#         'cfc': 'chemical'
#     }
# }
#
# Example 7:
# If ht contains ('golf', 'sport'):
# ht.lookup('golf') should return 'sport'.
#
# Example 8:
# If 'golf' does not exist:
# ht.lookup('golf') should return None.
#
# Example 9:
# If ht contains 'fcc' but not 'cfc':
# ht.lookup('cfc') should return None.




class HashTable:

    def __init__(self):
        self.collection = {}

    # Convert string into a hash number
    def hash(self, key):
        return sum(ord(char) for char in key)

    # Add key-value pair
    def add(self, key, value):
        index = self.hash(key)

        if index not in self.collection:
            self.collection[index] = {}

        self.collection[index][key] = value

    # Remove a specific key-value pair
    def remove(self, key):
        index = self.hash(key)

        if index in self.collection:
            self.collection[index].pop(key, None)

            if not self.collection[index]:
                del self.collection[index]

    # Retrieve value using key
    def lookup(self, key):
        index = self.hash(key)

        if index in self.collection:
            return self.collection[index].get(key)

        return None


ht = HashTable()
ht.add('dear', 'friend')
ht.add('read', 'book')
ht.add('golf', 'sport')
print(ht.lookup('golf'))
ht.add('fcc', '')
print(ht.lookup('cfc')) 
ht.add('fcc', 'coding')
ht.add('cfc', 'chemical')
ht.remove('golf')
ht.remove('cfc')
print(ht.collection)
