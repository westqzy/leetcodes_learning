
import re
s = "jeSsEJ"
a = re.findall(r'[A-Z][a-z]|[a-z][A-Z]', s)
print(a)