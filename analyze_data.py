# analyze_data.py
#
# Assignment: Pandas Dataset Analysis
# Dataset: nominations.csv (celebrity/music metadata)

import pandas as pd

def main():
    print("\n=== LOADING DATA ===")
    df = pd.read_csv("data/nominations.csv")

    print("\n=== FIRST FIVE ROWS ===")
    print(df.head())

    print("\n=== DATAFRAME INFO ===")
    df.info()

    print("\n=== DESCRIPTION ===")
    print(df.describe(include="all"))

    print("\n=== ACCESSING DATA WITH loc AND iloc ===")

    print("\nSingle row by label using loc:")
    print(df.loc[df.index[0]])

    print("\nSingle row by position using iloc:")
    print(df.iloc[1])

    print("\nSlice rows by label using loc:")
    print(df.loc[df.index[0]:df.index[4]])

    print("\nSlice rows by position using iloc:")
    print(df.iloc[0:5])

    print("\nSingle column ('work_title'):")
    print(df["work_title"].head())

    print("\nSingle cell example (row 0, work_title):")
    print(df.loc[df.index[0], "work_title"])

    print("\n=== BOOLEAN FILTERING ===")

    print("\nFilter 1: main_artist_id > 100000")
    filter1 = df[df["main_artist_id"] > 100000]
    print(filter1.head())

    print("\nFilter 2: main_artist_id > 100000 AND guest_artist_id is not null")
    filter2 = df[(df["main_artist_id"] > 100000) & (df["guest_artist_id"].notna())]
    print(filter2.head())

    print("\n=== ADDING AND DROPPING COLUMNS ===")

    print("\nAdding column 'has_guest_artist' (True/False)...")
    df["has_guest_artist"] = df["guest_artist_id"].notna()
    print(df[["work_title", "guest_artist_id", "has_guest_artist"]].head())

    print("\nDropping column 'category_id'...")
    df = df.drop(columns=["category_id"])
    print("Remaining columns:", df.columns.tolist())

    print("\n=== GROUPBY OPERATION ===")
    print("\nCount of work titles grouped by whether they feature a guest artist:")
    result = df.groupby("has_guest_artist")["work_title"].count()
    print(result)

    print("\n=== COMPLETE ===")


if __name__ == "__main__":
    main()

