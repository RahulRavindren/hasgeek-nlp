#-*- author: Rahul Ravindran
#-*- coding:UTF-8
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
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
		cnt_vector = CountVectorizer()
		cnt_vector.fit_transform(document)
		freq_term_matrix = cnt_vector.transform()
		return freq_term_matrix
	
	def  tfidfvector(self,f_matrix):
		tfidfObject = TfidfTransformer(norm = "12")
		return tfidfObject.fit(f_matrix)

	