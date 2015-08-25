'''
Created on Aug 24, 2015
@author: Ali Ilyas
'''
from fileinput import filename

'''
Using feed-forward neural network. No hidden Layers, simple classifier. Single dimensioned data
'''

import datetime
import os
import pickle

from pybrain.datasets            import ClassificationDataSet
from pybrain.structure.modules   import SoftmaxLayer
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.tools.shortcuts     import buildNetwork
from pybrain.utilities           import percentError
import numpy as np

log_filename                            = "\logging\log.txt";
bootstrapped_file_name_training         = "\sample_files\\bootstrapped\\bootstrap_training_set40_60";
bootstrapped_file_name_testing          = "\sample_files\\bootstrapped\\bootstrap_testing_set40_60";
original_file_name_training             = "\sample_files\originalfile\\original_training_set40_60";         
original_file_name_testing              = "\sample_files\\originalfile\\original_testing_set40_60";         
working_dir                             = "";

def ann(training_filename , testing_filename,itr,epoch,model_type):
    training_start_time = "The generation of data set and training started at :%s" % datetime.datetime.now()
    training_dataset            = np.genfromtxt(training_filename, skip_header=0,dtype="int", delimiter='\t' )
    data = ClassificationDataSet(len(training_dataset[0])-1, 2, nb_classes=2)
    for aSample in training_dataset:
        data.addSample(aSample[0:len(aSample)-1],[aSample[len(aSample)-1]] );
        
    #  
    data._convertToOneOfMany( )

    fann = buildNetwork(314,2,outclass=SoftmaxLayer);
    trainer = BackpropTrainer( fann, dataset=data, momentum=0.1, verbose=False, weightdecay=0.01)
    counter = 0;
    print training_start_time
    while(counter < itr):
        trainer.trainEpochs( epoch );
        counter = counter + 1;
    
    trnresult = percentError( trainer.testOnClassData(),data['class'] )
    trained_result_log = "epoch: %4d" % trainer.totalepochs, \
          "  train error: %5.2f%%" % trnresult;
    
    
    training_time_end = "The training and result logging ended at %s :" % datetime.datetime.now()
    
    filename = working_dir + "\models\\"+model_type + ".obj"
    save_trained_model(fann, filename)
    
    log_file.write("\n" + training_start_time+"\n")
    log_file.write(str(trained_result_log)+"\n")
    log_file.write(training_time_end+"\n")

    

    
    
    

def save_trained_model(model , filename):
    filemodel_saved =  "Saving the model at :  %s"%filename;
    fileObject = open(filename, 'w')
    pickle.dump(model, fileObject)
    fileObject.close()
    print filemodel_saved;
    log_file.write(filemodel_saved)

def test_trained_model(filename,training_filename):
    fileObject      = open(filename,'r')
    fann            = pickle.load(fileObject)
    testing_dataset            = np.genfromtxt(training_filename, skip_header=0,dtype="int", delimiter='\t' )
   
    data = ClassificationDataSet(len(testing_dataset[0])-1, 2, nb_classes=2)
    for aSample in testing_dataset:
        data.addSample(aSample[0:len(aSample)-1],[aSample[len(aSample)-1]] );
        
    #  
    data._convertToOneOfMany( )
    test = BackpropTrainer( fann, dataset=data, momentum=0.1, verbose=False, weightdecay=0.01)
    
    trnresult = percentError( test.testOnClassData(),data['class'] )
    results = "Train error on testing data : %5.2f%%"  % trnresult;
    log_file.write(results + "  , The length of data " + str(len(data)))
    print results




def main():
    global working_dir 
    global log_file
    working_dir =  os.path.dirname(os.path.abspath(""))
    file_trn    = working_dir+ original_file_name_training+".txt";
    file_tst    = working_dir+original_file_name_testing+".txt";
    model_type = "bootstrap60_40"
    testing_independent = True
    
    log_file = open(working_dir+log_filename, 'a')
    log_file.write("\n-------------- Neural Network -----------------\n");
    if(testing_independent != True):
        ann( file_trn, file_tst,10,5,model_type);
    
    if(testing_independent):
        log_file.write("Testing independent dataset on " + model_type);
        ind_test_set = working_dir+"\sample_files\\originalfile\\ind_dataset.txt";
        test_trained_model(working_dir +"\models\\"+model_type+".obj",file_tst);


    else:
        test_trained_model(working_dir +"\models\\"+model_type+".obj",file_tst);
    
    log_file.close()
    
if __name__ == "__main__":
    main();    