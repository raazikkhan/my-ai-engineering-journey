seat_type = input(f"Choose your seat type Sleeper/Ac/General/firstClass:  ").lower()
match seat_type:
    case "sleeper":
        print(f" Sleeper class is a budget-friendly option for long journeys.")

    case "ac":
        print(f"AC class gives you a comfortable journey")    
    case "general": 
        print(f"General class is a good middle-ground option")    
    case "firstclass":
        print(f"First class offers the best comfort and amenities")
 #Note the last block: the “variable name” _ acts as a wildcard and never fails to match.
    case _:
        print(f"Invalid seat type. Please choose from Sleeper, AC, General, or First Class.")