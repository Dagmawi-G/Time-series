# scripts/data_summary.py
import pandas as pd

def load_data(file_path):
    """
    Loads the Brent oil price dataset.
    :param file_path: str, path to the dataset file
    :return: DataFrame
    """
    df = pd.read_csv(file_path, parse_dates=["Date"], dayfirst=True)
    return df

def summarize_data(df):
    """
    Prints a summary of the dataset.
    """
    print("Dataset Summary:\n")
    print(df.info())
    print("\nFirst 5 rows:\n", df.head())
    print("\nDescriptive Statistics:\n", df.describe())

if __name__ == "__main__":
    # Update with the actual dataset path
    file_path = "data/BrentOilPrices.csv"
    df = load_data(file_path)
    summarize_data(df)


""
