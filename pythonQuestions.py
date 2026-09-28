print("Python Questions 1")
#PY04
numbers = [1, 2, 3, 4, 5, 6]
for num in numbers:
    if num % 2 == 0:
        print(num)

#PY05
def count_words(words):
    counts = {}

    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts

word1 = {"Hello", "hello", "Yay"}
print(count_words(word1))

#PY09


