# Cracking Contexto

Contexto is a word guessing game hosted at [https://contexto.me/](https://contexto.me/)

Here are the game's instructions, taken directly from their website:

> Find the secret word. You have unlimited guesses.
>
>The words were sorted by an artificial intelligence algorithm according to how similar they were to the secret word.
>
>After submitting a word, you will see its position. The secret word is number 1.
>
>The algorithm analyzed thousands of texts. It uses the context in which words are used to calculate the similarity between them.

The goal of this project is to come up with an algorithm that is able to automatically guess the correct word, in as few guesses as possible.

## Preliminary Analysis

Before thinking about writing a program to beat the game, we need to reflect on how the game is implemented in the first place. Using the language of a [one-way function](https://www.wikiwand.com/en/One-way_function), in this section we are going to talk about how the "forward direction" of contexto is computed and then we are going to reflect on strategies for "inverting" it.

### Forward Direction

The forward direction of contexto is quite easy to compute. In order to implement the core game's logic, all we need is a dictionary of words and a [word embedding](https://www.wikiwand.com/en/Word_embedding) on this set (word2vec, GloVe, etc.).

For each day, we execute the following algorithm:

1. Choose a random word from our data set in the upper echelon of most frequent words[^1]
2. Compute the distance between our chosen word and every other word in the dictionary
3. Sort all words based on their proximity to the hidden winner

The front-end API simply queries this pairing of words and their ranking for the given day.


[^1]: The randomly chosen word won't be uniformly random across the _entire_ dictionary of words. Contexto uses a word list of at least 80,000 words. If there was a chance of choosing words like "sv", "vei", "choy" (all valid Contexto words) then the game would be absolute crap! To further illustrate this point, the first five winners are: "banana", "neighborhood", "paper", "farm", and "address".

### Inverting

Proceeding in the opposite direction is far from trivial. Having only access the the distance between a word we guess and the hidden word, we have to navigate through a large-dimensional vector space to find the hidden word. There are multiple different approaches that we could take.

#### Brute force

Starting with a list of frequently used English words, guess every word on our list until we find the hidden word. This strategy completely disregards all the information retrieved from previous guesses. Pretending for a moment that all of the words in the 80,000[^2]-word dictionary are equally likely to be chosen, it would take us on average $ \frac{80,000 + 1}{2} \approx 40,000$ guesses to crack contexto - good thing we have unlimited guesses!

[^2]: I guess I haven't mentioned this yet, but contexto uses a dictionary with _at least_ 80,000 words!

#### "Triangulation"

This method

Consider the case of a 2-dimensional space. If one knows the coordinates of three guessed words and their distances between a hidden coordinate, you can unambiguously locate the coordinates of the hidden word. While this is not exactly

!!! note

    Maybe a visualization is in order?




## Phases

In order to solve this problem, our algorithm has been broken up into the following sections.

0. Word list establishment
1. Data collection
2. Model comparison
3. Training
4. Final algorithm

Each phase has a detailed explanation of implementation details and the problems that were faced when writing `contextocracker`. Check out each phase's dedicated page for an in-depth discussion.
