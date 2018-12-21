import numpy as np
import matplotlib.pyplot as plt

from sample_selector import SampleSelector
from optimized_local_hashing import OLH
from generalized_random_response import GRR

def main():
    createGraphs()

def getCounts(sampleSet, domain):
    real = np.zeros(domain)
    for i in range(len(sampleSet)):
        real[int(sampleSet[i])] += 1
    return real

def createGraphs():
    
    domain = [2, 8, 32, 256, 1024]
    l1_grr = []
    l1_olh = []
    
    for d in domain:
        ss = SampleSelector(1000, d)
        sampleSet = ss.getNewSampleSet() 
        real = getCounts(sampleSet, d)
        grr = GRR(2, d, sampleSet)
        grrEstimate = grr.estimate
        olh = OLH(2, d, sampleSet)
        olhEstimate = 2*(olh.estimate)
        l1_grr.append(np.linalg.norm((np.array(real) - np.array(grrEstimate)), ord=1))
        l1_olh.append(np.linalg.norm((np.array(real) - np.array(olhEstimate)), ord=1))
        
    
    grr_plot, = plt.plot(domain, l1_grr, '--o', label = 'GRR')
    olh_plot, = plt.plot(domain, l1_olh, '--o', label = 'OLH')
    plt.legend(handles=[grr_plot, olh_plot])
    plt.title('L1-error vs Domain Size')
    plt.ylabel('L1-error')
    plt.xlabel('Domain Size')
    plt.grid()
    plt.show()
    plt.close()

if __name__ == "__main__":
    main()
