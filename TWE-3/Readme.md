#TWE-3 Readme
Topical Word Embedding Model #3

##Requirements
**Please got the following installed:**

* python2
* numpy
* scipy
* cython
* gensim
 

##Usage

####1. Get the [gibbslda++](http://gibbslda.sourceforge.net), run it and get the tassign file and the wordmap.txt
####2. Use the command: `python train.py wordmap_filename tassign_filename` to run the TWE-3
####3. Output file are under the directory `output`: `word_vector.txt` and `topic_vector.txt`


##Output Format

* #### `word_vector.txt` : each line is as follows:
`word value#0 value#1 ... value#n`**: the word's vector is (value#1, value#2...value#n)**

* #### `topic_vector.txt` : each line is as follows:
`value#0 value#1 ... value#n` **: ith(from 0...) line means the ith topic's vector is (value#0, value#1...)**
