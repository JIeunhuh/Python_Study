import random
import math

NumEval = 0    # Total number of evaluations

def createProblem():
    ## Read in a TSP (# of cities, locatioins) from a file.
    ## Then, create a problem instance and return it.
    fileName = input("Enter the file name of a TSP : ")
    infile = open(fileName, 'r')
    # First line is number of cities
    numCities = int(infile.readline())
    locations = []
    line = infile.readline()  # The rest of the lines are locations
    while line != '':
        locations.append(eval(line)) # Make a tuple and append
        line = infile.readline()
    infile.close()
    table = calcDistanceTable(numCities, locations)
    return numCities, locations, table


def calcDistanceTable(numCities, locations): ###
    table = [] # 2차원 table
    for i in range(numCities):
        row = []
        for j in range(numCities):
            ## 피타고라스의 정리 이용(dx,dy의 좌표 길이 구하기)
            dx = locations[i][0]-locations[j][0] ## dx의 길이
            dy = locations[i][1] - locations[j][1] ## dy의 길이
            d = math.sqrt(dx**2 + dy**2) 
            row.append(d)
        table.append(row)
        # print('table ', table)
    return table # A symmetric matrix of pairwise distances


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

def inversion(current, i, j):  ## Perform inversion 
    curCopy = current[:]
    while i < j:
        curCopy[i], curCopy[j] = curCopy[j], curCopy[i]
        i += 1
        j -= 1
    return curCopy

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
