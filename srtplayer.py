# Author: Qi Liu, ql375@nyu.edu

import sys
import time

# substitle path, cmc line input
path = sys.argv[1]
delay = int(sys.argv[2])

# substitle file, list
lines = []

# time count
timeCount = delay

# load file
with open(path) as file:
	lines = file.readlines()

# next line to check at nextSec
nextLine = 0
nextSec = 0

for item in lines:
	if item[0:3] == "00:":
		tempStr = item[0:8]
		nextSec = int(tempStr[0:2]) * 3600 + int(tempStr[3:5]) * 60 + int(tempStr[6:8])
		break
	nextLine += 1

count = 0

while True:

	count += 1
	if count >= 200:
		break

	time.sleep(1)
	timeCount += 1

	#print("timeCount: " + str(timeCount))
	# display the substitile
	if timeCount == nextSec:

		nextLine += 1

		while True:
			if not lines[nextLine][0].isnumeric():
				print(lines[nextLine])

			if len(lines[nextLine]) >= 3 and lines[nextLine][2] == ':':
				tempStr = lines[nextLine][0:8]
				nextSec = int(tempStr[0:2]) * 3600 + int(tempStr[3:5]) * 60 + int(tempStr[6:8])
				break

			nextLine += 1
	#print("next line:" + str(nextLine))
	#print(lines[nextLine])
	#print("next sec: " + str(nextSec))
