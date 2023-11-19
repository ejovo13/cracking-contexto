"""Script to collect the scores using our dictionary with 12,000 words."""

import argparse
from datetime import date

from .data_collection_async import (
    extract_word_rank,
    get_urls,
    get_words,
    make_api_requests,
)

from .resources import words_alpha_filtered

# nov 18 2023 corresponds to the game id: 426
_GAME_426_DAY = date.fromisoformat("2023-11-18")
_DEFAULT_GAME_ID = 426 - (_GAME_426_DAY - date.today()).days
_DEFAULT_CHUNK_SIZE = 100
_DDOS_LIMIT = 28000  # Contexto starts sending errors if we go over 20000 requests
_DEFAULT_START_INDEX = 1
_DEFAULT_END_INDEX = 25000


def handle_args() -> tuple[int, int, str, int]:
    """Parse arguments using `argparse` library. Returns the args object"""
    parser = argparse.ArgumentParser(
        prog="CollectRankings",
        description="Collect the contexto.me rankings for each word in our default dictionary (24k English words)",
        epilog=f"path to dictionary: {words_alpha_filtered()}",
    )

    parser.add_argument(
        "--id",
        help="id of the game to collect data for",
        type=int,
        default=_DEFAULT_GAME_ID,
    )

    parser.add_argument(
        "--chunk-size",
        help="Size of batch of API requests. Default 100.",
        type=int,
        default=_DEFAULT_CHUNK_SIZE,
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
        "--limit",
        help="Limit the number of requests to make. Default None.",
        type=int,
        default=None,
    )

    parser.add_argument(
        "--dict",
        help="Path to the input dictionary text file.",
        type=str,
        default=words_alpha_filtered(),
    )

    # -------------------------------- Parameters -------------------------------- #
    return parser.parse_args()


def main():
    """Collect scores for a given day."""
    args = handle_args()

    game_id = args.id
    chunk_size = args.chunk_size
    dictionary_file = args.dict
    word_limit = args.word_limit
    start_index = args.to - 1
    end_index = args._from

    # ----------------------------- Send API requests ---------------------------- #
    all_words = get_words(dictionary_file, word_limit)
    words = all_words[start_index:end_index]
    urls = get_urls(words, game_id)

    print(
        "Gathering scores for words \n[{}]: {} \n\t.\n\t.\n\t. \n[{}]: {}".format(
            start_index, words[0], end_index, words[-1]
        )
    )
    print("source word list: {}".format(dictionary_file))

    responses = make_api_requests(urls, chunk_size)

    # ----------------------------- Process responses ---------------------------- #
    word_rankings = {}
    exception_count = 0

    for response in responses:
        try:
            lemma, rank = extract_word_rank(response)
            word_rankings[lemma] = rank
        except Exception as e:
            print(f"Unexpected network error! {e}")
            exception_count += 1

    # ------------------------------- Write to csv ------------------------------- #
    output_csv = f"rankings_{game_id}_{start_index}_{end_index}.csv"
    with open(output_csv, "w") as csv:

        csv.write("word, rank\n")

        for w in words:
            csv.write(f"{w}, {word_rankings[w]}\n")

    print("Number of exceptions: {}".format(exception_count))


if __name__ == "__main__":
    main()
