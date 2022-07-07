#mikafan88
#program to find easiest way to get wordcounting
#credit - https://gist.github.com/amankharwal/f72d45f7776ba19ce15201a0d94a1b8f#file-most-frequent-py

words = []
with open("BasilMergeV1Copy.txt", "r") as f:
    for line in f:
        words.extend(line.lower().split())

from collections import Counter
counts = Counter(words)
top50 = counts.most_common(50)
print(top50)
