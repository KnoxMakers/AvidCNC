#!/usr/bin/env python3
import serial
import time

# Configuration
SERIAL_PORT = "/dev/ttyACM0"  # Replace with your serial port
BAUD_RATE = 115200
TIMEOUT = 0.1  # Serial timeout in seconds
RETRY_DELAY = 1  # Delay before retrying in seconds
KEEP_ALIVE_INTERVAL = 5  # Keep-alive message interval in seconds

last_keep_alive = 0

def setup_serial_connection():
    """Set up the serial connection."""
    while True:
        try:
            print(f"Attempting to connect to {SERIAL_PORT}...")
            return serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=TIMEOUT)
        except serial.SerialException as e:
            print(f"SerialException: {e}. Retrying in {RETRY_DELAY} seconds...")
            time.sleep(RETRY_DELAY)

# Main script
arduino = setup_serial_connection()

try:
    while True:
        # Periodically send keep-alive signal
        current_time = time.time()
        if current_time - last_keep_alive > KEEP_ALIVE_INTERVAL:
            try:
                arduino.write(b"K\n")  # Keep-alive signal
                print("Keep-alive sent")
                last_keep_alive = current_time
            except (serial.SerialException, OSError) as e:
                print(f"Error during write: {e}. Reconnecting...")
                arduino.close()
                arduino = setup_serial_connection()

        # Read data from Arduino
        try:
            if arduino.in_waiting > 0:
                data = arduino.readline().decode("utf-8").strip()
                print(f"Received: {data}")
        except (serial.SerialException, OSError) as e:
            print(f"Error during read: {e}. Reconnecting...")
            arduino.close()
            arduino = setup_serial_connection()

        time.sleep(0.01)  # Small delay to prevent high CPU usage

except KeyboardInterrupt:
    print("Exiting program...")
    if arduino.is_open:
        arduino.close()
