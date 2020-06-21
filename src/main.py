from tkinter import Tk

from src.UI import Clustering
from src.DataPreprocessing import DataPreProcessing
from src.DataClustering import DataClustering
import pandas as pd
import resource
import os

outer_path = "../resource/Dataset.xlsx"
db = DataPreProcessing(outer_path)

# try:
#     grouped_df = db.prepareData()
#     dc = DataClustering(grouped_df, 100, 3)
#     dc.runClustering()
#     # out_path_grouped = os.path.join(resource.__path__[0], "groupedByCountryOutPutTest.xlsx")
#     # with pd.ExcelWriter(out_path_grouped) as writer:
#     #     grouped_df.to_excel(writer, sheet_name='Sheet1')
#
# except Exception as err:
#     print(err)

