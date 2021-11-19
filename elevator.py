class Elevator:

    def __init__(self, elevatorQualities) -> None:
        self._id = elevatorQualities.get('_id')
        self._speed = elevatorQualities.get('_speed')
        self._minFloor = elevatorQualities.get('_minFloor')
        self._maxFloor = elevatorQualities.get('_maxFloor')
        self._closeTime = elevatorQualities.get('_closeTime')
        self._openTime = elevatorQualities.get('_openTime')
        self._startTime = elevatorQualities.get('_startTime')
        self._stopTime = elevatorQualities.get('_stopTime')
        self.state = 0
        self.position = 0

    def __repr__(self) -> str:
        return f'id: {self._id}'

    def getID(self):
        return self._id

    def getSpeed(self):
        return self._speed

    def getCloseTime(self):
        return self._closeTime

    def getOpenTime(self):
        return self._openTime

    def getStarTime(self):
        return self._startTime

    def getStopTime(self):
        return self._stopTime

    def setPosition(self, position):
        self.position = position
