#!/usr/bin/env python
# coding: utf-8

# In[4]:


#ABCD 11年平均接近度趋势图

import matplotlib.pyplot as plt
import pandas as pd

# Assuming you have the data in a DataFrame named `data` with the same structure as described earlier
data = pd.read_excel("Data.xlsx") # Replace with the actual path to your data file

# Calculate the average score per year per rating category
average_scores_per_year = data.groupby(['Year', '22Grade'])['Score'].mean().unstack()

# Setting the matplotlib parameters to support Chinese characters in the plot
plt.rcParams['font.sans-serif'] = ['SimHei']  # Specify your Chinese font here
plt.rcParams['axes.unicode_minus'] = False  # Support the minus sign in Chinese fonts

# Plotting the trends
plt.figure(figsize=(10, 6))
for category in average_scores_per_year.columns:
    plt.plot(average_scores_per_year.index, average_scores_per_year[category], marker='o', label=f'{category}')

plt.xlabel('年份')
plt.ylabel('平均接近度')
plt.legend(title='2022年等级')
plt.grid(True)
plt.show()


# In[3]:


#22等级 因子趋势图
import matplotlib.pyplot as plt
import pandas as pd

# Setting the matplotlib parameters to support Chinese characters in the plot
plt.rcParams['font.sans-serif'] = ['SimHei']  # Specify your Chinese font here
plt.rcParams['axes.unicode_minus'] = False  # Support the minus sign in Chinese fonts
data= pd.read_excel("Data.xlsx")
# Group the data by year
grouped_by_year = data.groupby('Year')['Factor 1'].mean()


#因子1
# Group the data by year and grade
grouped_by_year_grade = data.groupby(['Year', '22Grade'])['Factor 1'].mean().unstack()


# Create the plot with Chinese titles and labels
plt.figure(figsize=(10, 6))

# Line for overall average by year
plt.plot(grouped_by_year.index, grouped_by_year.values, label='当年均值', color='black', linewidth=3,linestyle='--')

# Lines for each grade
colors = {'A': 'red', 'B': 'orange', 'C': 'blue', 'D': 'darkblue'}
for grade, color in colors.items():
    if grade in grouped_by_year_grade.columns:
        plt.plot(grouped_by_year_grade.index, grouped_by_year_grade[grade], label=f'医疗水平{grade}', color=color, linewidth=2)

plt.title('因子1趋势图')
plt.xlabel('年份')
plt.ylabel('因子1平均得分')
plt.legend(handlelength=4)
plt.grid(True)
scree_plot_path = 'C:/Users/DELL/Downloads/factor1.png'  # 指定文件路径和文件名
plt.savefig(scree_plot_path)  # 保存图像
plt.show()
#因子2
# Group the data by year and grade
grouped_by_year_grade = data.groupby(['Year', '22Grade'])['Factor 2'].mean().unstack()


# Create the plot with Chinese titles and labels
plt.figure(figsize=(10, 6))

# Line for overall average by year
plt.plot(grouped_by_year.index, grouped_by_year.values, label='当年均值', color='black', linewidth=3,linestyle='--')

# Lines for each grade
colors = {'A': 'red', 'B': 'orange', 'C': 'blue', 'D': 'darkblue'}
for grade, color in colors.items():
    if grade in grouped_by_year_grade.columns:
        plt.plot(grouped_by_year_grade.index, grouped_by_year_grade[grade], label=f'22年医疗水平{grade}', color=color, linewidth=2)

plt.title('因子2趋势图')
plt.xlabel('年份')
plt.ylabel('因子2平均得分')
plt.legend(handlelength=4)
plt.grid(True)
scree_plot_path = 'C:/Users/DELL/Downloads/factor2.png'  # 指定文件路径和文件名
plt.savefig(scree_plot_path)  # 保存图像
plt.show()

#因子3
# Group the data by year and grade
grouped_by_year_grade = data.groupby(['Year', '22Grade'])['Factor 3'].mean().unstack()


# Create the plot with Chinese titles and labels
plt.figure(figsize=(10, 6))

# Line for overall average by year
plt.plot(grouped_by_year.index, grouped_by_year.values, label='当年均值', color='black', linewidth=3,linestyle='--')

# Lines for each grade
colors = {'A': 'red', 'B': 'orange', 'C': 'blue', 'D': 'darkblue'}
for grade, color in colors.items():
    if grade in grouped_by_year_grade.columns:
        plt.plot(grouped_by_year_grade.index, grouped_by_year_grade[grade], label=f'医疗水平{grade}', color=color, linewidth=2)

plt.title('因子3趋势图')
plt.xlabel('年份')
plt.ylabel('因子3平均得分')
plt.legend(handlelength=4)
plt.grid(True)
scree_plot_path = 'C:/Users/DELL/Downloads/factor3.png'  # 指定文件路径和文件名
plt.savefig(scree_plot_path)  # 保存图像
plt.show()


# In[10]:


#当年等级因子趋势图
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def plot_factor_trend(data, factor_number):
    # Setting the matplotlib parameters to support Chinese characters in the plot
    plt.rcParams['font.sans-serif'] = ['SimHei']  # Specify your Chinese font here
    plt.rcParams['axes.unicode_minus'] = False  # Support the minus sign in Chinese fonts

    # Group the data by year and factor score
    grouped_by_year = data.groupby('Year')[f'Factor {factor_number}'].mean()
    grouped_by_year_grade = data.groupby(['Year', 'Grade'])[f'Factor {factor_number}'].mean().unstack()

    # Create the plot with Chinese titles and labels
    plt.figure(figsize=(10, 6))
    plt.plot(grouped_by_year.index, grouped_by_year.values, label='当年均值', color='black', linewidth=3, linestyle='--')

    # Lines for each grade
    colors = {'A': 'red', 'B': 'orange', 'C': 'blue', 'D': 'darkblue'}
    for grade, color in colors.items():
        if grade in grouped_by_year_grade.columns:
            plt.plot(grouped_by_year_grade.index, grouped_by_year_grade[grade], label=f'医疗水平{grade}', color=color, linewidth=2)

    plt.title(f'因子{factor_number}趋势图')
    plt.xlabel('年份')
    plt.ylabel(f'因子{factor_number}平均得分')

    # Set y-axis limits
    min_value = grouped_by_year_grade.min().min()  # Find the minimum value across all grades
    max_value = grouped_by_year_grade.max().max()  # Find the maximum value across all grades
    plt.ylim(min_value - 1, max_value + 1)  # Set limits with a small buffer

    # Set legend in the upper right corner
    plt.legend(loc='upper right', handlelength=4)

    plt.grid(True)
    scree_plot_path = f'C:/Users/DELL/Downloads/factor{factor_number}.png'  # Specify file path and file name
    plt.savefig(scree_plot_path)  # Save the plot
    plt.show()

# Load data
data = pd.read_excel("Data.xlsx")

# Plot trends for Factor 1, Factor 2, Factor 3
for i in range(1, 4):
    plot_factor_trend(data, i)


# In[ ]:




