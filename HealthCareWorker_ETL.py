import pandas as pd
import numpy as np

file_input = '~/healthCareWorkers.csv'

file_pre_processed = '~/Pre_Processed_Data.csv'

df_input = pd.read_csv(file_input, header = 0)

#print(df_input)

data_Filter = pd.DataFrame(df_input.filter(["Variable", "Country", "Value"]))

#print(data_Filter)

data_ValueSum = pd.DataFrame(data_Filter.groupby(["Variable", "Country"]).sum().reset_index())
print(data_ValueSum)


data_ValueSum.to_csv(file_pre_processed, encoding='utf-8', index=False)

df_pre_processed = pd.read_csv(file_pre_processed, header = 0)

df_pre_processed.loc[ : , ['Variable', 'Country', 'Value'] ]
