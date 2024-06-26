while True:
    try:
        init_pos = float(input("Enter the initial position: "))
        init_vel = float(input("Enter the initial velocity: "))
        acceleration = float(input("Enter the acceleration: "))
        time = float(input("Enter the time: "))

        if time < 0:
            print("Error: Enter a non-negative float.")
            continue

        final_pos = init_pos + (init_vel * time) + (0.5 * acceleration * (time ** 2))

        print(f"Final position = {final_pos}")

        while True:
            loop = input("Perform another calculation? Enter y to continue: ").lower()
            if loop == 'y':
                break
            else:
                exit()

    except ValueError:
        print("Error: Enter a valid float value.")
