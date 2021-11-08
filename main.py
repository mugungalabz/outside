import requests
import hashlib
from spellutil import mispelled

"""
Calls the outside API for a body of text, and checks for spelling errors.

Return the MD5 of the concatenated misspelled words.
"""
response = requests.get('https://outside-interview.herokuapp.com/document')
if response.status_code not in range(200, 299):
    print('Error retrieving text:', response.status_code)
    exit()

mispelled_words = mispelled(response.text)

print(mispelled_words)
print(hashlib.md5(mispelled_words).encode('utf-8').hexdigest())
