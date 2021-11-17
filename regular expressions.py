import re

pattern = "Cookies"
sequence = "Cookie"
print(re.match(pattern, sequence))



normal_string = 'I am a normal string\tyou can tab\nyou can break the line'
raw_string = r'I am prefixed with r\tyou cannot tab\nyou cannot break the line'

print('normal string output:', normal_string)
print('raw string output:', raw_string)


