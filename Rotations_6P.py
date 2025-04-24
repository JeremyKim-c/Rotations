import sys

# --- Player Roles ---
S = "Setter"
OH1 = "OH1"
OH2 = "OH2"
MB1 = "MB1"
MB2 = "MB2"
OPP = "Oppo"

# --- Initial Lineup (Rotation 1) --- Ordered from Position 1 to Position 6
initial_lineup = [S, OH1, MB1, OH2, MB2, OPP]

# --- Rotation Logic ---
def rotate_clockwise(current_lineup):
    """
    Performs a clockwise rotation of the players.

    Args:
        current_lineup (list): A list of 6 players representing positions 1-6.

    Returns:
        list: The new lineup after rotation.
    """
    if len(current_lineup) != 6:
        raise ValueError("Lineup must contain exactly 6 players.")

    player_from_pos1 = current_lineup[0]
    new_lineup = current_lineup[1:]
    new_lineup.append(player_from_pos1)
    return new_lineup

# --- Visual Net ---
def display_rotation(lineup, rotation_number):
    """
    Displays the current court rotation in a visual format (Revised Alignment).

    Args:
        lineup (list): The current lineup list [Pos1, Pos2, Pos3, Pos4, Pos5, Pos6].
        rotation_number (int): The current rotation number (1-6).
    """
    if len(lineup) != 6:
        print("Invalid lineup size for display.")
        return

    # Player names/roles for each position
    pos1_player, pos2_player, pos3_player, pos4_player, pos5_player, pos6_player = lineup[0], lineup[1], lineup[2], lineup[3], lineup[4], lineup[5]
    setter_pos = -1

    try:
        setter_pos = lineup.index(S) + 1
    except ValueError:
        pass

    # --- Formatting Constants ---
    player_col_width = 12 # Width for the player name/role cell content (adjust if needed)
    pos_label_width = player_col_width # Width for the (Pos X) label cell content
    first_col_label = "| Net |"
    first_col_spacer = "|     |" # Must be same length as first_col_label
    first_col_width = len(first_col_label) # Width of the first column including pipes

    player_separator = "-" * (player_col_width + 2) 
    first_separator = "-" * (first_col_width - 2)   

    # Construct separator lines dynamically
    separator_line = f"|{first_separator}|{player_separator}|{player_separator}|{player_separator}|"
    total_width = len(separator_line)
    border_line = "-" * total_width

    # --- Print Output ---
    print(f"\n--- Rotation {rotation_number} ---")
    if setter_pos != -1:
        print(f"   Setter is in Position: {setter_pos}")
    else:
        print("   Setter not found in lineup.") # EXPAND ON THIS IF PLAYING WITH MORE THAN 6 PEOPLE

    print(border_line) # Top row of ----
    # Front Row Players (Pos 4, 3, 2)
    print(f"{first_col_label}  {pos4_player:<{player_col_width}}|  {pos3_player:<{player_col_width}}|  {pos2_player:<{player_col_width}}|")
    print(separator_line)

    # Front Row Position Label
    print(f"{first_col_spacer} {f'(Pos 4)':^{pos_label_width}} | {f'(Pos 3)':^{pos_label_width}} | {f'(Pos 2)':^{pos_label_width}} |")

    print(f"{border_line} FRONT ROW") # Divider label
    print(f"{border_line} BACK ROW")  # Divider label

    # Back Row Players (Pos 5, 6, 1)
    print(f"{first_col_spacer}  {pos5_player:<{player_col_width}}|  {pos6_player:<{player_col_width}}|  {pos1_player:<{player_col_width}}|")
    print(separator_line)

    # Back Row Position Labels (Centered in their columns)
    print(f"{first_col_spacer} {f'(Pos 5)':^{pos_label_width}} | {f'(Pos 6)':^{pos_label_width}} | {f'(Pos 1)':^{pos_label_width}} |")
    print(border_line) # Bottom row of ----

    # Serving Player
    serving_player = lineup[0] 
    print(f"Serving: {serving_player} (from Pos 1)")


# --- Main Application Loop ---
def run_rotation_app():
    """Runs the command-line interface for the rotation simulator."""
    current_lineup = initial_lineup[:] 
    rotation_count = 1

    while True:
        display_rotation(current_lineup, rotation_count)

        user_input = input("\nPress Enter to ROTATE, or type 'q' to QUIT: ").strip().lower()

        if user_input == 'q':
            print("Exiting the rotation simulator.")
            sys.exit()
        elif user_input == '':
            current_lineup = rotate_clockwise(current_lineup)
            rotation_count = (rotation_count % 6) + 1 # Cycle through 1-6
        else:
            print("Invalid input. Please press Enter or type 'q'.")

# --- Start the App ---
if __name__ == "__main__":
    print("Volleyball 5-1 Rotation Simulator")
    print("Initial Setup (Rotation 1): Setter starts in Pos 1")
    run_rotation_app()