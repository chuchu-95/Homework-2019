import re,string
def examine(n):
    s = re.sub(' +', ' ', n.strip())
    s = re.sub('([{}])(\w)'.format(string.punctuation), r'\1 \2', s)
    return s

print(examine("This  is   a  very cool.Day!"))
