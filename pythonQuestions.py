#PY04
print("\n[PY04] Even Numbers")
print("-" * 40)
numbers = [1, 2, 3, 4, 5, 6]
for num in numbers:
    if num % 2 == 0:
        print(num)


#PY05
print("\n[PY05] Word Count")
print("-" * 40)
def count_words(words):
    counts = {}

    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts

word1 = ["Hello", "hello", "Yay"]
print(count_words(word1))

#PY09
print("\n[PY09] Floating Point Rounding")
print("-" * 40)
print(round(2.675, 2))

#PY10
print("\n[PY10] Try / Finally Return")
print("-" * 40)
def f():
    try:
        return 1
    finally:
        return 2
print(f())