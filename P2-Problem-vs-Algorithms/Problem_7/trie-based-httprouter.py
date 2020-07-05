# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler = None):
        # Initialize the node with children as before, plus a handler
        self.children = dict()
        self.handler = handler

    def insert(self, path):
        # Insert the node as before
        if path not in self.children:
            self.children[path] = RouteTrieNode()


# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, handler = None):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode(handler)

    def insert(self, path_list, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        node_ptr = self.root

        for path in path_list:
            node_ptr.insert(path)
            node_ptr = node_ptr.children[path]

        node_ptr.handler = handler

    def find(self, path_list):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        node_ptr = self.root

        for path in path_list:
            if path not in node_ptr.children:
                return None
            node_ptr = node_ptr.children[path]

        return node_ptr.handler
        

# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, handler = None, not_found_handler = None):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.route_trie = RouteTrie(handler)
        self.not_found_handler = not_found_handler if not_found_handler else "404 Not found"


    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        path_list = self.split_path(path)
        self.route_trie.insert(path_list, handler)

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        path_list = self.split_path(path)
        handler = self.route_trie.find(path_list)

        if not handler:
            return self.not_found_handler

        return handler

    def split_path(self, path):
        # you need to split the path into parts for 
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        return [p  for p in path.split('/') if p != '']


# Here are some test cases and expected outputs you can use to test your implementation

print(f"=========== Test Case 1 ===========")
# create the router and add a route
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route
router.add_handler("/home/about/me/edit", "edit handler")  # add a route

# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about/me/edit"))  # should print 'edit handler'


print(f"=========== Test Case 2 ===========")
router = Router("root handler") 
router.add_handler("/home/about", "about handler")  # add a route
router.add_handler("/home/contact", "contact handler")  # add a route
router.add_handler("/home/pages/1/", "Page 1 Handler")
router.add_handler("/home/pages/2/", "Page 2 Handler")

print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print '404 Not found'
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/pages/1/")) # should print 'Page 1 Handler'
print(router.lookup("/home/pages/3")) # should print '404 Not found'