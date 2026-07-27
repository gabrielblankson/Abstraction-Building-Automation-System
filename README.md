# Abstraction – Building Automation System

Demonstrates abstraction using Python's `abc` module.

`BuildingSystem` is an abstract class defining the contract every
automated system must follow: `start()`, `stop()`, `status()`. Child
classes (`AirConditioningSystem`, `LightingSystem`, `SecuritySystem`,
`FireAlarmSystem`) each implement these methods differently. Objects
are stored in a list and processed through the same loop, showing
polymorphic behaviour — `FireAlarmSystem` was added without changing
the processing loop.

## Run
```
python building_systems.py
```Author```
BLANKSON GABRIEL
