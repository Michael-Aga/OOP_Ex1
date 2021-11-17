from Elevators import *
from Building import *
from Calls import *


class AllocateElevator:
    def __init__(self, building, calls) -> None:
        self.building = building
        self.calls = calls


def allocateElevator(buildingName, callsCsv):
    elevators = buildingName._elevators
    print(elevators[0])
    
    # for call in callsCsv:
    #    call.assign = 0
