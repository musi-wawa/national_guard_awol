import random
import math

def generateHeatmap(rows, cols, seed, nodes, distanceChecked, averageGoal, baseline, maximum):
    random.seed(seed)
    matrix = [[0 for _ in range(rows)] for _ in range(cols)] #generate a matrix of 0s
    nodeLocations = distributeNodes(rows,cols,nodes) #gets list of node locations
    for row in range(rows):
        for col in range(cols):
            matrix[row][col] = calculateDistance(str(row) + "," + str(col),nodeLocations,distanceChecked) 
    matrix = scaleMap(matrix, rows, cols, averageGoal, baseline, maximum)
    return matrix

def distributeNodes(rows, cols, nodes):  #returns list of coordinates of randomly placed nodes
    iterations = 0
    nodeLocations = []
    while iterations < nodes:
        x = random.randint(1,rows)  #get random row
        y = random.randint(1,cols)  #get random column
        node = str(x) + "," + str(y)
        if node in nodeLocations:
            continue
        else:
            iterations += 1
            nodeLocations.append(node) #caches node location
    return nodeLocations

def calculateDistance(pointLocation, nodeLocations, distanceChecked):
    totalDistance = 0.0
    pointX, pointY = map(int, pointLocation.split(','))

    for currentNode in nodeLocations:  # check if the point is within the specified distance range of the node
        nodeX, nodeY = map(int, currentNode.split(','))
        xDistance = abs(pointX - nodeX)
        yDistance = abs(pointY - nodeY)

        if xDistance <= distanceChecked and yDistance <= distanceChecked:
            distance = math.sqrt(xDistance**2 + yDistance**2) #complicated maths stuff. asked chatGPT to do this part for me. thank you chatGPT.
            scaledDistance = 1 / (distance + 1)
            totalDistance += scaledDistance
    if totalDistance > 1.0:
        totalDistance = 1.0
    return totalDistance
    
def scaleMap(matrix, rows, cols, goal, baseline, maximum):
    total = 0
    for row in matrix:
        total += sum(row)
    average = total / (rows * cols)
    change = goal / average  
    for row in range(rows):
        for col in range(cols):
            matrix[row][col] *= change    ##makes sure the average is happy
            if matrix[row][col] > maximum: matrix[row][col] = maximum
    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] > baseline:    #enforces baseline and rounds result
               matrix[row][col] = round(matrix[row][col]-baseline,2)   
            else: matrix[row][col] = 0
    return matrix        

def main():
    rows, cols = 25, 25
    nodes = 6                #debug, testing parameters
    distanceChecked = 25
    seed = 123
    averageGoal = 0.5     #actual goal ends up being subtracted by the minimum
    baseline = .6
    maximum = .4
    heatmapData = generateHeatmap(rows, cols, seed, nodes, distanceChecked, averageGoal, baseline, maximum)

    total = 0
    for row in heatmapData:    #print the heatmap along with the average
        total += sum(row)
        print(row)
    print(total / (rows * cols))

if __name__ == "__main__":
    main()