#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
import numpy as np

class SampleSelector:

    def __init__(self, sampleSize, domain):
        self.sampleSize = sampleSize
        self.domain = domain
        self.sampleSet = np.zeros(self.sampleSize)
        self.getNewSampleSet();

    def getNewSampleSet(self):
        for i in range(self.sampleSize):
            self.sampleSet[i] = random.randint(0, self.domain)


#Old Code
'''
import nltk
nltk.download('brown')
from nltk.corpus import brown

class SampleSelector:

    def __init__(self, sampleSize, category):
        self.sampleSize = sampleSize
        self.category = category
        self.sampleSet = self.getNewSampleSet()

    def getNewSampleSet(self):
        sampleSet = []
        words = brown.words(categories = self.category)
        i = 0
        while (i < self.sampleSize):
            rand = random.randint(0,len(words))
            randWord = words[rand].lower()
            while (not randWord[0].isalpha()):
                rand = random.randint(0,len(words))
                randWord = words[rand].lower()
            sampleSet.append(randWord)
            i += 1
        return sampleSet

    def setSampleSize(self, size):
        self.sampleSize = size;

    def setCategory(self, category):
        self.category = cat