import numpy as np
import random
import math
import time

########################################################################################
# initiating the coordinates
########################################################################################

k = 2
n = 8
r = 5
np.random.seed(0)

x = np.random.permutation(n)
y = np.random.permutation(n)
coordinates = []
cluster = []

for count in range(n):
    coordinates.append([x[count], y[count], [1]])
#print(coordinates)

coordinates = [[1,2,1], [1,1,1], [10,2,1], [10,1,1], [10,10,1], [13,9,1], [1, 9,1], [1, 12,1]]

########################################################################################
# initiating the centroids
########################################################################################

xc = np.random.permutation(n)
yc = np.random.permutation(n)
centeroid = []

for count in range(k):
    centeroid.append([xc[count], yc[count]])
#print("original centeroid is")
#print(centeroid)

########################################################################################
# initiating the functions
########################################################################################

def getDistance(point1, point2):
    distanceX = abs(point1[0] - point2[0])
    distanceY = abs(point1[1] - point2[1])
    distance = math.sqrt(distanceX ** 2 + distanceY ** 2)
    return distance
    #print(distance)

def findClosestCenteroid(point):
    distance = []
    for count in range(k):
        distance.append(getDistance(point, centeroid[count]))
    #print(distance)
    return distance.index(min(distance))

########################################################################################
# assigning coordinates to their closest centroids
########################################################################################

def assignCoordinatesToCentroids():
    for count in range(len(coordinates)):
        coordinates[count][2] = findClosestCenteroid(coordinates[count])
        
    #print("Points are")
    #print(coordinates)

########################################################################################
# grouping the pooints into clusters
########################################################################################

def groupingIntoClusters():
    for count in range(k):
        cluster.append([])

    for count2 in range(len(coordinates)):
        for count in range(k):
            if (coordinates[count2][2] == count):
                cluster[count].append(coordinates[count2])

########################################################################################
# getting centroid for each cluster
########################################################################################

def updateCentroids():
    for count in range(k):
        sumX = 0
        sumY = 0
        for point in cluster[count]:
            sumX = sumX + point[0]
            sumY = sumY + point[1]
        #print(sump)
        centeroid[count] = [sumX / len(cluster[count]), sumY / len(cluster[count])]
    #print("New centeroids are")
    #print(centeroid)




def main():
    assignCoordinatesToCentroids()
    groupingIntoClusters()
    updateCentroids()
    

for count in range(6):
    cluster = []
    main()

    if count == 5:
        print("new clusters are")
        print(cluster)


    









