#!/usr/bin/env python2
#-*- coding: UTF-8 -*-
#Author: Yang Liu <largelymfs@gmail.com>
#Description: Topical Word Embedding TWE-2 

def generate(input_filename, output_filename, logfile, id2word):
    word_label = 0
    content2id = {}
    id2content = {}
    id2number = {}
    with open(input_filename) as input:
        with open(output_filename,"w") as output:
            with open(logfile, "w") as log:
                for l in input:
                    words = l.strip().split()
                    for w in words:
                        word_number, topic_number = w.split(':')
                        word_number = int(word_number)
                        topic_number = int(topic_number)
                        if (word_number, topic_number) not in content2id:
                            content2id[(word_number, topic_number)] = word_label
                            id2content[word_label] = (word_number, topic_number)
                            word_label +=1
                        now_id = content2id[(word_number, topic_number)]
                        print >>output, now_id,
                        if now_id not in id2number:
                            id2number[now_id] = 1
                        else:
                            id2number[now_id]+=1
                    print>>output
                #generate the logfile
                res = []
                for (k, v) in content2id.items():
                    word_number = k[0]
                    topic_number = k[1]
                    content_id = v
                    if word_number not in id2word:
                        continue
                    word = id2word[word_number]
                    if content_id not in id2number:
                        continue
                    freq = id2number[content_id]
                    res.append((word, word_number, topic_number, content_id, freq))
                    
                res = sorted(res, cmp=lambda x, y:(-cmp(x[4], y[4])))
                for (word, word_number, topic_number, content_id, freq) in res:
                    print >> log, word, word_number, topic_number, content_id, freq
    return content2id, id2content, id2number
def load_wordmap(word_map_filename):
    id2word = {}
    word2id = {}
    with open(word_map_filename) as f:
        f.readline()
        for l in f:
            words, id = l.strip().split()
            id = int(id)
            word2id[words] = id
            id2word[id] = words
    return word2id, id2word

def gen(filename):
    s = []
    with open(filename) as f:
        s = [l.strip().split() for l in f]
    return s
if __name__=="__main__":
    import sys
    if len(sys.argv)!=3:
        print "USAGE : python train.py wordmap train_t"
        sys.exit(1)
    word_map_filename = sys.argv[1]
    word2id, id2word = load_wordmap(word_map_filename)
    import gensim
    print "Generate the temp file...",
    generate(sys.argv[2], "tmp/train.txt","output/log.txt", id2word)
    print "finish!"
    sentences = gensim.models.word2vec.LineSentence("tmp/train.txt")
    w = gensim.models.Word2Vec(sentences,size=400, workers=8)
    w.save_word_vectors("output/vectors.txt")
