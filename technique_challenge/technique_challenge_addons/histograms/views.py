from rest_framework.views import APIView
from rest_framework.response import Response
import requests
from bs4 import BeautifulSoup
from collections import OrderedDict
import itertools
def word_count(sentence):
    """
    Word Counter

    Given an body of text, return a hash table of the frequency of
    each word.

    ..  warnings::

        - Capital and lower case versions of the same word should be counted

    as the same word.

        - Remove punctuations from all words.

    ..  note::


    Where N is the number of characters in the string.

        - Time: O(N)

        - Space: O(N)

    :Example:

    >>> word_count('The cat and the hat.')
    {'the': 2, 'cat': 1, 'and': 1, 'hat': 1}
    >>> word_count('As soon as possible.')
    {'as': 2, 'soon': 1, 'possible': 1}
    >>> word_count("It's a man, it's a plane, it's superman!")
    {'its': 3, 'a': 2, 'man': 1, 'plane': 1, 'superman': 1}

    :param sentence: Input string
    :type sentence: str

    :return: Returns hash-table of frequence of each word in input
    :rtype: dict
    """

    translate = sentence.maketrans({char: None for char in "'.,:*!|/^';/><&+=-)(~`@#$^1234567890"})
    cleaned_words = sentence.lower().translate(translate).split()
    word_counter = {}
    for word in cleaned_words:
        if word in word_counter:
            word_counter[word] += 1
        else:
            word_counter[word] = 1
    return word_counter

class HistogramsView(APIView):



	def get(self, request, format=None):
		url = request.GET.get('url')
		page = requests.get(url)
		clean_text = ' '.join(BeautifulSoup(page.content, "html.parser").stripped_strings)
		histogramsAll = word_count(clean_text)
		histogramSorted = {k: v for k, v in sorted(histogramsAll.items(), key=lambda item: item[1], reverse=True)}
		sliceOrderedDict = OrderedDict(itertools.islice(histogramSorted.items(), 100))
		return Response(sliceOrderedDict)
