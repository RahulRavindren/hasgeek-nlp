#-*- author: Rahul Ravindran
#-*- coding:UTF-8
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import SVC
import numpy as np

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
        self.document = document
        vocab=['python','js','android','php','django','javascript','oracle','ruby','rails','java']
        cnt_vector = CountVectorizer(vocabulary=vocab)
        freq_term_matrix = cnt_vector.fit_transform(self.document)
        return freq_term_matrix.toarray()

    def tfidfvector(self,f_matrix):
        """
        This creates a sparse matrix format of document frequency.
        input : countFreq matrix
        output : (np array of the sentence,sparse csr_matrix type)
        """
        tfidfObject = TfidfTransformer(norm="l2")
        tfidfMatrix = tfidfObject.fit_transform(f_matrix)
        tfidfMatrixTemp = tfidfMatrix.toarray()
        y_label=[]
        for x in tfidfMatrixTemp.tolist():
            ylabel_temp = []
            for i,y in enumerate(x) :
                if(y != 0.0):
                    ylabel_temp.append(i)
            y_label.append(ylabel_temp)  
        return (tfidfMatrix,y_label)

    def MultiLabelClassifier(self,xNpArray,yNpArray):
        """
        multilabelclassfier for the multilabel componet
        input : document x, y_label corresponding to it
        ouput : fit transform for the classifier
        """
        self.classifierObject = OneVsRestClassifier(SVC(kernel ='linear',probability = True))
        self.classifierObject.fit(xNpArray,yNpArray)

    def SimilarityRankingComponent(self,objectTemp):
        for document in objectTemp:
            self.ObjI_count = countFreq(document)
        return 
  






