from Elevators import *
class Buildings:
    def __init__(self, BuildingQualities) -> None:
        self._minFloor = BuildingQualities.get("_minFloor")
        self._maxFloor = BuildingQualities.get("_maxFloor")
        self._elevators = BuildingQualities.get("_elevators")
        
        elevatorsQuantity = []
        for elevator in self._elevators:
            elevatorsQuantity = elevatorsQuantity.append(Elevator(elevator))
        
def __repr__(self) -> str:
    return f"minFloor: {self._minFloor} maxFloor: {self._maxFloor} elevators: {self.elevatorsQuantity}"