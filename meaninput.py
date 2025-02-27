#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd

def main():
    # Load the data from the Excel file
    file_path = 'Data file"'
    data = pd.read_excel(file_path)

    # Split the "Country*Year" column into "Country" and "Year"
    data[['Country', 'Year']] = data['国家'].str.split('*', expand=True)
    data.drop(columns=['国家'], inplace=True)

    # Reorder columns to place "Country" and "Year" first
    cols = data.columns.tolist()
    cols = ['Country', 'Year'] + [col for col in cols if col not in ['Country', 'Year']]
    data = data[cols]

    # Apply mean imputation only when there are at least two non-missing values
    for column in data.columns[2:]:
        # Apply transformation: Calculate mean where there are at least two valid data points
        means = data.groupby('Country')[column].transform(lambda x: x.mean() if x.count() > 1 else None)
        # Fill missing values only where the mean is available, keep existing values otherwise
        data[column] = data[column].where(data[column].notna(), means)

    # Save the processed data to a new Excel file
    output_file_path = 'T1_mean_imputation.xlsx'
    data.to_excel(output_file_path, index=False)
    print(f'File saved to {output_file_path}')

if __name__ == '__main__':
    main()


# In[ ]:




