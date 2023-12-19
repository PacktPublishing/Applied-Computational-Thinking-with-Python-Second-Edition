import pandas as pd
import numpy as np

# Sample dataset
data = {
'Name': ['Ed', 'Carina', 'Jeanie', 'Scott', 'John'],
'Height': [160, '5.9ft', 170.5, 'Unknown', '6ft']
}
df = pd.DataFrame(data)
print("Original DataFrame with Mixed Data types:")
print(df)

# Convert to a Consistent Format using a Function
def convert_height(height):
    if 'ft' in str(height):
        return float(height.replace('ft', '')) * 30.48
    elif isinstance(height, (int, float)):
        return height
    else:
        return np.nan
    
# Apply the Conversion Function
df['Height'] = df['Height'].apply(convert_height)
print("\nFixed Data Types:")
print(df)    

# Handling Missing Values
average_height = df['Height'].mean()
df['Height'].fillna(average_height, inplace=True)
print("\nFinalized Data Types:")
print(df)
