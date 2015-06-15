'''
attempt to pluralize an an English noun
'''

import re

def plural(noun):
    if re.search('[sxz]$', noun):
        return re.sub('$', 'es', noun)
    elif re.search('[^aeioudgkprt]h$', noun):
        return re.sub('$', 'es', noun)
    elif re.search('[^aeiou]y$', noun):
        return re.sub('y$', 'ies', noun)
    else:
        return noun + 's'



if __name__ == '__main__':
    import sys
    if sys.argv[1:]:
        print(plural(sys.argv[1]))
    else:
        print(__doc__)

# fun for testing
# grep -i quit /usr/share/dict/words | while read word; do python3 pluralize.py $word; done | less
