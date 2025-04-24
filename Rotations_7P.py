import sys
from Rotations_6P import rotate_clockwise

def initialize_roster_7P():
    # --- Player Roles ---
    S = input("Enter Setter's Name: ").strip() or "Shubham"
    OH1 = input("Enter Outside Hitter 1's Name: ").strip() or "Jeremy"  
    OH2 = input("Enter Outside Hitter 2's Name: ").strip() or "Tony"  
    MB1 = input("Enter Middle Blocker 1's Name: ").strip() or "Eddy"  
    MB2 = input("Enter Middle Blocker 2's Name: ").strip() or "Tashi"  
    OPP = input("Enter Opposite's Name: ").strip() or "Aron" 
    FLEX = input("Enter Flexer's Name: ").strip() or "Flex" 
    print() 

    # --- Initial Lineup (Rotation 1) --- Ordered from Position 1 to Position 6 with Flex
    initial_lineup = [S, FLEX, OH1, MB1, OPP, OH2, MB2]
    initial_position = ["S", "Flex", "OH1", "MB1", "OPP", "OH2", "MB2"]

    return initial_lineup, initial_position

# --- Visual Net ---
def display_rotation_7P(lineup, position, rotation_number):
    """
    Displays the current court rotation in a visual format.

    Args:
        lineup (list): The current lineup list [Name1, Name2, Name3, ... , Name7].
        rotation_number (int): The current rotation number (1-7).
    """
    if len(lineup) != 7:
        print("Invalid lineup size for display.")
        return

    # Player names/roles for each position
    pos1_player, flex_player, pos2_player, pos3_player, pos4_player, pos5_player, pos6_player = lineup[0], lineup[1], lineup[2], lineup[3], lineup[4], lineup[5], lineup[6]
    pos1, flex, pos2, pos3, pos4, pos5, pos6 = position[0], position[1], position[2], position[3], position[4], position[5], position[6]

    # --- Formatting Constants ---
    player_col_width = 12 # Width for the player name/role cell content (adjust if needed)
    pos_label_width = player_col_width # Width for the (Pos X) label cell content
    first_col_label = "| Net |"
    first_col_spacer = "|     |" # Must be same length as first_col_label
    first_col_width = len(first_col_label) # Width of the first column including pipes

    offset = "          "

    player_separator = "-" * (player_col_width + 2)
    flex_separator = "-" * (player_col_width + 2) 
    first_separator = "-" * (first_col_width - 2)   

    # Construct separator lines dynamically
    separator_line = f"|{first_separator}|{player_separator}|{player_separator}|{player_separator}|"
    total_width = len(separator_line)
    border_line = "-" * total_width

    # --- Print Output ---
    print(f"\n--- Rotation {rotation_number} ---")

    # Determine the player who is OUT
    out_player = lineup[1] 
    out_position = position[1]
    print(f"{out_player} ({out_position}) is OUT")

    if 'S' in position:
        setter_index = position.index('S') + 1
        if setter_index == 1:
            print(f"Setter is in Position: 1")
        elif setter_index == 2:
            print("Setter is OUT")
        else:
            print(f"Setter is in Position: {setter_index - 1}")

    print(f"{offset}{border_line}") # Top row of ----
    # Front Row Players (Pos 4, 3, 2)
    print(f"{offset}{first_col_label}  {pos4_player:<{player_col_width}}|  {pos3_player:<{player_col_width}}|  {pos2_player:<{player_col_width}}|") # Top Row of Names
    print(f"{offset}{separator_line}{flex_separator}")

    # Front Row Position Label
    print(f"{offset}{first_col_spacer} {pos4:^{pos_label_width}} | {pos3:^{pos_label_width}} | {pos2:^{pos_label_width}} | {flex_player:^{pos_label_width}}|")

    print(f"FRONT ROW{border_line}|{' ' * player_col_width} |") # Divider label
    print(f" BACK ROW{border_line}| {flex:^{pos_label_width}}|")  # Divider label

    # Back Row Players (Pos 5, 6, 1)
    print(f"{offset}{first_col_spacer}  {pos5_player:<{player_col_width}}|  {pos6_player:<{player_col_width}}|  {pos1_player:<{player_col_width}}| {'(OUT)':^{player_col_width}}|") # Bottom Row of Names
    print(f"{offset}{separator_line}{flex_separator}")

    # Back Row Position Labels (Centered in their columns)
    print(f"{offset}{first_col_spacer} {pos5:^{pos_label_width}} | {pos6:^{pos_label_width}} | {pos1:^{pos_label_width}} |")
    print(f"{offset}{border_line}") # Bottom row of ----

    # Serving Player
    serving_player = lineup[0] 
    serving_position = position[0]
    print(f"Serving: {serving_player} ({serving_position})")


# --- Main Application Loop ---
def run_rotation_app_7P():

    initial_lineup, initial_position = initialize_roster_7P()
    current_lineup = initial_lineup[:] 
    current_position = initial_position[:]
    rotation_count = 1

    while True:
        display_rotation_7P(current_lineup, current_position, rotation_count)

        user_input = input("\nPress Enter to ROTATE, or type 'q' to QUIT: ").strip().lower()

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
        else:
            print("Invalid input. Please press Enter or type 'q'.")