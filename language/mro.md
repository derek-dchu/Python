Method Resolution Order (MRO)
=============================
MRO defines the class search path used by Python to search for the right method.

Note: MRO comes with old and new algorithms.

Python 2 vs 3
-------------
In Python 2, not every object inherits from the root 'object'. In Python 3, every object inherits from the root 'object'. Old algorithm will be used for those objects doesn't inherits root object. New algorithm is used for the rest of them.

Old MRO
-------
It is deep first, from left to right. And a class cannot appears twice in search path.

scenario 1:
```python
''' 
	A
   / \
   B C
   \ /
   	D
'''
class A():
	pass

class B(A):
	pass

class C(A):
	pass

class D(B, C):
	pass
```
Search path: D, B, A, C, skip(A).

scenario 2:
```python
''' 
	A1	A2	A3
   	\   /   |
   	  B     C
   	   \    /
   		  D
'''
class A1():
	pass

class A2():
	pass

class A3():
	pass

class B(A1, A2):
	pass

class C(A3):
	pass

class D(B, C):
	pass
```
Search path: D, B, A1, A2, C, A3.

New MRO (C3 Method)
-------
Merge linearized list. The linearization of a class C is the sum of C plus the merge of the linearizations of the parents and the list of the parents.

> L[C(P1, ..., PN)] = C + merge(L[P1], ..., L[PN], P1 ... PN)  
> L[object] = object

how to merge: 
> Take the head of the first list, i.e L[B1][0]; if this head is not in the tail of any of the other lists, then add it to the linearization of C and remove it from the lists in the merge, otherwise look at the head of the next list and take it, if it is a good head. Then repeat the operation until all the class are removed or it is impossible to find good heads. In this case, it is impossible to construct the merge, Python 2.3 will refuse to create the class C and will raise an exception.

For example, in scenario 1:
> L[D(B, C)] = D + merge(L[B(A)], L[C(A)], BC)  
> L[B(A)]    = B + merge(L[A], A) = B, A  
> L[C(A)]    = C + merge(L[A], A) = C, A  
> L[D(B, C)] = D + merge((B, A), (C, A), BC)  
>            = D + B + (A, (C, A), C) // B is good head  
>            = D + B + C + (A, A) // A is bad head, and C is good head  
>            = D + B + C + A

TypeError
---------
scenario 3:
```python
'''
	X	Y
	|/ \|
	A   B
	 \ /
	  C
'''
class X():
	pass

class Y():
	pass

class A(X, Y):
	pass

class B(Y, X):
	pass

class C(A, B):
	pass
```
Under old MRO: C, A, X, Y, B, skip(X, Y)

Under new MRO: we will have ```TypeError: Cannot create a consistent method resolution order (MRO) for bases X, Y```.

> L[F(A, B)] = F, A, B + merge((X, Y), (Y, X)) // both X and Y are bad heads

[Reference](https://www.python.org/download/releases/2.3/mro/)
