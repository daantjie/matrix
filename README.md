matrix.py
=========
A python module that implements basic matrix and vector computation. It uses Python 3, which you can download [here](https://python.org/downloads).

-----------------
### Documentation
You can initialise a matrix like so:
``` python
>>> M = Matrix([1, 2, 3],[4, 5, 6], [7, 8, 9])
```
Now `M` is initialised, displaying it is only a `print()` away!
``` python
>>> print(M)
[1, 2, 3]
[4, 5, 6]
[7, 8, 9]
```
Want to initialise a matrix by column instead of by row? No problem.
``` python
>>> N = Matrix.Column([1, 2, 3], [4, 5, 6], [7, 8, 9])
>>> print(N)
[1, 4, 7]
[2, 5, 8]
[3, 6, 9]
```
No ugly methods like `M.plus(N)`, simply use the `+` and `-` operators.
(Notice how the spacing is corrected to make sure the matrices looks orderly!)
``` python
>>> M + N
[ 2,  6, 10]
[ 6, 10, 14]
[10, 14, 18]
>>> M - N
[0, -2, -4]
[2,  0, -2]
[4,  2,  0]
```
