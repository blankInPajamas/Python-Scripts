''' 
    I downloaded a list of books. However, certain files had different naming conventions.
    Therefore, I created this program to do the following things:

    1. Append out the files in list with the substr "Vol-"
    2. If '-' is found in the list, 
        a. Split the items name, based on '-'
        b. Renames the first item
        c. Join the renamed item and into a new variable
        d. Rename the file
'''

import os

# Actual program

path = '{Add your directory location}'
books = []
toBeChanged = []

for items in os.listdir(path):
    if 'Vol-' in items:
        toBeChanged.append(items)
    
    books.append(items)

books.sort()

print(toBeChanged)


for items in toBeChanged:
    if '-' in items:
        temp = items.split('-')
        temp[0] = 'Volume '

        finalResult = ''.join(temp)

        print(finalResult)
        os.rename(os.path.join(path,items), os.path.join(path,finalResult))

    else:
        print('Not found')