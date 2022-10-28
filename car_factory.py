from car import Car
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from battery.nubbin_battery import NubbinBattery
from battery.spindle_battery import SpindleBattery
from tire.carrigan_tires import CarriganTire
from tire.octoprime_tires import OctoprimeTire


class CarFactory(Car):
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage, current_sensor):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindleBattery(last_service_date, current_date)
        tire = CarriganTire(current_sensor)
        car = Car(engine, battery, tire)
        return car
    
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage, current_sensor):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindleBattery(last_service_date, current_date)
        tire = OctoprimeTire(current_sensor)
        car = Car(engine, battery, tire)
        return car
    
    def create_palindrome(current_date, last_service_date, warning_light_on, current_sensor):
        engine = SternmanEngine(warning_light_on)
        battery = SpindleBattery(last_service_date, current_date)
        tire = CarriganTire(current_sensor)
        car = Car(engine, battery, tire)
        return car
    
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage, current_sensor):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        tire = OctoprimeTire(current_sensor)
        car = Car(engine, battery, tire)
        return car
    
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage, current_sensor):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        tire = CarriganTire(current_sensor)
        car = Car(engine, battery, tire)
        return car