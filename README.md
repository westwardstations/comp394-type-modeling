# Programming Languages: Type Modeling

This assignment asks you to

- implement a simplified model of Python’s runtime member lookup in Java, and
- implement a simplified model of Java’s compile-time type checking in Python.

This pair of exercises serves two purposes.

First, implementing something in code is a great way to think through it in detail. In class, you’ve done a lot of receptive learning: looking at pictures on the board, and following along with live coding examples. Now I want you to think through for yourself the foundations of how dynamic and statically typed languages treat data types.

Second, I want you to practice switching between languages often in this class, and to note the differences in their taste and texture as you do. For example, this assignment involves collections and unit tests in both Java and Python. How do these similar features play out across the two languages?

Please note the important difference between the two parts of this assignment: in the first part, you are simulating how Python individual objects behave **at runtime**, i.e. while a Python program is actually running. In the second part, you are simulating how Java checks types and resolves method calls in expressions **at compile time**, i.e. for _all possible values_ that might actually show up in that expression when the code actually does run.

In both cases, I have given you a starting structure and tests that show you what you need to implement. You **should not modify any of the tests** in this assignment. (Do let me know if you find a mistake, however!)


## Problem 0: Python in Java

In the `python-attr-lookup/` directory, I have set up an IntelliJ project that provides a simplified model of Python types and objects. Your job is to implement object instantiation and attribute lookup in this model.

### Part 0.0: Study the starting code

Spend some time reading through the structure of the classes under `python-attr-lookup/src/`, especially `PythonObject` and `PythonType`. Their javadoc describes the behavior you are aiming for. The `"not implemented yet"` exceptions indicate the parts you need to fill in.

Now look over the tests in `PythonObjectTest.java`. What do they expect to happen, and why?

### Part 0.1: Implement object instantiation

Implement `PythonType.instantiate()`. Read the javadoc for that method to see what it is supposed to do. The solution is very simple to implement, but think carefully about what it is and why.

Implementing this will make the first test pass.

### Part 0.2: Implement method resolution order

Python first looks for attributes on an object itself, then on its type and the type’s base types (i.e. superclasses). Python uses a “method resolution order” (MRO) to determine where to look for attributes and in what order. It is called “method” resolution order even though it also applies to attributes that are not methods.

Real-life Python supports a class having more than one base class (a.k.a “multiple inheritance”), and uses a [fancy algorithm](https://en.wikipedia.org/wiki/C3_linearization) to work out the MRO. For this assignment, however, you will only be supporting single inheritance.

Implement `PythonType.buildMRO()` and `PythonObject.buildMRO()`. This will make the test under the `MRO tests` heading all pass.

### Part 0.3: Implement get() and set()

Make the rest of the tests pass by implementing `PythonObject.get()` and `PythonObject.set()`. When implemented correctly, these will make all the remaining tests pass — but they should not require a large amount of code.

I recommend making the tests pass one at a time, _in the order they appear in the test class_. They are set up to guide you through a good implementation strategy.

### Wrap it up

If you’ve been running individual test cases, go back and **double check that all the tests pass**.

Don’t forget to commit and push as you work!


## Problem 1: Java in Python

In the `java-type-checker/` directory, I have given you some Python code that provides a simplified model of Java’s static type system and expression AST. Note that there is no parser here; the test example build up the Java AST one node at a time. By “simplified,” I mean that this model captures just the most basic aspects of a very few language features: only expressions (no if statements or loops), only method calls, no generics (e.g. `List<String>`), not even arithmetic operations!

There is just enough structure here for you to get the feel of how a static type checker works.

### Part 1.0: Study the starting code

Run these tests; they should already pass:

```bash
cd comp394-type-modeling/type-checker  # If you are not already there

python3 -m tests.test_class_structure
```

Study those tests, and understand why they pass. Study the code in `types.py` and `expressions.py`, and understand the structure you are about to fill out. How do the roles of the things in those two files differ? What parts of Java do they represent?

### Part 1.1: Implement subtype logic

Implement `Type.is_subtype_of()` to make these tests pass:

```bash
python3 -m tests.test_type_relationships
```

### Part 1.2: Implement expression types

Implement `static_type()` for all the subclasses of `Expression`, to make these tests pass:

```bash
python3 -m tests.test_static_types
```

These implementations will be quite small. Please take a moment to think about each one, what it means, and why the test is asking you to implement the behavior it describes.

### Part 1.3: Implement the type checker

Implement `check_types()` for all the subclasses of `Expression`, to make these tests pass:

```bash
python3 -m tests.test_type_checking
```

This is the most labor-intensive part of this assignment. The tests will guide you through it; I recommend making them pass one at a time.

Many of you may be rusty on Python; if you are, please seek help from me, or from fellow students on our Slack channel. (Be careful **not** to post code that would give away part of the solution for other students! Do however feel free to ask “What’s the Python syntax for….”)

Because you may especially be rusty on Python string formatting, and because formatting error messages is not the point of this assignment, here are two snippets you may find useful (and that give you a tiny hit about the shape of the solution):

```python
raise TypeError(
    "Wrong number of arguments for {0}: expected {1}, got {2}".format(
        call_name,
        len(expected_types),
        len(actual_types)))
```

```python
raise TypeError(
    "{0} expects arguments of type {1}, but got {2}".format(
        call_name,
        names(expected_types),
        names(actual_types)))
```

Note that this second snippet uses the `name()` helper already implemented for you in `expressions.py`.

### Part 1.4: Support `null`

Java’s `null` is a quirky special case:

- it cannot be instantiated and
- it has no methods, yet
- it behaves like a subtype of every class and every interface.

Making it work properly requires a special class in our type checker, `NullType`. Implement it. (You will find a placeholder for it in `types.py`.)

You’ll find this poses some tricky questions: what should you subclass to implement it? Can it inherit any of its logic from existing classes in that file? There is no single correct answer. However, although this takes a lot of thinking, the solution _does not take a lot of code._ Don’t go down a rabbit hole!

Get the null tests to pass:

```bash
python3 -m tests.test_null
```

### Wrap it up

Double check that **all** the tests pass:

```bash
python3 -m unittest
```

Commit, push, and **send me a pull request** to hand in your assignment. Then take a pleasant walk as you muse on how much work it must have been to implement these entire languages.
