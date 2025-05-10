import pandas as pd


def load_data(file_path):
    """Load raw data from the specified file path."""
    return pd.read_csv(file_path)


def preprocess_data(df):
    """Preprocess the raw data for model training."""
    # Example preprocessing step
    df = df.dropna()
    return df