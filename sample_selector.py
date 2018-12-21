#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
import numpy as np
from scipy.stats import truncnorm

class SampleSelector:

    def __init__(self, sampleSize, domain):
        self.sampleSize = sampleSize
        self.domain = domain - 1

    def getNewSampleSet(self):
        mean = np.random.randint(0, self.domain)
        std = self.domain / 0.25
        
        x = truncnorm((0 - mean)/std, (self.domain - mean)/std, loc=mean, scale=std).rvs(size=self.sampleSize)
        x = x.round().astype(int)
        return x
