import math
import random

from Setup import Setup

class Problem(Setup):
    def __init__(self):
        Setup.__init__(self)
        self._solution = []
        self._value = 0
        self._numEval = 0
        
        self._bestSolution = []
        self._bestMinimum = 0.0
        self._avgMinimum = 0.0
        self._avgNumEval = 0
        self._sumOfNumEval = 0  
        
        self._pFileName = ''
        
    # 자식 클래스가 오버라이딩 해서 쓰게 부모 클래스에선 함수만 생성함
    def setVariables(self,parameters): #createProblem
        self._pFileName = parameters['pFileName']
        Setup.setVariables(self,parameters)
    def getSolution(self):
        return self._solution
    def getValue(self):
        return self._value
    def getNumEval(self):
        return self._numEval
    def randomInit(self):
        pass
    def evaluate(self): 
        pass
    def mutants(self): 
        pass
    def randomMutant(self):
        pass
    def describe(self): #describeProblem
        pass
    def storeResult(self,solution,value):
        self._solution = solution
        self._value = value
    def storeExpResult(self, results):
        self._bestSolution = results[0]
        self._bestMinimum = results[1]
        self._avgMinimum = results[2]
        self._avgNumEval = results[3]
        self._sumOfNumEval = results[4]
                
    def report(self):
       print()
       print('Total number of evaluations : {0:,}'.format(self._avgNumEval))
    
class Numeric(Problem):
    def __init__(self):
        Problem.__init__(self)
       
        self._expression = ''
        self._domain = []
        
    def setVariables(self, parameters): #createProblem
        Problem.setVariables(self,parameters)
        
        # 이미 pFilename으로 파일이름을 불러왔으므로 변수만 입력하면 됨
        infile = open(self._pFileName, 'r') # file open하기, read mode
        self._expression = infile.readline()
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
        self._domain = [varNames,low,up]
    
    def randomInit(self):
        domain = self._domain
        low = domain[1]
        up = domain[2]
        init = []
        for i in range(len(low)):
            r = random.uniform(low[i],up[i]) # .uniform
            init.append(r)
        return init     # Return a random initial point
                        # as a list of values
    
    def takeStep(self, x, v):
        #현재 변수값, 함수값 전달
        grad = self.gradient(x,v)
        # x의 전체값? 다가져옴?
        xCopy = x[:]
        # maximize/minimize f by
        for i in range(len(x)):
            xCopy[i] -= self._alpha * grad[i]
            
        if self.isLegal(xCopy):
            return xCopy
        else:
            return x
             
    def gradient(self,x,v):
        grad = []
        for i in range(len(x)):
            xCopy = x[:]
            # xCopy의 편미분값? 조금 변화시킨 값
            xCopy[i] += self._dx
            df = self.evaluate(xCopy) - v
            # g = df/dx
            g = df / self._dx
            
            grad.append(g)
            
        return grad
        
    def isLegal(self,x):
        domain = self._domain
        low = domain[1]
        up = domain[2]
        for i in range(len(low)):
            l,u = low[i],up[i]
            if l <= x[i] <= u:
                pass
            else:
                return False
        
    def evaluate(self,current): 
        ## Evaluate the expression of 'p' after assigning
        ## the values of 'current' to the variables
        
        # global로 선언 할 필요 없음
        self._numEval += 1
        # 수학 식(txt 파일의 수식)
        expr = self._expression         # p[0] is function expression
        # .txt파일의 변수
        varNames = self._domain[0]  # p[1] is domain
        for i in range(len(varNames)):
            assignment = varNames[i] + '=' + str(current[i])
            exec(assignment)
        return eval(expr)
    
    def mutants(self,current): 
        neighbors = []
        for i in range(len(current)):
            mutant = self.mutate(current,i,self._delta)
            neighbors.append(mutant)
        return neighbors     #
    
    def mutate(self,current, i, d): ## Mutate i-th of 'current' if legal
        curCopy = current[:]
        domain = self._domain      # [VarNames, low, up]
        l = domain[1][i]     # Lower bound of i-th
        u = domain[2][i]     # Upper bound of i-th
        if l <= (curCopy[i] + d) <= u:
            curCopy[i] += d
        return curCopy
    
    def randomMutants(self,current):
        i = random.randint(0,len(current)-1)
        if random.uniform(0,1)>0.5:
            d = self._delta
        else:
            d = -self._delta
            
        return self.mutate(current,i,d) 
    
    ## 여기서 오류 뜸 !! 내일 해결해보기(해결)
    def describe(self): #describeProblem
        print()
        print("Objective function:")
        print(self._domain[0])   # Expression
        print("Search space:")
        varNames = self._domain[0] # p[1] is domain: [VarNames, low, up]
        low = self._domain[1][1]
        up = self._domain[2][1]
        for i in range(int(low)):
            print(" " + varNames[i] + ":", (low[i], up[i]))  
        
    def report(self):
       print()
       print("Avarage Minimun value : {0:,.3f}".format(self._avgMinimum)) 
       print('Best Solution Found')
       print(self.coordinate())
       print("Best Minimum value : {0:,.3f}".format(self._bestMinimum))
       Problem.report(self) # 부모 클래스 가져오깅
    
    def coordinate(self):
        c = [round(value,3) for value in self._bestSolution]
        return tuple(c)
       
