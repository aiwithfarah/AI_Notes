# ----------------TASK--------------
# Think of it like a traffic light 🚦:

# IF the light is Green -> Go.

# ELSE IF (elif) the light is Yellow -> Slow down.

# ELSE IF (elif) the light is Red -> Stop.

# ELSE (none of the above) -> The light is broken, proceed with caution.

light = input('Enter a color - Green", "Yellow", or "Red" : ').lower()

if light == "green":
    print("Go")
elif light == 'yellow':
    print('Slow Down')
elif light == 'red':
    print('Stop')
else:
    print('Light is broken Proceed with caution')
