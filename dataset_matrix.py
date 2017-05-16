import matplotlib
import pandas as pd

# This code reads the data set of constituents downloaded from Siblis research and converts it to a data matrix.
# The data is handled as a pandas frame, and it is saved as a .csv file. The file used is
# "S&P_500_Composition_Changes_1990_-_2017_noHeader.xlsx"
# For which the first row was removed to enable the use of headers (column names).


# Import the data from the excel file as a pandas frame.
data = pd.read_excel("D:\odrive\Personal\Maestria_Ciencias_Computacionales_INAOEP\Thesis\Datasets\S&P_500_Composition_Changes_1990_-_2017_noHeader.xlsx")
# Separate the 'Ticker', 'ISIN Code' and 'Company Name' from the composites info.
company_info = data[data.columns[0:3]]  # The info about the company
composite_info = data[data.columns[3:]] # The binary info telling is it is part of the index or not.

# Replace the data with binary info.
binaryMatrix = composite_info.replace('X',1)    # Convert 'X' mark to 1.
binaryMatrix = binaryMatrix.replace('NaN',0)    # Convert 'Nan' mark to 0.

# Create a new datafame containing the binary info.
binaryData = pd.concat([company_info, binaryMatrix], 1)

# Save the data to excel.
binaryData.to_excel("D:\odrive\Personal\Maestria_Ciencias_Computacionales_INAOEP\Thesis\Datasets\S&P_500_Composition_Changes_1990_-_2017_binary.xlsx")