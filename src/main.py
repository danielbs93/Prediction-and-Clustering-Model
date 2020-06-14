from tkinter import Tk

from src.UI import Clustering
from src.data_preprocessing import DataPreProcessing

db = DataPreProcessing()
try:
    db.prepareData()
except Exception as err:
    print(err)

