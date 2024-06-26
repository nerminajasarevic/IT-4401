init_pos = float(input("Enter the initial position: "))
init_vel = float(input("Enter the initial velocity: "))
acceleration = float(input("Enter the acceleration: "))
time = float(input("Enter the time: "))

final_pos = init_pos + (init_vel * time) + (0.5 * acceleration * (time ** 2))

print(f"Final position = {final_pos}")
