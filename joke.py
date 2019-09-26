#! /usr/bin/env python3
import re
import sys
import json

import markovify
import spacy

infile = sys.argv[1]

if len(sys.argv) >= 3:
    jokes = int(sys.argv[2])
else:
    jokes = 5

with open(infile) as f:
    data = f.read()


nlp = spacy.load('en')


def join_punctuation(seq, characters='.,;?!'):
    characters = set(characters)
    seq = iter(seq)
    current = next(seq)

    for nxt in seq:
        if nxt in characters:
            current += nxt
        else:
            yield current
            current = nxt

    yield current


class POSifiedText(markovify.Text):
    def word_split(self, sentence):
        return ['::'.join((word.orth_, word.pos_)) for word in nlp(sentence)]

    def word_join(self, words):
        if ' ' in words:
            words.remove(' ')

        sentence = ' '.join(join_punctuation(
            word.split('::')[0] for word in words))
        return sentence


big_model = POSifiedText.from_json(data)

for i in range(jokes):
    sentence = big_model.make_sentence()
    sentence = sentence.replace('”', '').replace('“', '')
    print(sentence)
