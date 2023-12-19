import pandas as pd

# ch16_cleaningDemo4.py
data = {
'Title': ['The Midnight Library', 'The Forever War', 'The Power',
'The Midnight Library', 'The Forever War', 'To Kill a Mockingbird'],
'Author': ['Matt Haig', 'Joe Haledeman', 'Naomi Alderman', 'Matt Haig', 
           'Joe Haledeman', 'Harper Lee']
}
df = pd.DataFrame(data)

# Identify duplicates
duplicates = df[df.duplicated()]
print("\nDuplicates:\n")
print(duplicates)

# Remove duplicates
df_cleaned = df.drop_duplicates()
print("\nDataset after removing duplicates:\n")
print(df_cleaned)
