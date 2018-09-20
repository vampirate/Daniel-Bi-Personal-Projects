from bokeh.plotting import figure 
from bokeh.io import show


from numpy import cos, linspace
x = linspace(-6, 6, 100)
y = cos(x)

p = figure(width=500, height=500)
p.scatter(x, y)
show(p)