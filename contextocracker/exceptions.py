"""Exceptions that can occur when making API requests."""

class WordNotFound(Exception):
    """Used when contexto responds: "I'm sorry, I don't know this word"."""

class WordTooCommon(Exception):
    """Used when contexto responds: "This word doesn't count, it's too common"."""

class WordDoesNotCount(Exception):
    """Used when contexto doesn't like the word. For example, "negro"."""

class LemmaAlreadyUsed(Exception):
    """Indicates that a word in our word list is redundant."""