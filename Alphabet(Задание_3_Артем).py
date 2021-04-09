class Alphabet:

    def __init__(self, language):
        self.language = language



    def english(self):
        alphabet_string = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                           's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        for index in alphabet_string:
            print(index, end=" ")
        print("\nВ английском алфавите", len(alphabet_string), "символов.")


language = Alphabet("english")
language.english()