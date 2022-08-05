"""
Opens a gpx file, prints each line of gpx, finds the beginning of the first data point.
"""

fileref = open("/Users/ericwarren/Documents/Projects/GPXFiles/b_med.gpx", "r")

numLines = 0

## Prints each line of the gpx file
fileList = fileref.readlines()
for line in fileList:
    ##print(line)
    numLines += 1

## Finds the beginning of the first data point
numLines = 0
for line in fileList:
    if line == "  <trkseg>\n":
        print("yes")
        print(numLines)
    numLines += 1
print(numLines)

fileref.close()
