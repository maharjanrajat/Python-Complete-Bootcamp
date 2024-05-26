# Control Flow
- By default, code is executed sequentially from top to bottom
- However, such sequantial execution can only solve simple problems
- Control flow statements can be used to change the order of execution of code

## Types of Control Flow
- Conditional Statements
- Loops


## Conditional Statements
- if
- if-else
- if-elif-else
- match (after python 3.10)- Similar to switch in other languages


## Loops
- for
- while


## If Conditional Statements
- if statement is used to check if a condition is true or false
- if the condition is true, the code inside the if block is executed
- if the condition is false, the code inside the if block is skipped

### Syntax:
```python
if condition:
    # code to be executed if condition is true
```

### Example 1:
```python
if 5 > 3:
    print("5 is greater than 3")
```

### Example 2:
if customer has buyed a product and amount is greater than 1000, then give 10% discount.
```python
amount = 1200
discount = 0
if amount > 1000:
    discount = amount * 10 / 100

print("Discount: ", discount)
print("Amount to be paid: ", amount - discount)
```
