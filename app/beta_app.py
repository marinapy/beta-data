import pandas
import numpy as np

panda_beta_data = pandas.read_csv("~/Desktop/beta-data/app/BetaTracker.csv")

#rint(panda_beta_data.head())

### Selecting Columns from Original Data to Keep
header = ["Prospect Name", "Prospect email ", "FR Name", "Published Date"]


### Filtering Data by Published Date: 7/13 - 7/20

panda_beta_data["Published Date"] = panda_beta_data["Published Date"].replace('SV', np.nan)

panda_beta_data['Published Date'] = pandas.to_datetime(panda_beta_data['Published Date'], format="%m/%d/%Y")

range_panda_beta_data = panda_beta_data[panda_beta_data["Published Date"].isin(pandas.date_range('7/13/2017', '7/20/2017'))]

#prospect_email = range_panda_beta_data[(range_panda_beta_data["Prospect email "] != 'n/a')]
#prospect_email_new = prospect_email[(prospect_email["Prospect email "] != 'not in WR, FF or CRM')]

range_panda_beta_data = range_panda_beta_data[(range_panda_beta_data['Prospect email '].str.contains('@', regex=True) == True)]

range_panda_beta_data.to_csv('output.csv', columns = header)





### Filtering Data by missing email address > exclude
