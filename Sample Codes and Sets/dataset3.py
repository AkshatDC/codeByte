import pandas as pd

file_path = 'D:\Krishna\IBM Project\Data\RawData3.csv'
df = pd.read_csv(file_path)

columns_to_drop = [
    'occurrenceID', 'datasetKey', 'kingdom', 'infraspecificEpithet',
    'taxonRank', 'scientificName', 'verbatimScientificName', 'verbatimScientificNameAuthorship',
    'countryCode', 'locality', 'occurrenceStatus', 'individualCount', 'publishingOrgKey',
    'decimalLatitude', 'decimalLongitude', 'coordinateUncertaintyInMeters', 'coordinatePrecision',
    'elevation', 'elevationAccuracy', 'depth', 'depthAccuracy', 'taxonKey', 'speciesKey',
    'basisOfRecord', 'institutionCode', 'collectionCode', 'catalogNumber', 'recordNumber',
    'identifiedBy', 'dateIdentified', 'license', 'rightsHolder', 'recordedBy', 'typeStatus',
    'establishmentMeans', 'lastInterpreted', 'mediaType', 'issue'
]


df_cleaned = df.drop(columns=columns_to_drop)

df_cleaned['date'] = pd.to_datetime(df_cleaned[['year', 'month', 'day']], errors='coerce')

df_cleaned.drop(columns=['day', 'month', 'year'], inplace=True)

output_file = 'D:\Krishna\IBM Project\Data\cleaned_marine_species_data.csv'
df_cleaned.to_csv(output_file, index=False)

print(f"Cleaned data saved to {output_file}")
