from numpy.core.numeric import Infinity as INF
from queue import PriorityQueue
 
 
class Graph(object):
    def _init_(self, n_vertices):
        self.vertice = n_vertices
        self.edges = [[-1 for column in range(n_vertices)]
                      for row in range(n_vertices)]
        # this ccontains vertices that have already been visited
        self.a_visit = []
        #  b represents the number of verices in the graph
    def a_edge(self, a, b, w):
        # if not b in self.vertice[a].keys() or self.vertice[a][b] > w:
        # the edges represent it's list in matrix form
        self.edges[a][b] = w
        self.edges[b][a] = w
 
def dijkstra(graph, s_vertex):
    pq = PriorityQueue()
    pq.put((0, s_vertex))
        # creation of a list D_algo of size v
    D_algo = {vertice:float('INF') 
         for vertice in range(graph.vertice)}
    # initialize the starting vertex to 0 since it is the distance from itself
    D_algo[s_vertex] = 0
    while not pq.empty():
        (d, c_vertex) = pq.get()
        graph.a_visit.append(c_vertex)
    # we will iterate through the close vertices
        for k in range(graph.vertice):
            if graph.edges[c_vertex][k] != -1:
                distance = graph.edges[c_vertex][k]
                # if the nearby has not already been visited there is a comparrison between the former weight and the current
                if k not in graph.a_visit:
                    o = D_algo[k]
                    n = D_algo[c_vertex] + distance
                    # if the former weight is less than the new one 
                    if n < o:
                        pq.put((n, k))
                        D_algo[k] = n
    return D_algo
 
def shortestReach(n_node, g_edges, s_node):
    # initialize empty list
    g_list = []
    
    # number of nodes in the graph
    graph = Graph(n_node)
    r = len(g_edges)
    # looping through the edges 
    for j in range(r):
        c = g_edges[j][0]
        d= g_edges[j][1]
        e= g_edges[j][2]
        graph.a_edge(c, d, e) 
        #  djikistra function taking in the number of nodes and starting nodes
    Djkt = dijkstra(graph, s_node)  
    t = len(Djkt)
    # looping 
    for i in range(t):
        if i != s_node:
            g_list.append(Djkt[i])
    mylist = []
    for k in g_list:
        if k == float('INF'):
            mylist.append(-1)
        else:
            mylist.append(k) 

    return mylist
print(shortestReach(4, [[1,2,24], [1,3,3], [1,4,20], [3,4,12]], 1))