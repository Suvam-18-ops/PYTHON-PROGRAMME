import re
text = "cat123 cat4567 cat89"
result = re.findall(r'cat\d{1,3}', text)
print(result)  # Output: ['cat123', 'cat89']