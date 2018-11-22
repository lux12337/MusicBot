import csv
import difflib
import sys

#track = [note, 'Note_on/off_c']
tracks = [[], [], [], []]
clock = 0

#Convert char representation of note to numerical
def intoNote(char):
    return ord(char) - 33

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

#Find the slot number that the char belongs to
def findSlot(string, char):
    index = string.find(char)
    if index < findDivider(string, 1):
        return 0
    elif findDivider(string, 1) < index < findDivider(string, 2):
        return 1
    elif findDivider(string, 2) < index < findDivider(string, 3):
        return 2
    else:
        return 3

#Find difference of old notes to new notes and inserts data into tracks
def findDiff(old, new, clock):
    for i, s in enumerate(difflib.ndiff(old, new)):
        if s[0] == ' ':
            continue
        elif s[0] == '-': #Delete
            if s[-1] == '%':
                continue
            else:
                temp = findSlot(old, s[-1])
                tracks[temp].append([temp + 2, clock, 'Note_off_c', temp, intoNote(s[-1]), 0])
        elif s[0] == '+': #Add
            if s[-1] == '%':
                continue
            else:
                temp = findSlot(new, s[-1])
                tracks[temp].append([temp + 2, clock, 'Note_on_c', temp, intoNote(s[-1]), 100])


#Parse input and store tracks
with open('input.txt', 'r') as f:
    temp = ''
    for line in f:
        for word in line.split():
            if temp == '':
                temp = word
            else:
                findDiff(temp, word, clock)

            temp = word
            clock += 5
print('Done parsing input')

#Add track delimiters
for track in tracks:
    track.insert(0, [track[0][0], 0, 'Program_c', track[0][3], 0])
    track.insert(0, [track[0][0], 0, 'Title_t', '"No Name"'])
    track.insert(0, [track[0][0], 0, 'Start_track'])
    track.append([track[0][0], track[len(track) - 1][1], 'End_track'])

#Write csv file with correct format
with open('mycsv.csv', 'w', newline='') as out:
    outFile = csv.writer(out)
    outFile.writerow([0, 0, 'Header', 1, 6, 480])
    outFile.writerow([1, 0, 'Start_track'])
    outFile.writerow([1, 0, 'Title_t', '"Luigi"'])
    outFile.writerow([1, 0, 'Time_signature', 4, 2, 24, 8])
    outFile.writerow([1, 0, 'Tempo', 500000])
    outFile.writerow([1, 0, 'End_track'])
    for track in tracks:
        for row in track:
            outFile.writerow(row)
    outFile.writerow([0, 0, 'End_of_file'])
print('Done')
