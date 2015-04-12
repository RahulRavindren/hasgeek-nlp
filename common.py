#-*- author:Rahul Ravindran
#-*- coding:UTF-8
from nltk import FreqDist
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt


class CommonFunctions():
	"""
	CommonFunctions for the language module
	"""

	def freqDistribution(self,tokenizedWords):
		"""
		Calculate frequency distribution of words in the corpora
		input : array of tokenized words 
		"""
		return FreqDist(tokenizedWords)
	
	def histogramPlot(self,fd):
		"""
		Histogram plot of the most frequent words in the corpora.
		"""
		return
	def pcaplot(self,matrix):
		"""
		PCA plot of the common freq terms in the corpora.
		Inputs - 
		matrix : count freq matrix
		"""
		pcaObject = PCA().fit(matrix)
	 	data2d = pcaObject.transform(matrix)
	 	print data2d
	 	plt.scatter(data2d[:,0],data2d[:,1])


