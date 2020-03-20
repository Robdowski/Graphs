class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

from ast import literal_eval

# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

room_graph=literal_eval(open(map_file, "r").read())

# room_graph = {
#   0: [(3, 5), {'n': 1, 's': 5, 'e': 3, 'w': 7}],
#   1: [(3, 6), {'s': 0, 'n': 2}],
#   2: [(3, 7), {'s': 1}],
#   3: [(4, 5), {'w': 0, 'e': 4}],
#   4: [(5, 5), {'w': 3}],
#   5: [(3, 4), {'n': 0, 's': 6}],
#   6: [(3, 3), {'n': 5}],
#   7: [(2, 5), {'w': 8, 'e': 0}],
#   8: [(1, 5), {'e': 7}]
# }

def dft(graph, starting_node):

    s = Stack()

    s.push([starting_node, 'start'])

    visited = set()
    traversal_path = []
    while s.size() > 0:
      
        v = s.pop()

        room = v[0]

        direction = v[1]

       

        if room not in visited:

            traversal_path.append((room, direction))
            print("Room:", room, "Direction:", direction)
            visited.add(room)
            
            for poss_dir in graph[room][1]:
                print("Room:", graph[room][1][poss_dir])
                s.push([graph[room][1][poss_dir], poss_dir])
        
    return traversal_path


def bfs(starting_vertex, destination_vertex, graph, visited = None):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        q = Queue()

        q.enqueue( [(starting_vertex, 'start')] )

        visited = set()

        while q.size() > 0:

            path = q.dequeue()

            v = path[-1]

            room = v[0]

            direction = v[1]

            if room not in visited:

                visited.add(room)

                if room == destination_vertex:

                    return path

                for neighbor in graph[room][1]:
                    path_copy = path.copy()
                    path_copy.append((graph[room][1][neighbor], neighbor))
                    q.enqueue(path_copy)
                    



def make_connections(graph, path_to_connect):
    final_path = []

    for i in range(len(path_to_connect)):
        current_room = path_to_connect[i][0]
        if i != len(path_to_connect)-1:
            next_room = path_to_connect[i+1][0]

        final_path.append(path_to_connect[i])

        if next_room not in graph[current_room][1].values(): # if they aren't connected, get path from current to next, put it in between them in the array
            path = bfs(current_room, next_room, graph)
            
            sliced_path = path[1:-1]

            print("Path:", path)
            print("Sliced:", sliced_path)

            for item in sliced_path:
                final_path.append(item)

    return final_path

def connected_to_directions(connected_path):
    output = []
    for item in connected_path:
        output.append(item[1])
    return output


def traverse_graph(graph, starting_room):

    unconnected_path = dft(graph, starting_room)[1::]

    print("Unconnected Path:", unconnected_path)

    connected_path = make_connections(graph, unconnected_path)

    print("Connected Path:", connected_path)

    output = connected_to_directions(connected_path)

    return output

final = traverse_graph(room_graph, 0)

print(final)