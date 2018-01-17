# Python Practice Problems

This repository is a collection of python practice problems from interview questions, code katas, pyjam, or anything I felt was interesting. Each .py file has a corresponding test file located in /tests as well as a description as a part of README.md to explain the problem.

You can run all tests by entering:
`py.test`

or running a specific test by entering:
`py.test tests/test_name_file.py`

At first pass I attempt to solve the practice problem as quickly as possible and adhere to a [shameless green](https://www.sandimetz.com/99bottles/sample/#_shameless_green) philosophy.

I will then attempt to optimize the practice problem in regards to space and time by adding much larger test cases and provide benchmarking.

I will eventually be breaking down my process on my website: [scottyabrown](http://scottyabrown.com)

Thanks for visiting.

## Problem List

### Bubble Sort

Bubble sort is a simple sorting algorithm that repeatedly steps through the list to be sorted, compares each pair of adjacent items and swaps them if they are in the wrong order. The pass through the list is repeated until no swaps are needed, which indicates that the list is sorted. The algorithm, which is a comparison sort, is named for the way smaller or larger elements "bubble" to the top of the list. Although the algorithm is simple, it is too slow for most problems even when compared to insertion sort. It can be practical if the input is usually in sorted order but may occassionally have some out-of-order elements nearly in position.

[Wikipedia reference](https://en.wikipedia.org/wiki/Bubble_sort)

A visual of how the algorithm works can be seen here: [bubble sort gif](https://en.wikipedia.org/wiki/Bubble_sort#/media/File:Bubble-sort-example-300px.gif)

### Anagrams

We consider two strings to be anagrams of each other if the first string's letters can be rearranged to form the second string. In other words, both strings must contain the same exact letters in the same exact frequency. For example, 'bacdc' and 'dcbac' are anagrams, but 'bacdc' and 'dcbad' are not.

In this anagram iteration, the function will return the minimum number of character deletions required to make 'a' and 'b' anagrams. Any characters can be deleted from either of the strings.

**Sample Input**
`a = 'abc'`
`b = 'cde'`

**Sample Output**
`4`

**Explanation**
You must delete 'b' and 'c' from `a` and 'd' and 'e' from `b` which results in four deletions for `a` and `b` to become anagrams.
