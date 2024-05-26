
4. **range** - Range is used to store a sequence of numbers. Range is immutable.

    ```python
    a = range(10)
    b = range(1, 10)
    c = range(1, 10, 2)

    print(type(a)) # <class 'range'>
    print(a) # range(0, 10)

    for i in range(10):
        print(i) # 0 1 2 3 4 5 6 7 8 9

    # range(start, stop, step)
    # mutating range
    a[0] = 10 # TypeError: 'range' object does not support item assignment
    ```

    

## Boolean Data Type
1. **bool** - Boolean represents one of two values: True or False.

    ```python
    a = True
    b = False

    print(type(a)) # <class 'bool'>
    print(a) # True
    print(b) # False

    print(10 > 5) # True
    ```
## Set Data Type
1. **set** - Set is used to store multiple items in a single variable. it is unordered and unindexed. Duplicate values are not allowed. It is used to perform mathematical set operations like union, intersection, etc.

    ```python
    a = {1, 2, 3, 4, 5}
    b = {"apple", "banana", "cherry"}
    c = {1, "apple", True, 1.5}

    print(type(a)) # <class 'set'>
    print(a) # {1, 2, 3, 4, 5}
    print(a[0]) # TypeError: 'set' object is not subscriptable

    # Mutating set
    a.add(6)
    print(a) # {1, 2, 3, 4, 5, 6}

    # adding duplicate value
    a.add(6)
    print(a) # {1, 2, 3, 4, 5, 6} # duplicate value is not added

    # adding multiple values
    
    #union and intersection
    a = {1, 2, 3, 4, 5}
    b = {4, 5, 6, 7, 8}
    print(a.union(b)) # {1, 2, 3, 4, 5, 6, 7, 8}
    print(a.intersection(b)) # {4, 5}

    ```
2. **frozenset** - Frozenset is used to store multiple items in a single variable. Frozenset is immutable. It is the unchangeable version of set.

    ```python
    a = frozenset({1, 2, 3, 4, 5})
    b = frozenset({"apple", "banana", "cherry"})
    c = frozenset({1, "apple", True, 1.5})

    print(type(a)) # <class 'frozenset'>
    print(a) # frozenset({1, 2, 3, 4, 5})
    print(a[0]) # TypeError: 'frozenset' object is not subscriptable
    ```