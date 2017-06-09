# Python

## Drawing an Owl

1.	Draw a couple of circles
2. DTROTFO

##Installation

Go here to [Download]('https://www.python.org/downloads/')

1. From there go to Downloads.
2. Click latest version to download Python
3. Figure it out

Next we will install Django and Pip. Pip is similar to npm and gems on Node and Ruby.

In the command line run:

1. brew install python
2. pip --version (check to see if pip was installed)

![Pip](http://pa1.narvii.com/5955/bf6b5f02a02a0ae0d22e768c8de183d085c04b95_hq.gif)

## Hello World from command line

In the terminal you can run a "Hello World" command by declaring it as a vaiable. In the example below, we declare the variable ```message``` and set it equal to the desired text ```"Hello World"```

The ```print``` statement is not allows the user to print the ```message``` variable.  

* Python 2: In this version ```print``` is **not** a **function** and is invoked **WITHOUT** parentheses.
* Python 3: In this version, ```print``` is a **function** and **MUST** be invoked **WITH** parentheses

To exit out of python: ```quit()```

```
>>> message = "Hello World"
>>> print(message)
Hello World
>>> 
>>> quit()
```

## Indentation

Similar to Ruby, Python uses indentation for blocks instead of curly braces.

Python

```
x = 1
if x == 1:
    # indented four spaces
    print("x is 1.")
```
Ruby

```
> x = 1
 => 1 
> if x == 1
> 	print "x is 1."
> end
x is 1. => nil 
```
Javascript

```
> x = 1;
1
> x
1
> if (x == 1)
... console.log('x is 1.')
x is 1.
```
## Variables and Types

Python is completely **Object-Orientated**

Every variable in Python is an **Object**

You do not need to declare variables before using them

#### Data Types
*	Numbers
* 	Strings
*  List
*  Tuple
*  Dictionary

### Numbers
Number data types store numberic values. Python supports two types of numbers:

*	Integers
* 	Floating point numbers

### Strings

Strings can either be defined in single ```''``` or double ```""``` quotes. 

*	Double quotes ```""``` is preferred when using apostrophes

```
>>> myname = "Ed O'Connell"
>>> print(myname)
Ed O'Connell
```
Subsets of strings can be taken using the slice operator ([ ] and [:] ) with indexes starting at 0 in the beginning of the string and working their way from -1 at the end

```
>>> str = "Hello World"
>>> str
'Hello World'
>>> print str[0]
H
>>> print str[2:5]
llo
>>> print str[2:]
llo World
```

### Lists

Lists are very similar to arrays and the most versatile of Pythons data types.

```
>>> list = ['rock', 'paper', 'scissor']
>>> print list
['rock', 'paper', 'scissor']
>>> print list[0]
rock
>>> print list[1:2]
['paper']
>>> print list[1:3]
['paper', 'scissor']
```
### Tuples

Tuples are very similar to lists except they are enclosed within parentheses instead of brackets and the values **cannot** be changed.

The main differences between lists and tuples are: Lists are enclosed in brackets ( [ ] ) and their elements and size can be changed, while tuples are enclosed in parentheses ( ( ) ) and cannot be updated.

```
>>> exampletuple = ('cat', 'dog', 'gustave', 'other fish')
>>> exampletuple
('cat', 'dog', 'gustave', 'other fish')
>>> print exampletuple
('cat', 'dog', 'gustave', 'other fish')
>>> print exampletuple[1:3]
('dog', 'gustave')
>>> print exampletuple[2:]
('gustave', 'other fish')
```

### Tuples

A dictionary is a data type similar to arrays, but works with keys and values instead of indexes. Each value stored in a dictionary can be accessed using a key, which is any type of object (a string, a number, a list, etc.) instead of using its index to address it.

Dictionaries are enclosed by curly braces ({ }) and values can be assigned and accessed using square braces ([])

```
>>> dict = {}
>>> dict['one'] = 'This is a cat'
>>> dict[2] = 'probably a dog'
>>> print dict
{2: 'probably a dog', 'one': 'This is a cat'}
>>> print dict['one']
This is a cat
>>> print dict[2]
probably a dog

>>> otherdict = {'name': 'gustave', 'type': 'fish', 'age': 100 }
>>> print otherdict
{'age': 100, 'type': 'fish', 'name': 'gustave'}
>>> print otherdict.keys()
['age', 'type', 'name']
>>> print otherdict.values()
[100, 'fish', 'gustave']
```