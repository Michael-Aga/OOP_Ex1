from elevator import Elevator


class Building:
    def __init__(self, minFloor: int, maxFloor: int, elevators: Elevator) -> None:
        self._minFloor = minFloor
        self._maxFloor = maxFloor
        self._elevators = elevators

    def __repr__(self) -> str:
        return f"minFloor: {self._minFloor} maxFloor: {self._maxFloor} elevators: {self._elevators}"
