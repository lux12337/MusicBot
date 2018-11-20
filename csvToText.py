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
        reader = csv.reader(csvfile)
        for row in reader:
            if row[2].strip() == 'Note_on_c' or row[2].strip() == 'Note_off_c':
                if int(row[0]) + 1 > len(tracks):
                    tracks.append([row])
                else:
                    tracks[int(row[0])].append(row)
    break #reading only one file

#debugging
# with open('test.csv', 'w') as f:
#     for row in tracks[3]:
#         f.write("%s\n" % row)


clock = 0
#setup iterators for the 4 tracks
iter1 = 0
iter2 = 0
iter3 = 0
iter4 = 0

unit = '%%%'

# with open('input.txt', 'w') as f:
#     while True:
#         if iter1 >= len(tracks[2]) and iter2 >= len(tracks[3]) and iter3 >= len(tracks[4]) and iter4 >= len(tracks[5]):
#             break
#         #track 1
#         if iter1 < len(tracks[2]) and clock <= int(tracks[2][iter1][1]):
#             if tracks[2][iter1][2].strip() == 'Note_on_c':
#                 while iter1 < len(tracks[2]) and tracks[2][iter1][2].strip() == 'Note_on_c':
#                     unit = intoChar(int(tracks[2][iter1][4])) + unit
#                     iter1 += 1
#             else:
#                 unit = unit[:unit.find(intoChar(int(tracks[2][iter1][4])))] + unit[unit.find(intoChar(int(tracks[2][iter1][4]))):]
#             iter1 += 1
#         #track 2
#         if iter2 < len(tracks[3]) and clock <= int(tracks[3][iter2][1]):
#             if tracks[3][iter2][2].strip() == 'Note_on_c':
#                 while iter2 < len(tracks[3]) and tracks[3][iter2][2].strip() == 'Note_on_c':
#                     unit = unit[:unit.find('%', unit.find('%') + 1,)] + intoChar(int(tracks[3][iter2][4])) + unit[unit.find('%', unit.find('%') + 1,) + 1:]
#                     iter2 += 1
#             else:
#                 unit = unit[:unit.find(intoChar(int(tracks[3][iter2][4])))] + unit[unit.find(intoChar(int(tracks[3][iter2][4]))):]
#             iter2 += 1
#         #track 3
#         if iter3 < len(tracks[4]) and clock <= int(tracks[4][iter3][1]):
#             if tracks[4][iter3][2].strip() == 'Note_on_c':
#                 while iter3 < len(tracks[4]) and tracks[4][iter3][2].strip() == 'Note_on_c':
#                     unit = unit[:unit.find('%', unit.find('%', unit.find('%') + 1,) + 1,)] + intoChar(int(tracks[4][iter3][4])) + unit[unit.find('%', unit.find('%', unit.find('%') + 1,) + 1,):]
#                     iter3 += 1
#             else:
#                 unit = unit[:unit.find(intoChar(int(tracks[4][iter3][4])))] + unit[unit.find(intoChar(int(tracks[4][iter3][4]))):]
#             iter3 += 1
#         #track 4
#         if iter4 < len(tracks[5]) and clock <= int(tracks[5][iter4][1]):
#             if tracks[5][iter4][2].strip() == 'Note_on_c':
#                 while iter4 < len(tracks[5]) and tracks[5][iter4][2].strip() == 'Note_on_c':
#                     unit = unit[:unit.find('%', unit.find('%', unit.find('%', unit.find('%') + 1, ), ) + 1, )] + intoChar(int(tracks[4][iter3][4])) + unit[unit.find('%', unit.find('%', unit.find('%', unit.find('%') + 1, ), ) + 1, ):]
#                     iter4 += 1
#             else:
#                 unit = unit[:unit.find(intoChar(int(tracks[5][iter4][4])))] + unit[unit.find(intoChar(int(tracks[5][iter4][4]))):]
#             iter4 += 1
#
#         f.write(str(clock))
#         f.write(unit)
#         f.write(' ')
#         clock += 5

print('Done!')

#empty %
