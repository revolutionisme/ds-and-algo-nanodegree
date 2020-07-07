from math import sqrt
import heapq


class Node:

    def __init__(self, index, coordinates = None, parents = None) -> None:
        self.coordinates = coordinates
        self.parent = parents
        self.index = index
        self.g = 0.0
        self.f = 0.0

    def calculate_f(self, current, goal):
        '''
        Calculate f for A* algo, using g of current node and calculating distance from the neighbour to goal and start 
        '''
        self.g = current.g + self.__distance(current)
        h = self.__distance(goal)
        self.f = self.g + h

    def __distance(self, other):
        '''
           Find out the Euclidean distance between 2 points - Heuristic for A* algo
        '''
        return sqrt(
            (self.coordinates[0] - other.coordinates[0])**2 + 
            (self.coordinates[1] - other.coordinates[1])**2
            )

    def __eq__(self, other):
        return self.coordinates == other.coordinates

    def __lt__(self, other):
         return self.f < other.f

def add_to_open(open_list, neighbour_node):
    for node in open_list:
        if (neighbour_node == node and neighbour_node.f >= node.f):
            return False
    return True


def shortest_path(M,start,goal):
    print("shortest path called")
    open_list = []
    closed_list = []
    
    start_node = Node(start, M.intersections[start])
    goal_node = Node(goal, M.intersections[goal])

    #Maintain a min heap to get nodes with minimum f distance
    heapq.heappush(open_list, start_node)
    
    while len(open_list) > 0:
        current_node = heapq.heappop(open_list)
        closed_list.append(current_node)

        if current_node == goal_node:
            path = []
            while current_node != start_node:
                path.append(current_node.index)
                current_node = current_node.parent
            
            path.append(current_node.index)
            # Return reversed path
            return path[::-1]

        neighbours = M.roads[current_node.index]

        for neighbour in neighbours:
            neighbour_node = Node(neighbour, M.intersections[neighbour], current_node)

            # If we have traversed a node, dont traverse again
            if neighbour_node in closed_list:      
                continue

            neighbour_node.calculate_f(current_node, goal_node)

            # If neighbour is already in open_list, check whether
            # the f distance is lower or not and then add neighbour
            if(add_to_open(open_list, neighbour_node) == True):
                heapq.heappush(open_list, neighbour_node)

    return None
