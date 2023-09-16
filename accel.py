import openzen
import time

zen = openzen.Zen()

def on_sensor_discovery(device_id):
    device_info = zen.get_device_info(device_id)
    print(f"Found device {device_info.display_name} ({device_info.serial_number})")

    zen.enable_device(device_id)

    sensors = zen.get_sensors(device_id)
    print(f"  {len(sensors)} sensors:")

    for sensor in sensors:
        sensor_info = zen.get_sensor_info(sensor)
        print(f"    {sensor_info.sensor_type} ({sensor_info.serial_number})")

zen.set_on_sensor_discovery_callback(on_sensor_discovery)

print("Searching for sensors...")
zen.scan_for_sensors()

while not zen.has_pending_events():
    time.sleep(0.1)

print("IMU Data:")

while zen.has_pending_events():
    zenEvent = zen.wait_for_event(timeout=100)
    if zenEvent.event_type == openzen.ZenEventType.SensorData:
        for i in range(zenEvent.num_samples):
            sample = zenEvent.get_sample(i)
            if sample.sensor_type == openzen.SensorType.Accelerometer:
                print(f"Accelerometer: x={sample.values[0]}, y={sample.values[1]}, z={sample.values[2]}")
