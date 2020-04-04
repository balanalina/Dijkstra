import heapq
from Graph import *

"""
Returns a tree having lowest path.
"""
def Dijkstra(g,startVertex,endVertex):
    if g.inDegree(endVertex) == 0 or g.outDegree(startVertex) == 0:
        print("There is no path.")
        return None
    """
    visited
    for i in range(g.getVertices()):
        visited[i] = False
        """
    queue = []
    path = [(0,startVertex,None)]
    minCost = {startVertex : 0}
    heapq.heappush(queue,(0,startVertex,None))
    found = False
    while queue != [] and not found:
        print(queue)
        cost , currentVertex , parent = heapq.heappop(queue)
        if parent != None:
            if parent == path[len(path)-1][1]:
                path.append((cost,currentVertex,parent))
        it = g.parseOut(currentVertex)
        while it.valid():
            if not it.getCurrent() in minCost.keys() or (minCost[currentVertex] + g.getCost(currentVertex,it.getCurrent()) < minCost[it.getCurrent()]):
                minCost[it.getCurrent()] = minCost[currentVertex] + g.getCost(currentVertex,it.getCurrent())
                heapq.heappush(queue,(minCost[it.getCurrent()],it.getCurrent(),currentVertex))
            it.next()
        if currentVertex == endVertex:
            found = True
            if parent == path[len(path)-1][1]:
                path.append((cost,currentVertex,parent))
    return path


        
    