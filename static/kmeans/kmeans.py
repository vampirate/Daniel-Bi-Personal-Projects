import numpy as np
import random
import math
import time
import matplotlib.pyplot as plt
import matplotlib.animation as anim

########################################################################################
# initiating the coordinates
########################################################################################

k = 3
n = 200
r = 30
plt.ion()

np.random.seed(2)
x = np.random.permutation(n)
y = np.random.permutation(n)
coordinates = []
clusters = []

for count in range(n):
    coordinates.append([x[count], y[count], 1])
#print(coordinates)

########################################################################################
# initiating the centroids
########################################################################################

xc = np.random.permutation(n)
yc = np.random.permutation(n)
centeroid = []

for count in range(k):
    centeroid.append([xc[count], yc[count]])
#print(centeroid)

########################################################################################
# initiating the functions
########################################################################################

def getDistance(point1, point2):
    distanceX = abs(point1[0] - point2[0])
    distanceY = abs(point1[1] - point2[1])
    distance = math.sqrt(distanceX ** 2 + distanceY ** 2)
    return distance

def findClosestCenteroid(point):
    distance = []
    for count in range(k):
        distance.append(getDistance(point, centeroid[count]))
    return distance.index(min(distance))

########################################################################################
# assigning coordinates to their closest centroids
########################################################################################

def assignCoordinatesToCentroids():
    for count in range(len(coordinates)):
        coordinates[count][2] = findClosestCenteroid(coordinates[count])

########################################################################################
# grouping the pooints into clusters
########################################################################################

def groupingIntoClusters():
    for count in range(k):
        clusters.append([])

    for count2 in range(len(coordinates)):
        for count in range(k):
            if (coordinates[count2][2] == count):
                clusters[count].append(coordinates[count2])

########################################################################################
# getting centroid for each cluster
########################################################################################

def updateCentroids():
    for count in range(k):
        sumX = 0
        sumY = 0
        for point in clusters[count]:
            sumX = sumX + point[0]
            sumY = sumY + point[1]
        centeroid[count] = [sumX / len(clusters[count]), sumY / len(clusters[count])]

########################################################################################
# main algorith
########################################################################################

def update():
    assignCoordinatesToCentroids()
    groupingIntoClusters()
    updateCentroids()

########################################################################################
# drawing the clusters
########################################################################################

def draw():
    print("Iteration: " + str(count))
    
    printflag = 1
    for countY in range(n, -1, -1):
        for countX in range(n):
            for cluster in clusters:
                for point in cluster:
                    if (point[0] == countX) & (point[1] == countY):
                        for center in range(k):
                            if point[2] == center:
                                print(center, end=" ")
                            printflag = 2
            if printflag == 1:        
                print("_", end=" ")
            else:
                printflag = 1
        print("")
    print(" ")

def draw2():
    xpoints = []
    ypoints = []
    cpoints = []
    xcpoints = []
    ycpoints = []

    for cluster in clusters:
        for point in cluster:
            xpoints.append(point[0])
            ypoints.append(point[1])
            cpoints.append(point[2])

    for point in centeroid:
        xcpoints.append(point[0])
        ycpoints.append(point[1])
    
    plt.scatter(xpoints, ypoints, c=cpoints)
    plt.scatter(xcpoints, ycpoints, c="r")
    plt.draw()
    plt.pause(1)
    plt.clf()

########################################################################################
# show the points
########################################################################################

def showPoints():
    for cluster in clusters:
        for point in cluster:
            print(point)

def showCentroids():
    for point in centeroid:
        print(point)

########################################################################################
# main function
########################################################################################

for count in range(r):
    clusters = []
    update()
    draw2()



