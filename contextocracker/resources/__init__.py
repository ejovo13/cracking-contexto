from os.path import join, dirname

def brown_words_filtered() -> str:
    """Return the full path to a list of Brown words that are recognized by contexto."""
    parent_dir = dirname(__file__)
    file_name = "brown_words_filtered.txt"
    return join(parent_dir, file_name)

def words_alpha_unfiltered() -> str:
    """Return the full path to a list of 350k English words.

    Taken from https://github.com/dwyl/english-words
    """
    parent_dir = dirname(__file__)
    file_name = "words_alpha.txt"
    return join(parent_dir, file_name)

def words_alph_filtered() -> str:
    """Return the full path to a list of words in 'words_alpha.txt' that contexto recognizes."""
    return join(dirname(__file__), "words_alpha_filtered.txt")

def brown_and_alpha_filtered() -> str:
    """Return the union of brown_words_filtered.txt and words_alpha_filtered.txt"""
    return join(dirname(__file__), "brown_and_word_list.txt")