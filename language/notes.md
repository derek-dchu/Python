1.	r"" # raw string
	print r"\nwoow" will print "\nwoow"

2.	\x # hexadicmal number encoding a char
	"\x48\x49!" => "HI!"

3.	0x # hex int
	0xA + 0xA == 20 # True

4.	Python is a strongly typed language
	"foo" + 2 # throws an TypeError

5.	Putting a string on the first line after the start of function definition becomes docstring.
	```python
	def func():
		"<docstring>"

	# "<docstring>" == func.__doc__
	```

6.	`re.match` vs `re.search`
	match: in the beginning of the string, search: anywhere

7.	Key in dict can be only immutable type (numbers, string, tuple). Numbers have same evaluation are same key.
	```py
	foo[1] == foo[1.0] # True
	```
8.	If index can not find the specified value in the list, ValueError is thrown.

9.	list a + list b = new list contains elements within list a and list b

10.	input & raw_input
	In Python 2, `input()` is equalvent to `eval(raw_input()).
	In Python 3, `input` is renamed `raw_input`

11.	`[x * x for x in range(3)]` creates an iterable. `(x * x for x in range(3))` creates a generator. And the latter can only be used once.

12. `yield` pauses a function and return a generator object. `next()` resumes where it left off.	
	