import numpy as np
import random
import math

k = 3
np.random.seed(0)

x = np.random.permutation(10)
y = np.random.permutation(10)
coordinates = []

for count in range(10):
    coordinates.append([x[count], y[count]])
#print(coordinates)

xc = np.random.permutation(10)
yc = np.random.permutation(10)
#centeroid = []

for count in range(k):
    centeroid.append([xc[count], yc[count]])
print(centeroid)

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

c = findClosestCenteroid([8, 9])
print(c)
