#Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.
#The output should be two capital letters with a dot separating them.
#It should look like this:
#Sam Harris => S.H
#patrick feeney => P.F

def abbrev_name1(name):
    #split the 2 names apart at the space
    two_names = name.split()
    #two_names[0] is first name; two_names[0][0] is first character of first name
    return two_names[0][0].upper() + '.' + two_names[1][0].upper()


#this is maybe a bit neater
def abbrevName2(name):
    first, last = name.upper().split(' ')
    return first[0] + '.' + last[0]

#this solution squishes that into one line
# as above, split() breaks the string into two names
# for w in name.split() allows you to iterate through both names
# and w[0] gets you each initial
def abbrevName3(name):
    return '.'.join(w[0] for w in name.split()).upper()

#
