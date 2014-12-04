#!/usr/bin/env python2
#-*- coding: UTF-8 -*-
#File: train.py
#Date: 20140810
#Author: Yang Liu <largelymfs@gmail.com>
#Description Train the topic representation using the topic model and the word2vec's skip gram

import gensim #modified gensim version
import pre_process # read the wordmap and the tassgin file and create the sentence
import sys
if __name__=="__main__":
    if len(sys.argv)!=4:
        print "Usage : python train.py wordmap tassign topic_number"
        sys.exit(1)	
    reload(sys)
    sys.setdefaultencoding('utf-8')
    wordmapfile = sys.argv[1]
    tassignfile = sys.argv[2]
    topic_number = int(sys.argv[3])
    id2word = pre_process.load_id2word(wordmapfile)
    pre_process.load_sentences(tassignfile, id2word)
    sentence_word = gensim.models.word2vec.LineSentence("tmp/word.file")
    print "Training the word vector..."
    w = gensim.models.Word2Vec(sentence_word,size=400, workers=20)
    sentence = gensim.models.word2vec.CombinedSentence("tmp/word.file","tmp/topic.file")
    print "Training the topic vector..."
    w.train_topic(topic_number, sentence)
    print "Saving the topic vectors..."
    w.save_topic("output/topic_vector.txt")
    print "Saving the word vectors..."
    w.save_wordvector("output/word_vector.txt")
