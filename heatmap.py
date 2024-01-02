import random
import math

def generateHeatmap(rows, cols, seed, nodes, distanceChecked):
    random.seed(seed)
    matrix = [[0 for _ in range(rows)] for _ in range(cols)] #generate a matrix of 0s
    nodeLocations = distributeNodes(rows,cols,nodes) #gets list of node locations
    for row in range(rows):
        for col in range(cols):
            matrix[row][col] = calculateDistance(str(row) + "," + str(col),nodeLocations,distanceChecked) 
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
            scaled_distance = 1 / (distance + 1)
            totalDistance += scaled_distance

    return float("{:.2f}".format(totalDistance)) #set maximum numbers after decimal to 2.

def main():
    rows, cols = 25, 25
    nodes = 10                #debug, testing parameters
    distanceChecked = 5
    seed = 123

    heatmapData = generateHeatmap(rows, cols, seed, nodes, distanceChecked)    #debug, prints heatmap
    for row in heatmapData:
        print(row)

if __name__ == "__main__":
    main()