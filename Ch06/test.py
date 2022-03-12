import svmMLiA
import numpy

dataArr,labelArr = svmMLiA.loadDataSet('testSet.txt')
# print(dataArr)
b,alphas=svmMLiA.smoSimple(dataArr,labelArr,0.6,0.001,40)

# print("-----------------------------------")
# print(b)
# print(alphas[alphas>0])

numpy.shape(alphas[alphas>0])
for i in range(100):
    if alphas[i]>0.0:
        print(dataArr[i],labelArr[i])