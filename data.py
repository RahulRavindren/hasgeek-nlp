#-*- author:Rahul Ravindran
#-*- coding:UTF-8
import nltk
from nltk.tokenize.punkt import PunktSentenceTokenizer as st
from nltk.corpus import stopwords
import csv,pickle
from bs4 import BeautifulSoup

class StatPreProcessing():
	"""
	Pre Processing applied on the data coming from a post.
	noise removed : html tags,stop words

	"""
	def __init__(self):
		self.nounSentence = []
		self.dictClean = []
	
	def nounExtractor(self,sentence):
		self.tokenizedText = nltk.word_tokenize(sentence)
		posTagSentence = nltk.pos_tag(self.tokenizedText)
		for t in posTagSentence:
			if(t[1]== "NNP"):
				self.nounSentence.append(posTagSentence)						
	
	def stopWordFilter(self):
		stop = stopwords.words('english')
		for i in self.nounSentence:
			if i[0] not in stop:
				self.dictClean.append(i[0])	
	
	def tagSentenceDump(self,object):
		with open('data/sent_job_title.tab', 'wb') as file:
				pickle.dump(object,file)
		file.close()

	def loadPickleDump(self,pickleFileName):
		temp = pickle.load(open(pickleFileName,'rb'))
		return temp

	
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
					self.htmlTagStripper(row[3])
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
					self.jobPostBody.append(t.encode('utf-8'))
			#tagList = ["p","li","a"]
			# soup = BeautifulSoup(data);
			# for tag in tagList:
			# 	soup.findAll(tag)
			# 	tag.attrs = None
			# self.clean.append(soup)
					
		def DictDataFormat(self,x,y):
			return {x:y}

