import sys

num_from = int(sys.argv[1])
num_to = int(sys.argv[2])+1

flags = ''
if len(sys.argv) > 3:
    if sys.argv[3] == '-r':
        flags = 'order="DESC"'

if flags:
    flags = ' %s'%flags
print '[gallery link="file" include="%s"%s]'%(','.join([str(x) for x in xrange(num_from,num_to)]),flags)

