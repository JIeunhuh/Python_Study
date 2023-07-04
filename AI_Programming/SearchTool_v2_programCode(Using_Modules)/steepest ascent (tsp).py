import random
import math




def main():
    # Create an instance of TSP
    p = createProblem()    # 'p': (numCities, locations, table)
    # Call the search algorithm
    solution, minimum = steepestAscent(p)
    # Show the problem and algorithm settings
    describeProblem(p)
    displaySetting()
    # Report results
    displayResult(solution, minimum)
    



def steepestAscent(p):
    current = randomInit(p)   # 'current' is a list of city ids
    valueC = evaluate(current, p)
    while True:
        neighbors = mutants(current, p)
        (successor, valueS) = bestOf(neighbors, p)
        if valueS >= valueC:
            break
        else:
            current = successor
            valueC = valueS
    return current, valueC

def randomInit(p):   # Return a random initial tour
    n = p[0]
    init = list(range(n))
    random.shuffle(init) # random하게 섞음
    return init


def evaluate(current, p): ###
    ## Calculate the tour cost of 'current'
    global NumEval
    
    NumEval += 1
    numCities = p[0]
    table = p[2]
    cost = 0
    for i in range(numCities-1):
        locFrom = current[i] # 시작점
        locTo = current[i+1] # 그 다음으로 이동하는 점
        cost += table[locFrom][locTo] # 다 합해줌
    cost += table[current[numCities-1]][current[0]] # 마지막 지점에서 시작점으로 다시 이동하는 거리
    ## 'p' is a Problem instance
    ## 'current' is a list of city ids
    return cost


def mutants(current, p): # Apply inversion
    n = p[0]
    neighbors = []
    count = 0
    triedPairs = []
    while count <= n:  # Pick two random loci for inversion
        i, j = sorted([random.randrange(n) for _ in range(2)])
        if i < j and [i, j] not in triedPairs:
            triedPairs.append([i, j])
            curCopy = inversion(current, i, j) ## i, j번째 current 바꿔치기
            count += 1
            neighbors.append(curCopy)
    return neighbors

def inversion(current, i, j):  ## Perform inversion 
    curCopy = current[:]
    while i < j:
        curCopy[i], curCopy[j] = curCopy[j], curCopy[i]
        i += 1
        j -= 1
    return curCopy

def bestOf(neighbors, p): ### 총 거리가 가장 작은 것
    best = neighbors[0]
    bestValue = evaluate(best,p)
    for i in range(1,len(neighbors)):
        newVal = evaluate(neighbors[1],p)
        if(newVal < bestValue):
            bestValue = newVal
            best = neighbors[i]
    return best, bestValue

def describeProblem(p):
    print()
    n = p[0]
    print("Number of cities:", n)
    print("City locations:")
    locations = p[1]
    for i in range(n):
        print("{0:>12}".format(str(locations[i])), end = '')
        if i % 5 == 4:
            print()

def displaySetting():
    print()
    print("Search algorithm: Steepest-Ascent Hill Climbing")

def displayResult(solution, minimum):
    print()
    print("Best order of visits:")
    tenPerRow(solution)       # Print 10 cities per row
    print("Minimum tour cost: {0:,}".format(round(minimum)))
    print()
    print("Total number of evaluations: {0:,}".format(NumEval))

def tenPerRow(solution):
    for i in range(len(solution)):
        print("{0:>5}".format(solution[i]), end='')
        if i % 10 == 9:
            print()

main()