class Tsp(Problem):
    def __init__(self):
        Problem.__init__(self)
        self._numCities = 0
        self._location = []
        self._distanceTable = []
        
    def setVariables(self,parameters): #createProblem
        ## Read in a TSP (# of cities, locatioins) from a file.
        Problem.setVariables(self,parameters)
        infile = open(self._pFileName, 'r')
        # First line is number of cities
        self._numCities = int(infile.readline())
        self._location = []
        line = infile.readline()  # The rest of the lines are locations
        while line != '':
            self._location.append(eval(line)) # Make a tuple and append
            line = infile.readline()
        infile.close()
        self._distanceTable = self.calcDistanceTable()
        
    def calcDistanceTable(self):
        table = []
        location = self._location
        for i in range(self._numCities):
            row = []
            for j in range(self._numCities):
                ## 피타고라스의 정리 이용(dx,dy의 좌표 길이 구하기)
                dx = location[i][0] - location[j][0] ## dx의 길이
                dy = location[i][1] - location[j][1] ## dy의 길이
                d = math.sqrt(dx**2 + dy**2) 
                row.append(d)
            table.append(row)
            # print('table ', table)
        return table
    
    def randomInit(self):
        n = self._numCities
        init = list(range(n))
        random.shuffle(init) # random하게 섞음
        return init
    
    
    def evaluate(self,current): 
        
        self._numEval += 1
        numCities = self._numCities
        table = self._distanceTable
        cost = 0
        for i in range(numCities-1):
            locFrom = current[i] # 시작점
            locTo = current[i+1] # 그 다음으로 이동하는 점
            cost += table[locFrom][locTo] # 다 합해줌
        cost += table[current[numCities-1]][current[0]] # 마지막 지점에서 시작점으로 다시 이동하는 거리
        ## 'p' is a Problem instance
        ## 'current' is a list of city ids
        return cost
    def mutants(self,current):
        n = self._numCities
        neighbors = []
        count = 0
        triedPairs = []
        while count <= n:  # Pick two random loci for inversion
            i, j = sorted([random.randrange(n) for _ in range(2)])
            if i < j and [i, j] not in triedPairs:
                triedPairs.append([i, j])
                curCopy = self.inversion(current, i, j) ## i, j번째 current 바꿔치기
                count += 1
                neighbors.append(curCopy)
        return neighbors
    
    def inversion(self, current, i, j):  ## Perform inversion 
        curCopy = current[:]
        while i < j:
            curCopy[i], curCopy[j] = curCopy[j], curCopy[i]
            i += 1
            j -= 1
        return curCopy
    
    def randomMutants(self, current): # Apply inversion
        while True:
            i, j = sorted([random.randrange(self._numCities)
                        for _ in range(2)])
            if i < j:
                curCopy = self.inversion(current, i, j)
                break
        return curCopy

    def displaySetting():
        print()
        print("Search algorithm: First-Choice Hill Climbing")

    def describe(self): #describeProblem
        print()
        n = self._numCities
        print("Number of cities:", n)
        print("City locations:")
        locations = self._location
        for i in range(n):
            print("{0:>12}".format(str(locations[i])), end = '')
            if i % 5 == 4:
                print()
                    
    def report(self):
        print()
        print('Average tour cost : {0:,}'.format(round(self._avgMinimum)))
        print("Best of best order of visits:")
        self.tenPerRow()       # Print 10 cities per row
        print("Minimum tour cost: {0:,}".format(round(self._bestMinimum)))
        print()
        print('Total number of evaluations : {0:,}'.format(self._numEval))

    def tenPerRow(self):
        for i in range(len(self._solution)):
            print("{0:>5}".format(self._solution[i]), end='')
            if i % 10 == 9:
                print()