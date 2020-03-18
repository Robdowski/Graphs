from collections import defaultdict

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

def earliest_ancestor(ancestors, starting_node):

    graph = defaultdict(list)
    # key: child, value: parent

    for ancestor in ancestors:
        graph[ancestor[1]].append(ancestor[0])

    if graph[starting_node] == []:
        return -1
    
    ancestor = find_longest_ancestor(graph, starting_node)

    print(graph)

    return ancestor

def find_longest_ancestor(graph, start):

    q = Queue()

    longest = float("-inf")

    ancestor = float("inf")

    q.enqueue( [start] )

    visited = set()

    while q.size() > 0:

        path = q.dequeue()

        if len(path) > longest:
            longest = len(path)
            ancestor = path[-1]
        
        elif len(path) == longest:
            if path[-1] < ancestor:
                ancestor = path[-1]

        v = path[-1]

        if v not in visited:
            visited.add(v)

        for neighbor in graph[v]:
            path_copy = path.copy()
            path_copy.append(neighbor)

            q.enqueue(path_copy)

    return ancestor
