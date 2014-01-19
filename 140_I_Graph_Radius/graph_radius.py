# Daily programer challenge 140 - Graph Radius - Intermediate
# http://www.reddit.com/r/dailyprogrammer/comments/1tiz4z/122313_challenge_140_intermediate_graph_radius/
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

# Convert to more workable ints
for i in xrange(dim):
    adjMatrix[i] = [int(val) for val in adjMatrix[i]]

def getNeighbours(adjList):
    return [i for i in xrange(len(adjList)) if adjList[i]]

def getMinDistanceVertex(unvisitedList, distances):
    minDist = sys.maxint
    for i in unvisitedList:
        if distances[i] < minDist:
            minDist = distances[i]
            u = i
    return u

def dijkstra(src, adjMatrix):
    distances = [sys.maxint] * dim
    distances[src] = 0
    previous = [sys.maxint] * dim
    unvisitedList = range(dim)
    while unvisitedList:
        # Find vertex with minimum distance
        u = getMinDistanceVertex(unvisitedList, distances)
        unvisitedList.remove(u)
        if distances[u] == sys.maxint:
            break # Unreachable node
        # Calculate new shortest paths via our new vertex to neighbours
        neighbours = getNeighbours(adjMatrix[u])
        for v in neighbours:
            if distances[u] == sys.maxint:
                alt = 1 # Vertex previously had no path to it
            else:
                alt = distances[u] + 1
            # Is going via our vertex is shorter than existing path?
            if alt < distances[v]:
                 # if so set this new path and mark vertex unvisited
                distances[v] = alt
                previous[v] = u
                if v not in unvisitedList:
                    unvisitedList.append(v)
    return distances

distGraph = [[0] * dim] * dim
for src in xrange(dim):
    distGraph[src] = dijkstra(src, adjMatrix)

radius = max([max(row) for row in distGraph])
if radius == sys.maxint:
    radius = "Infinity"
print radius
