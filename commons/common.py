#-*- author:Rahul Ravindran
#-*- coding:UTF-8
from nltk import FreqDist
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import numpy as np
import collections

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

  #       def MultiLabelPredict(self,document):
  #   		ftrextract = FeatureExtraction()
		# ftrextract.classifierObject.predict(document)
	
	def weight_scoring(self,nObji,nObj,tfij,dfij):
		return                


	def terms_sentences(self,matrix):
		termFreqSentence =[]
		for i in matrix.toarray():
			temp = np.nonzero(i)[0]
			termFreqSentence.append(len(temp))
		return termFreqSentence		

	def termFreq_doc(self,matrix):
		_indexArray = []
		temp = np.nonzero(matrix.toarray())[1]
		_indexFreq = collections.Counter(temp)
		return _indexFreq
