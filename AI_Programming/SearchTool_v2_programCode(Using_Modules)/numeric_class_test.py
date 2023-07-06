from problem import Numeric 

def main():
    p = Numeric()
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
    # 초기값 랜덤으로 정함
    current = p.randomInit() # 'current' is a list of values
    valueC = p.evaluate(current)
    while True:
        neighbors = p.mutants(current)
        successor, valueS = bestOf(p,neighbors)
        if valueS >= valueC:
            break
        else:
            current = successor
            valueC = valueS
    return current, valueC
    
def bestOf(p,neighbors): ###
    best = neighbors[0]
    bestValue = p.evaluate(best)
    # 1번째 index부터 시작
    for i in range(1,len(neighbors)):
        newVal = p.evaluate(neighbors[i])
        if(newVal < bestValue):
            bestValue = newVal
            best = neighbors[i]
    return best, bestValue

main()
