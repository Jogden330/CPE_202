from stack_array import *  # Needed for Depth First Search
from queue_array import *  # Needed for Breadth First Search


class Vertex:
    '''Add additional helper methods if necessary.'''

    def __init__(self, key):
        '''Add other attributes as necessary'''
        self.id = key
        self.adjacent_to = []
        self.not_visited = True
        self.is_red = False
        self.is_perple = False

    def get_adjacent_list(self):
        adjacent_list = self.adjacent_to
        # adjacent_list.sort()
        return adjacent_list

    # def __eq__(self, other):
    #     return type(other) == Vertex and self.id == other.id and self.adjacent_to == other.adjacent_to


class Graph:
    # '''Add additional helper methods if necessary.'''
    #
    # '''reads in the specification of a graph and creates a graph using an adjacency list representation.
    #     You may assume the graph is not empty and is a correct specification.  E.g. each edge is
    #     represented by a pair of vertices.  Note that the graph is not directed so each edge specified
    #     in the input file should appear on the adjacency list of each vertex of the two vertices associated
    #     with the edge.'''
    def __init__(self, filename):
        self.graph = {}
        with open(filename, "r") as file:  # opens the file as readable
            for line in file:
                words = line.split()
                self.add_vertex(words[0])
                self.add_vertex(words[1])
                self.add_edge(words[0], words[1])
                # self.stop_table.insert(line.lower())

        # This method should call add_vertex and add_edge

        # '''Add vertex to graph, only if the vertex is not already in the graph.'''

    def add_vertex(self, key):
        if not self.graph.get(key):
            self.graph[key] = Vertex(key)

        # Should be called by init

    # '''v1 and v2 are vertex id's. As this is an undirected graph, add an
    #     edge from v1 to v2 and an edge from v2 to v1.  You can assume that
    #     v1 and v2 are already in the graph'''

    def add_edge(self, v1, v2):
        vert = self.graph.get(v1)
        vert.adjacent_to.append(v2)
        vert = self.graph.get(v2)
        vert.adjacent_to.append(v1)

        # Should be called by init

    # '''Marks all verteses as not visited'''
    def restet_visit(self):
        for key in self.graph:
            vert = self.graph.get(key)
            vert.not_visited = True

    # '''Marks all vertaces coolers as falce'''
    def restet_color(self):
        for key in self.graph:
            vert = self.graph.get(key)
            vert.is_red = False
            vert.is_perple = False

    # '''Return the Vertex object associated with the id. If id is not in the graph, return None'''
    def get_vertex(self, key):
        if not self.graph.get(key):
            return None
        else:
            return self.graph.get(key)

    # '''Returns a list of id's representing the vertices in the graph, in ascending order'''
    def get_vertices(self):
        # return = list(self.graph.keys())
        list = [None] * len(self.graph.keys())
        spot = 0
        for key in self.graph.keys():
            list[spot] = key
            spot += 1

        list.sort()
        return list

    # '''Return a list of lists.  For example: if there are three connected components
    # then you will return a list of three lists.  Each sub list will contain the
    # vertices (in ascending order) in the connected component represented by that list.
    # The overall list will also be in ascending order based on the first item of each sublist.'''

    def conn_components(self):
        self.restet_visit()
        # vert_list_not_visited = self.get_vertices()
        vert_list_master = self.get_vertices()
        stack = Stack(len(vert_list_master))
        list_of_vert_list = []

        while not self.check_visited(vert_list_master):

            vert_list = []
            vert = self.next_unvisited(vert_list_master).id
            # vert_list_not_visited.remove(vert)
            vert_list.append(vert)
            stack.push(vert)
            ajecency_index = 0
            vert = self.graph.get(vert)
            vert.not_visited = False

            while not stack.is_empty():
                key = stack.peek()
                vert = self.graph.get(key)

                ajacency_list = vert.get_adjacent_list()

                if (len(ajacency_list) - 1) < ajecency_index:
                    stack.pop()
                    ajecency_index = 0
                elif not self.graph.get(ajacency_list[ajecency_index]).not_visited:
                    ajecency_index += 1
                else:
                    key = ajacency_list[ajecency_index]
                    # vert_list_not_visited.remove(key)
                    vert_list.append(key)
                    stack.push(key)
                    vert = self.graph.get(key)
                    vert.not_visited = False
                    ajecency_index = 0
            vert_list.sort()
            list_of_vert_list.append(vert_list)

        return list_of_vert_list

        # This method MUST use Depth First Search logic!
        # '''Return True if the graph is bicolorable and False otherwise.'''
    def is_bipartite(self):

        # This method MUST use Breadth First Search logic!
        self.restet_visit()
        self.restet_color()
        # vert_list_not_visited = self.get_vertices()
        vert_list = self.get_vertices()
        queue = Queue(len(vert_list))
        # is_perple = []
        # is_red = []

        while not self.check_visited(vert_list):

            vert = self.next_unvisited(vert_list).id
            # vert_list_not_visited.remove(vert)
            # is_red.append(vert)
            queue.enqueue(vert)
            vert = self.graph.get(vert)
            vert.is_red = True
            vert.not_visited = False

            while not queue.is_empty():
                key = queue.peek()

                vert = self.get_vertex(key)

                ajacency_list = vert.get_adjacent_list()
                if vert.is_red:
                    for entry in ajacency_list:
                        ajacent_vert = self.get_vertex(entry)
                        ajacent_vert.is_perple = True
                else:
                    for entry in ajacency_list:
                        ajacent_vert = self.get_vertex(entry)
                        ajacent_vert.is_red = True

                for entry in ajacency_list:
                    vert = self.graph.get(entry)
                    if vert.not_visited:

                        queue.enqueue(entry)
                        vert.not_visited = False

                queue.dequeue()

        for key in vert_list:                               # checkis is any vertexs are bothe colors
            vert = self.graph.get(key)
            if vert.is_red and vert.is_perple:
                return False

        return True

    # '''Return True if all vertaseys have been visited and False otherwise.'''
    def check_visited(self, vert_list):
        for key in vert_list:
            vert = self.graph.get(key)
            if vert.not_visited:
                return False
        return True

    # '''Return the next unvisited vertex in assending order.'''
    def next_unvisited(self, vert_list):
        for key in vert_list:
            vert = self.graph.get(key)
            if vert.not_visited:
                return vert