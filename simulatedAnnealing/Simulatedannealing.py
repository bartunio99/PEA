import sys

from Graph import *
import math
import random

class Simulatedannealing:

    #konstruktor - parametry: praf, schemat chłodzenia, dlugosc epoki, temperatura startowa, sposob przeszukiwania sasiedztwa
    def __init__(self, graph: Graph, coolingSchedule: str, epochLength: int, initialTemperature: float, neighbourFindMethod: str):
        self.graph = graph.g    #macierz grafu
        self.size = graph.vertices  #rozmiar grafu
        self.vertices = []
        self.coolingSchedule = coolingSchedule
        self.epochLength = epochLength
        self.initialTemperature = initialTemperature
        self.neighbourFindMethod = neighbourFindMethod
        self.minTemperature = 0.01

        #epochLength = self.size*3
        for i in range(self.size):
            if (i != 0):
                self.vertices.append(i)




    def solution(self) -> []:

        currentPath, currentCost = self.genetatePathGreedy(self.size)
        bestPath, bestCost = currentPath, currentCost


        currentTemperature = self.initialTemperature
        alpha = 0.999   #musi byc bliskie 1



        while(currentTemperature>self.minTemperature):
            epochCount = 0    #ktora epoki
            #print(currentTemperature)
            while(epochCount<self.epochLength):

                #wybieranie nowej sciezki
                if(self.neighbourFindMethod == "swap"):
                    newPath, newCost = self.vertexSwap(currentPath, self.size)
                elif(self.neighbourFindMethod == "insert"):
                    newPath, newCost = self.vertexInsert(currentPath, self.size)


                if(newCost < bestCost):
                    bestPath, bestCost = newPath, newCost

                probability = self.acceptSolution(1/currentCost, 1/newCost, currentTemperature)
                if(probability > random.uniform(0,1)):
                    currentPath, currentCost = newPath, newCost


                #print(newPath, newCost)
                epochCount+=1

            if(self.coolingSchedule == "geometric"):
                currentTemperature = self.geometricColling(currentTemperature, alpha, epochCount)
            elif(self.coolingSchedule == "boltzmann"):
                currentTemperature = self.boltzmannColling(currentTemperature, epochCount)


        return bestCost





    #metoda zamieniajaca miejscami 2 wierzcholki w sciezce - 2-zamiana:
    def vertexSwap(self, path, size) -> []:
        #print(path, self.calculateCost(path,size))
        a = random.randint(0,size-1)
        b = a
        while(b == a):
            b = random.randint(0,size-1)

        c = path[a]
        path[a] = path[b]
        path[b] = c


        path[size] = path[0]
        cost = self.calculateCost(path, size)
        return path, cost

    #zmienia ścieżkę, zmieniając miejsce jednego wierzchołka na inne, losowe
    def vertexInsert(self, path, size) -> []:
        a = random.randint(0, size-1)
        b = a
        value = path[a]
        del path[a]

        while (b == a):
            b = random.randint(0, size - 1)

        path.insert(b, value)

        path[size] = path[0]
        cost = self.calculateCost(path,size)

        return path, cost
    #generacja losowej permutacji
    def randomPermutation(self, iterable, r) -> tuple:
        "Random selection from itertools.permutations(iterable, r)"
        pool = tuple(iterable)
        r = len(pool) if r is None else r
        return tuple(random.sample(pool, r))


    #generacja losowego rozwiazania - TODO zmienic to by mi nie liczylo kazdej mozliwej sciezki xd

    def generatePathRandom(self, vertices) -> []:
        path = []
        path.append(0)


        for i in self.randomPermutation(vertices, None):
            path.append(i)
        path.append(0)

        cost = self.calculateCost(path, self.size)

        return path, cost


    #generacja wstepnego rozwiazania uzywajac algorytmu zachlannego
    def genetatePathGreedy(self, size) -> []:
        path = []
        addedVertices = []
        path.append(0)
        addedVertices.append(0)

        currentV = 0

        while(len(path) < size):
            newV = self.getClosestNeighbour(currentV,size, addedVertices)
            path.append(newV)
            addedVertices.append(newV)
            currentV = newV

        path.append(0)

        cost = self.calculateCost(path, size)

        return path, cost

    #metoda zwracajaca najblizszego sasiada wierzcholka, pod warunkiem ze nie byl wczesniej uwzgledniony w liczonej sciezce
    def getClosestNeighbour(self, vertex, size, checkedVertices) -> int:
        res = sys.maxsize
        ans = 0
        for i in range(size):
            if(self.graph[vertex][i] < res and vertex!=i and i not in checkedVertices):
                res = self.graph[vertex][i]
                ans = i

        return ans

    #oblicza koszt sciezki
    def calculateCost(self, path, size):

        cost = 0
        for i in range(size):
            cost+=self.graph[path[i]][path[i+1]]

        return cost


    #schematy chlodzenia:
    #geometryczny
    def geometricColling(self, initialTemperature: float, coolingCoefficient : float, epochNumber: int) -> float:
        return initialTemperature*(coolingCoefficient**epochNumber)

    #boltzmanna
    def boltzmannColling(self, initialTemperature: float, epochNumber: int) -> float:
        return initialTemperature/(1+math.log(epochNumber))

   #metoda obliczajaca prawdopodobienstwo zaakceptowania nowego rozwiazania
    def acceptSolution(self, previousResult: int, currentResult: int, currentTemperature: float) -> float:

        try:
            res = math.exp(-(currentResult-previousResult)/currentTemperature)
        except: #wywala dokladnosc brzy bradzo malych wartosciach
            res = 0

        return res