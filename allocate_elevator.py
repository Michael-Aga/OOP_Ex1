from elevator import *
from building import *
from call import *
import random


class AllocateElevator:
    def __init__(self, building: Building, calls: Call) -> None:
        self.building = building
        self.calls = calls
        self.elevators = building._elevators

    def find_the_best_elevator(self):
        for call in self.calls:
            pick = self.pick_elevator(call.time, call.source, call.destination)

        return pick

    def calculate_execution_time(self, elevator: Elevator, calls: list):
        last_position = 0
        sum_of_time = 0
        time = 0

        for call in calls:
            time = self.total_time(elevator, call.source,
                                   call.destination, last_position)
            sum_of_time += time
            last_position = call.destination

        return sum_of_time

    def calculate_every_elevators_time(self, elevator2calls: dict):
        sum = 0
        for elevator, calls in elevator2calls.items():
            sum += self.calculate_execution_time(elevator, calls)

        return sum

    def find_best_allocation(self):
        min_dict = float('inf')
        best_dict = {}

        for i in range(0, 10000):
            rand_dict = self.generate_random_allocation()
            sum = self.calculate_every_elevators_time(rand_dict)
            if sum < min_dict:
                sum = min_dict
                best_dict = rand_dict

        return best_dict

    def converte_dict_to_index(self, best_dict: dict):
        all_calls = []
        for elevator, calls in best_dict.items():
            for c in calls:
                c.assign = elevator.getID()
                all_calls.append(c)
        all_calls.sort(key=lambda call: float(call.time))
        return all_calls

    def generate_random_allocation(self):
        allocation = {}
        for elevator in self.elevators:
            allocation[elevator] = []

        for call in self.calls:
            rand_elevator = random.randint(0, len(self.elevators) - 1)
            allocation.get(self.elevators[rand_elevator]).append(call)

        return allocation

    def total_time(self, elevator: Elevator, source, destination, last_position):
        speed = float((elevator.getSpeed()))
        close_time = float(elevator.getCloseTime())
        open_time = float(elevator.getOpenTime())
        start_time = float(elevator.getStarTime())
        stop_time = float(elevator.getStopTime())

        answer = (2*start_time) + (2*stop_time) + (2*open_time) + (2*close_time) + (abs(float(
            last_position) - float(source)))/speed + (abs(float(source) - float(destination)))/speed

        return answer

    def __repr__(self) -> str:
        return f'{self.building._elevators[0]}'
