from example_gamma2 import *

class Graph():
    def __init__(self, vertices = [], edges = []) -> None:
        """Creates an undirected graph.
        
        Vertices are stored as a list self.V without duplicates.
        Edges are stored in a dictionnary self.E mapping a vertex to a list
        of neighbours.

        Input parameters:
          vertices -- a list of distinct vertices (default : empty)
          edges -- a list of pairs of vertices (default : empty)
        """
        self.V = []
        self.E = {}
        self.mu = {}
        self.rho = {}
        self.phi = {}
        for v in vertices:
            self.add_vertex(v)
        for (u,v) in edges:
            self.add_edge(u,v)
        for v in self.V :
            self.rho[v] = v
            self.phi[v] = v
            

    def __str__(self) -> str:
        s = "Graph with vertices: {ver}\n\n".format(ver = str(self.V))
        s+= "Edges: {edg}\n\n".format(edg=str(self.E))
        s+= "Matching: {m}\n".format(m=str(self.matching()))
        return s
    
    def add_vertex(self, v):
        """Adds a vertex to the grap."""
        assert(v not in self.V)
        self.V.append(v)
        self.E[v] = []
        self.mu[v] = v
    
    def add_edge(self, u, v):
        """Adds an edge to the grap
        
        Input parameters :
          u, v -- end nodes of the added edge.
        """
        assert(u in self.V)
        assert(v in self.V)
        self.E[u].append(v)
        self.E[v].append(u)    

    def matching(self):
        """
        Returns the current matching indicated by self.mu as a list of edges.
        """
        m = []
        for v in self.E:
            if self.mu[v] > v:
                m.append((v,self.mu[v]))
        return m
        
    def is_outer(self, v):
        """
        Returns True if the vertex v is an outer vertex in the current special
        blossom forest decomposition. 
        """
        if (self.mu[v] == v or self.phi[self.mu[v]] != self.mu[v]):
            return True
    
    def is_inner(self, v):
        """
        Returns True if the vertex v is an inner vertex in the current special
        blossom forest decomposition. 
        """
        if (self.phi[self.mu[v]] == self.mu[v] and self.phi[v] != v):
            return True
    
    def is_outside(self, v):
        """
        Returns True if the vertex v is outside the current special blossom forest. 
        """
        if (self.mu[v] != v and self.phi[v] == v and self.phi[self.mu[v]] == self.mu[v]):
            return True

    def path(self, v):
        """
        Returns the path from v to its root in the current special blossom forest
        decomposition as a list of vertices.

        Pre-condition : v should be an outer node

        Post-condition : the list should represent a path of even length, with
        edges alternating between edges from the matching (at odd distance from v) 
        and edges outside the matching (at even distance from v)
        """
        P = []
        if self.is_outer(v):
            P.append(v)
        else:
            raise ValueError("Le sommet v n'est pas externe")
        result = self.mu[v]
        while result != v:
            if self.is_outer(result):
                result = self.phi[result]
                P.append(result)
                result = self.mu[result]
                P.append(result)
        
        return P
                

    
    def _are_disjoint(self, u, v):
        raise NotImplementedError("The student should implement this method.")
    
    def _next_unscanned(self):
        raise NotImplementedError("The student should implement this method.")
    
    def _next_neighbour(self, x):
        raise NotImplementedError("The student should implement this method.")
    
    def _grow(self, x, y):
        raise NotImplementedError("The student should implement this method.")

    def _path_disjoint(self, x, y):
        raise NotImplementedError("The student should implement this method.")

    def _augment(self, x, y):
        raise NotImplementedError("The student should implement this method.")

    def _shrink(self, x, y):
        raise NotImplementedError("The student should implement this method.")
    
    def maximum_matching(self):
        """
        Computes a matching of maximum cardinality using Edmonds' algorithm
        """
        raise NotImplementedError("The student should implement this method.")


if __name__ == "__main__":
    graph2 = Gamma2
    graph2.mu = muGam2
    graph2.rho = rhoGam2
    graph2.phi = phiGam2
    graph2.outer = outerGam2
    graph2.inner = innerGam2
    graph2.outside = outsideGam2
    print(graph2)

    for v in graph2.V:
        if graph2.is_outer(v):
            assert(v in graph2.outer)
        if graph2.is_inner(v):
            assert(v in graph2.inner)
        if graph2.is_outside(v):
            assert(v in graph2.outside)

    # test 
    
#    Gamma1.maximum_matching()
