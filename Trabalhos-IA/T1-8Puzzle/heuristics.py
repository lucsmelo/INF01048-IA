
def hamming(state: str) -> int:
    only_numbers = state.replace('_', '9')
    normalized = [int(ch)-1 for ch in only_numbers]
    
    diffs = 0
    for i in range(len(normalized)):  
        diffs += 1 if normalized[i] != i else 0
    
    return diffs

def manhattan(state: str) -> int:
    only_numbers = state.replace('_', '9')
    normalized = [int(ch)-1 for ch in only_numbers]

    total_distance = 0
    for i in range(len(normalized)):
        expected_pos_col = i % 3
        expected_pos_row = i // 3
        actual_pos_col = normalized[i] % 3
        actual_pos_row = normalized[i] // 3

        distance_col = abs((expected_pos_col - actual_pos_col))
        distance_row = abs((expected_pos_row - actual_pos_row))
        distance = distance_col + distance_row

        total_distance += distance
    
    return total_distance
