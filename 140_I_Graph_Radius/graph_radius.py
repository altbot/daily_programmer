# Implementation of Dijkstra's algorithm despite uniform edge weights
# http://en.wikipedia.org/wiki/Dijkstra%27s_algorithm

import sys

try:
    inFile = sys.argv[1]
except IndexError:
    inFile = "input.txt" # default

# Read data
data = [line.strip() for line in open(inFile).readlines()]
dim = int(data[0])
adjMatrix = [row.split() for row in data[1:]]
assert(dim == len(adjMatrix))

# Convert to nicer ints
for i in xrange(dim):
    adjMatrix[i] = [int(val) for val in adjMatrix[i]]

def getNeighbours(adjList):
    return [i for i in xrange(len(adjList)) if adjList[i]]

def walk(src, adjMatrix):
    distances = [sys.maxint] * dim
    distances[src] = 0
    previous = [sys.maxint] * dim
    unvisitedList = range(dim)
    while unvisitedList:
        minDist = sys.maxint
        for i in unvisitedList:
            if distances[i] < minDist:
                minDist = distances[i]
                u = i
        unvisitedList.remove(u)
        if distances[u] == sys.maxint:
            break # Unreachable node
        neighbours = getNeighbours(adjMatrix[u])
        for v in neighbours:
            if distances[u] == sys.maxint:
                alt = 1
            else:
                alt = distances[u] + 1
            if alt < distances[v]:
                distances[v] = alt
                previous[v] = u
                if v not in unvisitedList:
                    unvisitedList.append(v)
    return distances

distGraph = [[0] * dim] * dim
for src in xrange(dim):
    distGraph[src] = walk(src, adjMatrix)

print max([max(row) for row in distGraph])
