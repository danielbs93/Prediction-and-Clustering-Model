from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import KFold
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
import os
import resource
import pandas as pd
from sklearn import preprocessing
import numpy as np
# import matplotlib as mtl
import statistics as st

class DataPreProcessing:
    def __int__(self, path):
        self.path = path
    # read the data and insert missing values into
    def prepareData(self):
        self.path = os.path.join(resource.__path__[0], "Dataset.xlsx")
        dataFrame = pd.read_excel(self.path)
        # check if the data is not empty
        if dataFrame.empty:
            raise Exception('Data is empty')
        # fill na cells with average value for each numeric columns
        for i in dataFrame.columns:
            if i != 'country':
                dataFrame[i] = dataFrame[i].fillna(dataFrame[i].mean())
        standardization = preprocessing.StandardScaler
        # numOfNull = dataFrame.apply(lambda x: sum(x.isnull()), axis=0)
        # print(dataFrame.apply(lambda x: sum(x.isnull()), axis=0))




