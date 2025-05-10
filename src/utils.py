import os
import time
import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx


def save_to_csv(dataframe, path, filename):
    """
    Save a DataFrame to a CSV file.

    Args:
        dataframe (pd.DataFrame): The DataFrame to save.
        path (str): The directory where the file will be saved.
        filename (str): The name of the CSV file.

    Returns:
        str: The full path to the saved file.
    """
    if not os.path.exists(path):
        os.makedirs(path)
    full_path = os.path.join(path, filename)
    dataframe.to_csv(full_path, index=False)
    return full_path


def load_csv(filepath):
    """
    Load a CSV file into a DataFrame.

    Args:
        filepath (str): Path to the CSV file.

    Returns:
        pd.DataFrame: The loaded DataFrame.
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")
    return pd.read_csv(filepath)


def visualize_graph(graph, color_map=None, figsize=(7, 7), layout_seed=42):
    """
    Visualize a graph using NetworkX.

    Args:
        graph (networkx.Graph): The graph to visualize.
        color_map (list, optional): Node colors. Defaults to None.
        figsize (tuple, optional): Size of the figure. Defaults to (7, 7).
        layout_seed (int, optional): Seed for the layout. Defaults to 42.
    """
    plt.figure(figsize=figsize)
    plt.xticks([])
    plt.yticks([])
    layout = nx.spring_layout(graph, seed=layout_seed)
    nx.draw_networkx(graph, pos=layout, with_labels=False, node_color=color_map, cmap="Set2")
    plt.show()


def retry_function(func, max_attempts=3, sleep_time=60, *args, **kwargs):
    """
    Retry a function with exponential backoff.

    Args:
        func (callable): The function to retry.
        max_attempts (int): Maximum retry attempts. Defaults to 3.
        sleep_time (int): Time to wait between retries in seconds. Defaults to 60.
        *args: Positional arguments for the function.
        **kwargs: Keyword arguments for the function.

    Returns:
        Any: The return value of the function.
    """
    for attempt in range(max_attempts):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            if attempt < max_attempts - 1:
                print(f"Attempt {attempt + 1} failed: {e}. Retrying in {sleep_time} seconds...")
                time.sleep(sleep_time)
            else:
                raise


def extract_triplets_from_text(text):
    """
    Extract knowledge graph triplets from text.

    Args:
        text (str): Text containing triplets in the format ('head', 'relation', 'tail').

    Returns:
        list: List of triplets as tuples.
    """
    triplets = []
    for line in text.strip().split("\n"):
        parts = line.strip("()").split(", ")
        triplets.append(tuple(part.strip("'") for part in parts))
    return triplets