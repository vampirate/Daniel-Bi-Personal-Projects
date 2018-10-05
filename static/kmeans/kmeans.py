import itertools
import numpy as np
import random, math, copy, time, sys
from random import random
from bokeh.palettes import Colorblind7
from bokeh.models import CustomJS, ColumnDataSource, Slider, DataSource
from bokeh.plotting import figure, show
from bokeh.layouts import column
from bokeh.embed import file_html
from bokeh.embed import components

k = 3
n = 100
r = 40

k = int(sys.argv[1])
n = int(sys.argv[2])
r = int(sys.argv[3])

totalColors = []
totalXPoints = []
totalYPoints = []
totalXCPoints = []
totalYCPoints = []

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
# main algorith
########################################################################################
def update():
    global clusters
    global totalXPoints
    global totalYPoints
    global totalXCPoints
    global totalYCPoints
    global totalColors

    clusters = []
    xpoints = []
    ypoints = []
    xcpoints = []
    ycpoints = []
    colors = []

    assignCoordinatesToCentroids()
    groupingIntoClusters()
    updateCentroids()

    if (finishFlag == 0):
        for cluster, color in zip(clusters, itertools.cycle(Colorblind7)):
            for point in cluster:
                xpoints.append(point[0])
                ypoints.append(point[1])
                colors.append(color)

        for point in centeroid:
            xcpoints.append(point[0])
            ycpoints.append(point[1])

        totalXPoints.append(xpoints)
        totalYPoints.append(ypoints)
        totalXCPoints.append(xcpoints)
        totalYCPoints.append(ycpoints)
        totalColors.append(colors)

########################################################################################
# main function
########################################################################################
ps = []
finishFlag = 0

for countFrames in range(r):
    update()
    if finishFlag == 1:
        break
    
sourcePoint = ColumnDataSource(data=dict(x=totalXPoints[0], y=totalYPoints[0], color=totalColors[0]))
sourcePointTotal = ColumnDataSource(data=dict(xdata=totalXPoints, ydata=totalYPoints, cdata=totalColors))

sourceCentroid = ColumnDataSource(data=dict(x=totalXCPoints[0], y=totalYCPoints[0]))
sourceCentroidTotal = ColumnDataSource(data=dict(xdata=totalXCPoints, ydata=totalYCPoints))

p = figure(plot_width=600, plot_height=600)
p.circle('x', 'y', size=6 + 400/n, source=sourcePoint, alpha=0.5, fill_color="color")
p.triangle('x', 'y', size=10, source=sourceCentroid, alpha=0.7, fill_color="red")

callbackPoints = CustomJS(args=dict(s=sourcePoint, sT=sourcePointTotal), code="""
        var data = s.data;
        var frame = cb_obj.value - 1
        var x = data['x']
        var y = data['y']
        var c = data['color']

        var data2 = sT.data;
        var xdata = data2['xdata']
        var ydata = data2['ydata']
        var cdata = data2['cdata']
        for (var i = 0; i < x.length; i++) {
            x[i] = xdata[frame][i]
            y[i] = ydata[frame][i]
            c[i] = cdata[frame][i]
        }
        s.change.emit();
    """)

callbackCentroids = CustomJS(args=dict(s=sourceCentroid, sT=sourceCentroidTotal), code="""
        var data = s.data;
        var frame = cb_obj.value - 1
        var x = data['x']
        var y = data['y']

        var data2 = sT.data
        var xdata = data2['xdata']
        var ydata = data2['ydata']
        for (var i = 0; i < x.length; i++) {
            x[i] = xdata[frame][i]
            y[i] = ydata[frame][i]
        }
        s.change.emit();
    """)

slider = Slider(start=1, end=r, value=1, step=1, title="Frames")
slider.js_on_change('value', callbackCentroids, callbackPoints)
layout = column(slider, p)
#show(layout)

script, div = components(layout)
script = script[:-10]
script = script[32:]
print(div)

f = open("static/kmeans/bokehScript.js",'w')
print(script, file=f) # Python 3.x





