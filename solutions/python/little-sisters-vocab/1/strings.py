"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word):
    return 'un'+word


def make_word_groups(vocab_words):
    prefix = vocab_words[0]
    new_vocab = ' :: '.join([prefix] + [prefix + word for word in vocab_words[1:]])
    return new_vocab


def remove_suffix_ness(word):
    new_word = word [:-4]
    if new_word[-1] == 'i':
        return new_word[:-1]+'y'
    return new_word

def adjective_to_verb(sentence, index):
    words = sentence.split()
    word = words[index].rstrip('.')
    return word + 'en'
 