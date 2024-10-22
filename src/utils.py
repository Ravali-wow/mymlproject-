import os 
import sys 
import numpy as np 
import pandas as pd 
from src.exception_handler import CustomException
import dill

def save_object(file_path,obj):
    try :
        dir_path=os.path.dirname(file_path)#takes folder name in which file is present
        os.makedirs(dir_path,exists_ok=True)#creates a directory if not there
        with open(file_path,"wb") as file_obj:#opens file in write binary mode
            dill.dump(obj,file_obj)#takes content of file from obj and writes it  into new file
    except Exception as e:
        raise CustomException(e,sys)