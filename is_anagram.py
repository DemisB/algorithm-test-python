def is_anagram(s1, s2):
    """
    Write an algorithm that returns whether s1 and s2 are anagrams of each other, i.e.
    if s1 and s2 contain the same letters in a possibly different order.
    E.g.: "abc" and "cab" are anagrams, "aab" and "bba" are not.
    :param s1: string
    :param s2: string
    :return: True or False
    """

    def build_counter(word):
        counter = {}
        for letter in word:
            counter[letter] = counter.get(letter, 0) + 1
        return counter

    letter_counter_1 = build_counter(s1)
    letter_counter_2 = build_counter(s2)

    return letter_counter_1 == letter_counter_2
