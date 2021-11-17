import sys
import json
import csv
from Building import *
from Calls import *
from Elevators import *
from AllocateElevator import *


def getBuilding(buildingName):
    with open(buildingName, "r+") as file:
        buildingDict = json.load(file)
        minFloor = buildingDict.get("_minFloor")
        maxFloor = buildingDict.get("_maxFloor")

        elevatorsQuantity = []
        for elevator in buildingDict.get("_elevators"):
            elevatorsQuantity.append(Elevator(elevator))

        return Building(minFloor, maxFloor, elevatorsQuantity)


def getCalls(calls):
    with open(calls, "r+") as file:
        callsQuantity = []
        csvreader = csv.reader(file)

        for row in csvreader:
            c = Call(elevator_str=row[0], time=row[1], source=row[2],
                     destination=row[3], state=row[4], assign=row[5])
            callsQuantity.append(c)

        return callsQuantity


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
    #outputName = sys.argv[3]
    b1 = getBuilding(buildingJson)
    c1 = getCalls(callsCsv)
    #out(outputName, c1)

    allocateElevator(b1, c1)
