# Take Skip
Create a class called take_skip. Upon initialization, it should receive a step (int) and a count (int). Implement the __iter__ and __next__ functions. The iterator should return the count numbers (starting from 0) with the given step.

# Dictionary Iterator
Create a class called dictionary_iter. Upon initialization, it should receive a dictionary object. Implement the iterator to return each key-value pair of the dictionary as a tuple of two elements (the key and the value).

# Countdown Iterator
Create a class called countdown_iterator. Upon initialization, it should receive a count. Implement the iterator to return each countdown number (from count to 0 inclusive), separated by a single space.

# Sequence Repeat
Create a class called sequence_repeat which should receive a sequence and a number upon initialization. Implement an iterator to return the given elements, so they form a string with a length - the given number. If the number is greater than the number of elements, then the sequence repeats as necessary.

# Take Halves
You are given a skeleton with the following code:

Implement the three generator functions:
- integers() - generates an infinite amount of integers (starting from 1)
- halves() - generates the halves of those integers (each integer / 2)
- take(n, seq) - takes the first n halves of those integers