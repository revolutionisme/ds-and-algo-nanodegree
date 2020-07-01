Huffman coding implements a counter using dictionary and then uses heapq to maintain a sorted list so that the minimum frequency elements can be evicted and the huffman coding can be created. Also, a couple of dictionary for encoding and decoding is created for the ease of use. 

Time Complexity:

encoding() - O(n) - where n is the number of characters in the original data
decoding() - O(m) - where m is the encoded message

Space COmplexity:

encoding() - O(n) - data is stored as frequency of characters and then a heap and finally the encoder and decoder dict but they all store max n entries if no duplicates.

decoding() - O(n) - using the decoder dictionary 
