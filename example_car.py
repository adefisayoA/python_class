class Car(object):
    """ blueprint for car  """

    def __init__(self, model, color, company, speed_limit):
        self.color = color
        self.company = company
        self.speed_limit = speed_limit
        self.model = model

    def start(self):
        print("started")

    def stop(self):
        print("stopped")

    def accelarate(self):
        print("accelerating...")
        "accelerator functionality here"

    def change_gear(self, gear_type):
        print("gear changed")
        " gear related functionality here"

    def __str__(self):
        return f"This is a {self.color} {self.model} from {self.company} "


# (self, model, color, company, speed_limit):
maruthi_suzuki = Car("ertiga", "black", "suzuki", 60)
audi = Car("A6", "red", "audi", 80)
print(audi)
print(maruthi_suzuki)
