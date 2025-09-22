"""
Problem 1: Duplicate Tracker

You are given a collection of product IDs. Some IDs may appear more than once.
Write a function that returns True if any duplicates are found, and False otherwise.

Example:
Input: [10, 20, 30, 20, 40]
Output: True

Input: [1, 2, 3, 4, 5]
Output: False
"""


def has_duplicates(product_ids):
    # Using a set to track seen IDs allows O(1) average time complexity for insertions and lookups.
    seen = set()
    for pid in product_ids:
        if pid in seen:
            return True  # Duplicate found
        seen.add(pid)
    return False

# Justification:
# A set is ideal because it ensures constant-time membership checks. 
# We iterate through the list once (O(n)) and check/add each item in O(1), giving overall O(n) runtime.




"""
Problem 2: Order Manager

You need to maintain a list of tasks in the order they were added, and support removing tasks from the front.
Implement a class that supports add_task(task) and remove_oldest_task().

Example:
task_queue = TaskQueue()
task_queue.add_task("Email follow-up")
task_queue.add_task("Code review")
task_queue.remove_oldest_task() → "Email follow-up"
"""

class TaskQueue:
    def __init__(self):
        # Using a simple list to store tasks
        self.queue = []

    def add_task(self, task):
        # Add task to the end of the list
        self.queue.append(task)

    def remove_oldest_task(self):
        # Remove task from the front of the list
        if self.queue:
            return self.queue.pop(0)
        return None

# Justification:
# A list can act as a simple queue: append() adds to the end, pop(0) removes from the front.
# For small queues this is fine. append() is O(1), pop(0) is O(n), so overall runtime depends on queue size.



"""
Problem 3: Unique Value Counter

You receive a stream of integer values. At any point, you should be able to return the number of unique values seen so far.

Example:
tracker = UniqueTracker()
tracker.add(10)
tracker.add(20)
tracker.add(10)
tracker.get_unique_count() → 2
"""

class UniqueTracker:
    def __init__(self):
        # Using a set to store unique values ensures duplicates are ignored automatically
        self.unique_values = set()

    def add(self, value):
        self.unique_values.add(value)  # O(1) average time complexity

    def get_unique_count(self):
        return len(self.unique_values)  # Returns count of unique items in O(1)

# Justification:
# A set automatically allows constant-time insertion and size retrieval.
# This makes it efficient to track unique values as a stream with O(1) operations per add and count.
