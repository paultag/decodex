
from decodex.utils.words import Words

def test_word():
    w = Words('american-english')
    for gram in w.anagram("topgears"):
        print gram
