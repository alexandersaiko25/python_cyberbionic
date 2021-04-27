def sort_words():
    words_in_text = input("Введите Ваш текст: ")
    print(words_in_text)
    sort_list = sorted(words_in_text.split())
    print(sort_list)

sort_words()