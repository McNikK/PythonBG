def int_func():
    sentence = str(input('Write a sentence in lowercase register: '))
    word_list = list(sentence.split(' '))
    for i in range(len(word_list)):
        word_list[i] = word_list[i].capitalize()
    print(' '.join(word_list))

int_func()