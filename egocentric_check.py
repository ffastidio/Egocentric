import sys

f = open('README.md', 'r')

check = False

for line in f:
    words = line.split()
    if "ffastidio" in words:
        check = True
        break
                
if check == True:
    sys.exit(0)
    
else: 
    raise Exception ('Sorry, file README.md must contain the name "Federica" for the push to be succesful')

