# Pythoic Code 
```python
letters = ['a', 'b', "c"]
# letter will equal to 'a', then 'b', and then 'c'
for letter in letters:
  print(letter)
# enumerate() function will allow you to access the index of a function
for index, letter in enumerate(letters):
  print("index: {} -> letter: {}".format(index, letter))

# you can also write a list in one line
# here range() function return a list of numbers from 0 up to 9
# the for loop iterates over the list and gets the value at that index and stores
# it in number variable which is then added to the numbers list
numbers = [number for number in range(0, 10)]
print(numbers)

# above code does same thing as below
numbers2 = []
for number in range(10):
  numbers2.append(number)
print(numbers2)

# here is some practice: try to create a 2-d array using one line for loop
```