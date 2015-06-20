'''
Final pluralizer, uses a file for patterns.
'''

import re

def build_match_and_apply_functions(pattern, search, replace):

    def matches_rule(word):
        return re.search(pattern, word)

    def apply_rule(word):
        return re.sub(search, replace, word)

    return (matches_rule, apply_rule)

rules = []

with open('plural-rules.txt') as pattern_file:

    for line in pattern_file:

        pattern, search, replace = line.split(None, 3)

        rules.append(
            build_match_and_apply_functions(
                pattern, search, replace
                )
            )

def plural(noun):
    for matches_rule, apply_rule in rules:
        if matches_rule(noun):
            return apply_rule(noun)

if __name__ == '__main__':
    import sys
    if sys.argv[1:]:
        print(plural(sys.argv[1]))
    else:
        print(__doc__)

# fun for testing:
# grep -i quit /usr/share/dict/words | while read word
#   do python3 plural.py $word
#   done | less
