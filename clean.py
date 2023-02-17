import pandas as pd

df = pd.read_csv("respondent_contact.csv")
df1 = pd.read_csv("respondent_other.csv")
df2 = pd.merge(df, df1, left_on='respondent_id', right_on='id', how="outer")
df2 = df2.drop(columns='id')
df2 = df2.dropna()
df2 = df2[~df2['job'].str.contains('insurance|Insurance')]

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('input', help='contact_info_file')
    parser.add_argument('input', help='other_info_file')
    parser.add_argument('output', help='output_file')
    args = parser.parse_args()

    cleaned = df2
    cleaned.to_csv(args.output, index=False)

    print(f"the shape of the output file:{cleaned.shape}")
