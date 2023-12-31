from Graph import *
from BruteForceAlgorithm import *
from TimeCounter import *
import csv

class Tests:
    def test(self, graph, numberOfTests):
        v = graph.vertices
        t = TimeCounter()

        times = []
        for i in range(numberOfTests):
            t.timeStart()
            BruteForceAlgorithm(graph,0)
            times.append(t.timeStop())

        timeAvg = sum(times)/len(times)

        return timeAvg, times


    def testing(self):
        data = self.openINI("bf.ini")   #0 - nazwa pliku, 1 - ilosc powtorzen testu, 2 - dlugosc optymalnej sciezki, 3 - optymalna sciezka

        for i in range (len(data[0])):
            l = self.test(Graph(data[0][i]), data[1][i])
            self.saveResults(data[0][i], l[0], l[1], data[1][i], data[2][i], data[3][i])


    def saveResults(self, filename,timeAvg, times, repeats, length, path):
        file = open('results.csv', 'a')
        writer = csv.writer(file)

        data = [filename, repeats, length, path]
        writer.writerow(data)
        writer.writerow(['sredni czas:', timeAvg])

        for i in times:
            writer.writerow([i])

        file.close

    def openINI(self, filename):
        fileNames, repeats, length, path = [], [], [], []

        with open(filename, "r") as file:
            lines = file.readlines()
            for line in lines:
                parts = line.split()
                if len(parts) >= 3:
                    fileNames.append(parts[0])
                    repeats.append(int(parts[1]))
                    length.append(int(parts[2]))
                    part = slice(3, len(parts), 1)

                    path.append(str(parts[part]).replace('\'', '').replace(',', ''))

        return fileNames, repeats, length, path

