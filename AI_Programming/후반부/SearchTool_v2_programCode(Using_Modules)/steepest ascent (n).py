import random
import math
from numeric import * # numeric의 함수를 가져오도록 하기위해서 

DELTA = 0.01   # Mutation step size
NumEval = 0    # Total number of evaluations

def main():
    # Create an instance of numerical optimization problem
    p = createProblem()   # 'p': (expr, domain)
    # Call the search algorithm
    solution, minimum = steepestAscent(p)
    # Show the problem and algorithm settings
    describeProblem(p)
    displaySetting()
    # Report results
    displayResult(solution, minimum)


def steepestAscent(p):
    # 초기값 랜덤으로 정함
    current = randomInit(p) # 'current' is a list of values
    valueC = evaluate(current, p)
    while True:
        neighbors = mutants(current, p)
        successor, valueS = bestOf(neighbors, p)
        if valueS >= valueC:
            break
        else:
            current = successor
            valueC = valueS
    return current, valueC


def mutants(current, p): ###
    neighbors = []
    for i in range(len(current)):
        mutant = mutate(current,i,DELTA,p)
        neighbors.append(mutant)
    return neighbors     # Return a set of successors

def bestOf(neighbors, p): ###
    best = neighbors[0]
    bestValue = evaluate(best,p)
    # 1번째 index부터 시작
    for i in range(1,len(neighbors)):
        newVal = evaluate(neighbors[i],p)
        if(newVal < bestValue):
            bestValue = newVal
            best = neighbors[i]
    return best, bestValue



def displaySetting():
    print()
    print("Search algorithm: Steepest-Ascent Hill Climbing")
    print()
    print("Mutation step size:", DELTA)



main()
