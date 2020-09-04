
def ngram_freqs(ngrams):
    """ Builds dict of token collocation and label frequencies """
    ngram_freqs = {}

    for ngram in ngrams:
        tokens = ngram[0]  # "BOS ég vil"
        label = ngram[1]   # "O"

        if tokens not in ngram_freqs:
            ngram_freqs[tokens] = {}

        if label not in ngram_freqs[tokens]:
            ngram_freqs[tokens][label] = 0

        ngram_freqs[tokens][label] += 1

    return ngram_freqs


def Unigram(tokens, labels):
    unigram_pairs = []
    for i in range(len(tokens)):
        unigram_pairs.extend(
            list(zip(tokens[i].split(" "), labels[i].split(" "))))
    return ngram_freqs(unigram_pairs)


def Bigram(tokens, labels):
    bigram_pairs = []
    for i in range(len(tokens)):
        _tokens = tokens[i].split(" ")
        tokens_before = _tokens.copy()
        tokens_before.insert(0, 'BOS')  # Begining of Sentance
        tokens_before.pop()  # remove last
        _labels = labels[i].split(" ")

        bigram_tokens = list(zip(zip(tokens_before, _tokens), _labels))
        bigram_pairs.extend(bigram_tokens)

    return ngram_freqs(bigram_pairs)


def Trigram(tokens, labels):
    trigram_pairs = []
    for i in range(len(tokens)):
        _tokens = tokens[i].split(" ")
        tokens_before = _tokens.copy()
        tokens_before.insert(0, 'BOS')  # Begining of Sentance
        tokens_before.pop()  # remove last element
        tokens_after = _tokens.copy()
        tokens_after.append('EOS')
        tokens_after.pop(0)  # remove first element
        _labels = labels[i].split(" ")
        trigram_tokens = list(
            zip(zip(tokens_before, _tokens, tokens_after), _labels))
        trigram_pairs.extend(trigram_tokens)
    return ngram_freqs(trigram_pairs)


if __name__ == "__main__":
    print("Scripts to us create Ngrams")
