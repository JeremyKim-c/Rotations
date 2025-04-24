from Rotations_6P import run_rotation_app_6P
from Rotations_7P import run_rotation_app_7P

# --- Start the App ---
if __name__ == "__main__":
    print("Volleyball 5-1 Rotation Simulator")
    user_input = input("Enter number of players (6 or 7): ").strip()

    if user_input == '6':
        run_rotation_app_6P()

    elif user_input == '7':
        run_rotation_app_7P()
        
    else:
        print("Invalid input. Please enter 6 or 7.")
        exit(1)


