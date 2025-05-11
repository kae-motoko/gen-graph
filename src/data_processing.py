import pandas as pd
import time
from sklearn.model_selection import train_test_split
from constants import refine_text_prompt_base
from gemini_model_config import get_safety_settings, initialize_gemini_model


def get_model():
    return initialize_gemini_model

def load_data(file_path):
    """Load raw data from the specified file path."""
    return pd.read_csv(file_path)


def get_data_by_setting(split_type, df_raw_data):
    """
    Splits the raw data into train, test, and evaluation sets and returns the requested split.

    Args:
        split_type (str): The type of data to return ('train', 'test', or 'eval').
        df_raw_data (pd.DataFrame): The raw data as a pandas DataFrame.

    Returns:
        list: A list of records corresponding to the requested split.
    """
    # Convert DataFrame to a list of values
    sample_docs = df_raw_data.values.tolist()

    # Split data into 80% train and 20% temporary set (for test + eval)
    train_docs, temp_docs = train_test_split(sample_docs, test_size=0.2, random_state=42)

    # Split the temporary set into 50% test and 50% evaluation
    test_docs, eval_docs = train_test_split(temp_docs, test_size=0.5, random_state=42)

    # Print the sizes of each split
    print(f"Training set size: {len(train_docs)}")
    print(f"Test set size: {len(test_docs)}")
    print(f"Evaluation set size: {len(eval_docs)}")

    # Match the requested split type
    match split_type:
        case 'test':
            return test_docs
        case 'train':
            return train_docs
        case 'eval':
            return eval_docs
        case _:
            raise ValueError(f"Invalid split_type: {split_type}. Must be one of ['train', 'test', 'eval'].")

# to-do: s-lit in train test and evalution brtaches

def refine_data(raw_df):

    model = get_model()

    refined_text_df = pd.DataFrame(columns=['original_text', 'refined_text', 'label'])

    for idx, doc in enumerate(raw_df):
        prompt_refined = refine_text_prompt_base + doc[1]
        response_ref = model.generate_content(prompt_refined, safety_settings=get_safety_settings)

        if(idx == 8):
            print('sleeping')
            time.sleep(60)
        if(idx == 999):
            break

        if(response_ref):
            text = response_ref.text
            new_row = {'original_text': doc[1], 'refined_text': text, 'label': doc[2]}
            refined_text_df = pd.concat([refined_text_df, pd.DataFrame([new_row])], ignore_index=True)

    refined_text_df.to_csv(os.path.join('/content/drive/MyDrive/mestrado/data/ag_news_subset',r'refined_text_df.csv'))