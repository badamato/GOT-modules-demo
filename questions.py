from got import characters  #from the got.py file import the characters dictionary

#How many characters names start with "A"?
count = 0
for person in characters:
    if person['name'] !                     = ''and person['name'][0] == 'A':
        count = count + 1

print(count)


#How many characters names start with "Z"?
#How many characters are dead?
#Who has the most titles?
#How many are Valyrian?
#What actor plays "Hot Pie" (and don't use IMDB)?
#How many characters are *not* in the tv show?
#Produce a list characters with the last name "Targaryen"
#Create a histogram of the houses (it's the "allegiances" key)