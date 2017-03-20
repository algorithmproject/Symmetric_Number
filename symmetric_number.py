import re
def get_next_symmetric_number(N):
    # if N is 9+
    if re.match(r"^9+$", ''.join(map(str, N))):
        return map(int, str(int(''.join(map(str, N[::]))) + 2))
    # if N is a single number and lower than 9
    if len(N) == 1 and (N[0] >= 0 or N[0] <= 8):
        return [int(N[0]) + 1]
    # if N is a odd length number
    if len(N) % 2 != 0:
        return odd_number(N)
    else:
        return even_number(N)
    
def odd_number(N):
    # if number is odd
    # say N = [1, 3, 5, 6, 2, 7, 3]
    # first to find [1, 3, 5] => 135 => 531
    # because 531 > 273 then return [135] + [6] + [531]
    #
    # say N = [1, 3, 5, 6, 8, 7, 3]
    # first to find [1, 3, 5] => 135 => 531
    # because 531 < 873 then (1356 + 1) => 1357
    # return [135] + [7] + [531] 
    pivot = len(N) / 2
    reverse_previous_part = list(reversed(N[:pivot]))
    reverse_previous_part = int(''.join(map(str, reverse_previous_part)))
    next_part = int(''.join(map(str, N[pivot + 1:])))
    if reverse_previous_part > next_part:
        N[pivot + 1:] = map(int, str(reverse_previous_part))
    else:
        previous_part_pivot = int(''.join(map(str, N[:pivot + 1]))) + 1
        previous_part_pivot = map(int, str(previous_part_pivot))
        reverse_previous_part = list(reversed(previous_part_pivot[:pivot]))
        N = previous_part_pivot + reverse_previous_part
    return N

def even_number(N):
    # if number if even number
    # say N = [6, 3, 5, 1, 8, 7]
    # first to find [6, 3, 5] => 635 = 536
    # because 536 > 187 then return [635] + [536]
    #
    # say N = [6, 3, 5, 6, 8, 7]
    # first to find [6, 3, 5] => 635 => 536
    # because 536 < 687 then (635 + 1) => 636
    # return [636] + [636]
    
    pivot = len(N) / 2
    reverse_previous_part = list(reversed(N[:pivot]))
    reverse_previous_part = int(''.join(map(str, reverse_previous_part)))
    next_part = int(''.join(map(str, N[pivot:])))
    if reverse_previous_part > next_part:
        N[pivot:] = map(int, str(reverse_previous_part))
    else:
        previous_part = int(''.join(map(str, N[:pivot]))) + 1
        previous_part = map(int, str(previous_part))
        reverse_previous_part = list(reversed(previous_part[:pivot]))
        N = previous_part + reverse_previous_part
    return N

N = [9,9,9,9,9,9,9,9,9,9,9,9,9,9]
print get_next_symmetric_number(N)
        
        
        
        
