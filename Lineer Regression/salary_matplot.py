# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 20:24:11 2019

@author: laptop
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
data  = pd.read_csv("salary.csv")
df = pd.DataFrame(data, columns=["year","salary"])
import  matplotlib.pyplot as plt
plt.scatter(df.year, df.salary)
plt.savefig("salarymatplot.png")