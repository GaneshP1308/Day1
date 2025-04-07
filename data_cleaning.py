import pandas as pd

# Load the dataset
df = pd.read_csv('E:\\Elevate labs\\Day1\\netflix_titles.csv', encoding='latin1')

# Drop columns with all missing values
df.dropna(axis=1, how='all', inplace=True)

# Fill missing values in 'country' with 'unknown'
df['country'].fillna('unknown', inplace=True)

# Fill missing values in 'director' and 'cast' with 'Not Available'
df['director'].fillna('Not Available', inplace=True)
df['cast'].fillna('Not Available', inplace=True)

# Fill missing values in 'date_added' with 'Not Available'
df['date_added'].fillna('Not Available', inplace=True)

# Fill missing values in 'rating' and 'duration' with 'Not Rated' and 'Unknown' respectively
df['rating'].fillna('Not Rated', inplace=True)
df['duration'].fillna('Unknown', inplace=True)

#removing the duplicate
df.drop_duplicates(inplace=True)

#standardizing the country name
df['country'] = df['country'].str.strip()      
df['country'] = df['country'].str.title()  

#converting date to dd-mm-yy format

df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
df['date_added'] = df['date_added'].dt.strftime('%d-%m-%Y')

# Renaming column headers
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# Check for missing values after cleaning
print(df.isnull().sum())

df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
df['release_year'] = pd.to_numeric(df['release_year'], errors='coerce')

print(df.dtypes)

cleaned_df = df.copy()  # copy of the cleaned data
cleaned_df.to_csv('E:\\Elevate labs\\Day1\\netflix_cleaned.csv', index=False)
