import os
import resource
import pandas as pd
import numpy as np
import matplotlib as mtl
import statistics as st


class DataPreProcessing:
    path = ""

    def __init__(self, outer_path):
        self.path = outer_path

    # ==========================================================================
    # read the data and insert missing values into

    def prepareData(self):
        self.path = os.path.join(resource.__path__[0], "Dataset.xlsx")
        dataFrame = pd.read_excel(self.path)
        # check if the data is not empty
        if dataFrame.empty:
            raise Exception('Data is empty')
    # ==========================================================================

        # fill na cells with average value for each numeric columns
        for i in dataFrame.columns:
            if i != 'country':
                dataFrame[i] = dataFrame[i].fillna(dataFrame[i].mean())
    # ==========================================================================

        # Standardization to the values of the data set, currently not included the coulmns in the 'if' section
        for i in dataFrame.columns:
            if i != 'country' and i != 'year' and i != 'Standard deviation of ladder by country-year' and i != 'Standard deviation/Mean of ladder by country-year':
                dataFrame[i] = ((dataFrame[i] - dataFrame[i].mean()) / dataFrame[i].std())

        # ========== CHECKING IF THE RESULTS ARE THE RIGHT OUTCOME =================
        # out_path_normalized = os.path.join(resource.__path__[0], "normalizedDataOutputTest.xlsx")
        # with pd.ExcelWriter(out_path_normalized) as writer:
        #     dataFrame.to_excel(writer, sheet_name='Sheet1')
        # ==========================================================================

        # Combining all records under country by the years and performing average on all feature's values related to it

        grouped_df = pd.DataFrame((dataFrame.groupby(by='country', axis=0, as_index=False).mean())).drop(columns=['year'])

        # ========== CHECKING IF THE RESULTS ARE THE RIGHT OUTCOME =================
        # out_path_grouped = os.path.join(resource.__path__[0], "groupedByCountryOutPutTest.xlsx")
        # with pd.ExcelWriter(out_path_grouped) as writer:
        #     grouped_df.to_excel(writer, sheet_name='Sheet1')
        # ==========================================================================
        return grouped_df;