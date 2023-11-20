"""Verify that the winners of all 425 games are in our total set of words."""

from contextocracker.data_collection_async import (
    extract_word_rank,
    get_words,
    make_api_requests,
)
from contextocracker.resources import brown_and_alpha_filtered, winning_words

def retrieve_winning_words(game_id: int) -> list[str]:
    """Retrieve a list of winning words up until game number `game_id`."""
    give_up_url = lambda game_id: f"https://api.contexto.me/machado/en/giveup/{game_id}"

    # Get a list of all the winners up until 425
    urls = [give_up_url(idx) for idx in range(0, game_id)]
    responses = make_api_requests(urls, chunk_size=50)
    winning_ranks = [extract_word_rank(response) for response in responses]
    return [w for w, _ in winning_ranks]

def missing_words(word_list_path: str = brown_and_alpha_filtered()) -> list[str]:
    """Return a list of winning words that don't appear in brown_and_alpha_filtered."""

    all_words = set(get_words(word_list_path))
    winners = winning_words()
    return [lemma for lemma in winners if lemma not in all_words]

if __name__ == '__main__':
    print(missing_words())
    print(missing_words("top_3000.txt"))

    print(len(missing_words("top_3000.txt")))


