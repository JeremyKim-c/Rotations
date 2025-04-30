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
        # _G_6P = {'Jeremy': {'OH_1': 2, 'OH_2': 2, 'MB_1': 0, 'MB_2': 0, 'S': 0, 'OPP': 0},
        #          'Tony': {'OH_1': 2, 'OH_2': 2, 'MB_1': 0, 'MB_2': 0, 'S': 0, 'OPP': 0},
        #          'Eddy': {'OH_1': 0, 'OH_2': 0, 'MB_1': 2, 'MB_2': 2, 'S': 0, 'OPP': 0},
        #          'Aron': {'OH_1': 0, 'OH_2': 0, 'MB_1': 0, 'MB_2': 0, 'S': 0, 'OPP': 2},
        #          'Tashi': {'OH_1': 0, 'OH_2': 0, 'MB_1': 2, 'MB_2': 2, 'S': 0, 'OPP': 0},
        #          'Shubham': {'OH_1': 0, 'OH_2': 0, 'MB_1': 0, 'MB_2': 0, 'S': 2, 'OPP': 0}}
        # num_players = 6
        
        # _G_7P = {'Jeremy': {'OH_1': 2, 'OH_2': 2, 'MB_1': 0, 'MB_2': 0, 'S': 0, 'OPP': 0, 'FLEX': 0},
        #          'Tony': {'OH_1': 2, 'OH_2': 2, 'MB_1': 0, 'MB_2': 0, 'S': 0, 'OPP': 0, 'FLEX': 0},
        #          'Eddy': {'OH_1': 0, 'OH_2': 0, 'MB_1': 2, 'MB_2': 2, 'S': 0, 'OPP': 0, 'FLEX': 0},
        #          'Shubham': {'OH_1': 0, 'OH_2': 0, 'MB_1': 0, 'MB_2': 0, 'S': 2, 'OPP': 0, 'FLEX': 0},
        #          'Andy': {'OH_1': 0, 'OH_2': 0, 'MB_1': 0, 'MB_2': 0, 'S': 2, 'OPP': 0, 'FLEX': 0},
        #          'Aron': {'OH_1': 0, 'OH_2': 0, 'MB_1': 1, 'MB_2': 1, 'S': 0, 'OPP': 2, 'FLEX': 0},
        #          'Tashi': {'OH_1': 0, 'OH_2': 0, 'MB_1': 2, 'MB_2': 2, 'S': 0, 'OPP': 1, 'FLEX': 0}}      
        # num_players = 7   
        
        _G, num_players = get_G()
        result = find_matching(_G, matching_type = 'max', return_type = 'list')
        player_positions = [(player, position) for (player, position), _ in result]
        
        if num_players == 6:
            print("Running 6-player rotation app with custom lineup...")
            order_6P = ['S', 'OH_1', 'MB_1', 'OPP', 'OH_2', 'MB_2']
            player_positions.sort(key=lambda x: order_6P.index(x[1]))
            print(type(player_positions))
            print(player_positions)
            run_rotation_app_6P(custom_lineup = player_positions)

        elif num_players == 7:
            print("Running 7-player rotation app with custom lineup...")
            order_7P = ['S', 'FLEX', 'OH_1', 'MB_1', 'OPP', 'OH_2', 'MB_2']
            player_positions.sort(key=lambda x: order_7P.index(x[1]))
            print(type(player_positions))
            print(player_positions)
            run_rotation_app_7P(custom_lineup = player_positions)
    

        
        

    


