#TWE-2 Readme
Topical Word Embedding Model #2

##Requirements
**Please got the following installed:**

* python2
* numpy
* scipy
* cython
* gensim
 

##Usage

####1. Get the [gibbslda++](http://gibbslda.sourceforge.net), run it and get the tassign file and the wordmap.txt
####2. Use the command: `python train.py wordmap_filename tassign_filename` to run the TWE-2
####3. Output file are under the directory `output`: `vectors.txt`,`log.txt`


##Output Format

* #### `log.txt` : each line is as follows:
`word word's_id topic's_id ID frequency`
	* word : word
	* word's_id : word's id in the wordmap
	* topic's_id : the topic's id
	* ID : we assign each (word, topic) as unique id
	* frequency : the frequency of pair (word, topic)

* #### `vectors.txt` : each line is as follows: 
`ID value#1 value#2 ... value#n` : the (word, topic) with id of ID's vector is `(value#1, value#2 ... value#n)`