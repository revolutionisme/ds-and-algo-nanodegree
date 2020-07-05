perfoming autocomplete using trie data structure, which is similar to tree. 

Time Complexity:
insert and find  - O(n) - where n is the number of characters in a word 
suffixes() - O(n*m) - where n is the total number of nodes and m is the number of children of each node 

Space Complexity:
insert - O(n) - Space required for each new node
suffixes - O(n*m) - the suffixes_result list will add each character of all the n words whcih match the suffix and return, this reduces as the length of suffix variable increases.