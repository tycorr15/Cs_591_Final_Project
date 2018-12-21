import numpy as np
import matplotlib.pyplot as plt

from sample_selector import SampleSelector
from optimized_local_hashing import OLH
from generalized_random_response import GRR

def main():
    domain = 32
    sampleSize = 30
    epsilon = 5
    ss = SampleSelector(sampleSize, domain)
    sampleSet = ss.sampleSet
    real = getCounts(sampleSet, domain)
    grr = GRR(epsilon, domain, sampleSet)
    grrEstimate = grr.estimate
    print(sampleSet)
    print(real)

    #olh = OLH(epsilon, domain, sampleSet)
    #olhEstimate = olh.estimate
    #print(olhEstimate)

def getCounts(sampleSet, domain):
    real = np.zeros(domain + 1)
    for i in range(len(sampleSet)):
        real[int(sampleSet[i])] += 1
    return real

if __name__ == "__main__":
    main()