import sys
from itertools import combinations

class HeldKarp():


    def __init__(self, graph):
        vertices = []
        self.graph = graph
        self.matrix = self.graph.g     #macierz sasiedztwa grafu
        self.size = self.graph.size

        for i in range(self.size):
            if (i!=0):
                vertices.append(i)


        print(self.solution(vertices))




    def solution(self, vertices):
        d = {}  #dict zawierajacy trasy zaczynajasce sie z self.start i przechodzace przez *klucz1* wierzcholki i konczacy na *klucz2* wierzcholku, o dlugosci *wartosc*

        for i in vertices:
            d[(i,),i] = (self.matrix[i][0],[i])


        for v in vertices:
            if(v!=1):
                combination = tuple(combinations(vertices, v))     #zestaw wszystkich kombinacji liczb ze zbioru wierzcholkow o wielkosci v
                for group in combination:                               #jedna kombinacja
                    for k in group:
                        pathCost = sys.maxsize
                        for m in group:
                            if(m!=k):
                                helpList = list(group)
                                helpList.remove(k)

                                prevPathCost,prevPath = d[tuple(helpList), m]

                                newPathCost  = prevPathCost+self.matrix[m][k]
                                if(newPathCost < pathCost):
                                    pathCost  = newPathCost
                                    bestPath = prevPath + [k]
                                    d[group, k] = (newPathCost, bestPath)



        cost = sys.maxsize
        bestPath = []
        tup = tuple(vertices)


        for v in vertices:
            newCost, newPath = d[tup,v]
            newCost += self.matrix[v][0]
            if(newCost<cost):
                cost = newCost
                bestPath = newPath

        return cost, [0] + bestPath + [0]


























