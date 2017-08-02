import pandas
import numpy as np

panda_beta_data = pandas.read_csv("~/Desktop/beta-data/app/BetaTracker.csv")
#print (panda_beta_data.head())

### Selecting Columns from Original Data to Keep
header = ["Prospect Name", "Prospect email ", "FR Name", "Published Date"]

### Format 'Published Date' as date_time

panda_beta_data["Published Date"] = panda_beta_data["Published Date"].replace('SV', np.nan)
panda_beta_data["Published Date"] = pandas.to_datetime(panda_beta_data['Published Date'], format="%m/%d/%Y")

panda_beta_data.to_csv('output.csv', columns = header)

### Defining the data range
