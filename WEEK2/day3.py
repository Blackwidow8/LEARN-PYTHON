import re

email = "walobwadan@gmail.com"

# ^ -> Start of the string
# [a-zA-Z0-9] -> checking for char/numbers inside the brackets
# + -> tracking occurences
# | -> or
# ()-> grouping

pattern = r'^[a-z]+@(gmail|yahoo|outlook)\.(com|net|org)'

# print(re.search(pattern, email))
 print(re.findall(pattern, email))
# print(re.match(pattern, email))

if re.match(pattern, email):
    print("Valid Email")
elif re.match(pattern, email)== None:
    print("Invalid Email")