import re
s = '<composer>Wolfgang Amadeus Mozart</composer>\n<author>Samuel Beckett</author>\n<city>London</city>'
s = re.sub('(<)(\w*)(>)(.*)(</\w*>)', r'\2: \4', s)
print(s)
