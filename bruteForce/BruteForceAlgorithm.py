import sys

from itertools import permutations

class BruteForceAlgorithm:
    def __init__(self, graph, start):
        self.graph = graph
        self.start = start
        self.solution(start, graph.vertices)

    def solution(self, start, size):
        shortestPath = [start]
        sLength = sys.maxsize       #dlugosc najkrotszej trasy

        perms = self.permutation(start, size)    #wszystkie permutacje (bez wezla startowego)

        for p in perms:
            currentNode = start
            length = 0
            path = [start]
            for i in p:
                length += self.graph.g[currentNode][i]
                path.append(i)
                currentNode = i
            length += self.graph.g[currentNode][start]
            path.append(start)
            if length<sLength:
                sLength = length
                shortestPath = path
        return shortestPath, sLength

    def permutation(self, s, size):
        l = []
        for num in range(size):
            if(num!=s):
                l.append(num)

        return permutations(l)

