# PyDLint

The goal of this project is to create a Dynamic Analysis tool for Python similar to [DLint](https://github.com/Berkeley-Correctness-Group/DLint).  In essence, this project aims to fill in the gap in the following table: 

|                 |Python | Javascript | C      |
|-----------------|-------|------------|--------|
|Static Analysis  |Pylint |JSHint      |lint    |
|Dynamic Analaysis|       |DLint       |valgrind|

## What is Static Analaysis
Static Analysis is any analysis of a computer program that does not involve running the program.  Generally this involves programmatically reading the source code of a computer program, finding portions that are likely to be erroneous or unintuitive, and reporting them to the programmer so that the programmer may change them.

Tools that perform Static Analysis are often called `linters`.  Pylint, pyflakes, pychecker, jshint, jslint, and cppcheck are all examples of common linters.  

## What is Dynamic Analysis
Dynamic Analysis is analysis of a computer program that does involve running the program.  Dynamic analysis can sometimes catch more types of errors than static analysis because the program can find the values of variables at runtime.  However, Dynamic Analysis is limited to checking only the code branches that are executed while under inspection.  Also, Dynamic Analysis programs are not guaranteed to terminate, especially if the underlying program does not terminate.

While Dynamic Analysis tools are less common than Static Analysis, there are a few that people do use.  Valgrind/Memcheck is the most common; it's a tool that can detect and report certain classes of memory errors by running the program under inspection.

## What does PyDLint do?

```python
from __future__ import print_function, division

NUMBER_OF_FRUITS = 3

print("PyDLint detects and reports a variety of code-quality issues that "
      "static analysis tools like pylint just can't")
z = eval
z("'You can\\'t fool me, I\\'m the gingerbread man!'")


from math import *

factorable = int(2**32 + 1)

def factor(n):
    while n % 2 == 0:
        print(2)
        n = n / 2
    for factor in range(3, ceil(sqrt(n)), 2):
        while n % factor == 0:
            print(factor)
            n = n / factor
    print(int(n))

factor(factorable)
print("PyDLint can report when you accidentally change the type of a variable")


total = 0
fruits = {"apples": 1, "bananas": 2, "oranges": 3}
for quantity in fruits:
    total += quantity
print("What's wrong with the code above?  This is a simple example but it "
      "might not always be so obvious")

NUMBER_OF_FRUITS = 6
print("Dynamic analysis can also find the sorts of issues that a static "
      "analaysis tool can find")
```

outputs

```
PyDLint detects and reports a variety of code-quality issues that static analysis tools like pylint just can't
ISSUE: Called a banned function: <built-in function eval>
641
ISSUE: Type change:  variable <class 'int'> was type <class 'float'>, now is type n
6700417
PyDLint can report when you accidentally change the type of a variable
ISSUE: Tried to iterate over a dictionary without explicitly calling
What's wrong with the code above?  This is a simple example but it might not always be so obvious
ISSUE: Modified a variable whos name is in all caps: NUMBER_OF_FRUITS
Dynamic analysis can also find the sorts of issues that a static analaysis tool can find
```

## How do I use PyDLint?

`git clone git@github.com:yabberyabber/PyDLint.git`

`cd PyDLint`

`python setup.py install`

`python -m pydlint NAME_OF_SOURCE_FILE_TO_RUN`

PyDLint will run the source file referenced and report any issues as they come up.  You may wish to end execution as soon as an error is found instead of continuing.  To do so, use the following syntax:

`python -m ptdlint -strict NAME_OF_SOURCE_FILE_TO_RUN`

## What kinds of issues can PyDLint detect now?
The following are Code Quality Issues that PyDLint can detect at the moment.  
 - Changing the value of a constant (by convention, constants are variables whose names are in all caps, e.g. NUM_FRUITS)
 - Changing the type of a variable
 - Iterating over a dictionary without explicitly specifying whether you want keys, values, or items
 - Calling eval

The following are Code Quality Issues that PyDLint should be able to detect but currently cannot:
 - Saving the result of a function that returns None
 - Modifying default function parameter objects

## Can I read the paper you wrote?
[It's in the repo](https://github.com/yabberyabber/PyDLint/blob/master/pydlint-dynamically-checking.pdf)

# Limitations
PyDLint is not able to run all python programs properly yet (there's an error in how PyDLint runs the program above; 50 points if you can spot it ;^).  With that in mind, it does run enough of the language to be useful as a proof of concept.  

# Acknowledgements
This project is a modification of an existing project called [Byterun](https://github.com/nedbat/byterun).  Byterun is a pure-Python implementation of a Python bytecode execution virtual machine.  Check out [A Python Interpretor Written in Python](http://aosabook.org/en/500L/a-python-interpreter-written-in-python.html) for an awesome explanation of how Byterun works.  
