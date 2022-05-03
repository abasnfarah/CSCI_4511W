# Traveling Salesman Problem using naive approach.
import sys
import time
from itertools import permutations

# implementation of traveling Salesman Problem
def naiveTSP(graph):

    nodes = []
    for i in range(len(graph)):
        if i != 0:
            nodes.append(i)

    min_weight = sys.maxsize
    next_permutation=permutations(nodes)
    for i in next_permutation:

        current_pathweight = 0

        k = 0
        for j in i:
            current_pathweight += graph[k][j]
            k = j
        current_pathweight += graph[k][0]

        # update minimum
        if(current_pathweight < min_weight): 
            min_path = [0] + list(i)
            min_weight = current_pathweight

    # output should be 1 based not zero
    min_path = list(map(lambda node: node+1, min_path))
    return min_path

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
    solution = naiveTSP(graph)
    end = time.time()
    runtime = end - start
    print('\nThe input is a ' + str(len(inputFile)) + ' by ' + str(len(inputFile[0])) + ' Adjecency matrix')
    print('\nOur solution using the naive algorithm is: ' + str(solution))
    print('Runtime of our algorithm is: ' + str(runtime) + ' seconds')

if __name__ == "__main__":
    main()

