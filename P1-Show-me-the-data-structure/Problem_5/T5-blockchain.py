import hashlib
from datetime import datetime

class Block:

    def __init__(self, timestamp, data, previous_hash):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash()
      self.previous = None

    def calc_hash(self):
      sha = hashlib.sha256()

      hash_str = str(self.data).encode('utf-8')
      sha.update(hash_str)

      return sha.hexdigest()

    def __repr__(self):
        return repr(f"(Timestamp - {self.timestamp}, Data - {self.data}, Hash - {self.hash})")

class Blockchain():

    def __init__(self, data):
        self.__current = Block(datetime.now().timestamp(), data, 0)

    def add(self, data):
        new_block = Block(datetime.now().timestamp(), data, self.__current.hash)
        new_block.previous = self.__current
        self.__current = new_block

    def __repr__(self):
        nodes = []
        curr = self.__current
        while curr is not None:
            nodes.append(repr(curr))
            curr = curr.previous
        return '[' + '<== '.join(nodes) + ']'
    

print("============ Test Case 1 ============")
blockchain = Blockchain(123)
print(f"Current status of blockchain - {blockchain}\n") # Data = 123
blockchain.add(456)
print(f"Current status of blockchain - {blockchain}\n") # Data = 456 <== Data = 123
blockchain.add(78910)
print(f"Current status of blockchain - {blockchain}\n") # Data = 78910 <== Data = 456 <== Data = 123


print("============ Test Case 2 ============")
blockchain = Blockchain(1)
print(f"Current status of blockchain - {blockchain}\n") # Data = 1
blockchain.add(2)
print(f"Current status of blockchain - {blockchain}\n") # Data = 2 <== 1
blockchain.add(3)
print(f"Current status of blockchain - {blockchain}\n") # Data = 3 <== 2 <== 1
blockchain.add(4)
print(f"Current status of blockchain - {blockchain}\n") # Data = 4 <== 3 <== 2 <== 1
blockchain.add(5)
print(f"Current status of blockchain - {blockchain}\n") # Data = 5 <== 4 <== 3 <== 2 <== 1
blockchain.add(6)
print(f"Current status of blockchain - {blockchain}\n") # Data = 6 <== 5 <== 4 <== 3 <== 2 <== 1
blockchain.add(7)
print(f"Current status of blockchain - {blockchain}\n") # Data = 7 <== 6 <== 5 <== 4 <== 3 <== 2 <== 1
blockchain.add(8)
print(f"Current status of blockchain - {blockchain}\n") # Data = 8 <== 7 <== 6 <== 5 <== 4 <== 3 <== 2 <== 1
blockchain.add(9)
print(f"Current status of blockchain - {blockchain}\n") # Data = 9 <== 8 <== 7 <== 6 <== 5 <== 4 <== 3 <== 2 <== 1
blockchain.add(10)
print(f"Current status of blockchain - {blockchain}\n") # Data = 10 <== 9 <== 8 <== 7 <== 6 <== 5 <== 4 <== 3 <== 2 <== 1


print("============ Test Case 3 ============")
blockchain = Blockchain()       # TypeError: __init__() missing 1 required positional argument: 'data' 
