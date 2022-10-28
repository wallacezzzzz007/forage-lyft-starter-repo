from tire.tire import Tire


class CarriganTire(Tire):
    def __init__(self, current_sensor):
        self.current_sensor = current_sensor

    def needs_service(self):
        for val in self.current_sensor:
            if val >= 0.9:
                return True
        return False