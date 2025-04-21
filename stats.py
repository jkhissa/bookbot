def get_num_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    letters = {}
    for letter in text:
        lower_letter = letter.lower()
        if lower_letter not in letters:
            letters[lower_letter] = 0
        letters[lower_letter] += 1
    return letters

def sort_on(dictionary):
    return dictionary["count"]

def report(letters):
    list_of_dics=[{"char":k,"count":v} for k,v in letters.items()]
    list_of_dics.sort(reverse=True, key=sort_on)
    return list_of_dics


