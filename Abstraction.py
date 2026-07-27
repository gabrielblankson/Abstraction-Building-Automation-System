from abc import ABC, abstractmethod


class BuildingSystem(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def status(self):
        pass


class AirConditioningSystem(BuildingSystem):
    def start(self):
        print("AC: cooling started")

    def stop(self):
        print("AC: cooling stopped")

    def status(self):
        print("AC: status OK")


class LightingSystem(BuildingSystem):
    def start(self):
        print("Lighting: lights ON")

    def stop(self):
        print("Lighting: lights OFF")

    def status(self):
        print("Lighting: status OK")


class SecuritySystem(BuildingSystem):
    def start(self):
        print("Security: armed")

    def stop(self):
        print("Security: disarmed")

    def status(self):
        print("Security: status OK")


class FireAlarmSystem(BuildingSystem):
    def start(self):
        print("Fire Alarm: monitoring active")

    def stop(self):
        print("Fire Alarm: monitoring stopped")

    def status(self):
        print("Fire Alarm: status OK")


# Test
systems = [
    AirConditioningSystem(),
    LightingSystem(),
    SecuritySystem(),
    FireAlarmSystem()
]

for system in systems:
    system.start()
    system.status()
    system.stop()