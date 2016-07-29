fp = open('testnote.txt')
a = fp.readlines()
b = ''.join(line for line in a)
print sum(1 for line in a)
print b
fp.close()
