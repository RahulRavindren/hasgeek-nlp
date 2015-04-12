#-*- author: Rahul Ravindran
#-*- coding:UTF-8
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import Orange

class FeatureExtraction():
	"""
	Feature extraction for both post.title as well as post.body
	"""
	def __init__(self):
		return

	def countFreq(self,document):
		"""
		 this function creates a freq count vector of the common words in a document.
		 input:
		 document : lines from the corpora
		"""
		vocab=['python','js','android','php','django','javascript','oracle','ruby','rails','java']
		cnt_vector = CountVectorizer(vocabulary=vocab)
		freq_term_matrix = cnt_vector.fit_transform(document)
		return freq_term_matrix.toarray()
	
	def  tfidfvector(self,f_matrix):
		tfidfObject = TfidfTransformer(norm = "l2")
		return tfidfObject.fit_transform(f_matrix)

	def multilabelClassifier(self,freq_term_matrix):
		"""
		This is acheived using binary relevance algorithm.
		input : Table format of data ( freq matrix)
		output : 
		"""
		dataTable = Orange.data.Table(freq_term_matrix)
		# learner = Orange.multilabel.BinaryRelevanceLearner()
		# classifier = learner(dataTable)
		# pprint (classifier(dataTable[0]))

        
    
    
  
