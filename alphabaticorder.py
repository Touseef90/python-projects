s = 'azcbobobegghaklabcdef'
asciiValue = 97
newCount = 0
count = 0
index = 0
substr = ''

for x in range(0, len(s)):
	if ord(s[x]) >= asciiValue:
		count += 1
		asciiValue = ord(s[x])
		if count > newCount:
			newCount = count
			index = x
	else:
		count = 1
		asciiValue = ord(s[x])

start = index + 1 - newCount

while newCount > 0:
	substr += s[start]
	start += 1
	newCount -= 1

print('Longest substring in alphabetical order is: ' + substr)