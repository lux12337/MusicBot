import csv
import glob
import sys

#Convert the note played to an ASCII representation
def intoChar(num):
    return chr(33 + num)

#Find index of '%' dividing different tracks in string
def findDivider(string, n):
    if n == 1:
        return string.find('%')
    elif n == 2:
        return string.find('%', findDivider(string, 1) + 1,)
    elif n == 3:
        return string.find('%', findDivider(string, 2) + 1,)
    else:
        sys.exit('Divided number out of range!')

#Remove specific char from a specific slot within the string
def removeChar(string, char, slot):
    if slot == 1:
        if string.find(char) == -1:
            sys.exit("Trying to remove nonexisting char from slot 1!")
        return string[:string.find(char)] + string[string.find(char) + 1:]
    elif slot == 2:
        if string.find(char, findDivider(string, 1),) == -1:
            sys.exit("Trying to remove nonexisting char from slot 2!")
        return string[:string.find(char, findDivider(string, 1),)] + string[string.find(char, findDivider(string, 1),) + 1:]
    elif slot == 3:
        if string.find(char, findDivider(string, 2),) == -1:
            sys.exit("Trying to remove nonexisting char from slot 3!")
        return string[:string.find(char, findDivider(string, 2),)] + string[string.find(char, findDivider(string, 2),) + 1:]
    elif slot == 4:
        if string.find(char, findDivider(string, 3),) == -1:
            sys.exit("Trying to remove nonexisting char from slot 4!")
        return string[:string.find(char, findDivider(string, 3),)] + string[string.find(char, findDivider(string, 3),) + 1:]
    else:
        sys.exit('Trying to remove char out of slot range!')

#Inserts specific char into a specific slot in the passed string
def insertChar(string, char, slot):
    if slot == 1:
        return string[:string.find('%')] + char + string[string.find('%'):]
    elif slot == 2:
        return string[:findDivider(string, 2)] + char + string[findDivider(string, 2):]
    elif slot == 3:
        return string[:findDivider(string, 3)] + char + string[findDivider(string, 3):]
    elif slot == 4:
        return string[:findDivider(string, 3) + 1] + char + string[findDivider(string, 3) + 1:]
    else:
        sys.exit('Trying to insert char out of slot bounds!')

tracks = []

#iterate through csv files
for file in glob.glob("Data/*.csv"):
    with open(file, 'r') as csvfile:
        tracks.append([])
        reader = csv.reader(csvfile)
        for row in reader:
            if row[2].strip() == 'Note_on_c' or row[2].strip() == 'Note_off_c':
                if int(row[0]) - 1 > len(tracks[len(tracks) - 1]):
                    tracks[len(tracks) - 1].append([row])
                else:
                    tracks[len(tracks) - 1][int(row[0]) - 2].append(row)
    print(file)
    break

#debugging
# with open('test.csv', 'w') as f:
#     for row in tracks[3]:
#         f.write("%s\n" % row)

with open('test.txt', 'w') as f:
    for track in tracks:
        clock = 0
        iter1 = 0
        iter2 = 0
        iter3 = 0
        iter4 = 0
        unit = '%%%'
        # f.write('Begin')
        # f.write(' ')

        while True:
            if iter1 >= len(track[0]) and iter2 >= len(track[1]) and iter3 >= len(track[2]) and iter4 >= len(track[3]):
                break

            #track 1
            if iter1 < len(track[0]) and clock >= int(track[0][iter1][1]):
                time = int(track[0][iter1][1])
                while iter1 < len(track[0]) and time == int(track[0][iter1][1]):
                    if track[0][iter1][2].strip() == 'Note_on_c':
                        unit = insertChar(unit, intoChar(int(track[0][iter1][4])), 1)
                    else:
                        unit = removeChar(unit, intoChar(int(track[0][iter1][4])), 1)
                    iter1 += 1

            #track 2
            if iter2 < len(track[1]) and clock >= int(track[1][iter2][1]):
                time = int(track[1][iter2][1])
                while iter2 < len(track[1]) and time == int(track[1][iter2][1]):
                    if track[1][iter2][2].strip() == 'Note_on_c':
                        unit = insertChar(unit, intoChar(int(track[1][iter2][4])), 2)
                    else:
                        unit = removeChar(unit, intoChar(int(track[1][iter2][4])), 2)
                    iter2 += 1

            #track 3
            if iter3 < len(track[2]) and clock >= int(track[2][iter3][1]):
                time = int(track[2][iter3][1])
                while iter3 < len(track[2]) and time == int(track[2][iter3][1]):
                    if track[2][iter3][2].strip() == 'Note_on_c':
                        unit = insertChar(unit, intoChar(int(track[2][iter3][4])), 3)
                    else:
                        unit = removeChar(unit, intoChar(int(track[2][iter3][4])), 3)
                    iter3 += 1

            #track 4
            if iter4 < len(track[3]) and clock >= int(track[3][iter4][1]):
                time = int(track[3][iter4][1])
                while iter4 < len(track[3]) and time == int(track[3][iter4][1]):
                    if track[3][iter4][2].strip() == 'Note_on_c':
                        unit = insertChar(unit, intoChar(int(track[3][iter4][4])), 4)
                    else:
                        unit = removeChar(unit, intoChar(int(track[3][iter4][4])), 4)
                    iter4 += 1

            #f.write(str(clock))
            f.write(unit)
            f.write(' ')
            clock += 5
print('Done!')

#empty %
