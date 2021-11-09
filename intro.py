# import math
#
# from tqdm import *
#
#
# def is_prime(n):
#     max_val = round(math.sqrt(n))
#     with tqdm(total=max_val) as pbar:
#         for i in trange(2, max_val):
#             if n % i == 0:
#                 return False
#             pbar.update(1)
#     return True
#
#
# print(is_prime(67280421310721))
#
# # 170141183460469231731687303715884105727
#
# ----
#
# def perms(str_: str, prefix: str):
#     if len(str_) == 0:
#         print(prefix)
#     else:
#         for i in range(len(str_)):
#             rem = str_[0:i] + str_[i+1:]
#             perms(rem, prefix + str_[i])
#
#
# perms("sam", "")
#
# ----
#
# def all_fib(n):
#     memo = [0 for i in range(n + 1)]
#     for i in range(n):
#         print(f"{i}: {_fib(i, memo)}")
#
#
# def _fib(n, memo):
#     if n <= 0:
#         return 0
#     elif n == 1:
#         return 1
#     elif memo[n] > 0:
#         return memo[n]
#
#     memo[n] = _fib(n-1, memo) + _fib(n-2, memo)
#     return memo[n]
#
#
# print(all_fib(10))
#
# ----
#
# class Max:
#     def __init__(self, powers):
#         self.max = 2**powers
#
#
# def powers_of_2(n, m):
#     if n > m.max:
#         return
#     else:
#         prev = powers_of_2(n * 2, m)
#         curr = int(n)
#         print(curr)
#         return curr
#
#
# powers_of_2(1, Max(500))
#
# ----
#
# def sqrt(n):
#     return sqrt_helper(n, 1, n)
#
# def sqrt_helper(n, min, max):
#     if max < min:
#         return -1
#     print(f"min: {min}, max: {max}")
#     guess = (min + max) // 2
#     print(guess)
#     print()
#     if guess * guess == n:
#         return guess
#     elif guess * guess < n:
#         return sqrt_helper(n, guess + 1, max)
#     else:
#         return sqrt_helper(n, min, guess - 1)
#
# print(sqrt(111222338559598866946777344))
#
# ----
#
# def sum_digits(n):
#     sum = 0
#     while n > 0:
#         print(n)
#         sum += n % 10
#         n //= 10
#     print()
#     return sum
#
# print(sum_digits(12349123))
#
# ----
#
# import random
#
#
# def diff_k(k, arr):
#     pairs = set()
#     hash_t_arr = {x: x for x in arr}
#     for item in arr:
#         temp = [hash_t_arr.get(item - k), hash_t_arr.get(item + k)]
#         pairs.update([frozenset([item, x]) for x in temp if x])
#
#     return list(map(tuple, pairs))
#
#
# arr = [random.randint(1, 1000) for i in range(100)]
#
# print(diff_k(2, arr))
#
# ----
#
# import timeit
#
# def solve_ab_eq_cd(n):
#     for a in range(1, n + 1):
#         for b in range(1, n + 1):
#             for c in range(1, n + 1):
#                 d = pow((a ** 3 + b ** 3 - c ** 3), 1 / 3)
#                 d = int(d) if isinstance(d, float) else d
#                 left = a ** 3 + b ** 3
#                 right = c ** 3 + d ** 3
#                 if left == right:
#                     print(f"ab: ({a}, {b})\t cd: ({c}, {d})")
#                     # break
#                     pass
#
#
# timed = timeit.repeat(lambda: solve_ab_eq_cd(10), repeat=5, number=100)
# average = sum(timed) / len(timed)
# print(average)
#
# # # 1: 0.63079764 (brute force)
# # # 2: 0.57837134 (added break)
# # # 3: 0.13155724 (compute d)


















