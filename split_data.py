import os
from shutil import copyfile
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("input")
parser.add_argument("output")
#parser.add_argument("train_size")
#parser.add_argument("val_size")
args=parser.parse_args()

#define the function
def gen_sample_data(input_dir,output_dir):
    
    #storing names of directories-these are class names
    dirs = [d for d in os.listdir(input_dir) if os.path.isdir(os.path.join(input_dir, d))]
    
    data_dir = ['train','validation','test'] #array storing train, validation names
    
    #create folders with similar class names for both train and validation in output dir
    for data_name in data_dir:
        for dir_name in dirs:
            output_path = os.path.join(output_dir,data_name,dir_name)
            if not os.path.exists(output_path):
                os.makedirs(output_path)
    
    #copying images from each class dir to train and validation class dir with sample size
    for dir_name in dirs:
        file_names=[]
        for f in os.listdir(os.path.join(input_dir,dir_name)):
            file_names.append(os.path.join(input_dir,dir_name,f))
        
        train_size= int(len(file_names)*0.7)
        
        for i in range(0,train_size):
            copyfile(file_names[i], os.path.join(output_dir,"train",dir_name,os.path.basename(file_names[i])))
            print(os.path.join(output_dir,"train",dir_name+os.path.basename(file_names[i])))
        
        val_size = int((len(file_names)-train_size)*0.5)
        
        for j in range(train_size,(train_size+val_size)):
            copyfile(file_names[j], os.path.join(output_dir,"validation",dir_name,os.path.basename(file_names[j])))
            print(os.path.join(output_dir,"validation",dir_name+os.path.basename(file_names[j])))
        
        #test_size = int(len(file_names)-train_size-val_size)
        
        for k in range((train_size+val_size),len(file_names)):
            copyfile(file_names[k], os.path.join(output_dir,"test",dir_name,os.path.basename(file_names[k])))
            print(os.path.join(output_dir,"test",dir_name+os.path.basename(file_names[k])))


gen_sample_data(args.input,args.output)
        
    
    
    
