from problem import Numeric 

LIMIT_STUCK = 100 

def main():
    p = Numeric()
    # Create an instance of numerical optimization problem
    p.setvariable()   # 'p': (expr, domain)
    # Call the search algorithm
    solution, minimum = firstChoice(p)
    p.storeResult(solution,minimum)
    # Show the problem and algorithm settings
    p.describe()
    # Report results
    p.report()
    
        
def firstChoice(p):
    current = p.randomInit()   # 'current' is a list of values
    valueC = p.evaluate(current)
    i = 0
    while i < LIMIT_STUCK:
        successor = p.randomMutants(current)
        valueS = p.evaluate(successor)
        if valueS < valueC:
            current = successor
            valueC = valueS
            i = 0              # Reset stuck counter
        else:
            i += 1
    return current, valueC

main()
