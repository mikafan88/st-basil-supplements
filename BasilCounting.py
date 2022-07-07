#mikafan88
#program to find easiest way to get wordcounting
#credit - https://gist.github.com/amankharwal/f72d45f7776ba19ce15201a0d94a1b8f#file-most-frequent-py
#word counter = https://www.geeksforgeeks.org/python-program-to-count-words-in-text-file/


words = []
numWords = 0
with open("BasilMergeV1Copy.txt", "r") as f:
    for line in f:
        words.extend(line.lower().split())
        
with open("BasilMergeV1Copy.txt", "r") as f:
    data = f.read()
    lines = data.split()
    numWords += len(lines)
    print(numWords)
    
from collections import Counter
counts = Counter(words)
top50 = counts.most_common(50)
print(top50)

percentArray = []
for i in range(len(top50)):
    percentArray.append((top50[i][0], round((100 * top50[i][1]/numWords), 4)))

print(percentArray)
