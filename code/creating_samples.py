'''
Created on Aug 22, 2015

'''
from idlelib.ReplaceDialog import replace
from nt import remove
from random import randint
import random

import numpy as np
import sklearn.utils as skut


#configuration and global variables
metabolites                  =[];
samples                      =[];
samples_diseased             =[];
samples_nondiseased          =[];
bootstrapped_samples         =[];
batch_read_filename          = "batch1_final.txt";
samples_read_filename        = "samples_batch1.txt"
write_samples_file           = True;


def read_batchfile():
    global samples;
    global samples_diseased
    global samples_nondiseased
    '''
    Removed the header from the batch file, removed the sample ids.
    '''
    samples = np.genfromtxt(batch_read_filename, skip_header=1,dtype="int", delimiter='\t' );
    samples = np.delete(samples,np.s_[0:1],1)
    if write_samples_file:
        np.savetxt(samples_read_filename, samples, delimiter='\t', fmt="%s") 
    count_diseased = 0;
    count_nondiseased = 0;
    for aRow in samples:
        if aRow[len(aRow)-1] == "1":
            #samples_diseased.insert(count_diseased,aRow);
            samples_diseased.append(aRow)
            count_diseased+=1;
        else:
            #samples_nondiseased.insert(count_nondiseased,aRow)
            samples_nondiseased.append(aRow)
            count_nondiseased+=1;
    if write_samples_file:
        np.savetxt("diseased.xls", samples_diseased, delimiter='\t', fmt="%s") 
        np.savetxt("nondiseased.xls", samples_nondiseased, delimiter='\t', fmt="%s") 
    

def generate_bootstrapped_samples():
    '''
    Generating the bootstrapped samples
    
    rand_index = random.randint(0 , len(samples)-1);
    candidate_sample =  samples[rand_index];
    print candidate_sample
    resample  = skut.resample(candidate_sample,replace=False);
    print resample

    global metabolites
    size = len(samples[0]);
    count = 0
    while(count < size):
        metabolites.append( samples[:, [count]])
        count +=1;
    np.savetxt("meta.xls", metabolites, delimiter='\t', fmt="%s") 
    
    '''
    rand_index = random.randint(0 , len(samples)-1);
    candidate_sample =  samples[rand_index];
    
    print candidate_sample
    AnArray= [];
    for anInt in candidate_sample:
        AnArray.append( random.randint(anInt - (int)(anInt *0.10) ,anInt + (int)(anInt *0.10) ))
    AnArray[len(AnArray)-1] = candidate_sample[len(candidate_sample)-1]
    print AnArray;
        
    
    

def main():
    read_batchfile();
    generate_bootstrapped_samples();
    
if __name__ == "__main__":
    main();    