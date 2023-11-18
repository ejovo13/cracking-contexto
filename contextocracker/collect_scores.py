"""Script to collect the scores using our dictionary with 12,000 words."""

from datetime import datetime, date, timedelta
import argparse


from .resources import nltk_filtered_path


def main():
    """Collect scores for a given day"""

    parser = argparse.ArgumentParser(
                         prog="CollectRankings",
                         description="Collect the contexto.me rankings for each word in our default dictionary",
                         epilog="The default dictionary is 'nltk_filtered', a list of 12k common English words.")
    parser.add_argument("-g", "--game-id", help="id of the game to collect data for")
    args = parser.parse_args()

    if args.game_id:
        game_id = args.game_id

    else:
        # nov 18 2023 corresponds to the game id: 426
        game_426_day = date.fromisoformat("2023-11-18")
        default_game_id = 426 - (game_426_day - date.today()).days
        game_id = default_game_id

    print("Collecting data for game: {}".format(game_id))

    dictionary_file = nltk_filtered_path()

    print("using dictionary: {}".format(dictionary_file))




if __name__ == '__main__':
    main()
