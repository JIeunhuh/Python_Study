import random
import math

DELTA = 0.01 #Muation step size
LIMIT_STUCK = 100 
NumEval = 0 # Total number of evaluations

def createProblem(): ###
    ## Read in an expression and its domain from a file.
    fileName = input("Enter the fileName of function : ")
    # textfile 가지고 오기
    # name = f"C:\HJE_Python\AI_Programming\SearchTool_programCode\problem\{fileName}.txt"
    infile = open(fileName, 'r') # file open하기, read mode
    expression = infile.readline()
    # 변수, low, up
    varNames = []
    low = []
    up = []
    # txt 파일을 한줄씩 읽어옴
    line = infile.readline()
    # line이 종료되기 전까지
    while line != '':
        # ',' 기준으로 배열 나눠줌
        data = line.split(',')
        # 변수
        varNames.append(data[0])
        # 최소
        low.append(float(data[1]))
        # 최대
        up.append(float(data[2]))
        line = infile.readline().strip()
    infile.close()
    # 위에 배열을 domain list에 저장함
    domain = [varNames,low,up]
    
    
    ## Then, return a problem 'p'.
    ## 'p' is a tuple of 'expression' and 'domain'.
    ## 'expression' is a string.
    ## 'domain' is a list of 'varNames', 'low', and 'up'.
    ## 'varNames' is a list of variable names.
    ## 'low' is a list of lower bounds of the varaibles.
    ## 'up' is a list of upper bounds of the varaibles.
    return expression, domain

def randomInit(p): ###
    domain = p[1]
    low = domain[1]
    up = domain[2]
    init = []
    for i in range(len(low)):
        r = random.uniform(low[i],up[i]) # .uniform
        init.append(r)
    return init    # Return a random initial point
                   # as a list of values

def evaluate(current, p):
    
    ## Evaluate the expression of 'p' after assigning
    ## the values of 'current' to the variables
    global NumEval # 함수값을 바꾸기 위해서 전역변수라는 것을 알려줌?
    
    NumEval += 1
    # 수학 식(txt 파일의 수식)
    expr = p[0]         # p[0] is function expression
    # .txt파일의 변수
    varNames = p[1][0]  # p[1] is domain
    for i in range(len(varNames)):
        assignment = varNames[i] + '=' + str(current[i])
        exec(assignment)
    return eval(expr)


def mutate(current, i, d, p): ## Mutate i-th of 'current' if legal
    curCopy = current[:]
    domain = p[1]        # [VarNames, low, up]
    l = domain[1][i]     # Lower bound of i-th
    u = domain[2][i]     # Upper bound of i-th
    if l <= (curCopy[i] + d) <= u:
        curCopy[i] += d
    return curCopy

def describeProblem(p):
    print()
    print("Objective function:")
    print(p[0])   # Expression
    print("Search space:")
    varNames = p[1][0] # p[1] is domain: [VarNames, low, up]
    low = p[1][1]
    up = p[1][2]
    for i in range(len(low)):
        print(" " + varNames[i] + ":", (low[i], up[i])) 


def displayResult(solution, minimum):
    print()
    print("Solution found:")
    print(coordinate(solution))  # Convert list to tuple
    print("Minimum value: {0:,.3f}".format(minimum))
    print()
    print("Total number of evaluations: {0:,}".format(NumEval))

def coordinate(solution):
    c = [round(value, 3) for value in solution]
    return tuple(c)  # Convert the list to a tuple