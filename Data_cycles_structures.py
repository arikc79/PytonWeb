# 1

# from collections import Counter
#
# text = "aabbccc"
#
# freq = Counter(text)  # ++
#
# count_by_freq = Counter(freq.values())
#
# print(freq)
# print(count_by_freq)


# 2


# def is_zigzag(nums):
#     if len(nums) < 3:
#         return False
#
#     for i in range(len(nums) - 2):
#         a = nums[i]
#         b = nums[i + 1]
#         c = nums[i + 2]
#
#         if a == b or b == c:
#             return False
#
#         if a < b and not (b > c):
#             return False
#
#         if a > b and not (b < c):
#             return False
#
#     return True
#
#
# print(is_zigzag([1, 2, 3, 4]))
# print(is_zigzag([1, 3, 2, 4, 3]))
# print(is_zigzag([5, 1, 6, 2, 7]))

# 3

user1 = {"Alice", "Bob", "Charlie"}
user2 = {"Bob", "Diana", "Eve"}
result = set()

for name in user1:
    if name not in user2:
        result.add(name)

for name in user2:
    if name not in user1:
        result.add(name)

print(result)
