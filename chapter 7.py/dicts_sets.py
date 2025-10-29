# # dictionaries
# # A dictionary is a collection of key-value pairs
# # A dictionary is created by placing a comma-separated sequence of key-value pairs within curly braces
# band = {
#     "name": "The Beatles",
#     "members": ["John Lennon", "Paul McCartney", "George Harrison", "Ringo Starr"],
# }
# band2 = dict(
#     name="The Beatles",
#     members=["John Lennon", "Paul McCartney", "George Harrison", "Ringo Starr"],
# )


# # # print(band)
# # print(band2)
# # print(band["name"])
# # print(band["members"])
# # print(type(band))
# # print(type(band2))
# # print(len(band))

# # acess items in a dictionary
# print(band["name"])
# print(band.get("members"))

# # list all keys in a dictionary
# print(band.keys())

# # list all values in a dictionary
# print(band.values())

# # list all items in a dictionary
# print(band.items())

# # verify if a key exists in a dictionary
# print("name" in band)
# print("age" in band)

# # change a value in a dictionary
# band["name"] = "The cowboys"
# band.update({"bass": "john"})
# print(band)

# # # remove a key-value pair from a dictionary
# # print(band.pop("bass"))
# # print(band)

# # band["drummer"] = "Ringo Starr"
# # print(band)

# # print(band.popitem())  # tuple
# # print(band)

# # # delete a key-value pair from a dictionary
# # band["drummer"] = "Ringo Starr"
# # del band["drummer"]
# # print(band)

# # # clear a dictionary
# # band2.clear()
# # print(band2)

# # # copy a dictionary
# # band2 = band  # crete a reference
# # print("bad copy!")
# # print(band2)
# # print(band)

# # band2 = band.copy()  # create a copy
# # band2["name"] = "The Beatles"
# # print("good copy!")
# # print(band)
# # print(band2)

# # # dictionary constructors
# # band3 = dict(band)
# # print("good copy!")
# # print(band3)

# # nested dictionaries
# band4 = {
#     "name": "The Royals",
#     "members": {
#         "John Lennon": {
#             "instrument": "guitar",
#             "birth_year": 1940,
#         },
#         "Paul McCartney": {
#             "instrument": "bass",
#             "birth_year": 1942,
#         },
#         "George Harrison": {
#             "instrument": "guitar",
#             "birth_year": 1943,
#         },
#         "Ringo Starr": {
#             "instrument": "drums",
#             "birth_year": 1940,
#         },
#     },
# }

# band5 = {
#     "name": "The cowboys",
#     "members": {
#         "moses Faraday": {
#             "instrument": "piono",
#             "birth_year": 1960,
#         },
#         "Bob Dowel": {
#             "instrument": "violin",
#             "birth_year": 1940,
#         },
#         "Peter Owen": {
#             "instrument": "sax",
#             "birth_year": 1953,
#         },
#         "Dickson James": {
#             "instrument": "taking drums",
#             "birth_year": 1950,
#         },
#     },
# }

# band = {
#     "band4": "The Royals",
#     "band5": "The cowboys",
# }
# print(band)
# print(band4)


# # sets
# # A set is a collection of unique elements
# # A set is created by placing a comma-separated sequence of elements within curly braces
# nums = {1, 2, 3, 4, 5}
# num2 = set((1, 2, 3, 4, 5))
# # print(nums)
# # print(num2)
# # print(type(nums))
# # print(len(nums))

# no duplicates
nums = {1, 2, 3, 4, 5, 1, 2, 3}
# print(nums)

# true is a dupe of 1, false is a dupe of 0
nums({1, 2, 3, True, False})
print(nums)

# # check if an item is in a set
# print(1 in nums)
# print(6 in nums)

# # add a new element to a set
# nums.add(6)
# print(nums)

# # add elements from another set
# nums.update({7, 8, 9})
# print(nums)


# # add elements from one set to another
# nums2 = {10, 11, 12}
# nums.update(nums2)
# print(nums)

# #'merge two sets' to create a new set
# nums3 = nums.union(nums2)
# print(nums3)

# # keep only duplicates
# nums4 = nums.intersection(nums2)
# print(nums4)

# # keep everything except duplicates
# nums5 = nums.difference(nums2)
# print(nums5)
