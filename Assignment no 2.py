
input=("Enter a Story")
noun_list = ["dog", "cat", "apple", "book", "car", "boy", "girl", "Ali", "market", "school", "ball", "pen", "teacher", "student"]

story = input("Enter a short story: ")

for symbol in [".", ",", "!", "?"]:
    story = story.replace(symbol, "")

words = story.split()

nouns = set()
numbers = set()

for word in words:
    if word in noun_list:
        nouns.add(word)
    elif word.isdigit():
        numbers.add(int(word))

nested_number_set = frozenset(numbers)

nouns.add(nested_number_set)

print("Set of nouns (with numbers as a nested set):")
print(nouns)

