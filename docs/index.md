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

## Phases

In order to solve this problem, the algorithm has been broken up into various phases.

0. Word list establishment
1. Data collection
2. Model comparison
3. Training
4. Final algorithm

Each phase has a detailed explanation of implementation details and the problems that were faced when writing `contextocracker`. Check out each phase's dedicated page for a more in-depth discussion.