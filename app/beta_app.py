import pandas

panda_beta_data = pandas.read_csv("~/Desktop/beta-data/app/BetaTracker.csv")
#print (panda_beta_data.head())

### Selecting Columns from Original Data to Keep
header = ["Prospect Name", "Prospect email ", "FR Name", "Published Date"]
panda_beta_data.to_csv('output.csv', columns = header)
