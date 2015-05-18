''' I guess you choose a doc-string when planning to use the file as a module, and a shebang for a script meant to be invoked at the CLI. I guess. '''

import os

print(os.getcwd())
os.chdir('/home/dlwillson/git/diveintopython3/examples')
print(os.getcwd())
cwd=os.getcwd()
pathname=os.path.join(cwd,'humansize.py')
print(pathname)
(dirname, basename) = os.path.split(pathname)
print(dirname)
print(basename)
(filename,fileext) = os.path.splitext(basename)
print(filename)
print(fileext)

import glob
os.chdir('..')
something=glob.glob('examples/*.xml')
print(something)

for f in something:
    print (os.stat(f))
