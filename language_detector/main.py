# -*- coding: utf-8 -*-

"""This is the entry point of the program."""

from languages import LANGUAGES

def detect_language(text, languages):
    """Returns the detected language of given text."""
    # split text and save each word in a list
    words = text.split(' ')
    d = {'English': 0, 'Spanish': 0, 'German': 0}

    for word in words:
        for key in d:
            if word in [i.get('common_words') for i in LANGUAGES if i.get('name')  == key][0]:
                d[key] += 1
    return max(d, key = d.get)