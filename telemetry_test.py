import time
from pyaccsharedmemory import ACCSharedMemory

ac = ACCSharedMemory()

print("Waiting for Assetto Corsa telemetry...")

while True:
    ac.read()

    physics = ac.physics

    print(
        f"RPM: {physics.rpm:6.0f} | "
        f"Speed: {physics.speedKmh:6.1f} km/h | "
        f"Throttle: {physics.gas:.2f} | "
        f"Brake: {physics.brake:.2f} | "
        f"Gear: {physics.gear}"
    )

    time.sleep(0.01)