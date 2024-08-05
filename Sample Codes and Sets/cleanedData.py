import pandas as pd

file_path = 'D:\Krishna\IBM Project\Data\Marine Pollution.csv'
data = pd.read_csv(file_path)

columns_to_drop = ['OBJECTID', 'Short Reference', 'Long Reference', 'DOI', 'Organization', 'Keywords', 'Accession Number', 'Accession Link', 'GlobalID', 'x', 'y']
data_cleaned = data.drop(columns=columns_to_drop)

critical_columns = ['Oceans', 'Regions', 'SubRegions', 'Measurement', 'Unit', 'Density Range', 'Density Class', 'Latitude', 'Longitude', 'Date']
data_cleaned = data_cleaned.dropna(subset=critical_columns)

valid_density_classes = ['Very Low', 'Low', 'Medium', 'High', 'Very High']
data_cleaned = data_cleaned[data_cleaned['Density Class'].isin(valid_density_classes)]

cleaned_file_path = 'D:\Krishna\IBM Project\Data\CleanedData1.csv'
data_cleaned.to_csv(cleaned_file_path, index=False)

print("Data cleaning completed. Cleaned data saved to:", cleaned_file_path)
