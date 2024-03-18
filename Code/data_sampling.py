
import pandas as pd
import numpy as np

df = pd.read_csv(r'G:\.....\cleaned_dataset_29Jan.csv')

df = df[['NCT number','IPD Check', 'IPD Description','Overall Status','Last Update Posted', 'M_Label']]
df = df[df['Overall Status']=='Completed']

# Convert 'Last Update Posted' to datetime
df['Last Update Posted'] = pd.to_datetime(df['Last Update Posted'], errors='coerce')

# Now that 'Last Update Posted' is a datetime object, we can use .dt accessor to format it
df['Study First Posted'] = df['Last Update Posted'].dt.strftime('%m%Y')

# Filter the dataframe for entries from 2018 onwards
# Note: Ensure 'Last Update Posted' is a datetime object before comparing
df = df[df['Last Update Posted'].dt.year >= 2018]

df = pd.DataFrame(df)
print("The dataset info is as follow: ")
print("Rows of the dataset:" ,df.shape[0])
print(df['IPD Check'].value_counts())
def sample_and_merge(df, n_yes=0, n_no=0, n_undecided=0, random_state=42):
    df_yes = df[df['IPD Check'] == 'Yes']
    df_no = df[df['IPD Check'] == 'No']
    df_undecided = df[df['IPD Check'] == 'Undecided']

    sampled_df_yes = df_yes.sample(n=n_yes, random_state=random_state)
    sampled_df_no = df_no.sample(n=n_no, random_state=random_state)
    sampled_df_undecided = df_undecided.sample(n=n_undecided, random_state=random_state)

    merged_df = pd.concat([sampled_df_yes, sampled_df_no, sampled_df_undecided], ignore_index=True)

    return merged_df

# Example usage:
# Assuming df is your original DataFrame
df = sample_and_merge(df, n_yes=2000, n_no=2000, n_undecided=1000)
df = pd.DataFrame(df)
print("The dataset info is as follow: ")
print("Rows of the dataset:" ,df.shape[0])
print(df['IPD Check'].value_counts())

df.to_csv(r'G:\.....\df_Manual_5k.csv', index=False)
