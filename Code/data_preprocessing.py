# -*- coding: utf-8 -*-

import pandas as pd
import plotly.express as px


df = pd.read_csv(r'F:\.....\Clinicaltrials.csv')
df = pd.DataFrame(df)

df_IPD = df[['NCT number','IPD Check', 'IPD Description', 'Study Type', 'Start Date','Study First Posted', 'Last Update Posted','Overall Status']]

#Drop the NaN rows in sharing_ipd
df_IPD = df_IPD.dropna(subset=['IPD Description'])
df_IPD = df_IPD.dropna(subset=['IPD Check'])
print("The dataset info is as follow: ")
print("Rows of the dataset:" ,df_IPD.shape[0])
print(df_IPD['IPD Check'].value_counts())

# Define a function to remove leading dots
def remove_leading_dot(sentence):
    return sentence.lstrip('.')

# Apply the function to the 'ipd_description' column
df_IPD['IPD Description'] = df_IPD['IPD Description'].apply(remove_leading_dot)

# Drop rows with null values in 'IPD Description'
df_IPD['IPD Description'] = df_IPD['IPD Description'].astype(str)
df_IPD['IPD Description']=df_IPD['IPD Description'].str.lower()
df_IPD['IPD Description'] = df_IPD['IPD Description'].str.replace('[^a-zA-Z0-9\s]', '')

# drop the duplicated rows
df_IPD = df_IPD.drop_duplicates(subset=['IPD Check', 'IPD Description'])
df_IPD_3L = df_IPD
df_IPD_3L


# Count and display duplicated values in 'IPD Description'
duplicated_values_count = df_IPD['IPD Description'].duplicated(keep=False).sum()
duplicated_values = df_IPD[df_IPD['IPD Description'].duplicated(keep=False)]

#"""Drop the duplicated values in IPD Description"""

df_IPD = df_IPD.drop_duplicates(subset=['IPD Description'])
# Count and display duplicated values in 'IPD Description'
duplicated_values_count = df_IPD['IPD Description'].duplicated(keep=False).sum()
duplicated_values = df_IPD[df_IPD['IPD Description'].duplicated(keep=False)]

#"""now we should check what is the minimum beneficial length for IPD Description"""

values_to_drop_length = 10
specific_values_to_drop = ['gsk and wrair', 'glaxosmithkline', 'undecided.', 'n/a - phase i study']

# Filter the DataFrame
df_IPD = df_IPD[
    (df_IPD['IPD Description'].str.len() >= values_to_drop_length) &
    (~df_IPD['IPD Description'].isin(specific_values_to_drop))
]
print("The dataset info is as follow: ")
print("Rows of the dataset:" ,df_IPD.shape[0])
print(df_IPD['IPD Check'].value_counts())

# Removing @@ artifact from the statements
df['IPD Description'] = df['IPD Description'].str.replace('@@', '', regex=False)

# Create a new column for labels
df_IPD['M_Label'] = None

#"""Now lets check the distribution"""

# Filter the DataFrame for "Yes" and "No" values
df_yes = df_IPD[df_IPD['IPD Check'] == 'Yes']
df_no = df_IPD[df_IPD['IPD Check'] == 'No']

# Create a boxplot using Plotly
fig = px.box(df_IPD, x='IPD Check', y=df_IPD['IPD Description'].str.len(), points="all")

# Set plot labels and title
fig.update_layout(
    xaxis_title='IPD Check',
    yaxis_title='Length of IPD Description',
    title='Length Distribution of "Yes" and "No" in IPD Description'
)

# Show the plot
fig.show()

# Save the DataFrame to a CSV file
df_IPD.to_csv(r'G:\......\cleaned_dataset.csv', index=False)

#"""now we store and clean the dataset with three labels "Yes" "No" "Undecided"


# Count and display duplicated values in 'IPD Description'
df_IPD_3L = df_IPD_3L.drop_duplicates(subset=['IPD Description'])
duplicated_values_count = df_IPD_3L['IPD Description'].duplicated(keep=False).sum()
duplicated_values = df_IPD_3L[df_IPD_3L['IPD Description'].duplicated(keep=False)]

print("We also have ",duplicated_values_count," in the dataset which has to be dropped")
print("The dataset info is as follow: ")
print("Rows of the dataset:" ,df_IPD_3L.shape[0])
print(df_IPD_3L['IPD Check'].value_counts())

values_to_drop_length = 10
specific_values_to_drop = ['gsk and wrair', 'glaxosmithkline', 'undecided.', 'n/a - phase i study']

# Filter the DataFrame
df_IPD_3L = df_IPD_3L[
    (df_IPD_3L['IPD Description'].str.len() >= values_to_drop_length) &
    (~df_IPD_3L['IPD Description'].isin(specific_values_to_drop))
]
print("The dataset info is as follow: ")
print("Rows of the dataset:" ,df_IPD_3L.shape[0])
print(df_IPD_3L['IPD Check'].value_counts())

# Save the DataFrame to a CSV file
df_IPD_3L.to_csv(r'G:\.......\df_IPD_3L.csv', index=False)