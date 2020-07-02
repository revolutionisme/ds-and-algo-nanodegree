import sys
import heapq

class HuffNode:

    def __init__(self, value:str, frequency:int):
        self.value = value
        self.frequency = frequency
        self.left = None
        self.right = None
    
    def __lt__(self, other):
        return self.frequency < other.frequency
    
    def __repr__(self):            
        return f"{self.value} -> {self.frequency}"

class HuffmanCoding:
    
    def __init__(self):
        self.tree = None
        self.__huff_heap = []
        self.huffcode_enc_dict = dict()
        self.huffcode_dec_dict = dict()

    def encoding(self, data):
        
        if data == "":
            return "", None
        
        # Count the frequency of each character and store it in the dicitonary
        unique_dict = dict()
        for ch in data:
            if ch not in unique_dict:
                unique_dict[ch] = 1
            else:
                unique_dict[ch] += 1
        
        
        for key, value in unique_dict.items():
            heapq.heappush(self.__huff_heap, HuffNode(key, value))

        # print(self.__huff_heap)
        self.tree = self.__huff_tree()
        root_node = self.tree
        # print(root_node, root_node.left, root_node.right)
        self.__code_generator(root_node, "")

        # print(self.tree)
        # print(self.huffcode_enc_dict)
        encoded_data = ""
        for ch in data:
            encoded_data += self.huffcode_enc_dict[ch]
        return encoded_data, self.tree

    def __huff_tree(self):

        while len(self.__huff_heap) > 1:
            small_node_1 = heapq.heappop(self.__huff_heap)
            small_node_2 =  heapq.heappop(self.__huff_heap)
            new_node = self.__add_huff_nodes(small_node_1, small_node_2)
            heapq.heappush(self.__huff_heap, new_node)

        return heapq.heappop(self.__huff_heap)

    def __add_huff_nodes(self, node1:HuffNode, node2:HuffNode):
        # print(node1, node2)

        new_frequency = node1.frequency + node2.frequency
        new_value = f"{node1.value}{node2.value}"
        # print(f"New value and frequency = {new_value}, {new_frequency}")

        new_node = HuffNode(new_value, new_frequency)
        new_node.left = node1
        new_node.right = node2
        # print(new_node, new_node.left, new_node.right)

        return new_node
    
    def __code_generator(self, node: HuffNode, code:str):
        if node is None:
            return
        
        # print(f"Codegen - {node}, {code}, {node.left}, {node.right}")
        if not node.left and not node.right:
            if code == "":
                code = "0"
            self.huffcode_enc_dict[node.value] = code
            self.huffcode_dec_dict[code] = node.value
            return 
            

        self.__code_generator(node.left, f"{code}0")
        self.__code_generator(node.right, f"{code}1")


    def decoding(self, encoded_data):
        original_data= ""
        code = ""
        for digit in encoded_data:
            code += digit
            if code in self.huffcode_dec_dict:
                original_data += self.huffcode_dec_dict[code]
                code = ""
        
        return original_data
        

    def decoding_with_tree(self, encoded_data, tree):
        self.tree = tree
        self.__code_generator(tree, "")
        return self.decoding(encoded_data)
        

if __name__ == "__main__":
    codes = {}

    print("==========Test Case 1==========")
    a_great_sentence = "The bird is the word"

    print ("The content of the data is: {}".format(a_great_sentence))  # Expected - "The bird is the word"
    print ("The size of the data is: {}".format(sys.getsizeof(a_great_sentence))) # Expected - 69

    huff_code = HuffmanCoding()
    encoded_data, tree = huff_code.encoding(a_great_sentence)
    
    assert "1000111111100100001101110000101110110110100011111111001101010011100001" == encoded_data

    print ("The content of the encoded data is: {}".format(encoded_data)) # Expected - As asserted
    print ("The size of the encoded data is: {}".format(sys.getsizeof(int(encoded_data, base=2)))) # Expected - 36

    decoded_data = huff_code.decoding(encoded_data)

    print ("The content of the decoded data is: {}".format(decoded_data)) # Expected - "The bird is the word"
    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data))) # Expected - 69



    print("==========Test Case 2==========")
    #All unique characters
    test_data = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    print (f"The content of the data is: {test_data}")  # Expected - ABCDEFGHIJKLMNOPQRSTUVWXYZ
    print (f"The size of the data is: {sys.getsizeof(test_data)}") # Expected - 75

    huff_code = HuffmanCoding()
    encoded_data, tree = huff_code.encoding(test_data)
    
    assert "0110011010011011100111011000110100100111001001001111010110100000010101011100001011111111101111001011110001000000110111101110" == encoded_data
    print (f"The content of the encoded data is: {encoded_data}")  # Expected - As asserted
    print (f"The size of the encoded data is: {sys.getsizeof(int(encoded_data, base=2))}")  # Expected - 44

    decoded_data = huff_code.decoding(encoded_data)

    print ("The content of the decoded data is: {}".format(decoded_data))  # Expected - ABCDEFGHIJKLMNOPQRSTUVWXYZ
    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))  # Expected - 75


    print("==========Test Case 3==========")
    #Single character encoding
    test_data = "a"

    print (f"The content of the data is: {test_data}")  # Expected - a
    print (f"The size of the data is: {sys.getsizeof(test_data)}")  # Expected - 50

    huff_code = HuffmanCoding()
    encoded_data, tree = huff_code.encoding(test_data)
    assert "0" == encoded_data
    print (f"The content of the encoded data is: {encoded_data}")  # Expected - 0
    print (f"The size of the encoded data is: {sys.getsizeof(int(encoded_data, base=2))}")  # Expected - 24


    decoded_data = huff_code.decoding(encoded_data)

    print ("The content of the decoded data is: {}".format(decoded_data))  # Expected - a 
    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))  # Expected - 50


    print("==========Test Case 4==========")
    #Empty String
    test_data = ""

    print (f"The content of the data is: {test_data}")  # Expected - 
    print (f"The size of the data is: {sys.getsizeof(test_data)}")  # Expected - 49

    huff_code = HuffmanCoding()
    encoded_data, tree = huff_code.encoding(test_data)
    assert "" == encoded_data

    print (f"The content of the encoded data is: {encoded_data}")  # Expected - 
    print (f"The size of the encoded data is: {sys.getsizeof(int(encoded_data, base=2))}")  # ValueError: invalid literal for int() with base 2: ''
