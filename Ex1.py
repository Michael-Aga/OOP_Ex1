import sys
import json
import csv
from building import *
from call import *
from elevator import *
from allocate_elevator import *
import pandas as pd


def getBuilding(buildingName):
    try:
        with open(buildingName, "r+") as file:
            elevatorsQuantity = []
            buildingDict = json.load(file)
            minFloor = buildingDict.get("_minFloor")
            maxFloor = buildingDict.get("_maxFloor")

            for elevator in buildingDict.get("_elevators"):
                elevatorsQuantity.append(Elevator(elevator))

    except FileNotFoundError as e:
        print(e)

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


def print_to_csv(outputName, calls: list):
    with open(outputName, 'w+', newline='') as csv_file:
        wr = csv.writer(csv_file, delimiter=',')

        for call in calls:
            wr.writerow(call.iter())


if __name__ == '__main__':
    buildingJson = sys.argv[1]
    callsCsv = sys.argv[2]
    outputName = sys.argv[3]
    b1 = getBuilding(buildingJson)
    c1 = getCalls(callsCsv)
    find = AllocateElevator(b1, c1)
    print_to_csv(outputName, find.converte_dict_to_index(
        find.find_best_allocation()))
