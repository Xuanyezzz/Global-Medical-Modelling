#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
import numpy as np
from factor_analyzer import FactorAnalyzer
import matplotlib.pyplot as plt
from factor_analyzer.factor_analyzer import calculate_bartlett_sphericity, calculate_kmo

# Setting the matplotlib parameters to support Chinese characters in the plot
plt.rcParams['font.sans-serif'] = ['SimHei']  # Specify your Chinese font here
plt.rcParams['axes.unicode_minus'] = False  # Support the minus sign in Chinese fonts

# 加载Excel文件
file_path = '("Data.xlsx")'
df = pd.read_excel(file_path)

# 选择数值型数据列
numeric_cols = df.select_dtypes(include=[np.number]).columns
df = df[numeric_cols]


# 从第三列开始选择数值型数据列
df = df.iloc[:, 2:]

# 检查KMO值
kmo_all, kmo_model = calculate_kmo(df)
print(f"KMO test statistic: {kmo_model}")

# 检查Bartlett的球形度
chi_square_value, p_value = calculate_bartlett_sphericity(df)
print(f"Bartlett's test chi-square value: {chi_square_value}, p-value: {p_value}")

# 初始化因子分析对象，没有指定因子数量进行初始评估
fa = FactorAnalyzer(rotation=None, method='principal')
fa.fit(df)

# 获取特征值
ev, _ = fa.get_eigenvalues()

# 确定因子数量：特征值大于1的规则
n_factors = sum(ev > 1)
print(f"Number of factors chosen by eigenvalue > 1 criterion: {n_factors}")

# 可视化碎石图来确定因子数
plt.figure(figsize=(10, 5))
plt.plot(range(1, df.shape[1] + 1), ev, marker='o')
plt.title('碎石图')
plt.xlabel('因子')
plt.ylabel('特征值')
plt.axhline(y=1, color='r', linestyle='--')
plt.grid(True)
scree_plot_path = 'C:/Users/DELL/Downloads/scree_plot.png'  # 指定文件路径和文件名
plt.savefig(scree_plot_path)  # 保存图像
plt.show()


# 重新进行因子分析，使用选择的因子数和旋转
fa = FactorAnalyzer(n_factors=n_factors, rotation='varimax', method='principal')
fa.fit(df)

# 输出因子载荷矩阵和解释的总方差
loadings = pd.DataFrame(fa.loadings_, columns=[f'Factor {i+1}' for i in range(n_factors)], index=df.columns)


explained_variance = pd.DataFrame(fa.get_factor_variance(), index=['SS Loadings', 'Proportion Var', 'Cumulative Var'])
print("Factor Loadings:\n", loadings)
print("Explained Variance:\n", explained_variance)

# 输出特征值
ev, v = fa.get_eigenvalues()
print("Eigenvalues:\n", ev)

# 输出解释的总方差
explained_variance = pd.DataFrame(fa.get_factor_variance(), index=['SS Loadings', 'Proportion Var', 'Cumulative Var'])
print("Explained Variance:\n", explained_variance)

# 计算因子得分
factor_scores = fa.transform(df)

# 将因子得分转换为DataFrame
factor_scores_df = pd.DataFrame(factor_scores, columns=[f'Factor {i+1}' for i in range(n_factors)])

# 保存因子得分到Excel
output_file_path = 'C:/Users/DELL/Downloads/factor_scores.xlsx'  # 指定文件路径和文件名
factor_scores_df.to_excel(output_file_path, sheet_name='Factor Scores', index=False)

# 输出特征值和总方差解释
print("Eigenvalues:\n", ev)
print("Explained Variance:\n", explained_variance)

# 分析因子1和因子2的内部指标权重
factor1_loadings = loadings['Factor 1']
factor2_loadings = loadings['Factor 2']
factor1_df = pd.DataFrame(factor1_loadings, columns=['Factor 1'])
factor2_df = pd.DataFrame(factor2_loadings, columns=['Factor 2'])

# 按载荷绝对值大小排序
factor1_sorted = factor1_df.sort_values(by='Factor 1', ascending=True)
factor2_sorted = factor2_df.sort_values(by='Factor 2', ascending=True)

# 打印排序后的载荷，显示贡献最大的前几个变量
print("因子1的内部指标权重（按贡献度排序）:\n", factor1_sorted.head())
print("因子2的内部指标权重（按贡献度排序）:\n", factor2_sorted.head())
# 创建一个Pandas Excel writer 使用openpyxl引擎
writer = pd.ExcelWriter('C:/Users/DELL/Downloads/factor_loadings.xlsx', engine='openpyxl')

# 将因子载荷DataFrame写入到Excel文件的不同工作表
factor1_sorted.to_excel(writer, sheet_name='Factor 1 Loadings', index=True)
factor2_sorted.to_excel(writer, sheet_name='Factor 2 Loadings', index=True)

factor1_loadings = loadings['Factor 1']

# 计算归一化的权重：每个载荷的绝对值除以所有载荷的绝对值之和
factor1_weights = abs(factor1_loadings) / abs(factor1_loadings).sum()
print('因子1内部权重：', factor1_weights)
# 将权重转换为DataFrame以便输出或进一步使用
factor1_weights_df = pd.DataFrame(factor1_weights, columns=['Normalized Weights'])
factor1_weights.to_excel(writer, sheet_name='Factor 1 Weights', index=True)
# 保存Excel文件
writer.close()



# In[ ]:




