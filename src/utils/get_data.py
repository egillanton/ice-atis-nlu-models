import sys
import re
import pathlib
import random
from random import sample
from itertools import chain
import operator
import nltk
from nltk import ngrams
from collections import defaultdict


def clean_tokens(tokens):
    # Remove any unwanted symbols
    # tokens = re.sub(':', '', tokens)

    # Replace any Digits with the DIGIT token
    tokens = re.sub(r'\d+', 'DIGIT', tokens)

    return tokens


def strip_BOS_EOS_tokens(tokens, labels):
    """
    Removes the BOS and EOS tokens and their corresponding O label.

    strip_BOS_EOS_tokens('BOS text . . . text EOS', 'O X . . . X O')
    > 'text . . . text', 'X . . . X'
    """

    new_tokens = [' '.join(x.split(' ')[1:-1]).strip() for x in tokens]
    new_labels = [' '.join(x.split(' ')[1:-1]).strip() for x in labels]

    return new_tokens, new_labels


def get_ice_atis(data_dir="./ice-atis/ICE-ATIS/", train_data_name="ice_atis.train.w-intent.iob", test_data_name="ice_atis.test.w-intent.iob"):
    train_file = pathlib.Path(data_dir + train_data_name)
    test_file = pathlib.Path(data_dir + test_data_name)

    if not train_file.exists() or not test_file.exists():
        raise FileNotFoundError

    train_data = []
    test_data = []

    dicts = {
        "token2idx": {},
        "label2idx": {},
        "intent2idx": {},
        "idx2token": {},
        "idx2label": {},
        "idx2intent": {},
    }

    with train_file.open(encoding="utf-8") as file:
        for line in file:
            tokens, labels, intent = line.split('\t')
            tokens = clean_tokens(tokens)
            train_data.append(
                {"tokens": tokens.strip(), "labels": labels.strip(), "intent": intent.strip()})

    with test_file.open(encoding="utf-8") as file:
        for line in file:
            tokens, labels, intent = line.split('\t')
            tokens = clean_tokens(tokens)
            test_data.append(
                {"tokens": tokens.strip(), "labels": labels.strip(), "intent": intent.strip()})

    token_idx = 0
    label_idx = 0
    intent_idx = 0

    for pair in chain(train_data, test_data):
        tokens = [x.strip() for x in pair['tokens'].split(' ')]
        labels = [x.strip() for x in pair['labels'].split(' ')]
        intent = pair['intent'].strip()

        for token in tokens:
            if token not in dicts['token2idx']:
                if token_idx == 1469:
                    print(pair['tokens'])
                dicts['token2idx'][token] = token_idx
                token_idx += 1

        for label in labels:
            if label not in dicts['label2idx']:
                dicts['label2idx'][label] = label_idx
                label_idx += 1

        if intent not in dicts['intent2idx']:
            dicts['intent2idx'][intent] = intent_idx
            intent_idx += 1

        dicts['idx2token'] = {dicts['token2idx']
                              [k]: k for k in dicts['token2idx']}
        dicts['idx2label'] = {dicts['label2idx']
                              [k]: k for k in dicts['label2idx']}
        dicts['idx2intent'] = {dicts['intent2idx']
                               [k]: k for k in dicts['intent2idx']}

    return train_data, test_data, dicts


def get_most_common_label(tokens, ngram_freqs):
    defult_label = "O"
    try:
        labels = ngram_freqs[tokens].copy()
        max_label = max(labels.items(), key=operator.itemgetter(1))[0]
        return max_label
    except:
        return defult_label
