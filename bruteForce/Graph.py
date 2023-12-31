class Graph:
    g = []
    vertices = 0

    def __init__(self, filename):
        self.loadFromFile(filename)

    def loadFromFile(self, filename):
        self.g = []
        file = open(filename,"r")

        self.vertices = int(file.readline())

        for i in range(self.vertices):
            distance = [int(x) for x in file.readline().split()]
            self.g.append(distance)

        # Zamykanie pliku
        file.close()









