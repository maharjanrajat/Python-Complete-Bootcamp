
2. **list** - Lists are used to store multiple items in a single variable. Lists are mutable.

    ```python
    a = [1, 2, 3, 4, 5]
    b = ["apple", "banana", "cherry"]
    c = [1, "apple", True, 1.5]

    print(type(a)) # <class 'list'>
    print(a) # [1, 2, 3, 4, 5]
    print(a[0]) # 1
    print(a[0:5]) # [1, 2, 3, 4, 5]
    print(a[0:5:2]) # [1, 3, 5]
    print(a[::-1]) # [5, 4, 3, 2, 1]
    print(a + a) # [1, 2, 3, 4, 5, 1, 2, 3, 4, 5] # concatenation
    print(a * 2) # [1, 2, 3, 4, 5, 1, 2, 3, 4, 5] # prints list 2 times

    # Mutating list
    a[0] = 10
    print(a) # [10, 2, 3, 4, 5]


    ```
3. **tuple** - Tuples are used to store multiple items in a single variable. Tuples are immutable. Thus it is **read only** list.

    ```python
    a = (1, 2, 3, 4, 5)
    b = ("apple", "banana", "cherry")
    c = (1, "apple", True, 1.5)

    print(type(a)) # <class 'tuple'>
    print(a) # (1, 2, 3, 4, 5)
    print(a[0]) # 1
    print(a[0:5]) # (1, 2, 3, 4, 5)
    print(a[0:5:2]) # (1, 3, 5)
    print(a[::-1]) # (5, 4, 3, 2, 1)

    # mutating tuple
    a[0] = 10 # TypeError: 'tuple' object does not support item assignment
    ```

    <!-- table -->

    <table width="100%">
    <tr>
    <td><b>List</b></td>
    <td><b>Tuple</b></td>
    </tr>
    <tr>
    <td>[1, 2, 3, 4, 5]</td>
    <td>(1, 2, 3, 4, 5)</td>
    </tr>
    <tr>
    <td>["apple", "banana", "cherry"]</td>
    <td>("apple", "banana", "cherry")</td>
    </tr>
    <tr>
    <td>Mutable</td>
    <td>Immutable</td>
    </tr>
    <tr>
    <td>Lists consume more memory </td>
    <td>Tuples consume less memory</td>
    </table>

    ## Testing memory consumption of list and tuple
    ```python
    import sys
    my_list = [1, 2, 3, 4, 5]
    my_tuple = (1, 2, 3, 4, 5)

    print(sys.getsizeof(my_list)) # 104
    print(sys.getsizeof(my_tuple)) # 88
    ```