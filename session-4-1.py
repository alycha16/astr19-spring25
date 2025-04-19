class Giraffe:
    def __init__(self, arm_length, leg_length, num_eyes, has_tail):
        self.arm_length = arm_length 
        self.leg_length = leg_length 
        self.num_eyes = num_eyes
        self.has_tail = has_tail
    def describe(self):
        print("My favorite animal is the Giraffe!")
        print(f"Arm Length: {self.arm_length} feet")
        print(f"Leg Length: {self.leg_length} feet")
        print(f"Number of eyes: {self.num_eyes}")
        print(f"has a tail: {'Yes' if self.has_tail else 'No'}")
    def main():
        animal = Giraffe(6, 6, 2, True)
        animal.describe()

Giraffe.main()