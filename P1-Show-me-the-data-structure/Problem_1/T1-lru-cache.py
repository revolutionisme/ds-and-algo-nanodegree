class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        if capacity < 0:
            raise ValueError(f"Value of capacity can't be less than 0")
        self.__capacity = capacity
        self.__cache = dict()
        self.__key_order = []
        

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        #print(f"Get key - {key}")
        value = self.__cache.get(key, -1)
        if value != -1:
            self.__key_order.remove(key)
            self.__key_order.insert(0, key)
        return value

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        #print(self.__key_order, self.__cache, self.__capacity)

        if self.__capacity == 0:
            print("Capacity set to 0, can't set the key value")
            return None

        if len(self.__key_order) >= self.__capacity:
             self.__cache.pop(self.__key_order.pop(), None)

        self.__key_order.insert(0, key)
        self.__cache.update({key:value})


print("\n==========Test Case 1==========")
our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)


print(our_cache.get(1))       # returns 1
print(our_cache.get(2))       # returns 2
print(our_cache.get(9))      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5) 
our_cache.set(6, 6)

print(our_cache.get(3))      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

print("\n==========Test Case 2==========")
new_cache = LRU_Cache(0)
new_cache.set(1, 1)          # Capacity set to 0, can't set the key value
print(new_cache.get(1))      # -1

print("\n==========Test Case 3==========")
new_cache = LRU_Cache(-1)
new_cache.set(1, 1)
print(new_cache.get(1))      # ValueError: Value of capacity can't be less than 0