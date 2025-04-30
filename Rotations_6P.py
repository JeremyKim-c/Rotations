import sys

def initialize_roster_6P(custom_lineup=None):
    if custom_lineup:
        if len(custom_lineup) != 6:
            raise ValueError("Custom lineup must contain exactly 6 players.")
        initial_lineup = [player for player, _ in custom_lineup]
        initial_position = [position for _, position in custom_lineup]
    else:
        # --- Player Roles ---
        S = input("Enter Setter's Name: ").strip() or "Shubham"
        OH1 = input("Enter Outside Hitter 1's Name: ").strip() or "Jeremy"  
        OH2 = input("Enter Outside Hitter 2's Name: ").strip() or "Tony"  
        MB1 = input("Enter Middle Blocker 1's Name: ").strip() or "Eddy"  
        MB2 = input("Enter Middle Blocker 2's Name: ").strip() or "Tashi"  
        OPP = input("Enter Opposite's Name: ").strip() or "Aron" 
        print()

        # --- Initial Lineup (Rotation 1) --- Ordered from Position 1 to Position 6
        initial_lineup = [S, OH1, MB1, OPP, OH2, MB2]
        initial_position = ["S", "OH_1", "MB_1", "OPP", "OH_2", "MB_2"]

        print(initial_lineup)
        print(initial_position)

    return initial_lineup, initial_position


# --- Rotation Logic ---
def rotate_clockwise(current_lineup, current_position):
    """
    Performs a clockwise rotation of the players.

    Args:
        current_lineup (list): A list of 6 players representing positions 1-6.
        current_position (list): A list of the 6 positions 

    Returns:
        new_lineup (list): The new lineup after rotation.
        new_position (list): The new positions after rotation.
    """

    player_from_pos1 = current_lineup[0]
    new_lineup = current_lineup[1:]
    new_lineup.append(player_from_pos1)

    current_pos1 = current_position[0]
    new_pos = current_position[1:]
    new_pos.append(current_pos1)

    return new_lineup, new_pos


# --- Visual Net ---
def display_rotation_6P(lineup, position, rotation_number):
    """
    Displays the current court rotation in a visual format.

    Args:
        lineup (list): The current lineup list [Pos1, Pos2, Pos3, Pos4, Pos5, Pos6].
        rotation_number (int): The current rotation number (1-6).
    """
    if len(lineup) != 6:
        print("Invalid lineup size for display.")
        return

    # Player names/roles for each position
    pos1_player, pos2_player, pos3_player, pos4_player, pos5_player, pos6_player = lineup[0], lineup[1], lineup[2], lineup[3], lineup[4], lineup[5]
    pos1, pos2, pos3, pos4, pos5, pos6 = position[0], position[1], position[2], position[3], position[4], position[5]

    # --- Formatting Constants ---
    player_col_width = 12 # Width for the player name/role cell content (adjust if needed)
    pos_label_width = player_col_width # Width for the (Pos X) label cell content
    first_col_label = "|^Net^|"
    first_col_spacer = "|     |" # Must be same length as first_col_label
    first_col_width = len(first_col_label) # Width of the first column including pipes

    offset = "          "

    player_separator = "-" * (player_col_width + 2) 
    first_separator = "-" * (first_col_width - 2)   

    # Construct separator lines dynamically
    separator_line = f"|{first_separator}|{player_separator}|{player_separator}|{player_separator}|"
    total_width = len(separator_line)
    border_line = "-" * total_width
    net_line = "#" * total_width

    # --- Print Output ---
    print(f"\n--- Rotation {rotation_number} ---")
    print(f"Setter is in Position: {position.index('S') + 1}" if 'S' in position else "Setter not found in lineup.")

    print(f"{offset}{net_line}") # Top row of ####
    # Front Row Players (Pos 4, 3, 2)
    print(f"{offset}{first_col_label}  {pos4_player:<{player_col_width}}|  {pos3_player:<{player_col_width}}|  {pos2_player:<{player_col_width}}|")
    print(f"{offset}{separator_line}")

    # Front Row Position Label
    print(f"{offset}{first_col_spacer} {pos4:^{pos_label_width}} | {pos3:^{pos_label_width}} | {pos2:^{pos_label_width}} |")

    print(f"FRONT ROW {border_line}") # Divider label
    print(f"BACK ROW  {border_line}")  # Divider label

    # Back Row Players (Pos 5, 6, 1)
    print(f"{offset}{first_col_spacer}  {pos5_player:<{player_col_width}}|  {pos6_player:<{player_col_width}}|  {pos1_player:<{player_col_width}}|")
    print(f"{offset}{separator_line}")

    # Back Row Position Labels (Centered in their columns)
    print(f"{offset}{first_col_spacer} {pos5:^{pos_label_width}} | {pos6:^{pos_label_width}} | {pos1:^{pos_label_width}} |")
    print(f"{offset}{border_line}") # Bottom row of ----

    # Serving Player
    serving_player = lineup[0] 
    serving_position = position[0]
    print(f"Serving: {serving_player} ({serving_position})")


# --- Main Application Loop ---
def run_rotation_app_6P(custom_lineup=None):
    
    initial_lineup, initial_position = initialize_roster_6P(custom_lineup)
    current_lineup = initial_lineup[:] 
    current_position = initial_position[:]
    rotation_count = 1

    while True:
        display_rotation_6P(current_lineup, current_position, rotation_count)

        user_input = input("\nPress Enter to ROTATE, 'r' to reset, '1' to swap OHs, '2' to swap MBs, or 'q' to QUIT: ").strip().lower()

        if user_input == 'q':
            print("Exiting the rotation simulator.")
            sys.exit()
        elif user_input == 'r':
            print("Resetting to initial lineup and rotation.")
            current_lineup = initial_lineup[:]
            current_position = initial_position[:]
            rotation_count = 1
        elif user_input == '':
            current_lineup, current_position = rotate_clockwise(current_lineup, current_position)
            rotation_count = (rotation_count % 6) + 1 # Cycle through 1-6
        elif user_input == '1':
            current_lineup[1], current_lineup[4] = current_lineup[4], current_lineup[1]
            current_position[1], current_position[4] = current_position[4], current_position[1]
            print("\nSwapped Outside Hitters (OH_1 and OH_2).")
        elif user_input == '2': 
            current_lineup[2], current_lineup[5] = current_lineup[5], current_lineup[2]
            current_position[2], current_position[5] = current_position[5], current_position[2]
            print("\nSwapped Middle Blockers (MB_1 and MB_2).")
        else:
            print("Invalid input. Please press Enter or type 'q'.")
