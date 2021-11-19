class Call:

    def __init__(self, elevator_str, time, source, destination, state, assign) -> None:
        self.elevator_str = elevator_str
        self.time = time
        self.source = source
        self.destination = destination
        self.state = state
        self.assign = assign

    def iter(self):
        return iter([self.elevator_str, self.time, self.source, self.destination, self.state, self.assign])

    def __str__(self) -> str:
        return f"time: {self.time} source: {self.source} destinaiton: {self.destination} assign: {self.assign}"

    def __repr__(self) -> str:
        return f"time: {self.time} source: {self.source} destinaiton: {self.destination} assign: {self.assign}"