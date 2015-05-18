''' practicing list comprehensions and things '''

section_header = ' === list comprehensions ==='
print( section_header )

a_list = [1, 9, 8, 4]
print(a_list)
a_list = [ elem * 2 for elem in a_list ]
print(a_list)
import os, glob
os.chdir('/home/dlwillson/git/diveintopython3/examples/')
bigfiles=[ f for f in glob.glob('*.py') if os.stat(f).st_size > 6000 ]
for f in bigfiles:
    print(f,os.stat(f).st_size)
bigfiles=[ ( os.stat(f).st_size, os.path.realpath(f) ) for f in glob.glob('*.xml') ]
print ( bigfiles )


section_header = ' === dictionary comprehensions ==='
print( section_header )

metadata_dict = { f:os.stat(f) for f in glob.glob('*.xml') }

print ( 'type of metadata_dict:', type( metadata_dict ) )
print ( 'metadata_dict =', metadata_dict )
print ( metadata_dict['feed.xml'] )

section_header = ' === set comprehensions ==='
print( section_header )

a_set = set(range(10))
print ( { elem ** 2 for elem in a_set } )
print ( { elem: elem ** 2 for elem in range(100) if elem % 3 == 0 } )
