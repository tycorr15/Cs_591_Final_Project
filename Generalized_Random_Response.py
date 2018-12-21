# -*- coding: utf-8 -*-
"""
@author: durusarv, jdlips, tycorr (Duruvan Sarvanan, Jake Lipson and Tyler Correll)
"""

import numpy as np
import math

class GRR:

    def __init__(self, epsilon, domain, data):

        self.data = data
        self.d = domain
        self.epsilon = epsilon
        self.p = math.exp(self.epsilon) / (math.exp(self.epsilon) + self.d - 1)
        self.q = 1 / (math.exp(self.epsilon) + self.d - 1)

        self.numUsers = len(data)
        self.estimate = np.zeros(self.d)
        self.perturbed = np.zeros(self.numUsers)

        self.pi()
        self.aggregator()

    def pi(self):
        for i in range(self.numUsers):
            coin = np.random.random()
            if coin <= self.p:
                self.perturbed[i] = self.data[i]
            else:
                temp = np.random.randint(0, self.d)
                while (temp == self.data[i]):
                    temp = np.random.randint(0, self.d)
                self.perturbed[i] = temp

    def aggregator(self):
        for i in range(self.numUsers):
            self.estimate[int(self.perturbed[i])] += 1
        for i in range(len(self.estimate)):
            self.estimate[i] = self.estimate[i] * self.p + (self.numUsers - self.estimate[i]) * self.q
            self.estimate[i] = (self.estimate[i] - (self.numUsers * self.q)) / (self.p - self.q)
