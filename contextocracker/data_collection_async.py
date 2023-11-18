import grequests
import requests

from .exceptions import *

def get_words(input_file: str) -> list[str]:
    """Get a list of words from `input_file`."""
    with open(input_file) as words:

        lines = words.readlines()
        words = [line.strip("\n") for line in lines]

    return words


def get_urls(words: list[str], game_id: int, language_code = "en") -> list[str]:
    """Get a list of urls, one for each word in `words`."""
    def api_call(word: str) -> str:
        """Return the url of a single API call."""
        preformat_api_str = "https://api.contexto.me/machado/{}/game/{}/{}"
        return preformat_api_str.format(language_code, game_id, word)

    return [api_call(word) for word in words]

def extract_word_rank(response: requests.Response) -> tuple[str, int]:
    """Extract the lemma and rank of a word from an API request.

    Raises WordNotFound, WordTooCommon, or WordDoesNotCount on an error"""

    response_dict = response.json()

    if "error" in response_dict:
        error_message = response_dict["error"]

        if error_message == "This word doesn't count, it's too common": raise WordTooCommon()
        if error_message == "I'm sorry, I don't know this word": raise WordNotFound()
        if error_message == "This word doesn't count": raise WordDoesNotCount()

    stem = response_dict["lemma"]
    word_score = response_dict["distance"]

    return (stem, word_score)


def main():
    """Extract a filtered list of words that don't return an error when making contexto API calls."""

    # -------------------------------- Parameters -------------------------------- #
    request_limit = 20000
    chunk_size = 100
    dictionary_file = "nltk_common_words_20000.txt"
    game_id = 425

    filtered_output = "nltk_filtered.txt"
    failed_words = "nltk_failed.csv"


    # ----------------------------- Sending requests ----------------------------- #
    words = get_words(dictionary_file)
    urls = get_urls(words, game_id)
    response_chunks = [] # List of response chunks, needs to be flattened later!

    pos = 0
    while pos < request_limit:

        final_pos = pos + chunk_size

        request_chunk = [grequests.get(u) for u in urls[pos:final_pos]]
        response_chunks.append(grequests.map(request_chunk))

        print("Processed chunk of {} requests! ({:.1f}%)".format(
                                                                 chunk_size,
                                                                 float(final_pos / request_limit) * 100
                                                                )
        )
        pos += chunk_size


    # Flatten responses into a single list
    responses = [x for chunk in response_chunks for x in chunk]


    # ----------------------------- Handle Responses ----------------------------- #
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
    print("Handled {} total requests!".format(request_limit))

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




if __name__ == '__main__':
    main()
