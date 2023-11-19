"""Filter an input words list dropping all words that are invalid/unrecognized by contexto's dictionary."""

import argparse

from ..data_collection_async import WordDoesNotCount, WordNotFound, WordTooCommon, extract_word_rank, get_urls, get_words, make_api_requests
from ..resources import words_alpha_unfiltered

_DEFAULT_START_INDEX = 1
_DEFAULT_END_INDEX = 25000
_DEFAULT_CHUNK_SIZE = 50
_MAX_REQUESTS_ALLOWED = 28000
_DEFAULT_GAME_ID = 1


def handle_args() -> tuple[str, int, int, int]:
    """Parse arguments using `argparse` library. Returns the tuple (word_list_path, from_idx, to_idx, chunk_size)."""

    parser = argparse.ArgumentParser(
        prog="FilterWordList",
        description="Extract words that are recognized by contexto from a starting word list.",
        epilog=f"path to default word list: {words_alpha_unfiltered()}",
    )

    parser.add_argument(
        "--word-list",
        help="Path to the text file containing a list of words to filter.",
        type=str,
        default=words_alpha_unfiltered(),
    )

    parser.add_argument(
        "--from",
        help="Starting index of words to filter. '--from 1' will start with the first word",
        type=int,
        default=_DEFAULT_START_INDEX,
        dest="_from",
    )

    parser.add_argument(
        "--to",
        help="Final index of words to filter. '--to 10' will stop at the 10th word (inclusive)",
        type=int,
        default=_DEFAULT_END_INDEX,
    )

    parser.add_argument(
        "--chunk-size",
        help=f"Size of batch of API requests. Default {_DEFAULT_CHUNK_SIZE}.",
        type=int,
        default=_DEFAULT_CHUNK_SIZE,
    )

    # -------------------------------- Parameters -------------------------------- #
    args = parser.parse_args()

    if args.to - args._from > _DEFAULT_END_INDEX:
        raise Exception(f"Too many requests! [Limit: {_MAX_REQUESTS_ALLOWED}]")

    return args.word_list, args._from, args.to, args.chunk_size


def main():

    # ---------------------------- Program parameters ---------------------------- #
    word_list_path, starting_index, ending_index, chunk_size = handle_args()
    filtered_output = f"filtered_{starting_index}_{ending_index}.txt"
    failed_words = f"failed_{starting_index}_{ending_index}.csv"

    # ---------------------------- Word and URL lists ---------------------------- #
    all_words = get_words(word_list_path)
    words = all_words[(starting_index - 1) : ending_index]
    urls = get_urls(words, _DEFAULT_GAME_ID)

    print(
        "Filtering words \n[{}]: {} \n\t.\n\t.\n\t. \n[{}]: {}".format(
            starting_index, words[0], ending_index, words[-1]
        )
    )
    print("source word list: {}".format(word_list_path))

    # ---------------------- Make requests, handle responses --------------------- #
    responses = make_api_requests(urls, chunk_size)

    word_rankings = {}
    exceptions = {}

    for (word, response) in zip(words, responses):
        try:
            lemma, rank = extract_word_rank(response)
            word_rankings[lemma] = rank

        except WordDoesNotCount:

            exceptions[word] = "WordDoesNotCount"

        except WordNotFound:

            exceptions[word] = "WordNotFound"

        except WordTooCommon:

            exceptions[word] = "WordTooCommon"

        except Exception:

            exceptions[word] = "Other"

    print()
    print("Finished handling {} total requests!".format(len(words)))

    # ------------------------------- File outputs ------------------------------- #
    with open(filtered_output, "w") as file:

        words = list(word_rankings.keys())
        words.sort()
        lines = ["{}\n".format(w) for w in words]
        file.writelines(lines)

    with open(failed_words, "w") as file:

        file.write("word,error\n")

        for (word, reason) in exceptions.items():
            file.write("{},{}\n".format(word, reason))


if __name__ == "__main__":
    main()
