from lab3.Graph import Graph
from lab3.Dijkstra import Dijkstra
import random

def printGraph(g):
    s1 = "List out: \n"
    for vertice in range(len(g.getOUT())):
        s1 += str(vertice) + " --> " 
        for v in g.getOUT()[vertice]:
            s1+= str(v) + " : " + str(g.getCost(vertice,v)) +" \n"
        s1+="\n"
    s2 = "\nList in: \n"
    for vertice in range(len(g.getIN())):
        s2 += str(vertice) + " <-- "
        for v in g.getIN()[vertice]:
            s2+= str(v) + " : " + str(g.getCost(v,vertice)) + "\n"
        s2+="\n"
    print(s1)
    print(s2)

"""
Creates and returns a random graph having n vertices and m edges.
"""
def createRandomGraph(n, m):
    graph = Graph(n)
    for i in range(m):
        v1 = random.randint(0,n-1)
        v2 = random.randint(0,n-1)
        while not graph.addEdge(v1,v2,random.randint(0,100)):
            v1 = random.randint(0,n-1)
            v2 = random.randint(0,n-1)
    return graph

def printPathAndCost(l,g):
    for i in range(len(l)):
        print(l[i][1]," ")
    print("Having the cost of: ",l[len(l)-1][0])
    
def computeCost(l,g):
    sum = 0
    for i in range(len(l)-1):
        sum += g.getCost(l[i],l[i+1])
    return sum

def main():

    n = int(input("Enter the number of vertices: "))
    m = int(input("Enter the number of edges: "))
    g = createRandomGraph(n, m)
    """
    g = Graph(5)
    g.addEdge(1,2,5)
    g.addEdge(1,3,4)
    g.addEdge(3,0,7)
    g.addEdge(3, 4, 2)
    g.addEdge(4,0,3)
    """
    printGraph(g)
    while (True):
        s = int(input("Enter the starting vertex: "))
        e = int(input("Enter target vertex: "))
        if (s != e and s >= 0 and s < n and e >= 0 and e < n):
            break
    t = Dijkstra(g,1,0)
    #print(t)
    if t!=None:
        printPathAndCost(t,g)
        
main()