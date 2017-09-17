s = 'azcbobobegghakl'
count = 0

for bob in range(0, len(s)):
	if bob == len(s)-2:
		break
	if s[bob] == 'b' and s[bob+1] == 'o' and s[bob+2] == 'b':
		count += 1

print('Number of times bob occurs is: ' + str(count))