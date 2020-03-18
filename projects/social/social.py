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

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        import random
        def add_random_friendships(user_id, num_friends, num_users):
            friend_ids = set()
            for i in range(num_friends):
                rand_id = random.randint(1, num_users)
                if rand_id == user_id or rand_id in friend_ids:
                    continue
                friend_ids.add(rand_id)
                self.add_friendship(user_id, rand_id)

        # Add users
        import math
        for i in range(num_users):
            self.add_user(i+1)
        # Create friendships
        for i in range(num_users):
            num_friends =  round(random.random() * math.ceil(random.randint(0, avg_friendships * 2)))
            add_random_friendships(i+1, num_friends, num_users)
        
        print('Users', self.users)
        print('Friendships', self.friendships)

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        q = Queue()

        q.enqueue([user_id])

        while q.size() > 0:
            path = q.dequeue()

            v = path[-1]

            if v not in visited:
                visited[v] = path

        

                for neighbor in self.friendships[v]:
                        path_copy = path.copy()
                        path_copy.append(neighbor)
                        q.enqueue(path_copy)

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print("Connections:", connections)
