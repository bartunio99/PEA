from Graph import *
from Simulatedannealing import *
from TimeCounter import *
import csv

class Tests:

    T = 100000
    L = 100
    C = "geometric"
    F = "swap"


    def testTemperature(self, graph, numberOfTests, optimalCost):
        T = [1000,5000,10000,50000,100000, 500000, 1000000, 5000000]    #temperatury poczatkowe
        t = TimeCounter()
        times = []
        errors = []
        file = open('resultsTemp.csv', 'a')
        writer = csv.writer(file)
        writer.writerow(['rozmiar: ', 'temperatura: ',  'sredni czas:',  'sredni blad: ', 'schemat chlodzenia: ', 'wybor zamiany: '])

        for x in T:
            type(x)
            for i in range(numberOfTests):
                t.timeStart()
                result = Simulatedannealing(graph,self.C,self.L, x, self.F).solution()
                times.append(t.timeStop())
                errors.append((optimalCost-result)/optimalCost)
            timeAvg = sum(times)/len(times)
            errorAvg = sum(errors)/len(errors)
            writer.writerow([graph.vertices, x, timeAvg, errorAvg, self.C, self.F])
            print("zakonczono dla temperatury: ", x)

        file.close()

    def testEpoch(self, graph, numberOfTests, optimalCost):
        L = [10,20,50,100,200,500,1000,2000,5000,10000]                 #dlugosc epok
        t = TimeCounter()
        times = []
        errors = []
        file = open('resultsEpoch.csv', 'a')
        writer = csv.writer(file)
        writer.writerow(['rozmiar: ', 'dlugosc epoki: ',  'sredni czas:',  'sredni blad: ', 'schemat chlodzenia: ', 'wybor zamiany: '])

        for x in L:
            type(x)
            for i in range(numberOfTests):
                t.timeStart()
                result = Simulatedannealing(graph,self.C,x, self.T, self.F).solution()
                times.append(t.timeStop())
                errors.append((optimalCost-result)/optimalCost)
            timeAvg = sum(times)/len(times)
            errorAvg = sum(errors)/len(errors)
            writer.writerow([graph.vertices, x, timeAvg, errorAvg, self.C, self.F])
            print("zakonczono dla epok: ", x)

        file.close()





    # def testCooling(self, graph, numberOfTests, optimalCost):
    #     C = ["geometric", "boltzmann"]
    #     t = TimeCounter()
    #     times = []
    #     errors = []
    #     file = open('resultsCooling.csv', 'a')
    #     writer = csv.writer(file)
    #     writer.writerow(['rozmiar: ', 'schemat chlodzenia: ',  'sredni czas:',  'sredni blad: '])
    #
    #     for x in C:
    #         type(x)
    #         for i in range(numberOfTests):
    #             t.timeStart()
    #             result = Simulatedannealing(graph,x,self.L, self.T, self.F,self.A).solution()
    #             times.append(t.timeStop())
    #             errors.append((optimalCost-result)/optimalCost)
    #         timeAvg = sum(times)/len(times)
    #         errorAvg = sum(errors)/len(errors)
    #         writer.writerow([graph.vertices, x, timeAvg, errorAvg])
    #         print("zakonczono dla chlodzenia: ", x)
    #
    #     file.close()
    #
    #
    # def testMix(self, graph, numberOfTests, optimalCost):
    #     F = ["swap", "insert"]
    #     t = TimeCounter()
    #     times = []
    #     errors = []
    #     file = open('resultsMix.csv', 'a')
    #     writer = csv.writer(file)
    #     writer.writerow(['rozmiar: ', 'typ zmiany sasiedztwa: ',  'sredni czas:',  'sredni blad: '])
    #
    #     for x in F:
    #         type(x)
    #         for i in range(numberOfTests):
    #             t.timeStart()
    #             result = Simulatedannealing(graph,self.C,self.L, self.T, x,self.A).solution()
    #             times.append(t.timeStop())
    #             errors.append((optimalCost-result)/optimalCost)
    #         timeAvg = sum(times)/len(times)
    #         errorAvg = sum(errors)/len(errors)
    #         writer.writerow([graph.vertices, x, timeAvg, errorAvg])
    #         print("zakonczono dla zamiany sasiedztwa: ", x)
    #
    #     file.close()

    def test(self, graph, numberOfTests, optimalCost):


        self.testEpoch(graph, numberOfTests, optimalCost)
        self.testTemperature(graph, numberOfTests, optimalCost)

        self.F = "insert"

        self.testEpoch(graph, numberOfTests, optimalCost)
        self.testTemperature(graph, numberOfTests, optimalCost)

        self.C = "boltzmann"

        self.testEpoch(graph, numberOfTests, optimalCost)
        self.testTemperature(graph, numberOfTests, optimalCost)

        self.F = "swap"
        self.testEpoch(graph, numberOfTests, optimalCost)
        self.testTemperature(graph, numberOfTests, optimalCost)

        # self.testCooling(graph, numberOfTests, optimalCost)
        # self.testMix(graph, numberOfTests, optimalCost)



    def testing(self):
        data = self.openINI("sa.ini")   #0 - nazwa pliku, 1 - ilosc powtorzen testu, 2 - dlugosc optymalnej sciezki

        for i in range (len(data[0])):
            self.test(Graph(data[0][i]), data[1][i], data[2][i])

        print("Koniec!")
        input()


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

        return fileNames, repeats, length

