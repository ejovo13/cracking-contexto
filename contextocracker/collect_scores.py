"""Script to collect the scores using our dictionary with 12,000 words."""

import argparse
from datetime import date

from .data_collection_async import (
    extract_word_rank,
    get_urls,
    get_words,
    make_api_requests,
)
from .resources import nltk_path

# nov 18 2023 corresponds to the game id: 426
_GAME_426_DAY = date.fromisoformat("2023-11-18")
_DEFAULT_GAME_ID = 426 - (_GAME_426_DAY - date.today()).days
_DEFAULT_CHUNK_SIZE = 100
_DDOS_LIMIT = 28000  # Contexto starts sending errors if we go over 20000 requests


def handle_args() -> tuple[int, int, str, int]:
    """Parse arguments using `argparse` library. Returns the tuple (game_id, chunk_size, dictionary_file, word_limit)"""

    parser = argparse.ArgumentParser(
        prog="CollectRankings",
        description="Collect the contexto.me rankings for each word in our default dictionary (24k English words)",
        epilog=f"path to dictionary: {nltk_path()}",
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
        "--limit",
        help="Limit the number of requests to make. Default None.",
        type=int,
        default=None,
    )

    parser.add_argument(
        "--dict",
        help="Path to the input dictionary text file.",
        type=str,
        default=nltk_path(),
    )

    # -------------------------------- Parameters -------------------------------- #
    args = parser.parse_args()

    return args.id, args.chunk_size, args.dict, args.limit


def main():
    """Collect scores for a given day"""

    game_id, chunk_size, dictionary_file, word_limit = handle_args()

    # ----------------------------- Send API requests ---------------------------- #
    words = get_words(dictionary_file, word_limit)
    urls = get_urls(words, game_id)
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
    output_csv = f"rankings_{game_id}.csv"
    with open(output_csv, "w") as csv:

        csv.write("word, rank\n")

        for w in words:
            csv.write(f"{w}, {word_rankings[w]}\n")

    print("Number of exceptions: {}".format(exception_count))


if __name__ == "__main__":
    main()
