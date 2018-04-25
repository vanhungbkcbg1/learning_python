import codecs

file =codecs.open('unicode.txt','r','sjis');
line=file.readline()
str=file.read(1)



print line

print str

file.close()