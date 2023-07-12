from problem import Tsp

def main():
    p = Tsp()
    # Create an instance of numerical optimization problem
    p.setvariable()   # 'p': (expr, domain)
    # Call the search algorithm
    solution, minimum = steepestAscent(p)
    p.storeResult(solution,minimum)
    # Show the problem and algorithm settings
    p.describe()
    # Report results
    p.report()
    
def steepestAscent(p):
    current = p.randomInit()   # 'current' is a list of city ids
    valueC = p.evaluate(current)
    while True:
        neighbors = p.mutants(current)
        (successor, valueS) = bestOf(neighbors,p)
        if valueS >= valueC:
            break
        else:
            current = successor
            valueC = valueS
    return current, valueC
    
def bestOf(neighbors, p):
    best = neighbors[0]
    bestValue = p.evaluate(best)
    for i in range(1,len(neighbors)):
        newVal = p.evaluate(neighbors[1])
        if(newVal < bestValue):
            bestValue = newVal
            best = neighbors[i]
    return best, bestValue  

main()      
