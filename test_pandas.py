import pandas as pd
import numpy as np

my_series = pd.Series([5, 6, 7, 8, 9, 10])
print(my_series)
print(my_series.index)
print(my_series.values)
print(my_series[4])
print(my_series[[4]])
mask = my_series > 7
print(mask)
print(my_series[mask])
