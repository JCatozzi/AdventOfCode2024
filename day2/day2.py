with open('day2/input.txt') as file:
    pass_count: int = 0
    for i, line in enumerate(file):
        line_array = line.strip().split()
        line_array = [int(item) for item in line_array]
        is_increasing: bool = None
        is_safe: bool = True
        for i, level in enumerate(line_array):
            previous_level: int = line_array[i - 1] if i < 0 else None
            current_level: int = level
            # breakpoint()
            if previous_level is not None and current_level is not None:
                if previous_level < current_level:
                    if is_increasing is None:
                        is_increasing = True
                    elif is_increasing is False:
                        is_safe = False
                        # breakpoint()
                        break

                    if current_level - previous_level < 1 or current_level - previous_level > 3:
                        is_safe = False
                        # breakpoint()
                        break
                        
                        
                else: 
                    if is_increasing is None:
                        is_increasing = False
                    elif is_increasing is True:
                        is_safe = False
                        # breakpoint()
                        break

                    if previous_level - current_level < 1 or previous_level - current_level > 3:
                        is_safe = False
                        # breakpoint()
                        break

                

    print(f"Pass count: {pass_count}")
                
                
                   


