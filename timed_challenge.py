
# Problem: Remove Duplicates (Keep Order)
# Return the values in the order, without any duplicates.
# Example:
# Input: ["apple", "banana", "apple", "kiwi", "banana"]
# Output: ["apple", "banana", "kiwi"]

def remove_duplicates_keep_order(items):
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result
# Test cases
print(remove_duplicates_keep_order(["apple", "banana", "apple", "kiwi", "banana"]))  # ["apple", "banana", "kiwi"]
print(remove_duplicates_keep_order([1, 2, 3, 2, 4, 1]))                               # [1, 2, 3, 4]
print(remove_duplicates_keep_order([]))                                              # []
print(remove_duplicates_keep_order(["a", "a", "a"]))                                  # ["a"]
print(remove_duplicates_keep_order([True, False, True, False]))                       # [True, False]


# For this problem, I chose to use a combination of a set and a list. The set is used to track which values have already been seen, and
# remove them. This combination of sets and list is able to remove duplicates while keeping the sequence the same. I chose this structure, because I used to do these problems all the time in highschool.
# This is one of the first problems you learn when you start to learn python. 
# The time limit influenced my decision to avoid more complex structures like nested loops, which could of taken me longer time to make.
# This approach balances efficiency with simpleness, which is important when working with a time constraint.
#  The primary trade-off under time pressure was that while using a set and list is very effective, it requires extra space to work with the number of unique elements.
# In a situation with very large datasets, this would cause some problems. I also prioritized clarity and readability over anything to crazy for a simple program.
# By choosing a simple way to this program, I avoided going over the time limit. I made sure to test edge cases like empty lists, repeated elements, and different data types quickly and confidently.