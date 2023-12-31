from Tests import *
from Graph import *
from HeldKarp import *

def main():
    print("Rozpoczęto działanie programu...")
    t = Tests()
    t.testing()

def t():
     HeldKarp(Graph("tsp_18_1.txt"))


if __name__ == '__main__':
    t()
