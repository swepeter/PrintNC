import hal
import linuxcnc

# Create a HAL component
h = hal.component("laser_control")

# Create a HAL pin to receive the laser enable command
h.newpin("enable", hal.HAL_BIT, hal.HAL_IN)

# Initialize the HAL component
h.ready()

# Create an instance of the LinuxCNC interpreter
lc = linuxcnc.command()

try:
    while True:
        # Check the enable pin
        enable = h['enable']

        # If enable is True (M62 command), turn on the laser
        if enable:
            lc.mdi("M62 P0")  # Adjust the P value as needed
        else:
            lc.mdi("M63 P0")  # Adjust the P value as needed

except KeyboardInterrupt:
    pass

# Clean up
h.exit()

