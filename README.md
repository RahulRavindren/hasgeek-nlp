Hasgeek Tag Recommendation model for predicting tags for Job posts
=====

The process has two phases :

*Model Building Phase
*Tag Prediction Phase

Model Building Phase
--------------------

The steps involed in this phase are :

* Multi Label Classifier 
	This involves building a multi label classifier for prediction of multiple tags for a particular document(job post here). This gives the score of the of a particular software term in a document. With these we build a ranking component to rank top best tags in a particular document. This feature is used to build a linear SVM model.

* TF-IDF vectors 
	In this step, we build term frequency and document frequency sparse matrix vectors for predicting the frequency of occurence of the tags. This works with a pre-defined dictionary. The dictionary can be updated for more new tags.

* Term tag affinity
	This step gives affinity score of a tag with tags of the same name. Example, "PHP"->"PHP5" . Here both tags mean the same. And hence the score doesn't add up if both the tags are present in the same document.
