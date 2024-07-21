import pandas as pd

data = pd.read_csv('D:\\Krishna\\IBM Project\\Data\\Biodiverty_Final_raw.csv', encoding='ISO-8859-1')

columns_to_retain = [
    'phylum', 'class', 'order', 'genus',
    'individualCount', 'occurrenceStatus',
    'decimalLatitude', 'decimalLongitude',
    'taxonRank', 'scientificName', 
    'day', 'month', 'year'
]

cleaned_data = data[columns_to_retain]

cleaned_data['eventDate'] = pd.to_datetime(cleaned_data[['year', 'month', 'day']])

cleaned_data = cleaned_data.drop(columns=['day', 'month', 'year'])

cleaned_data.to_csv('D:\\Krishna\\IBM Project\\Data\\Biodiverty_Final_cleaned.csv', index=False)

print("Data cleaning complete. Cleaned data saved to 'cleaned_data.csv'.")
