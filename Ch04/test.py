import bayes
import numpy

listOPosts,listClasses = bayes.loadDataSet()
myVocabList = bayes.createVocabList(listOPosts)
# print(myVocabList)
# print(bayes.setOfWords2Vec(myVocabList,listOPosts[1]))

trainMat=[]
for postinDoc in listOPosts:
    trainMat.append(bayes.setOfWords2Vec(myVocabList,postinDoc))

p0V,p1V,pAb=bayes.trainNB0(trainMat,listClasses)
print(p0V)
print(p1V)
print(pAb)