# 1. Implement an algorithm to determine if a string has all unique characters.
#   What if you cannot use additional data structures?

# BCR: O(n): Have to check each character.

# With data structures:
#   Place each char in s into a set. Return len(set) == len(s)

def uniq_chars(s: str) -> bool:
    return len(set(s)) == len(s)


# print(uniq_chars("thequickbrown"))


# ----
# 2. Given two strings, write a method to decide if one is a permutation of the other.

# BCR: O(s1+s2): Have to check each char in both strings.

from collections import Counter


def string_perm(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False
    return Counter(s1) == Counter(s2)


# print(string_perm("basiparachromatin", "marsipobranchiata"))


# ----
# 3. Write a method to replace all spaces in a string with '%20': You may assume that the string
# has sufficient space at the end to hold the additional characters, and that you are given the "true"
# length of the string.


def urlify(s: str) -> str:
    return "".join(["%20" if c == " " else c for c in s])


# print(urlify("Hi my name is sam    "))


# ----
# 4. Given a string, write a function to check if it is a permutation of a palindrome.
# A palindrome is a word or phrase that is  the same forwards and backwards. A permutation
# is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.


def palin_perm(s: str) -> bool:
    char_count = Counter([char.lower() for char in s])
    char_count.__delitem__(" ")
    odd_chars = 0
    for count in char_count.values():
        is_odd_count = count % 2 == 1
        if is_odd_count:
            if odd_chars == 0:
                odd_chars += 1
            else:
                return False

    return odd_chars <= 1


# print(palin_perm("Tact Cooooovvo"))


# ----
# 5.
