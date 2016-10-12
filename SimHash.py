# -*- coding: utf-8 -*-
import jieba
import sys
import numpy as np
reload(sys)
sys.setdefaultencoding('utf8')



def jiebasplit(strtext):
    seg=jieba.cut(strtext,cut_all=False)

    return list(seg)


def RSHash(strtext):
    b=378551
    a=63689
    h=0


    for i in range(len(strtext)):

        h=h*a+ord(strtext[i])
        a=a*b

    return h


def JSHash(strtext):
    h=(2**64)-1
    for i in range(0,len(strtext)-2,3):
        temp=(ord(strtext[i])*ord(strtext[i+1])*ord(strtext[i+2]))**4
        h^=((h<<20)+temp+(h>>2))
    num=len(bin(h))-66
    return h>>num

def simhash(text):
    wordlist=jiebasplit(text)
    wordhash={}
    for word in wordlist:
        if word in wordhash:
            wordhash[word]+=1
        else:
            wordhash[word]=1
    sumh=np.zeros(64)
    for word in wordlist:
        jshash=JSHash(str(word))
        htable=[]
        for i in range(2, len(bin(jshash))):
            htable.append(bin(jshash)[i])

        tempht=map(lambda x: wordhash[word] if int(x)>0 else -wordhash[word],htable)
        sumh=sumh+np.array(tempht)

    sumh=map(lambda x: 1 if x>0 else 0,sumh)

    return sumh










if __name__ =="__main__":

    #print RSHash("人们特别好")
    a='特别'
   # print len(a)
    simhash(a)
   # print('kkk',JSHash(a))
    # print bin(JSHash(a)>>25)
    # print len(bin(JSHash(a)))


















