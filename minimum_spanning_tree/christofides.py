# Traveling Salesman Problem using christofides algorithm.
import sys
import time
import random
from itertools import permutations
from collections import defaultdict
INT_MAX = sys.maxsize
V = 5

# Kruskal's algorithm for building MSP
class UnionFind:
    def __init__(self):
        self.costs= {}
        self.levels= {}

    def __getitem__(self, object):
        if object not in self.levels:
            self.levels[object] = object
            self.costs[object] = 1
            return object
        path = [object]
        root = self.levels[object]
        while root != path[-1]:
            path.append(root)
            root = self.levels[root]
        for ancestor in path:
            self.levels[ancestor] = root
        return root

    def __iter__(self):
        return iter(self.levels)

    def union(self, *objects):
        roots = [self[x] for x in objects]
        maxCost = max([(self.costs[r], r) for r in roots])[1]
        for r in roots:
            if r != maxCost:
                self.costs[maxCost] += self.costs[r]
                self.levels[r] = maxCost

def buildMinimumSpanningTree(Graph):
    MSP = []
    MSP_S= UnionFind()
    for c, u, v in sorted((Graph[u][v], u, v) for u in Graph for v in Graph[u]):
        if MSP_S[u] != MSP_S[v]:
            MSP.append((u, v, c))
            MSP_S.union(u, v)
    return MSP

def getOddVertexes(MST):
    graph = {}
    output = []
    for E in MST:
        if E[0] not in graph:
            graph[E[0]] = 0
        if E[1] not in graph:
            graph[E[1]] = 0
        graph[E[0]] += 1
        graph[E[1]] += 1
    for vertex in graph:
        if graph[vertex] % 2 == 1:
            output.append(vertex)
    return output

def addMinimumWeightEdges(MST, Graph, oddVert):
    random.shuffle(oddVert)
    while oddVert:
        v = oddVert.pop()
        l = float("inf")
        u = 1
        near = 0
        for u in oddVert:
            if v != u and Graph[v][u] < l:
                l = Graph[v][u]
                near = u
        MST.append((v, near, l))
        oddVert.remove(near)

def getEulerianCircuit(MST):
    n = {}
    for e in MST:
        if e[0] not in n:
            n[e[0]] = []

        if e[1] not in n:
            n[e[1]] = []

        n[e[0]].append(e[1])
        n[e[1]].append(e[0])

    first = MST[0][0]
    eulerian = [n[first][0]]

    while len(MST) > 0:
        for i, v in enumerate(eulerian):
            if len(n[v]) > 0:
                break

        while len(n[v]) > 0:
            u = n[v][0]

            removeEdge(MST, v, u)

            del n[v][(n[v].index(u))]
            del n[u][(n[u].index(v))]

            i += 1
            eulerian.insert(i, u)

            v = u

    return eulerian


def removeEdge(MST, v, u):

    for i, item in enumerate(MST):
        if (item[0] == u and item[1] == v) or (item[0] == v and item[1] == u):
            del MST[i]

    return MST

def getHamiltonionPath(eulerian, graph):
    current = eulerian[0]
    path = [current]
    visited = [False] * len(eulerian)
    visited[eulerian[0]] = True
    total = 0
    for v in eulerian:
        if not visited[v]:
            path.append(v)
            visited[v] = True
            total += graph[current][v]
            current = v

    total +=graph[current][eulerian[0]]
    path.append(eulerian[0])

    return total, path[1:]


def christofidesTSP(graph):
    """ Steps for Chrisofides algorithm
    1. Generate a Minimum Spanning Tree from Graph
    2. Find the vertexes in MSP with odd degree
    3. Add the minimum weight edges to the MSP
    4. Create an eulerian circuit using the mimimum weight edges 
       and the MSP edges.
    5. Make a hamiltonian circuit by skipping repeated vertexes
    """
    print("Graph: ",  graph)
    # Step 1: Generate a MSP from a graph
    MST = buildMinimumSpanningTree(graph)
    print("MST: ", MST)

    # Step 2 Find the Vertexes in MSP with odd degree
    oddVert = getOddVertexes(MST)
    print("Odd Vert: ", oddVert)

    # Step 3: Add the minimum weight edges to the MSP 
    addMinimumWeightEdges(MST, graph, oddVert)
    print("Updated MST: ", MST)

    # Step 4: Create Eulerian Circuit using the minimum weight edges
    #       : and the MSP edges
    eulerian = getEulerianCircuit(MST)
    print("Eulerian Circuit", eulerian)

    # Step 5: Make Hamiltonian circuit by skipping repeating nodes 
    hamiltonian = getHamiltonionPath(eulerian, graph)
    hamiltonian = (hamiltonian[0], list(map(lambda node: node+1, hamiltonian[1])))
    print("Hamiltonian :", hamiltonian)


    return hamiltonian[1]

def main():
    # This formats the data into an adjMatrix to pass to the naiveTSP
    inputFile = sys.stdin.readlines()
    graph = []
    for i in range(0,len(inputFile)):
        inputFile[i] = inputFile[i].rstrip().split()
    print("Graph input: ")
    for i in range(len(inputFile)):

        inputFile[i] = list(map(float, inputFile[i]))
        inputFile[i] = list(map(int, inputFile[i]))
        print(inputFile[i])
    graph = inputFile

    # convert adjMatrix to adjList
    adjList = defaultdict(dict)
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j]!= 0:
                adjList[i][j] = graph[i][j]

    # This lets us track the runtime of our algorithm
    start = time.time()
    solution = christofidesTSP(adjList)
    end = time.time()
    runtime = end - start
    print('\nThe input is a ' + str(len(inputFile)) + ' by ' + str(len(inputFile[0])) + ' Adjecency List')
    print('\nOur solution using the naive algorithm is: ' + str(solution))
    print('Runtime of our algorithm is: ' + str(runtime) + ' seconds')

if __name__ == "__main__":
    main()

