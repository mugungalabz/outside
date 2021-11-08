from nltk.tokenize import TweetTokenizer
import requests


def mispelled(text):
    """
    This function tokenizes the input text and returns concatenated 
    string of all the mispelled words determine by the Outside api

    TweetTokenizer handles all the requirements except for tokenizing words
    separated with a dash.
    """
    correctly_spelled_words = set()
    incorrectly_spelled_words = set()
    mispelled_words_concatenated = str("")
    tknzr = TweetTokenizer()

    def checktoken(t):
        nonlocal mispelled_words_concatenated
        if len(t) >= 3 or t.isalnum():
            if t in correctly_spelled_words:
                return
            if t in incorrectly_spelled_words:
                mispelled_words_concatenated += t
                return
            print("looking up:", t)
            response = requests.get(
                'https://outside-interview.herokuapp.com/spelling/' + t)
            if response.status_code == 204:
                correctly_spelled_words.add(t)
            elif response.status_code == 404:
                incorrectly_spelled_words.add(t)
                mispelled_words_concatenated += t
            else:
                print('Error, unexpected error code from api:',
                      response.status_code)

    tokens = tknzr.tokenize(text)
    for t in tokens:
        if '-' in t:
            for x in t.split('-'):
                checktoken(x)
        else:
            checktoken(t)
    print(mispelled_words_concatenated)
    print(len(correctly_spelled_words))
    print(len(incorrectly_spelled_words))
    return mispelled_words_concatenated
