# lockers-problem
We got *n* lockers and the same *n* of students, the student *n* will open or close the lockers that are multiples of *n*. The sequence will go like this:

The student 1 will open every single locker, because they are multiples of 1.

The student 2 will close all the even numbers.

And we want to know in the end, what are the lockers that are open.

|     | 1 | 2 | 3 | 4 | 5 |
|:---:|---|---|---|---|---|
| 0   | f | f | f | f | f |
| 1   | t | t | t | t | t |
| 2   |   | f |   | f |   |
| 3   |   |   | f |   |   |
| 4   |   |   |   | t |   |
| 5   |   |   |   |   | f |
| res | t | f | f | t | f |

return = [1,4]


## Solutions

[Python]: Python/lockers-problem.py
* [Python]