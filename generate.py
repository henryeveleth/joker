#! /usr/bin/env python3
import os
import sys
import re

import spacy
import markovify

big_model = None
nlp = spacy.load("en")


def sanitize(string):
    no_brackets = re.sub(r'\[.*\]', '', string)
    no_parens = re.sub(r'\(.*\)', '', no_brackets)
    return no_parens.replace('…', '')


class POSifiedText(markovify.Text):
    def word_split(self, sentence):
        return ['::'.join((word.orth_, word.pos_)) for word in nlp(sentence)]

    def word_join(self, words):
        sentence = ' '.join(word.split('::')[0] for word in words)
        return sentence


directory = sys.argv[1]
outfile = sys.argv[2]
for (dirpath, _, filenames) in os.walk(directory):
    for filename in filenames:
        with open(os.path.join(dirpath, filename)) as f:
            text = sanitize(f.read())

            print('generating model for {}/{}'.format(dirpath, filename))
            model = POSifiedText(text, retain_original=False)

            if big_model:
                big_model = markovify.combine(models=[big_model, model])
            else:
                big_model = model

with open(os.path.join('models', outfile), 'w') as f:
    f.write(big_model.to_json())
