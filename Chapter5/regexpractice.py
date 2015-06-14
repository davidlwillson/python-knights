'''
This is for practicing with reg-ex's
'''

# first, a static array
phone_numbers = ('800-555-1212',
                 '800 555 1212',
                 '800.555.1212',
                 '(800) 555-1212',
                 '1-800-555-1212',
                 '800-555-1212-1234',
                 '800-555-1212x1234',
                 '800-555-1212 ext. 1234',
                 'work 1-(800) 555.1212 #1234')

for elem in phone_numbers:
    print(elem)

print("\n---\n")

# now, a compiled reg-ex
import re
phonePattern = re.compile(r'^(\d{3})\D+(\d{3})\D+(\d{4})\D+(\d+)$')

for elem in phone_numbers:
    print(elem)

    if phonePattern.search(elem) == None:
        print('none')
    else:
        print(phonePattern.search(elem).groups())

    print("---")

print("\n---\n")

# another differenter reg
phonePattern = re.compile(r'(\d{3})\D*(\d{3})\D*(\d{4})\D*(\d*)')

for elem in phone_numbers:
    print(elem)

    if phonePattern.search(elem) == None:
        print('none')
    else:
        print(phonePattern.search(elem).groups())

    print("---")

print("\n---\n")

# the same thing, presented differently

# phonePattern = re.compile(r'(\d{3})\D*(\d{3})\D*(\d{4})\D*(\d*)')
