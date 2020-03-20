import re
List = []
with open("Temp_data.txt", 'r') as Temp_txt:
    data = Temp_txt.read()

print(data)

text = ''
lmao = '''

email@example.com
firstname.lastname@example.com
email@subdomain.example.com
firstname+lastname@example.com
email@123.123.123.123.123
1234567890@example.com
email@example-one.com
_______@example.com
email@example.name
email@example.museum
email@example.co.jp
firstname-lastname@example.com

'''

email_pattern = re.compile(r'(^(?!\.)(?!.*\.\.)[a-zA-Z0-9!#$%^&*+/=?`{}|~_.-]{1,64}(?<!\.))@(?!-)([a-zA-Z0-9-]{1,63})(?<!-)((\.[a-zA-Z0-9]{1,63})+)', re.M)

pattern = re.compile(r'\w')

matches = email_pattern.finditer(data)

for match in matches:
    print(match)
