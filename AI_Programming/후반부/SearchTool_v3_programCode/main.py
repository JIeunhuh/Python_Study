from problem import *
from optimizer import *

def main():
    p, pType = selectProblem() # 문제 선택 , pType = 1(numeric) or 2(tsp)
    alg = selectAlgorithm(pType) # 알고리즘 선택
    
    alg.run(p) # 실행
    
    p.describe()
    alg.displaySetting()
    p.report()

## 문제 선택(numeric / tsp)
def selectProblem():
    print('Select the problem')
    print('1. Numeric')
    print('2. TSP')
    pType = int(input('Enter the number : '))

    if pType == 1:
        p = Numeric()
    elif pType == 2:
        p = Tsp()
    else:
        print('Wrong Input.')
        
    p.setvariable()    
    
    return p, pType
    
# 알고리즘 선택(steepdestascent / firstchoice / gradientDescent)
def selectAlgorithm(pType):
    print('Select the algorithm')
    print('1. SteepestAscent')
    print('2. FirstChoice')
    print('3. GradientDescent')    
    aType = int(input('Enter the number : '))
    try:
        # 1. 조건문 이용
        # if aType == 1:
        #     alg = SteepestAscent()
        # elif aType == 2:
        #     alg = FirstChoice()
        # elif aType == 3:
        #     alg =  GradientDescent()
        
        # 2. dictionary 이용
        optimizers = {1:'SteepestAscent()', 2:'FirstChoice()',3:'GradientDescent()'}
        alg = eval(optimizers[aType])
        
        alg.setvariables(pType)
        
        return alg
        
    except Exception as exc1:
        print('Wrong Input')
        print(exc1)
        
    
main()