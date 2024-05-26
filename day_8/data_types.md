## Mapping Data Type
1. **dict** - Dictionary is used to store data in key:value pairs. Dictionary is mutable. It is unordered and unindexed.

    ```python
    a = {"name": "John", "age": 36}
    b = {1: "apple", 2: "banana", 3: "cherry"}
    c = {1: "apple", "color": ["red", "green", "blue"]}

    my_dict = {}
    my_dict["name"] = "John"  # add/update key:value
    my_dict["age"] = 36 # add/update key:value

    print(my_dict) # {'name': 'John', 'age': 36}

    print(my_dict["name"]) # John
    print(my_dict.get("name")) # John

    print(my_dict.keys()) # prints all keys
    ```

## None Data Type
1. **None** - None is used to define a null value, or no value at all.

    ```python
    a = None
    b = None
    c = None
    ```

# Mutable vs Immutable
<!-- table -->
| Mutable | Immutable |
| --- | --- |
| Mutable objects can change their value  | Immutable objects can not change their value. |
| Eg: List, Set, Dictionary are mutable. |Eg: Tuple, Range, Boolean, Frozenset, Bytes, Bytearray, Memoryview, None are immutable. |
