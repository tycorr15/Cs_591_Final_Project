# -*- coding: utf-8 -*-
"""
@author: durusarv, jdlips, tycorr (Duruvan Sarvanan, Jake Lipson and Tyler Correll)
"""

import numpy as np
import xxhash
import math

class OLH:

    def __init__(self, epsilon, domain, data):

        self.data = data
        self.d = domain
        self.epsilon = epsilon
        self.d_prime = int(round(math.exp(self.epsilon))) + 1
        self.p = math.exp(self.epsilon) / (math.exp(self.epsilon) + self.d_prime - 1)

        self.numUsers = len(data)
        self.perturbed = np.zeros(self.numUsers)

        self.estimate = np.zeros(self.d)

        self.pi()
        self.aggregator()

    def pi(self):

        for i in range(self.numUsers):

            hashed = (xxhash.xxh32(str(self.data[i]), seed=i).intdigest() % self.d_prime)

            if np.random.random_sample() > self.p:
                sample = np.random.randint(0, self.d_prime - 1)
                if sample >= hashed:
                    sample += 1
                self.perturbed[i] = sample
            else:
                self.perturbed[i] = hashed

    def aggregator(self):

        for i in range(self.numUsers):
            if self.perturbed[i] == (xxhash.xxh32(str(self.data[i]), seed=i).intdigest() % self.d_prime):
                self.estimate[int(self.data[i])] += 1
