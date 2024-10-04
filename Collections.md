### Collections

Collections help us organize and manage groups of items, like toys, books, or even your favorite games.
Python has different types of collections, and each one is useful in its own way. Let’s dive in!

## Lists
What is a List?
A list is like a big box where you can keep many items. You can put things in, take them out, and even change them.

```
# Creating a list of fruits
fruits = ['apple', 'banana', 'orange']
print(fruits)  # Output: ['apple', 'banana', 'orange']

# Adding a fruit
fruits.append('grape')
print(fruits)  # Output: ['apple', 'banana', 'orange', 'grape']

# Changing a fruit
fruits[1] = 'strawberry'
print(fruits)  # Output: ['apple', 'strawberry', 'orange', 'grape']

```
## Tuples
What is a Tuple?

A tuple is like a list, but once you create it, you can’t change it. Think of it as a special box that locks once it’s filled!

```
# Creating a tuple of colors
colors = ('red', 'green', 'blue')
print(colors)  # Output: ('red', 'green', 'blue')
```
## Dictionaries
What is a Dictionary?

A dictionary is like a real dictionary or a treasure map. It has keys (like clues) and values (the treasures). You can look up a value using its key!

```
# Creating a dictionary of ages
ages = {'Alice': 10, 'Bob': 12, 'Charlie': 11}
print(ages['Bob'])  # Output: 12

# Adding a new person
ages['David'] = 9
print(ages)  # Output: {'Alice': 10, 'Bob': 12, 'Charlie': 11, 'David': 9}
```
## Sets
What is a Set?

A set is like a bag of unique items. You can’t have duplicates, and it’s perfect for when you want to keep things unique.

```
# Creating a set of animals
animals = {'dog', 'cat', 'bird'}
print(animals)  # Output: {'dog', 'cat', 'bird'}

# Adding an animal
animals.add('fish')
print(animals)  # Output: {'dog', 'cat', 'bird', 'fish'}

# Trying to add a duplicate
animals.add('cat')
print(animals)  # Output: {'dog', 'cat', 'bird', 'fish'} (no duplicates!)

```
