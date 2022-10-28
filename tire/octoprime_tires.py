from tire.tire import Tire


class OctoprimeTire(Tire):
    def __init__(self, current_sensor):
        self.current_sensor = current_sensor

    def needs_service(self):
        return sum(self.current_sensor) >= 3.0