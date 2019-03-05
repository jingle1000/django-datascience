import numpy as np
import matplotlib.pyplot as plt

def graph_function(equationString, minX, maxX, stepValue):
  xAxis = np.arange(minX, maxX, stepValue)
  yAxis = []
  fig, axes = plt.subplots()
  for data_point in xAxis:
    x = data_point
    y = eval(equationString)
    yAxis.append(y)
  axes.plot(xAxis, yAxis)
  plt.show()
  
graph_function("(.001*(-5*x**3-2*x**2+3*x)/(2/10))", -10, 10, 1)
