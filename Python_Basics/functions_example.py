# Concept: "Don't Repeat Yourself" (DRY). Define it once, use it many times.
# Keyword: def (short for define).

# ------TASK-------------
# Define a function named emergency_alert.
# Inside the function, print "⚠️ ALERT! ⚠️" three times. (You can use a loop inside the function if you want, or just three print lines!)
# Call the function once to test it.

def emergency_alert():
    for _ in range(3):
        print('⚠️ ALERT! ⚠️')


emergency_alert()
