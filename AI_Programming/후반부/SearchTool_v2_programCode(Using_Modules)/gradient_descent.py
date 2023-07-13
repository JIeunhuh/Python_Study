from problem import Numeric 

def main():
    p = Numeric()
    # Create an instance of numerical optimization problem
    p.setvariable()   # 'p': (expr, domain)
    # Call the search algorithm
    solution, minimum = gradientDescent(p)
    p.storeResult(solution,minimum)
    # Show the problem and algorithm settings
    displaySetting(p)
    p.describe()
    # Report results
    p.report()
    
        
def gradientDescent(p):
    # 초기값 랜덤으로 정함
    current = p.randomInit() # 'current' is a list of values
    valueC = p.evaluate(current)
    while True:
        successor = p.takeStep(current, valueC)
        valueS = p.evaluate(successor)
        if valueS >= valueC:
            break
        else:
            current = successor
            valueC = valueS
    return current, valueC

def displaySetting(p):
    print()
    print('Search algorithm : Gradient-descent Hill Climbing')
    print()
    print("Mutation step size:", p.getAlpha(0.01))
main()
