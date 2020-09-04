from scripts.ngrams import Ngram

def test_ngram_model():
	ngram = Ngram()
	assert ngram.count == 0