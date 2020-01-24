topsis_package
This package inpired when we stuck in such a situation where we have to choose one  within multiple choice varying by some fetures or properties.
This package suggest to with which one you should go based upon your weight on features and which feature you want to maximize or minmize.

use this package as:

from  topsis_shubham_dhanda import topsis
import pandas as pd

'-' -----you want to minimize it
'+' ---- you want to maximize it

#you have to define index column
df=pd.read_csv('topsis.csv', index_col="")
s=topsis(df,[.25,.25,.25,.25],['-','+','+','+'])
print("You should Choose item at:"+str(s.choose()))
