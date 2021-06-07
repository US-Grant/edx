# Problem 1
vowels = 0
for c in s:
    if c in "aeiou":
        vowels += 1
print("Number of vowels: " + str(vowels))


# Problem 2
i = 0
res = 0
for k in range(len(s)-2):
    if s[i:i+3] == "bob":
        res += 1
    i += 1
print("Number of times bob occurs is: " + str(res))


# Problem 3
s = 'azcbobobegghakl'
alphabet = "abcdefghijklmnopqrstuvwxyz"
res = s[0]
max = s[0]

if s == alphabet:
    max = s
else:
    for i in range(1, len(s)):
        if alphabet.find(res[-1]) <= alphabet.find(s[i]):
            res += s[i]
        else:
            if len(res) > len(max):
                max = res
            res = s[i]
print("Longest substring in alphabetical order is: " + max)