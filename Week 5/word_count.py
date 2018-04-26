
different_words = {}
text = input("Enter a string:  ")
words = text.split()
for word in words:
    try:
        different_words[word] += 1
    except KeyError:
        different_words[word] = 1

word_list = list(different_words.keys())
word_list.sort()
max_word_length = max((len(word) for word in words))
for word in word_list:
    print("{:{}} : }".format(word, max_word_length, different_words[word]))