import trees
import treePlotter

# mydata,labels=trees.createDataSet()
# print(labels)
# qwe=trees.calcShannonEnt(mydata)
# qwe=trees.splitDataSet(mydata,0,1)
# qwe=trees.chooseBestFeatureToSplit(mydata)
# print(qwe)

# treePlotter.createPlot(trees.createTree(mydata,labels))
# treePlotter.createPlot()

# trees.storeTree(trees.createTree(mydata,labels),'classifierStorage.txt')
# print(trees.grabTree('classifierStorage.txt'))

fr=open('lenses.txt')
lenses=[inst.strip().split('\t') for inst in fr.readlines()]
labels=['age','prescript','astigamtic','tearRate']
tree=trees.createTree(lenses,labels)
print(tree)
treePlotter.createPlot(tree)