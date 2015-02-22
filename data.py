import nltk
from nltk.tokenize.punkt import PunktSentenceTokenizer as st
import csv,re
from bs4 import BeautifulSoup

class StatPreProcessing():
	"""
	Pre Processing applied on the data coming from a post.
	The noise removed are html tags and stop words.

	"""
	def nounExtractor(self,sentence):

		tokenizedText = nltk.word_tokenize(sentence)
		posTagSentence = nltk.pos_tag(tokenizedText)
		for t in posTagSentence:
			if((t[1]== 'NNP') & (t[1] == 'NN')):
					nounSentence = posTagSentence
		return nounSentence
	def tagSentenceDump(self,sent_tokenize):
		return
class DataStripper():		
		"""
		Returns data in dictionary format 
		key: title of the job post
		value : The job post content

		""" 
		def __init__(self):
			self.jobtitles = []
			self.jobPostBody = []
		
		def dataFileStripper(self,filePath):
			with open(filePath,'rw') as file:
				reader  = csv.reader(file,delimiter=',')
				for row in reader:
					self.htmlTagStripper(row[2])
					#self.tagCleanedrow3.append(temprow3)
					# temprow2 = self.htmlTagStripper(row[2])
					# self.tagCleanedrow2.append(temprow2)
		def htmlTagStripper(self,data):
			"""
			Strips any html tags using regex
			Crude way of adopting instead of using a heavy library like Beautifulsoup 
			"""
			soup = BeautifulSoup(data)
			for t in soup.findAll(text=True):
					self.jobtitles.append(t.encode('utf-8'))
			#tagList = ["p","li","a"]
			# soup = BeautifulSoup(data);
			# for tag in tagList:
			# 	soup.findAll(tag)
			# 	tag.attrs = None
			# self.clean.append(soup)
					
		def DictDataFormat(self,x,y):
			return {x:y}

