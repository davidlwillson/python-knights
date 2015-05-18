''' Stringing myself along, I am. '''

s = '深入 Python'

print ( len(s) )
print ( s[0] )
print ( s + str(3) )

print ( '{0:.3f} {1}'.format(3.14159265, 'pi') )

print ( s[:3] )
print ( s[3:] )
print ( s[-3:] )

data="this:10 that:20 theotherthing:30"
attempted = [ row.split(':') for row in data.split(' ')]
print ( 'type of attempted', type ( attempted ) )
print ( attempted )

b = s.encode()

print( b )
print ( type ( b ) )

print ( b.decode() )
print ( type ( b.decode() ) )
