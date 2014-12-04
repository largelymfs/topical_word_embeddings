#!/usr/bin/env python2
#-*- coding: UTF-8 -*-
#File:
#Date:
#Author: Yang Liu <largelymfs@gmail.com>
#Description:


if __name__=="__main__":
    with open("test.log","w") as logout, open("result.out") as f, open("result.out.out","w") as fout, open("log.txt") as log:
        #log loading
        content2id = {}
        id2word = {}
        for l in log:
            word, word_number, topic_number, content_id, _ = l.strip().split()
            word_number = int(word_number)
            topic_number = int(topic_number)
            content_id = int(content_id)
            content2id[(word_number, topic_number)] = content_id
            id2word[word_number] = word
        print "LOADING COMPLETED"
        for (line_num, l) in enumerate(f):
            word1, topic1, word2, topic2, score = l.strip().split()
            word1 = int(word1)
            topic1 = int(topic1)
            word2 = int(word2)
            topic2 = int(topic2)
            try:
                content1 = content2id[(word1, topic1)]
                content2 = content2id[(word2, topic2)]
            except:
                print line_num
                continue
            print >> fout, content1, content2, score
            print >>logout, id2word[word1], id2word[word2]
