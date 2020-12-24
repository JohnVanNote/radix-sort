# Radix Sort

This is super old from college, its probably garbage.

There should be 3 files included in addition to this README:
* radix.py
* makefile
* example.input


radix.py is a simple implementation of a radix sort algorithm such that the user provides it input in the form of integers seperated by a whitespace and the algorithm will return the same list of integers sorted least the greatest.

There are two possible ways to do this:

```
$ make sort
```
Which allows the user to provide input, and:
```
$ make run
```
Which uses the input provided in example.input

Please keep in mind, radix sort does not account for negative values.

For more information, see: https://en.wikipedia.org/wiki/Radix_sort
