import re
str = ' val10 = \'Administrator\' nick.parlante@cs.stanford.edu hi how are you hello some text alice@google.org, bobatabc.com blah'

emails = re.findall(r'([\w\.-]*)(@|at)([\w\.-]*)', str)

for email in emails:
    print email[0]
    print email[2]

