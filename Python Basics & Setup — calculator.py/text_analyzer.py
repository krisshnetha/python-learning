from collections import Counter

text = input("Enter a paragraph: ")

words = text.lower().split()
unique_words = set(words)
word_count = len(words)
unique_word_count = len(unique_words)
sentence_count = text.count('.') + text.count('!') + text.count('?')
character_count = len(text.replace(" ", ""))
most_common = Counter(words).most_common(1)

print("Word Count:", word_count)
print("Unique Word Count:", unique_word_count)
print("Sentence Count:", sentence_count)
print("Character Count (without spaces):", character_count)

if most_common:
    print("Most Frequent Word:", most_common[0][0])

reversed_words = ' '.join(word[::-1] for word in words)
print("Reversed Words:")
print(reversed_words)