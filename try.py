from collections import Counter

al = "abccccdd"
result = 0

for i in Counter(al).values():
    result += i // 2 * 2

print(min(result+1, len(al)))