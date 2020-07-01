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
    

print("============ Test Case ============")
blockchain = Blockchain(123)
print(f"Current status of blockchain - {blockchain}\n") # Data = 123
blockchain.add(456)
print(f"Current status of blockchain - {blockchain}\n") # Data = 456 <== Data = 123
blockchain.add(78910)
print(f"Current status of blockchain - {blockchain}\n") # Data = 78910 <== Data = 456 <== Data = 123
