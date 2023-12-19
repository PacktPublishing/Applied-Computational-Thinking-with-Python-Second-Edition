import pandas as pd

data = {
'Title': ['The Midnight Library', 'The Forever War', 'The Power',
'The Midnight Library', 'The Forever War', 'To Kill a Mockingbird'],
'Author': ['Matt Haig', 'Joe Haledeman', 'Naomi Alderman', 'Matt Haig', 
           'Joe Haledeman', 'Harper Lee']
}

df = pd.DataFrame(data)

print("Original Dataset:\n")

print(df) 
