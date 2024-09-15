class Lift:
    def __init__(self, max_capacity):
        self.max_capacity = max_capacity
        self.current_weight = 0
        self.allocations = []

    def allocate(self, request_weight):
        if self.current_weight + request_weight <= self.max_capacity:
            self.current_weight += request_weight
            self.allocations.append(request_weight)
            return True
        else:
            return False

    def __str__(self):
        return (f"Lift capacity: {self.max_capacity} kg\n"
                f"Current weight: {self.current_weight} kg\n"
                f"Allocations: {self.allocations}")


def main():
    max_capacity = float(input("Enter the lift's maximum weight capacity (in kg): "))
    lift = Lift(max_capacity)

    while True:
        request_weight = float(input("Enter the weight of the request (in kg), or type -1 to finish: "))
        if request_weight == -1:
            break

        if lift.allocate(request_weight):
            print(f"Request for {request_weight} kg allocated successfully.")
        else:
            print(f"Request for {request_weight} kg could not be allocated. Exceeds maximum capacity.")

    print("\nFinal Lift Status:")
    print(lift)


if __name__ == "__main__":
    main()
