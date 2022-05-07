from sys import argv
from stack_array import *


'''
   * Performs a topological sort of the specified directed acyclic graph.  The
   * graph is given as a list of vertices where each pair of vertices represents
   * an edge in the graph.  The resulting string return value will be formatted
   * identically to the Unix utility "tsort".  That is, one vertex per
   * line in topologically sorted order.
   *
   * Raises a ValueError if:
   *   - vertices is emtpy with the message "input contains no edges"
   *   - vertices has an odd number of vertices (incomplete pair) with the
   *     message "input contains an odd number of tokens"
   *   - the graph contains a cycle (isn't acyclic) with the message 
   *     "input contains a cycle"'''

class adjacency:

    def __init__(self):

        self.degree = 0
        self.adjacency_list = []

    # def __eq__(self, other):
    #     return type(other) == adjacency and self.degree == other.degree and self.adjacency_list == other.adjacency_list

def tsort(vertices):
    # raise PostfixFormatException("Empty input")
    if vertices is None or vertices == []:
        raise ValueError("input contains no edges")
    if  (len(vertices)) % 2 == 1:
        raise ValueError("input contains an odd number of tokens")

    vertex_list = bulid_adjacency_dictionary(vertices)

    tsorted_string = ""
    stack = Stack(len(vertex_list))
    for key, adj in vertex_list.items():

        if adj.degree == 0:
            stack.push(key)

    while not stack.is_empty():
        key = stack.pop()
        tsorted_string = tsorted_string + key + "\n"
        adj = vertex_list.get(key)
        adjacency_list = adj.adjacency_list

        for entry in adjacency_list:
            vertex = vertex_list.get(entry)
            vertex.degree -= 1
            if vertex.degree == 0:
                stack.push(entry)

    for key, adj in vertex_list.items():

        if adj.degree != 0:
            raise ValueError("input contains a cycle")

    return tsorted_string




def bulid_adjacency_dictionary( vertices):

    vertex_list = {}
    for i in range(0, len(vertices), 2):
        if not vertex_list.get(vertices[i]):
            adj = adjacency()
            vertex_list[vertices[i]] = adj
        if not vertex_list.get(vertices[i + 1]):
            adj = adjacency()
            adj.degree += 1
            vertex_list[vertices[i + 1]] = adj
            adj = vertex_list.get(vertices[i])
            adj.adjacency_list.append(vertices[i + 1])
        else:
            adj = vertex_list.get(vertices[i + 1])
            adj.degree += 1
            adj = vertex_list.get(vertices[i])
            adj.adjacency_list.append(vertices[i + 1])

    return vertex_list

def main():
    '''Entry point for the tsort utility allowing the user to specify
       a file containing the edge of the DAG'''
    if len(argv) != 2:
        print("Usage: python3 tsort.py <filename>")
        exit()
    try:
        f = open(argv[1], 'r')
    except FileNotFoundError as e:
        print(argv[1], 'could not be found or opened')
        exit()
    
    vertices = []
    for line in f:
        vertices += line.split()
       
    try:
        result = tsort(vertices)
        print(result)
    except Exception as e:
        print(e)
    
if __name__ == '__main__': 
    main()
