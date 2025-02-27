#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


def load_data(file_path):
    return pd.read_excel(file_path)

def minmax_transform(group, positive_columns, negative_columns):
    scaler = MinMaxScaler()
    if positive_columns:
        group[positive_columns] = scaler.fit_transform(group[positive_columns])
    if negative_columns:
        group[negative_columns] = 1 - scaler.fit_transform(group[negative_columns])
    return group

def calculate_scores(group, attributes):
    ideal = group[attributes].max()
    negative_ideal = group[attributes].min()
    dist_to_ideal = np.sqrt(((group[attributes] - ideal) ** 2).sum(axis=1))
    dist_to_negative_ideal = np.sqrt(((group[attributes] - negative_ideal) ** 2).sum(axis=1))
    relative_closeness = dist_to_negative_ideal / (dist_to_ideal + dist_to_negative_ideal)
    return relative_closeness

def plot_similarity(results, year='2022'):
    # Filter results for the year 2022 and calculate grade occurrences
    results_2022 = results[results['Year'] == year]
    countries_by_grade = results_2022.pivot_table(index='Country', columns='Grade', aggfunc='size', fill_value=0)

    # Prepare to plot
    fig, ax = plt.subplots(figsize=(10, 6))
    markers = {'A': 'o', 'B': '^', 'C': 's', 'D': 'x'}
    colors = {'A': 'darkred', 'B': 'red', 'C': 'lightcoral', 'D': 'grey'}
    
     # Calculate similarity for each country and plot
    for grade, marker in markers.items():
        countries = countries_by_grade[countries_by_grade[grade] > 0].index.tolist()
        for country in countries:
            country_data = results[results['Country'] == country]
            std_dev = np.std(country_data['Score'])
            similarity = 1 / (1 + std_dev)  # Inverse of standard deviation to represent similarity
            ax.plot(country_data['Year'], [similarity] * len(country_data), marker=marker, color=colors[grade], label=f"{grade} - {country}")

    # Set labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Similarity')
    ax.set_title('Similarity of Country Grades Over Years by 2022 Grade')
    ax.legend(title='Grade - Country')

    plt.show()   
    
    
    # Prepare to plot
    fig, ax = plt.subplots(figsize=(10, 6))
    markers = {'A': 'o', 'B': '^', 'C': 's', 'D': 'x'}
    colors = {'A': 'darkred', 'B': 'red', 'C': 'lightcoral', 'D': 'grey'}


def plot_results(results, countries):
    colors = {'D': 'grey', 'C': 'lightcoral', 'B': 'red', 'A': 'darkred'}
    fig, ax = plt.subplots(figsize=(10, 6))


    # Determine the number of unique years to calculate marker size
    num_years = len(results['Year'].unique())
    # Calculate marker size dynamically based on figure size and number of years
    marker_size = (fig.get_size_inches()[1] * 72 / num_years)**2
    
    for i, country in enumerate(countries):
        country_data = results[results['Country'] == country]
        ax.scatter(country_data['Year'], [i] * len(country_data), 
                   s=marker_size, c=[colors[grade] for grade in country_data['Grade']], 
                   marker='s', edgecolors='none')
    
    # Set y-axis labels to be the countries
    ax.set_yticks(range(len(countries)))
    ax.set_yticklabels(countries)
    ax.set_xticks(sorted(results['Year'].unique()))

    # Add grid, legend, title, and labels
    ax.grid(True, which='both', linestyle='--', linewidth=0.5)
    ax.set_xlabel('Year')
    ax.set_ylabel('Country')
    ax.set_title('Country Grades by Year')

    # Create a legend
    legend_elements = [mpatches.Patch(facecolor=colors[grade], label=grade) for grade in colors]
    ax.legend(handles=legend_elements, title='Grade')

    plt.tight_layout()  # Adjust layout to fit all elements
    plt.show()
 

def main():
    data = load_data("Data.xlsx")
    grouped_data = data.groupby('Year')
    results_list = []
    
    # Your provided columns for positive and negative indicators
    positive_columns = [
        '死亡登记及死因信息的完整性', 'DPT 免疫接种率（占 12 - 23 个月年龄组的百分比）', 
        '每个国家每年每100000人在手术室进行的手术次数', '专业外科劳动力', '净移民', '女性出生预期寿命', 
        '男性出生预期寿命', '出生预期寿命', '出生登记完整性', '医院床位（每千人）', 
        '在熟练医护人员护理下的分娩（占总数的百分比）', '接受产前护理的孕妇（百分比）', '避孕普及率（占 15–49 岁女性的百分比）',
        
        '麻疹免疫接种率（占 12 - 23 个月年龄组的百分比）'
    ]
    negative_columns = [
        
        
        '糖尿病患病率',
        '道路交通伤害死亡人数（每10万人）', 
        '儿童贫血患病率（5岁以下儿童的百分比）',
        '严重消瘦的发生率，身高体重比（5 岁以下儿童的百分比）', 
        '当需要手术护理时，面临贫困支出风险的人口比例',
        '国际迁移者', 
        '孕产妇死亡率（模型估计值，每10万例活产中所占比例）', 
        '按来源国家或地区划分的难民人数', 
        '新生儿死亡率', 
        '未能满足的避孕需求',
        '死亡率（五岁以下儿童）', 
        '死亡率 婴幼儿', 
        '消瘦发生率（五岁以下儿童发生率）',
        '结核发病率（每十万人）', 
        '艾滋病病毒感染率，女性（15-24岁的百分比）', 
        '艾滋病病毒感染率，男性（占15-24岁的百分比）',
        '艾滋病病毒感染率，总数（占15-49岁人口的百分比）', 
        '营养不良发生率，年龄体重（占5岁以下儿童的百分比）',
        '营养不良的发生率（占人口的百分比）', 
        '营养不良的发生率，年龄身高（占5岁以下儿童的百分比）',
        '青少年母亲（占15-19岁年龄段内曾生育子女或正处于怀孕阶段的女性比例）', 
        '青春期生育率（每千名 15-19 岁女性生育数）'
    ]
    
    for year, group in grouped_data:
        original_length = len(group)
        group = group.drop_duplicates(subset=['Country'])  # Removing possible duplicate countries within the same year
        if len(group) != original_length:
            print(f"Removed duplicates in year {year}")
        
        group = minmax_transform(group, positive_columns, negative_columns)
        group['Score'] = calculate_scores(group, positive_columns + negative_columns)
        group['Grade'] = pd.qcut(group['Score'], 4, labels=['D', 'C', 'B', 'A'])
        
        results_list.append(group[['Country', 'Year', 'Score', 'Grade']])
    
    final_results = pd.concat(results_list)
    print(final_results.pivot_table(index='Country', columns='Grade', aggfunc='size', fill_value=0))
    final_results.to_excel('TOPSIS_Results_By_Year.xlsx', index=False)
    
    grade_counts = final_results.pivot_table(index='Country', columns='Grade', aggfunc='size', fill_value=0)
    # Optionally save the results to an Excel file
    grade_counts.to_excel('C:/Users/DELL/Downloads/Country_Grades_Count.xlsx')
    final_results.to_excel('C:/Users/DELL/Downloads/TOPSIS_Results.xlsx', index=False)
    print(grade_counts)
    print(final_results[['Year', 'Country', 'Score', 'Grade']])
    



if __name__ == "__main__":
    main()

