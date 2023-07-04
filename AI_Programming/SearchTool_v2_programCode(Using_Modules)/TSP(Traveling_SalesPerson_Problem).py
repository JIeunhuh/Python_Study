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