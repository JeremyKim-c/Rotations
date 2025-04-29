from Rotations_6P import run_rotation_app_6P
from Rotations_7P import run_rotation_app_7P
from Player_Logic import get_G, find_matching

# --- Start the App ---
if __name__ == "__main__":
    print("Volleyball 5-1 Rotation Simulator")

    user_input = input("Does everyone know what positions they want to play? (y/n): ").strip().lower()
    if user_input == 'y':
        num_players = input("Enter number of players (6 or 7): ").strip()

        if num_players == '6':
            run_rotation_app_6P()

        elif num_players == '7':
            run_rotation_app_7P()
            
        else:
            print("Invalid input. Please enter 6 or 7.")
            exit(1)
    else:
        _G = get_G()
        print(_G)
        """
        result = find_matching(_G, matching_type = 'max', return_type = 'list')
        print(result)
        """

    


