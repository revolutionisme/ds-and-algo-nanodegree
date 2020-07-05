Similar to the autocomplete with tries task, although the Router class here provides an interface to handlers and lookups.

Time Complexity:
insert/add_handler - O(n) - where n is the number of path in a given path after performing the split operation
lookup/find - O(n) - where n is the number of path in a given path after performing the split operation

Space Complexity:
O(n) - For both insert/add_handler and lookup/find, path is split to create a path list with n elements. 