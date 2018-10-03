import numpy as np
import random, math, copy, time, sys
import matplotlib
#matplotlib.use("macosx")
import matplotlib.pyplot as plt
import matplotlib.animation as anim
import itertools
from bokeh.plotting import figure 
from bokeh.io import show
from bokeh.palettes import Colorblind7

print("Program starting")
k = 3
n = 100
r = 40

k = int(sys.argv[1])
n = int(sys.argv[2])
r = int(sys.argv[3])
plt.ion()

xpoints = []
ypoints = []
cpoints = []
xcpoints = []
ycpoints = []

########################################################################################
# initiating the coordinates
########################################################################################
np.random.seed(2)
x = np.random.permutation(n)
y = np.random.permutation(n)
coordinates = []
clusters = []
for count in range(n):
    coordinates.append([x[count], y[count], 1])

########################################################################################
# initiating the centroids
########################################################################################
xc = np.random.permutation(n)
yc = np.random.permutation(n)
centeroid = []
for count in range(k):
    centeroid.append([xc[count], yc[count]])

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
    global finishFlag
    oldCenteroid = copy.deepcopy(centeroid)
    for count in range(k):
        sumX = 0
        sumY = 0
        for point in clusters[count]:
            sumX = sumX + point[0]
            sumY = sumY + point[1]
        centeroid[count] = [sumX / len(clusters[count]), sumY / len(clusters[count])]
    if oldCenteroid == centeroid:
        print("k-means cluster is stablized")
        time.sleep(1)
        print("closing the program...")
        time.sleep(1)
        #exit()
        finishFlag = 1


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
# main algorith
########################################################################################
def update():
    assignCoordinatesToCentroids()
    groupingIntoClusters()
    updateCentroids()

########################################################################################
# drawing the clusters in ASCII
########################################################################################
def drawASCII():
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

########################################################################################
# drawing the clusters in matlablib
########################################################################################
def drawMatlibplot():
    global xpoints
    global ypoints
    global cpoints
    global xcpoints
    global ycpoints

    xpoints = []
    ypoints = []
    cpoints = []
    for cluster in clusters:
        for point in cluster:
            xpoints.append(point[0])
            ypoints.append(point[1])
            cpoints.append(point[2])
    plt.scatter(xpoints, ypoints, c=cpoints)
    plt.scatter(xcpoints, ycpoints, c="r")
    plt.pause(1)
    plt.draw()
    plt.clf()

    xcpoints = []
    ycpoints = []
    for point in centeroid:
        xcpoints.append(point[0])
        ycpoints.append(point[1])
    plt.scatter(xpoints, ypoints, c=cpoints)
    plt.scatter(xcpoints, ycpoints, c="r")
    plt.pause(1)
    plt.draw()
    plt.clf()

########################################################################################
# drawing the clusters in bokeh
########################################################################################
def drawBokeh():
    global xpoints
    global ypoints
    global cpoints
    global xcpoints
    global ycpoints

    xpoints = []
    ypoints = []
    xcpoints = []
    ycpoints = []
    colors = []

    for cluster, color in zip(clusters, itertools.cycle(Colorblind7)):
        for point in cluster:
            xpoints.append(point[0])
            ypoints.append(point[1])
            colors.append(color)

    for point in centeroid:
        xcpoints.append(point[0])
        ycpoints.append(point[1])

    p.circle(xcpoints, ycpoints, size=15, fill_color="red", line_color=None)
    p.triangle(xpoints, ypoints, size=((100 / n) + 10), fill_color=colors, line_color=None)


########################################################################################
# main function
########################################################################################
ps = []
finishFlag = 0

for count in range(r):
    clusters = []
    update()

    if (finishFlag == 1):
        print("finish cycle")
        break

    p = figure(width=500, height=500, title="Frame: " + str(count))

    drawBokeh()
    ps.append(p)
    show(ps[count])

        






