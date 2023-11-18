from os.path import join, dirname

def nltk_filtered_path() -> str:
    """Return the full path to the nltk_filtered.txt word list."""
    parent_dir = dirname(__file__)
    file_name = "nltk_filtered.txt"
    return join(parent_dir, file_name)

def nltk_path() -> str:
    parent_dir = dirname(__file__)
    file_name = "nltk.txt"
    return join(parent_dir, file_name)