import re

emails = '''
CoreyMSchafer@gmail.com
corey.schafer@university.edu
coret-321-schafer@my-work.net

'''


# pattern = re.compile(r'/w+@/w+/.(com|edu|net)')
pattern = re.compile(r'.+@\w.+\.(com|edu|net)')

matches = pattern.finditer(emails)



for match in matches:
    print(match)
