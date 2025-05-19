'''import numpy as np
import matplotlib.pyplot as plt

# Define the parameters
amplitude = 1.0
frequency = 1.0  # in Hz
phase = 0.0  # in radians
sampling_rate = 1000  # samples per second
duration = 2.0  # in seconds

# Generate the time axis
t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)

# Generate the sine wave
y = amplitude * np.sin(2 * np.pi * frequency * t + phase)

# Plot the sine wave
plt.figure(figsize=(10, 4))
plt.plot(t, y, label=f'{frequency} Hz Sine Wave')
plt.title('Sine Wave')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()
plt.show()'''




import math

# # Angle in degrees
# angle_degrees = 30

# # Convert degrees to radians
# angle_radians = math.radians(angle_degrees)

# # Calculate sine
# sin_value = math.sin(angle_radians)

for i in range(0, 360, 1):
    angle_degrees = i
    angle_radians = math.radians(angle_degrees)
    sin_value = math.sin(angle_radians)
    print(f"sin({angle_degrees}°) = {sin_value}")