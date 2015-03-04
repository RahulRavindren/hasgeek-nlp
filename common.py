#-*- author:Rahul Ravindran
#-*- coding:UTF-8
from nltk import FreqDist
class CommonFunctions():
	"""
	CommonFunctions for the language module
	"""

	def freqDistribution(self,tokenizedWords):
		"""
		Calculate frequency distribution of words in the corpora
		input : array of tokenized words 
		"""
		self.fdist = FreqDist(tokenizedWords)
		print self.fdist
	
	def histogramPlot(self):
		"""
		Histogram plot of the most frequent words in the corpora.
		"""
		
		return 