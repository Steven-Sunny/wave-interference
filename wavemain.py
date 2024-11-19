import numpy as np
import matplotlib.pyplot as plt

#speed of light constant
c = 299792458

#user input for first function
while True:
    try:
        amp1 = float(input("Enter the amplitude of your first function: "))
        break
    except ValueError:
        print("Numbers only! Please enter a valid value.")
while True:
    try:
        feq1 = float(input("Enter the frequency of your first function: "))
        break
    except ValueError:
        print("Numbers only! Please enter a valid value.")
while True:
    try:
        phase1 = float(input("Enter the phase shift of your first function: "))
        if(0 <= phase1 <= 2*np.pi):
            break
        else:
            print("The number must be within 0 and 2pi")
    except ValueError:
        print("Numbers only! Please enter a valid value.")

#calculates all of the necessary variables
angf1 = 2 * np.pi * feq1
wlen1 = c / feq1
k1 = (2 * np.pi) / wlen1

#user input for second function
while True:
    try:
        amp2 = float(input("Enter the amplitude of your second function: "))
        break
    except ValueError:
        print("Numbers only! Please enter a valid value.")
while True:
    try:
        feq2 = float(input("Enter the frequency of your second function: "))
        break
    except ValueError:
        print("Numbers only! Please enter a valid value.")
while True:
    try:
        phase2 = float(input("Enter the phase shift of your second function: "))
        if(0 <= phase2 <= 2*np.pi):
            break
        else:
            print("The number must be within 0 and 2pi")
    except ValueError:
        print("Numbers only! Please enter a valid value.")

angf2 = 2 * np.pi * feq2
wlen2 = c / feq2
k2 = (2 * np.pi) / wlen2

#Allow user to choose their domain
while True:
    choice = input("Choose domain for addition (time/distance): ").strip().lower()
    if(choice == "time" or choice == "distance"):
        break
    else:
        print("Please enter 'time' or 'distance'")


# User input for fixed distance in time domain
if(choice == "time"):
    #get user's value of fixed distance (has error checking)
    while True:
        try:
            fixedx = float(input("Enter the value of your fixed distance x: "))
            break
        except ValueError:
            print("Numbers only! Please enter a valid value.")
    
    #create time domain values
    t = np.linspace(0, 1, 1000)

    #create values of the function using the given formula in assignment
    tfunc1 = amp1 * np.sin(k1 * fixedx - angf1 * t + phase1)
    tfunc2 = amp2 * np.sin(k2 * fixedx - angf2 * t + phase2)

    #sum of the 2 functions
    tfuncsum = tfunc1 + tfunc2

    #creates a popup for graphs that is 10in by 6in
    plt.figure(figsize=(10, 6))

   # Plot details of Signal 1
    plt.plot(t, tfunc1, label="Signal 1", color="blue", linestyle='-')

    # Plot details of Signal 2
    plt.plot(t, tfunc2, label="Signal 2", color="green", linestyle='--')

    # Plot details of the sum of Signal 1 and Signal 2
    plt.plot(t, tfuncsum, label="Sum of Signals", color="red", linestyle='-.')

    # Set title and labels
    plt.title("Signals and Their Sum in Time Domain")
    plt.xlabel('Time (t)')
    plt.ylabel('Displacement')
    plt.grid(True)
    #shows popup with all the graphs, with nice, tight format
    plt.tight_layout()
    plt.show()

# User input for fixed time in distance domain
if(choice == "distance"):
    #get user's value of fixed time (has error checking)
    while True:
        try:
            fixedt = float(input("Enter the value of your fixed time t: "))
            break
        except ValueError:
            print("Numbers only! Please enter a valid value.")
        # Create distance domain values
    x = np.linspace(0, 10, 1000)  # Distance from 0 to 10 meters

    # Create values of the functions using the given formula in the assignment
    xfunc1 = amp1 * np.sin(k1 * x - angf1 * fixedt + phase1)
    xfunc2 = amp2 * np.sin(k2 * x - angf2 * fixedt + phase2)

    # Sum of the two functions
    xfuncsum = xfunc1 + xfunc2

    # Creates a popup for graphs that is 10in by 6in
    plt.figure(figsize=(10, 6))

    # Plot details of the first function (Signal 1)
    plt.plot(x, xfunc1, label="Signal 1", color="blue", linestyle='-')

    # Plot details of the second function (Signal 2)
    plt.plot(x, xfunc2, label="Signal 2", color="green", linestyle='--')

    # Plot details of the sum of the first and second function
    plt.plot(x, xfuncsum, label="Sum of Signals", color="red", linestyle='-.')

    # Set title and labels
    plt.title("Signals and Their Sum in Distance Domain")
    plt.xlabel('Distance (x)')
    plt.ylabel('Displacement')
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.show()
