#!/usr/bin/env python2
#-*- coding: UTF-8 -*-
#File: pre_process.py
#Date: 20140810
#Author: Yang Liu <largelymfs@gmail.com>
#Description: read the tassign and the wordmap to create the training sentence_word and the
#sentence_topic

#load the id2word form the file wordmap
def load_id2word(wordmap):
    id2word = {}
    with open(wordmap) as f:
        f.readline()
        for l in f:
            try:
                word, id = l.strip().split()
            except:
                print l
            id = int(id)
            id2word[id] = word
    return id2word

#load the topic assign
def load_sentences(topic_assign, id2word):
    sentence_word = []
    sentence_topic = []
    topic_file = open("tmp/topic.file","w")
    word_file = open("tmp/word.file","w")

    with open(topic_assign) as f:
        for l in f:
            words = l.strip().split()
            tmp_sentence_word = []
            tmp_sentence_topic = []
            for word in words:
                id = 0
                try:
                    id, topic = word.split(':')
                except:
                    print word
                id = int(id)
                topic = int(topic)
                if id not in id2word:
                    continue
                word = id2word[id]
                print >> topic_file,topic,
                print >> word_file, word,
            print >>topic_file
            print >>word_file
    topic_file.close()
    word_file.close()

if __name__=="__main__":
    #first load the wordmap
    id2word = load_id2word("wordmap.txt")
    #second load the topic assignment
    sen_word, sen_topic = load_sentences("model-01600.tassign", id2word)
