import logRegres
from numpy import *

dataArr,labelMat=logRegres.loadDataSet()
# weight=logRegres.gradAscent(dataArr,labelMat)
# print(weight.getA())
# logRegres.plotBestFit(weight.getA())
weight=logRegres.stocGradAscent1(array(dataArr),labelMat)
logRegres.plotBestFit(weight)

