#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd



# 加载数据
data = pd.read_excel("Data.xlsx")

# 计算每列的缺失值百分比
missing_percentages = data.isnull().mean() * 100
print("缺失值百分比:")
print(missing_percentages.sort_values(ascending=False))

# 基础描述性统计
basic_stats = data.describe(include='all')
print("描述性统计:")
print(basic_stats)

