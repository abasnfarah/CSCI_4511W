# Traveling Salesman Problem using christofides algorithm.
import sys
import time
from itertools import permutations
from collections import defaultdict
INT_MAX = sys.maxsize
V = 5

# TODO: def buildMSP


def christofidesTSP(graph):
    """ Steps for Chrisofides algorithm
    1. Generate a Minimum Spanning Tree from Graph
    2. Find the vertexes in MSP with odd degree
    3. Find the minimum weight edges of MSP
    4. Create an eulerian circuit using the mimimum weight edges and the MSP edges.
    5. Make a hamiltonian circuit by skipping repeated vertexes
    """

	# convert adjMatrix to adjList
    adjList = defaultdict(list)
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j]!= 0:
                adjList[i].append((j,graph[i][j]))
    print(adjList)

    return []

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

    # This lets us track the runtime of our algorithm
    start = time.time()
    solution = christofidesTSP(graph)
    end = time.time()
    runtime = end - start
    print('\nThe input is a ' + str(len(inputFile)) + ' by ' + str(len(inputFile[0])) + ' Adjecency matrix')
    print('\nOur solution using the naive algorithm is: ' + str(solution))
    print('Runtime of our algorithm is: ' + str(runtime))

if __name__ == "__main__":
    main()

