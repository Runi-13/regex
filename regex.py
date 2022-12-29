import re
 
s = 'graceflorence: A computer science portal for geeks'
 
match = re.search(r'portal', s)
 
print('Start Index:', match.start())
print('End Index:', match.end())


#BACKSLASH-diminish special character status by putting this before any metacharacters
import re
 
s = 'graceflorence: A computer science portal for geeks.garland'
 
# without using \
match1 = re.search(r'.', s)
print(match1)
 
# using \
match2 = re.search(r'\.', s)
print(match2)


#^Caret matches the beginning of the string i.e. checks whether the string starts with the given character(s) or not. 
match3 = re.search(r'^gr', s)
print(match3)















