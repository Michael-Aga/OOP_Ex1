class Elevator:
    def __init__(self, elevatorQualities) -> None:
        self._id = elevatorQualities.get("_id")
        self._speed = elevatorQualities.get("_speed")
        self._minFloor = elevatorQualities.get("_minFloor")
        self._maxFloor = elevatorQualities.get("_maxFloor")
        self._closeTime = elevatorQualities.get("_closeTime")
        self._openTime = elevatorQualities.get("_openTime")
        self._startTime = elevatorQualities.get("_startTime")
        self._stopTime = elevatorQualities.get("_stopTime")
        
def __repr__(self) -> str:
    return f"id: {self._id} speed: {self._speed} closeTime: {self._closeTime} openTime: {self._openTime} startTime: {self._startTime}"       
