class Elevator:
    def __init__(self, max_weight, id):
        self.max_weight = max_weight
        self.current_weight = 0
        self.id = id
        self.occupants = []

    def can_accommodate(self, weight):
        return self.current_weight + weight <= self.max_weight

    def add_person(self, person_id, weight):
        if self.can_accommodate(weight):
            self.occupants.append(person_id)
            self.current_weight += weight
            return True
        return False


def allocate_lifts(people_weights, elevators):
    for person_id, weight in enumerate(people_weights):
        allocated = False
        for elevator in elevators:
            if elevator.can_accommodate(weight):
                elevator.add_person(person_id, weight)
                allocated = True
                break
        if not allocated:
            print(f"Person {person_id} with weight {weight} could not be allocated to any elevator.")

    return elevators


# Define elevators with different weight capacities
elevators = [
    Elevator(max_weight=500, id=1),
    Elevator(max_weight=800, id=2),
    Elevator(max_weight=900, id=3)
]

# List of people's weights
people_weights = [70, 120, 150, 200, 90, 110, 300, 220, 130,340,230,134,97,89]
def main():
    # Allocate lifts
    allocated_elevators = allocate_lifts(people_weights, elevators)

    # Display elevator allocations
    for elevator in allocated_elevators:
        print(f"Elevator {elevator.id} has occupants {elevator.occupants} with total weight {elevator.current_weight}")

if __name__ == "__main__":
    main()