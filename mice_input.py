#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
from sklearn.ensemble import RandomForestRegressor


my_data = pd.read_excel("Data.xlsx")



# 将数据拷贝到 obesity_mice_imputed
mice_imputed = my_data.copy()

# 初始化terativeImputer
mice_imputer = IterativeImputer(
    estimator=RandomForestRegressor(),
    max_iter=50,  # Increase max iterations
    tol=0.001,  # Adjust tolerance for stopping
    random_state=0,
    verbose=2  # Increase verbosity to monitor convergence
)

# 使用fit_tranform填补数据
mice_imputed.iloc[:, :] = mice_imputer.fit_transform(mice_imputed)



print(mice_imputed)
mice_imputed.to_csv('mice_imputed50.csv', index=False)


# In[ ]:




