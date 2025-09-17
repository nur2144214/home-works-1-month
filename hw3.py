while True:
    vowels = "aeiouаеёиоуыэюя"
    consonants = "bcdfghjklmnpqrstvwxyzбвгджзйклмнпрстфхцчшщъь"
    vowels_count = 0
    consonants_count = 0
    word_len = 0
    word = input("Введите слово/или'выход'для выхода из программы: ")
    if word.lower() == "выход":
        print("выхожу из программы")
        break
    else:
        for i in word:
            if i.isalpha():
                word_len += 1
                if i.lower() in vowels:
                    vowels_count += 1
                elif i.lower() in consonants:
                    consonants_count += 1 
        print(f"слово:{word}\nколичество букв:{word_len}\nгласных букв:{vowels_count}\nсогласных букв:{consonants_count}")
        print(f"гласные/согланые {round(consonants_count*100/word_len, 2)}/{round(vowels_count*100/word_len, 2)}")

        