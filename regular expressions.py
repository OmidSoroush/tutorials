import re

pattern = "Cookies"
sequence = "Cookie"
print(re.match(pattern, sequence))



normal_string = 'I am a normal string\tyou can tab\nyou can break the line'
raw_string = r'I am prefixed with r\tyou cannot tab\nyou cannot break the line'

print('normal string output:', normal_string)
print('raw string output:', raw_string)


import re

pattern = r"painting"
string1 = "This is my favorite painting"
string2 = "painting is a great hobby"

print(re.match(pattern, string1, re.IGNORECASE))
print(re.match(pattern, string2, re.IGNORECASE))


import re

pattern = r"^Python"
string1 = "Python is great for text manipulation"
string2 = "Regexes can be handled very fast by Python"

print(re.findall(pattern, string1))
print(re.findall(pattern, string2))



import re

pattern = "P..h.n"
string = "Python is great for text manipulation, a Pythonista said"

print(re.findall(pattern, string))



import re

pattern = "tion$"
string = "Python is great for text manipulation"

print(re.findall(pattern, string))


import re

pattern = "da?t"
string = "dt dat data daaaat day"

print(re.findall(pattern, string))