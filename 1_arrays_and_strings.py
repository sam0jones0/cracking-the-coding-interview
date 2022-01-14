# 1. Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures?

# BCR: O(n): Have to check each character.

# With data structures:
# Place each char in s into a set. Return len(set) == len(s)

from typing import List


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
# 5. There are three types of edits that can be performed on strings: insert a
# character, remove a character, or replace a character. Given two strings,
# write a function to check if they are one edit (or zero edits) away.


def one_away(s1: str, s2: str) -> bool:
    if abs(len(s1) - len(s2)) > 1:
        return False

    if len(s1) > len(s2):  # Removal
        res = removed_insertion(s1, s2)
    elif len(s1) < len(s2):  # Insertion
        res = removed_insertion(s2, s1)
    else:  # Replacement
        res = replaced(s1, s2)

    return res


def removed_insertion(s1: str, s2: str) -> bool:
    s1_idx = 0
    s2_idx = 0
    found_difference = False
    while s2_idx <= len(s2) - 1:
        if s1[s1_idx] != s2[s2_idx]:
            if not found_difference:
                found_difference = True
                s1_idx += 1
            else:
                return False
        else:
            s1_idx += 1
            s2_idx += 1

    return True


def replaced(s1: str, s2: str) -> bool:
    found_difference = False
    for c1, c2 in zip(s1, s2):
        if c1 != c2:
            if not found_difference:
                found_difference = True
            else:
                return False

    return True


# print(one_away("pale", "sale"))


# ----
# 6. String Compression: Implement a method to perform basic string compression using the counts
# of repeated characters. For example, the string aabcccccaaa would become a2b1c5a3. If the
# "compressed" string would not become smaller than the original string, your method should return
# the original string. You can assume the string has only uppercase and lowercase letters (a - z).


def string_compression(s: str) -> str:
    res = []
    count = 0
    cur_char = s[0]
    for char in s:
        if char == cur_char:
            count += 1
        else:
            res.append(f"{cur_char}{count}")
            count = 1
            cur_char = char
    res.append(f"{cur_char}{count}")
    final_str = "".join(res)

    return final_str if len(final_str) < len(s) else s


# print(string_compression("aabcccccaadddddddddde"))


# ----
# 7. Rotate Matrix: Given an image represented by an NxN matrix, where each  pixel in the image is 4
# bytes, write a method to rotate the image by 90 degrees. Can you do this in place?


def rotate_matrix(matrix: List[List]) -> List[List]:
    if len(matrix) != len(matrix[0]):
        raise ValueError("Matrix must be square.")

    n = len(matrix) - 1
    for offset in range(0, (n // 2) + 1):
        for x in range(offset, n - offset):
            temp = matrix[offset][x]
            # top_left = bot_left
            matrix[offset][x] = matrix[n - x][offset]
            # bot_left = bot_right
            matrix[n - x][offset] = matrix[n - offset][n - x]
            # bot_right = top_right
            matrix[n - offset][n - x] = matrix[x][n - offset]
            # top_right = top_left
            matrix[x][n - offset] = temp

    return matrix


def gen_matrix(n):
    return [[f"{x}{y}" for y in range(n)] for x in range(n)]


# print(rotate_matrix(gen_matrix(10)))

# matrix = [
#     ["00", "01", "02", "03", "04"],
#     ["10", "11", "12", "13", "14"],
#     ["20", "21", "22", "23", "24"],
#     ["30", "31", "32", "33", "34"],
#     ["40", "41", "42", "43", "44"],
# ]
#
#
# rot_matrix = [
#     ["40", "30", "20", "10", "00"],
#     ["41", "31", "21", "11", "01"],
#     ["42", "32", "22", "12", "02"],
#     ["43", "33", "23", "13", "03"],
#     ["44", "34", "24", "14", "04"],
# ]


# Or for a square image:

from PIL import Image


def rotate_image(im: Image) -> None:
    if im.width != im.height:
        raise ValueError("Image must be square.")

    im2 = Image.new("RGB", (im.width, im.height))
    n = im.width - 1
    for offset in range(0, (n // 2) + 1):
        for x in range(offset, n - offset):
            temp = im.getpixel((offset, x))
            # top_left = bot_left
            im2.putpixel((offset, x), im.getpixel((n - x, offset)))
            # bot_left = bot_right
            im2.putpixel((n - x, offset), im.getpixel((n - offset, n - x)))
            # bot_right = top_right
            im2.putpixel((n - offset, n - x), im.getpixel((x, n - offset)))
            # top_right = top_left
            im2.putpixel((x, n - offset), temp)

    im2.save("rot-image.jpg")

    return im


def rot_image(path_str: str) -> None:
    im = Image.open(path_str)
    rotate_matrix(im)
    print("Done... ", im)


# rot_image("girl-500x500.jpg")

# ----
# 8. Zero Matrix: Write an algorithm such that if an element in an MxN  matrix is 0,
# its entire row and column are set to O.

import random


def zero_matrix(matrix: List[List]) -> List[List]:
    print(f"original_matrix={matrix}\n")

    max_row = len(matrix)
    max_col = len(matrix[0])

    for row in range(max_row):
        if matrix[row][0] == -1:
            continue
        for col in range(max_col):
            if matrix[row][col] == 0:
                matrix[row][0], matrix[0][col] = -1, -1

    for row in range(1, max_row):
        if matrix[row][0] == -1:
            for col in range(max_col):
                matrix[row][col] = 0

    for col in range(max_col):
        if matrix[0][col] == -1:
            for row in range(max_row):
                matrix[row][col] = 0

    print(f"zero_matrix={matrix}\n")
    return matrix


def gen_random_matrix(n):
    return [[random.randint(0, 20) for y in range(n)] for x in range(n)]


# zero_matrix(gen_random_matrix(5))

# original_matrix = [
#     [18, 4, 10, 2, 15],
#     [1, 0, 16, 12, 1],
#     [2, 13, 8, 3, 19],
#     [10, 19, 13, 6, 13],
#     [13, 13, 0, 20, 0],
# ]
#
# zero_matrix = [
#     [18, 0, 0, 2, 0],
#     [0, 0, 0, 0, 0],
#     [2, 0, 0, 3, 0],
#     [10, 0, 0, 6, 0],
#     [0, 0, 0, 0, 0],
# ]


# ----
# 9. String Rotation: Assume you have a method isSubstring which checks if one word is a substring
# of another. Given two strings, 51 and 52, write code to check if 52 is a rotation of 51 using only one
# call to isSubstring (e.g., "waterbottle" is a rotation of "erbottlewat").


def string_rot_substring(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False

    return s1 in s2 + s2


# print(string_rot_substring("waterbottle", "erbottlewat"))
