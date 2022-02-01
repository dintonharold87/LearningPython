import pandas as pd
from matplotlib import pyplot as plt
indexed_avocado_data =pd.read_csv('avocado.csv',index_col='region')
print(indexed_avocado_data.loc["Albany"])
print(indexed_avocado_data.describe())