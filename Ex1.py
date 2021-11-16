import sys
import json
import csv
from Building import *
from Calls import *
from Elevators import *


def getBuilding(building):
    with open(building, "r+") as file:

        buildingDict = json.load(file)
        file.close()

        return Buildings(buildingDict)


def getCalls(calls):
    with open(calls, "r+") as file:
        callsQuantity = []
        csvreader = csv.reader(file)

        for row in csvreader:
            c = Call(elevator_str=row[0], time=row[1], source=row[2],
                     destination=row[3], state=row[4], assign=row[5])
            callsQuantity.append(c)
            
        file.close

        return callsQuantity


def allocateElevator(callsCsv):
    for call in callsCsv:
        call.assign = 0


def out(outputName, callsCsv):
    new_list = []
    
    for call in callsCsv:
        new_list.append(call.__dict__.values())

    with open(outputName, "w", newline="") as file:
        csvWriter = csv.writer(file)
        csvWriter.writerows(new_list)


if __name__ == '__main__':
    buildingJson = sys.argv[1]
    callsCsv = sys.argv[2]
    outputName = sys.argv[3]
    b1 = getBuilding(buildingJson)
    c1 = getCalls(callsCsv)
    allocateElevator(c1)
    out(outputName, c1)
