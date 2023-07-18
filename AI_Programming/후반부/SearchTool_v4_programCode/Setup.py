class Setup:
    def __init__(self):
        self._delta = 0.0
        self._alpha = 0.0
        self._dx = 0
        self._aType = 0
        
    # parameter라는 dictionary에 필요한 변수 다 넣어놨음
    def setVariables(self,parameters):
        self._aType = parameters['aType']
        self._delta = parameters['delta']
        self._alpha = parameters['alpha']
        self._dx = parameters['dx']
        
    def getAtype(self):
        return self._aType
        