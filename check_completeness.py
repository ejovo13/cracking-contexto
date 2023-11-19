"""Verify that the winners of all 425 games are in our total set of words."""

from contextocracker.data_collection_async import (
    extract_word_rank,
    get_words,
    make_api_requests,
)
from contextocracker.resources import brown_and_alpha_filtered

all_words = set(get_words(brown_and_alpha_filtered()))

give_up_url = lambda game_id: f"https://api.contexto.me/machado/en/giveup/{game_id}"

# Get a list of all the winners up until 425
urls = [give_up_url(idx) for idx in range(0, 426)]
responses = make_api_requests(urls, chunk_size=50)

missing_words = []

for response in responses:
    try:
        lemma, rank = extract_word_rank(response)
        # print("winning word: {}".format(lemma))

        if lemma not in all_words:
            missing_words.append(lemma)

    except:
        print("Something went wrong!")

print(missing_words)
