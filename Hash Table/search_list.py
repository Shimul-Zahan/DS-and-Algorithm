# ------ process-1 ---------
# ------ big O(n^2) ----------
# def match_list(list1, list2):
#     for i in list1:
#         for j in list2:
#             if i == j:
#                 return True
#     return False


# ------ process-2 ---------
# ------ big O(n) ----------
# def match_list(list1, list2):
#     my_dictionary = {}
#     for i in list1:
#         my_dictionary[i] = True
    
#     for j in list2:
#         if j in my_dictionary:
#             return True
#     return False

# list1 = [1, 2, 3, 4, 5]
# list2 = [8, 9, 3]
# print(match_list(list1, list2))
    