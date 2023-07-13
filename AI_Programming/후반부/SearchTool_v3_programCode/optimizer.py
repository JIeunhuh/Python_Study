from Setup import Setup
# from problem import *

class HillClimbing(Setup):
    def __init__(self):
        Setup.__init__(self)
        self._pType = 0
        self._limitStuck = 100
        
    def run(self):
        pass
    
    def displaySetting(self):
        if self._pType == 1:
            print()
            print('Mutation step size :',self._delta)    
            
    def setvariables(self, pType):
        self._pType = pType
        
            
    
class SteepestAscent(HillClimbing):
    
    ## 상속받아서 안써도 됨(안쓰면 부모 클래스의 생성자 가져옴)
    # def __init__(self):
    #     HillClimbing().__init__()
        
    def run(self,p):
        
        # 초기값 랜덤으로 정함
        current = p.randomInit() # 'current' is a list of values
        valueC = p.evaluate(current)
        while True:
            neighbors = p.mutants(current)
            successor, valueS = self.bestOf(p,neighbors)
            if valueS >= valueC:
                break
            else:
                current = successor
                valueC = valueS
        
        p.storeResult(current,valueC)
    
    def bestOf(self,p,neighbors): ###
        best = neighbors[0]
        bestValue = p.evaluate(best)
        # 1번째 index부터 시작
        for i in range(1,len(neighbors)):
            newVal = p.evaluate(neighbors[i])
            if(newVal < bestValue):
                bestValue = newVal
                best = neighbors[i]
        return best, bestValue
    
    def displaySetting(self):
        print()
        print('Search Algorithm : Steepest - Ascent Hill Climbing')
        # HillClimbing.displaySetting(self)
        
class FirstChoice(HillClimbing):
        
    def run(self, p):
        current = p.randomInit()   # 'current' is a list of values
        valueC = p.evaluate(current)
        i = 0
        while i < self._limitStuck:
            successor = p.randomMutants(current)
            valueS = p.evaluate(successor)
            if valueS < valueC:
                current = successor
                valueC = valueS
                i = 0              # Reset stuck counter
            else:
                i += 1
        p.storeResult(current,valueC)
    
    def displaySetting(self):
        print()
        print('Search Algorithm : FirstChoice Hill Climbing')
        HillClimbing.displaySetting(self)
        print('Max evaluations with no improvement : {0:,}'.format(self._limitStuck))

    
class GradientDescent(HillClimbing):    
    
    def run(self,p):
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
        p.storeResult(current,valueC)
    
    def displaySetting(self):
        print()
        print('Search Algorithm : Gradient Descent Hill Climbing')
        print('Update rate :', self._alpha)
        print('Increment for calculating derivatives :', self._dx)