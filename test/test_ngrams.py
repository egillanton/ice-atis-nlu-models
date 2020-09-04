import pytest
from scripts.ngrams import Unigram, Bigram, Trigram
from utils.get_data import get_ice_atis, strip_BOS_EOS_tokens, get_most_common_label, save_model, load_model


@pytest.fixture
def get_data():
    train_data, _, _ = get_ice_atis()
    tokens, labels = strip_BOS_EOS_tokens(
        map(lambda x: x['tokens'], train_data), list(
            map(lambda x: x['labels'], train_data)))
    return [tokens, labels]


def test_unigram(get_data):
    tokens = get_data[0]
    labels = get_data[1]
    unigram = Unigram(tokens, labels)
    unigram_test_token = "boston"
    unigram_test_label = get_most_common_label(unigram_test_token, unigram)

    assert unigram_test_label == "B-fromloc.city_name"


def test_bigram(get_data):
    tokens = get_data[0]
    labels = get_data[1]
    bigram = Bigram(tokens, labels)
    bigram_test_tokens = ('til', 'boston')
    bigram_test_label = get_most_common_label(bigram_test_tokens, bigram)

    assert bigram_test_label == "B-toloc.city_name"


def test_trigram(get_data):
    tokens = get_data[0]
    labels = get_data[1]
    trigram = Trigram(tokens, labels)
    trigram_test_tokens = ('til', 'boston', 'frá')
    trigram_test_label = get_most_common_label(trigram_test_tokens, trigram)

    assert trigram_test_label == "B-toloc.city_name"


def test_pickle(get_data):
    tokens = get_data[0]
    labels = get_data[1]
    trigram = Trigram(tokens, labels)
    file_name = "models/ngram.trigram.pickle"
    save_model(trigram, file_name)
    loaded_model = load_model(file_name)
    trigram_test_tokens = ('til', 'boston', 'frá')
    trigram_test_label = get_most_common_label(trigram_test_tokens, loaded_model)

    assert trigram_test_label == "B-toloc.city_name"
